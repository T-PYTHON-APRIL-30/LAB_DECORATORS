'''
Your task is to create a decorator named validate_numbers that ensures the arguments to a function are non-negative numbers.
Create a decorator named validate_numbers.
The validate_numbers decorator should check if all arguments are numbers and are non-negative numbers before calling the function. If any of the arguments is not a number or a non-negative number, the function should raise an exception.
Create two functions, add and multiply, both accepting two arguments. Decorate them with the validate_numbers decorator. (to test one of the arguments in the second function should be negative)
'''

def validate_numbers(fun):
    def wrapper(*args, **kwargs):
        
        for arg in args + tuple(kwargs.values()):
            if not isinstance(arg, (int,float)):
               raise Exception ("The input is not a number")
            if arg < 0:
                raise Exception ("The input is negative")
        return fun(*args, **kwargs)
    return wrapper
    
    

@validate_numbers
def add(num1 :int ,num2 :int):
    result :int = num1 + num2
    return(f"\nThe result of the addition = {result}\n")
@validate_numbers
def multiply(num1, num2):
    result = num1 * num2
    return(f"\nThe result of the multiply = {result}\n")

print(add(1,10))
print(multiply(10,20))
print(add("i",2))
print(multiply(-10,20))