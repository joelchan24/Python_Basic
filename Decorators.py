import functools


def make_upper(func):
    @functools.wraps(func)  #This decorator changes the debugging rules UwU
    def wrapper():
        return func().upper()
    
    return wrapper


def reverse_str(func):
    def wrapper():
        return func()[::-1]
    return wrapper

@reverse_str
@make_upper
def python_greeting():
    return "I am Python Developer"

# Calling the fuction decorated
print(python_greeting())



def decorate_sum(func):
    def wrapper(num1, num2):
        
        print(f"Values to sum are {num1} and {num2}")
        return func(num1,num2)
    return wrapper

@decorate_sum
def sum(num1,num2):
    return num1 + num2


print(sum(5,6))


# Arguments

def multiply_result(num_3):
    def inner_decorator(func):
        def wrapper(arg1, arg2):
            print(f'({arg1} + {arg2}) * {num_3}:')
            return func(arg1, arg2) * num_3 
        return wrapper
    return inner_decorator

@multiply_result(3)
def sum_nums(num_1, num_2):
    return num_1 + num_2

print(sum_nums(1, 2))