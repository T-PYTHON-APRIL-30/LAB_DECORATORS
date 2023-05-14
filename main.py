'''
Your task is to create a decorator named validate_numbers that ensures the arguments to a function are non-negative numbers.
Create a decorator named validate_numbers.
The validate_numbers decorator should check if all arguments are numbers and are non-negative numbers before calling the function. If any of the arguments is not a number or a non-negative number, the function should raise an exception.
Create two functions, add and multiply, both accepting two arguments. Decorate them with the validate_numbers decorator. (to test one of the arguments in the second function should be negative)
'''


from curses.ascii import isdigit


def validate_numbers(fun):
    def wrapper(*args, **kargs):
        
        for arg in args:
            if type(arg) != int:
               raise Exception ("The input is not a number")
            elif arg < 0:
                raise Exception ("The input is negative")
        fun(*args, **kargs)
    return wrapper
    
    

@validate_numbers
def add(num1 :int ,num2 :int):
    result :int = num1 + num2
    print(f"\nThe result of the addition = {result}\n")
@validate_numbers
def multiply(num1, num2):
    result = num1 * num2
    print(f"\nThe result of the multiply = {result}\n")

add(1,10)
multiply(10,20)
multiply(-10,20)