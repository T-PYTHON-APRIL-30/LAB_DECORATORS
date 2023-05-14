def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for number in args:
            if type(number) != int:
                raise ValueError("parameter isn't number!, you should write all parameter as a number")
            if number < 0:
                raise ValueError("parameter is negitive number!, you should write all parameter as a positve number")
            
        return func(*args, **kwargs)
    return wrapper

@validate_numbers
def add(num1: int, num2:int):
    return num1 + num2

@validate_numbers
def multiply(num1: int, num2:int):
    return num1 * num2

print(add(5,6))
print(multiply(-4, 8))
