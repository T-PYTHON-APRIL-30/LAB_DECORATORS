def validate_numbers (func):
    def new_Warpper(*args,**kwargs):

        print("Befor Run Method")
        for arg in args:
         arg = int(arg)
         if arg < 0 or type(arg) != int :
           raise print("you shoud enter positive number Or you shoud enter positive number")
         return func(*args,**kwargs)
        print("After Run Method")

    return new_Warpper


@validate_numbers 
def Add(num1,num2):
    result = num1 + num2
    return result
@validate_numbers 
def Multiply(x,y):
    result = x*y
    return result

# Calling Functions
print(Add(-1,"eee"))
print(Multiply(5,5))