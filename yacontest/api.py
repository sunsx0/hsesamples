import requests
import typing

import dataclasses as dc

from collections import deque
from lxml import html


def inline_text(s):
    return ' '.join(part.strip() for part in str(s).split('\n'))


def parse_code_node(node):
    data = node.xpath('div/div[1]/pre')
    if data:
        return data[0].text_content()
    else:
        return ''


@dc.dataclass
class TestInfo:
    name: str = ''
    test_input: str = ''
    output: str = ''
    answer: str = ''
    checker: str = ''
    stderr: str = ''


@dc.dataclass
class SubmissionInfo:
    contest_name: str = ''
    task: str = ''
    participant: str = ''
    tests: typing.List[TestInfo] = dc.field(default_factory=list)


FIELD_MAPPING = {
    'Ввод': 'test_input',
    'Вывод': 'output',
    'Ответ': 'answer',
    'Сообщение чекера': 'checker',
    'Stderr': 'stderr',
}


class YaApi:
    def __init__(self, session_id):
        self.session = requests.Session()
        self.session.cookies['Session_id'] = session_id

    def run_report(self, submission_id):
        submission_id = int(submission_id)
        url = f'https://contest.yandex.ru/admin/run-report?id={submission_id}'

        resp = self.session.get(url).text
        page = html.fromstring(resp)
        content = page.xpath('//*[@id="content"]')[0]

        submission_info = SubmissionInfo(
            contest_name=inline_text(content.xpath('table/tr[2]/td[2]/a')[0].text),
            task=inline_text(content.xpath('table/tr[3]/td[2]/a')[0].text),
            participant=content.xpath('table/tr[4]/td[2]')[0].text,
        )

        nodes: typing.Deque[html.HtmlElement] = deque(content.xpath(f'div[@width="100%"]/*'))
        while nodes:
            node = nodes.popleft()
            if node.tag != 'hr':
                continue
            nodes.popleft()

            test_info = TestInfo(list(nodes.popleft().itertext())[1])
            while nodes[0].tag != 'h4':
                name = nodes.popleft().text_content()
                code = parse_code_node(nodes.popleft())
                for k, v in FIELD_MAPPING.items():
                    if k in name:
                        setattr(test_info, v, code)
            submission_info.tests.append(test_info)
        return submission_info
