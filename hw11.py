# 1. double_result
# This decorator function should return the result of another function multiplied by two
def double_result(func):
    def inner(a, b):
        return func(a, b) * 2

    return inner


def add(a, b):
    return a + b


add(5, 5)  # 10


@double_result
def add(a, b):
    return a + b


add(5, 5)  # 20


# 2. only_odd_parameters
# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise return the string "Please use only odd numbers!"

def only_odd_parameters(func):
    def inner(*args, **kwargs):
        if all(arg % 2 == 0 for arg in args):
            print("Please use only odd numbers!")
        else:
            return func(*args, **kwargs)

    return inner


@only_odd_parameters
def add(a, b):
    return a + b


add(5, 5)  # 10
add(4, 4)  # "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):

def logged(func):
    def with_logging(*args, **kwargs):
        print(f"{func.__name__} was called with ({args}, {kwargs}). Result is {func(*args, **kwargs)}")
        return func(*args, **kwargs)

    return with_logging


@logged
def func(*args, **kwargs):
    return 3 + len(args) + len(kwargs)


func(4, 4, 4)


# you called func(4, 4, 4)
# it returned 6


# 4. type_check
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.

def type_check(correct_type):
    def type_decorator(func):
        def inner(arg):
            if isinstance(arg, correct_type):
                return func(arg)
            else:
                print(f"Wrong Type: {type(arg)}")
        return inner
    return type_decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2('Not A Number')  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated function
