def valideate_numbers(fnuc):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg<0:
                raise ValueError ("all arguments must be non negative numbers")
        return fnuc(*args)
    return wrapper
    
        
@valideate_numbers
def add(a, b):
    return a+b

@valideate_numbers
def multiply (a, b):
    return a*b
