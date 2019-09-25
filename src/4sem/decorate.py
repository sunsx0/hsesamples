import time


def time_print(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        work_time = time.time() - start_time
        print(f'{f} work time: {work_time} for args={args} and kwargs={kwargs}')
        return res
    return wrapper


# fibonacci = time_print(fibonacci)
@time_print
def fibonacci(n):
    a = 1
    b = 0
    for _ in range(n):
        a, b = a + b, a
    return a


print(fibonacci(100))
