def validate_numbers(check):
    def wrapper(*args,**kwargs):
        f = check(*args,**kwargs)
        for  args in args + tuple(kwargs):
            if not isinstance(args,(int,float)):
                raise Exception("The input is not a number") 
            
            if args <0:
                raise Exception("The input is not a positive number")
            
        return f
    return wrapper

@validate_numbers        
def numbers_mult (x,y):
    return x*y

print(numbers_mult(6,5))

@validate_numbers
def numbers_add (x,y):
    return x+y

print (numbers_add(8,9))
