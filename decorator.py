'''
Your task is to create a decorator named validate_numbers
that ensures the arguments to a function are non-negative numbers.

Create a decorator named validate_numbers.
The validate_numbers decorator
should check if all arguments are numbers
and are non-negative numbers before calling the function.
If any of the arguments is not a number or a non-negative number, 
the function should raise an exception.

Create two functions, add and multiply, both accepting two arguments. 
Decorate them with the validate_numbers decorator.
(to test one of the arguments in the second function should be negative)
'''

def validate_numbers(func):
    def wrapper(*args,**kwargs):
        for arg in args:
            if type(arg) == int or type(arg) == float:
                if arg >=0 :
                    return func(*args,**kwargs)
                else:
                    raise ValueError("You must provide a non-negative number")
            else:
                raise TypeError("You must provide numbers")
    return wrapper


try:
    @validate_numbers
    def add(x,y):
        return x+y
    @validate_numbers
    def multiply(x,y):
        return x*y
    
    print(f"result for add function: {add(10,5)}")
    print(f"result for multiply function: {multiply(-3,1)}")
except Exception as e:
    print(e)
