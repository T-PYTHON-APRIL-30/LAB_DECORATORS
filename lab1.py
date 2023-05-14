# LAB_DECORATORS

def validate_numbers(fun):
    def wrapper(*args, **kwargs):

        # since args is a tuple and kwargs is a dict we need to change kwargs to tuple
        for i in args + tuple(kwargs.values()):
            # we could use: "if not instance(i,(int, float)):"
            if type(i) != float and type(i) != int:
                raise Exception("only accept numbers")
            if i < 0:
                raise Exception("number is negative")

            if type(i) != float and type(i) != int:
                raise Exception("only accept numbers")
        return fun(*args, **kwargs)

    return wrapper


@validate_numbers  # calling the wrapper for the function
def add_function(x, y):
    return print(x+y)


@validate_numbers  # calling the wrapper for the function
def multiply_function(x, y):
    return print(x*y)


# variables
number = 5
number2 = 10
number3 = -10


# function calls
add_function(number, number2)
multiply_function(number, number3)
