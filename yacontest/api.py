import requests
import typing

import dataclasses as dc

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


@dc.dataclass
class SubmissionInfo:
    contest_name: str = ''
    task: str = ''
    participant: str = ''
    tests: typing.List[TestInfo] = dc.field(default_factory=list)


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

        with open('tmp.html', 'w') as f:
            f.write(resp)

        submission_info = SubmissionInfo(
            contest_name=inline_text(content.xpath('table/tr[2]/td[2]/a')[0].text),
            task=inline_text(content.xpath('table/tr[3]/td[2]/a')[0].text),
            participant=content.xpath('table/tr[4]/td[2]')[0].text,
        )

        nodes = content.xpath('div[8]/*')
        for i in range(0, len(nodes), 13):
            test_info = TestInfo(
                name=list(nodes[i + 2].itertext())[1],
                test_input=parse_code_node(nodes[i + 4]),
                output=parse_code_node(nodes[i + 6]),
                answer=parse_code_node(nodes[i + 8]),
                checker=parse_code_node(nodes[i + 10]),
            )
            submission_info.tests.append(test_info)
        return submission_info
