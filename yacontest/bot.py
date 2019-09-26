import enum
import html
import logging

from yacontest.api import YaApi, SubmissionInfo, TestInfo
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


BOT_HELP = (
    'Help:',
    '/gettest - respond last test by submission id',
    '/cancel - cancel current action'
    '/help - this text',
)


def render_test_report(test_info: TestInfo):
    return '\n'.join((
        f'<i>{html.escape(test_info.name)}</i>',
        f'<b>Input:</b>',
        f'<code>{html.escape(test_info.test_input)}</code>',
        f'<b>Output:</b>',
        f'<code>{html.escape(test_info.output)}</code>',
        f'<b>Answer:</b>',
        f'<code>{html.escape(test_info.answer)}</code>',
        f'<b>Checker:</b>',
        f'<code>{html.escape(test_info.checker)}</code>',
    ))


def render_submission_report(submission: SubmissionInfo):
    tests = submission.tests
    return '\n'.join((
        f'<b>{html.escape(submission.contest_name)} / {html.escape(submission.task)}</b>',
        render_test_report(tests[-1]) if tests else '<i>tests not found</i>',
    ))


class StateType(enum.Enum):
    Default = 'default'
    GetTest = 'gettest'


class Bot:
    def __init__(self, api: YaApi, token: str):
        self.logger = logging.getLogger('bot')

        self.api = api
        self.token = token
        self.updater = Updater(token, use_context=True)
        self.dispatcher = self.updater.dispatcher

        self.dispatcher.add_handler(CommandHandler("start", self.on_start))
        self.dispatcher.add_handler(CommandHandler("gettest", self.on_get_test))
        self.dispatcher.add_handler(CommandHandler("cancel", self.on_get_test))
        self.dispatcher.add_handler(CommandHandler("help", self.on_help))
        self.dispatcher.add_handler(MessageHandler(Filters.text, self.on_text))
        self.dispatcher.add_error_handler(self.on_error)

    def reply_help(self, update, head=None):
        head_items = ()
        if head is not None:
            head_items = (head, '')
        update.message.reply_text('\n'.join(head_items + BOT_HELP))

    def on_start(self, update, context):
        self.reply_help(update)

    def on_help(self, update, context):
        self.reply_help(update)

    def on_cancel(self, update, context):
        cur_state = context.chat_data.get('state', StateType.Default)
        if cur_state != StateType.Default:
            context.chat_data['state'] = StateType.Default
            self.reply_help(update, head=f'OK, {cur_state} action cancelled')
        else:
            self.reply_help(update, head='Nothing cancel')

    def on_get_test(self, update, context):
        context.chat_data['state'] = StateType.GetTest
        update.message.reply_text('OK, send me submission id')

    def on_text(self, update, context):
        if context.chat_data.get('state', StateType.Default) == StateType.GetTest:
            submission_id = update.message.text.strip()
            self.logger.info(f'run_report request from {update.message.from_user}: {submission_id}')

            submission_info = self.api.run_report(submission_id)
            update.message.reply_text(
                render_submission_report(submission_info),
                parse_mode=ParseMode.HTML,
            )
            context.chat_data['state'] = StateType.Default

    def on_error(self, update, context):
        self.logger.warning('Update \"%s\" caused error \"%s\"', update, context.error)
        context.chat_data['state'] = StateType.Default

    def run(self):
        self.updater.start_polling()
        self.updater.idle()
