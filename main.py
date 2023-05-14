def validate_numbers(func):
    def wrapper(*args, **kwargs):
        list1=[]
       
        for i in range(len(args)):
          if type(args[i])!=(int or float) or args[i]<0:
                raise Exception("the value shoud be non-negative number")
        for i in kwargs:
            if type(kwargs[i])!=(int or float) or kwargs[i]<0:
                raise Exception("the value shoud be non-negative number")


        return func(*args,**kwargs)
                
    return wrapper

@validate_numbers
def add_values(x,y):
    print(x+y)


@validate_numbers    
def multiply_value(x,y):
    print(x*y)


add_values(1,y=-6)
multiply_value(4,4)