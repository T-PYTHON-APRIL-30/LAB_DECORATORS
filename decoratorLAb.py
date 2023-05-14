'''Your task is to create a decorator named validate_numbers that ensures the arguments to a function are
 non-negative numbers.
Create a decorator named validate_numbers.
The validate_numbers decorator should check if all arguments are numbers and are non-negative numbers
 before calling the function. If any of the arguments is not a number or a non-negative number,
   the function should raise an exception.

Create two functions, add and multiply, both accepting two arguments. Decorate them with the 
validate_numbers decorator. (to test one of the arguments in the second function should be negative)'''


def validate_numbers(func):
    def wrapper(x,y):
        if (x < 0 or y <0) or (type(x) != int or type(y) != int):
            raise ValueError('This is a nigative number...')
        else:
            return func(x,y)

    return wrapper
    

@validate_numbers
def add(num1,num2):
    return num1+num2
    
@validate_numbers
def multiplay(num1,num2):
    return num1*num2


print(f'The sum of numbers = {add(1,-2)}')
print(f'The multiplication of numbers = {multiplay(2,-3)}')

