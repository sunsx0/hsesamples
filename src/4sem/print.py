import datetime


def time_print(*args, **kwargs):
    print(f'[{datetime.datetime.now()}]', *args, **kwargs)


time_print(123123, 31231231)
