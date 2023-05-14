def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg < 0:
                raise Exception("There's some error, either number is negative or the input not a number.")
        
        return func(*args, **kwargs)
        
    return wrapper


@validate_numbers
def add(num1, num2):
    return num1 + num2


@validate_numbers
def multiply(num1, num2):
    return num1 * num2


try:
    print(f"add function: {add(15, 20)}")
    print(f"multiply function: {multiply(-20, 11)}")
except Exception as e:
    print(e)