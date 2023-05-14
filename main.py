def validate_numbers(fun):
    def wrapper(*args,**kwargs):
        for i in args:
            if type(i) != int or i < 0 :
                raise Exception("Only expect positive numbers !!")
        return fun(*args,**kwargs)
    return wrapper

@validate_numbers
def add(num1:int,num2:int) -> int :
    return num1+num2
@validate_numbers
def multiply(num1:int,num2:int) -> int :
    return num1*num2

try:
    print(add(2,3))
except Exception as e:
    print(e)
try:
    print(multiply(2,8))
except Exception as e:
    print(e)