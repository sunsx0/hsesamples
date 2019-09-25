import traceback


counter = 0


def fibonacci(n):
    if n == 1 or n == 0:
        global counter
        counter += 1
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(40))


def go_deeper(n):
    if n == 0:
        traceback.print_stack()
        print('ok')
    else:
        go_deeper(n - 1)


try:
    go_deeper(1000100010001000)
except:
    traceback.print_exc(limit=0)
