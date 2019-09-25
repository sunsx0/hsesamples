import time


def params_decorator(decorator):
    def wrapper(f=None, **kwargs):
        if f is None:
            return lambda f: decorator(f, **kwargs)
        else:
            return decorator(f, **kwargs)
    return wrapper


@params_decorator
def time_print(f, *, coeff=1000, unit='ms'):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        work_time = (time.time() - start_time) * coeff
        print(f'{f} work time: {work_time} {unit}')
        return res
    return wrapper


@params_decorator
def magic(f, *, value='nothing'):
    def wrapper(*args, **kwargs):
        print(value)
        return f(*args, **kwargs)
    return wrapper


# fibonacci = time_print(fibonacci)
@magic
def fibonacci(n):
    a = 1
    b = 0
    for _ in range(n):
        a, b = a + b, a
    return a


print(fibonacci(1000))
