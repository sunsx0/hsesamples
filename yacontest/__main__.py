import os
import logging

from yacontest.api import YaApi
from yacontest.bot import Bot
from yacontest.daemon import run


def main(args):
    logging.info('started =)')

    session_id = os.environ.get('SESSION_ID')
    telegram_token = os.environ.get('TELEGRAM_TOKEN')

    api = YaApi(session_id=session_id)
    bot = Bot(api=api, token=telegram_token)
    bot.run()


if __name__ == '__main__':
    run(
        name='yacontest.bot',
        action=main,
    )
