def validate_numbers (fun):
    def wrapper(*args, **kwargs):
        for number in args:
            if not isinstance(number, (int, float)) or number < 0 :
                raise Exception("invalid number")
        result = fun(*args, **kwargs)
        return result
    return wrapper



@validate_numbers
def addition(x,y):
    result = x + y
    return result
@validate_numbers
def multiply(x,y):
    result = x * y
    return result


try:
    print(addition (5,5))
    print(multiply(-3,3))
except Exception as e:
    print (e)