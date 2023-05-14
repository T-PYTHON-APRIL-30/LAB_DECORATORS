'''
The validate_numbers decorator should check if all arguments
are numbers and are non-negative numbers before calling the function.
If any of the arguments is not a number or a non-negative number,
the function should raise an exception.

Create two functions, add and multiply, both accepting two arguments.
Decorate them with the validate_numbers decorator.
(to test one of the arguments in the second function should be negative)

'''
def validate_numbers(func):
    def wrapper(*args,**kwargs):
        for arg in args:
            if type(arg) == int:
                if arg >0 :
                    return func(*args,**kwargs)
                else:
                    raise Exception("Enter validate_numbers (non-negtive)")
            else:
                raise Exception("provide numbers")
    return wrapper


try:
    @validate_numbers
    def add(x,y):
        return x+y
    @validate_numbers
    def multiply(x,y):
        return x*y

    print(f"result for add function: {add(9,7)}")
    print(f"result for multiply function: {multiply(-8,6)}")
except Exception as e:
    print(e)