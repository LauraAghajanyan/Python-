import time


def warn_slow(func):
    def inner(x, y):
        start = time.time()
        result = func(x, y)
        dur = time.time() - start
        if dur > 2:
            print(f'execution of {func.__name__}  with {x, y} arguments took more than 2 seconds')
            print(f'duration is {dur} \nfunction name is {func.__name__} \n {x,y}')
        return result
    return inner


a = int(input("Enter the first argument:"))
b = int(input("Enter the second argument:"))


@warn_slow
def func_slow(a, b):
    time.sleep(3)


@warn_slow
def func_fast(a, b):
    print(a, b)


print(func_slow(a, b))
print(func_fast(a, b))
