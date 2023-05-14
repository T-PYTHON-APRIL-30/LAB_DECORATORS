def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for check in args:
            if check < 0 or not isinstance(check, (int,float)):
                raise Exception("the value is not a positiv or not a number!")
    
        return func(*args,**kwargs)
    
    return wrapper


@validate_numbers
def add(num_1:int, num_2:int):
    result = num_1 + num_2
    return result


@validate_numbers
def multiply(number_1:int, number_2:int):
    result = number_1 * number_2
    return result


print(add(10,5))


print(multiply(20,-10))