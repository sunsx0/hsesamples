import argparse
import logging
import sys
import os

from daemonize import Daemonize


def get_formatter():
    return logging.Formatter(
        '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
        datefmt='%H:%M:%S',
    )


def configure_logger(args):
    handlers = [
        logging.StreamHandler(sys.stdout),
    ]
    if args.log_path:
        fh = logging.FileHandler(args.log_path, 'a')
        handlers.append(fh)

    for handler in handlers:
        handler.setFormatter(get_formatter())

    logging.basicConfig(
        level=logging.DEBUG,
        handlers=handlers,
    )
    return handlers


def daemon(name, action, args):
    handlers = configure_logger(args)
    if args.daemonize:
        pid = args.pid_path
        keep_fds = [f.stream.fileno() for f in handlers]

        daemon = Daemonize(
            app=name,
            pid=pid,
            action=lambda: action(args),
            keep_fds=keep_fds,
            chdir=os.getcwd(),
        )
        logging.info('start daemon')
        daemon.start()
    else:
        action(args)


def run(name, action, args_parser=None):
    if args_parser is None:
        args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--daemonize', dest='daemonize', action='store_true', required=False, help='Daemonize')
    args_parser.add_argument('--pid', dest='pid_path', required=False, help='Daemon PID path')
    args_parser.add_argument('--log', dest='log_path', required=False, help='Log path')
    daemon(name, action, args_parser.parse_args())
