"""# LAB_DECORATORS

### Your task is to create a decorator named `validate_numbers` that ensures the arguments to a function are non-negative numbers.

### Create a decorator named `validate_numbers`.
- The `validate_numbers` decorator should check if all arguments are numbers and are non-negative numbers before calling the function.
If any of the arguments is not a number or  a non-negative number, the function should raise an exception.

- Create two functions, add and multiply, both accepting two arguments. Decorate them with the `validate_numbers` decorator. (to test one of the arguments in the second function should be negative)
"""


def validate_numbers(func):
    def wrapper(*args):
        for arg in args:
            if  not isinstance(arg, (int, float)):
                raise NameError("should be a number")
            elif arg < 0:
                raise ValueError("negative number not exepted")
        return func(*args)
    return wrapper

@validate_numbers
def addnumbers(number1,number2):
    return number1+number2

@validate_numbers
def multiplynumbers(number1,number2):
    return number1*number2   


print(addnumbers(9,9))
print(multiplynumbers(5,8))

