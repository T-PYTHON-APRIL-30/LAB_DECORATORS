
def no_negative_argu(func):
    def wrapper(x,y):
        print("before")
        if  type(x) == int and type(y) == int:
            if x > 0 and y > 0:
                res = func(x,y)
                print("after")
                return res
            else:
                raise Exception("negative number")
        else:
            raise Exception("Input not integer")
    return wrapper


@no_negative_argu
def add(x,y):
    return x+y

@no_negative_argu
def multiply(x,y):
    return x*y

try:
    print(add(-20,20))
    
except Exception as e:
    print(e)

print("--")
try:
   
    print(multiply("ff",20))

except Exception as e:
    print(e)

print("--")
try:
    print(add(10,20))
    print("--")
    print(multiply(10,20))

except Exception as e:
    print(e)




    
'''
def no_negative_argu(func):
    def wrapper(*args,**kwargs):
        print("before")
        for num in args:
            if type(args[num]) == int:
                if args[num] > 0:
                    res = func(*args,**kwargs)
                    print("after")
                    return res 
                else:
                    raise Exception("negative number")
            else:
                raise Exception("Input not integer")
    return wrapper


@no_negative_argu
def add(x,y):
    return x+y

@no_negative_argu
def multiply(x,y):
    return x*y

try:
    print(add(-20,20))
    
except Exception as e:
    print(e)

print("--")
try:
   
    print(multiply("ff",20))

except Exception as e:
    print(e)

print("--")
try:
    print(add(10,20))
    print("--")
    print(multiply(10,20))

except Exception as e:
    print(e)'''