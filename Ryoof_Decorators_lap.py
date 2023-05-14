# # LAB_DECORATORS

# ### Your task is to create a decorator named `validate_numbers` that ensures the arguments to a 
# function are non-negative numbers.

# ### Create a decorator named `validate_numbers`.
# - The `validate_numbers` decorator should check if all arguments are numbers and are non-negative
# numbers before calling the function.
# If any of the arguments is not a number or  a non-negative number, the function should raise an 
# exception.

# - Create two functions, add and multiply, both accepting two arguments.
#  Decorate them with the `validate_numbers` decorator. 
# (to test one of the arguments in the second function should be negative)

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if type(arg) != int:
               raise Exception (f"You {func.__name__} {arg} are not int values type, please try again with appropriate values")
            elif arg < 0 :
                raise Exception (f"You {func.__name__} {arg} are not positive value, please try again with appropriate values")
        return func(*args, **kwargs)
    return wrapper

           
@validate_numbers
def add(x,y):
    return x+y

@validate_numbers
def multiply(x,y):
    return x*y

print(multiply("iuy",7))
print(add(8,-9))
