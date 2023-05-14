# LAB_DECORATORS

### Your task is to create a decorator named `validate_numbers` that ensures the arguments to a function are non-negative numbers.

### Create a decorator named `validate_numbers`.
- The `validate_numbers` decorator should check if all arguments are numbers and are non-negative numbers before calling the function.
If any of the arguments is not a number or  a non-negative number, the function should raise an exception.

- Create two functions, add and multiply, both accepting two arguments. Decorate them with the `validate_numbers` decorator. (to test one of the arguments in the second function should be negative)
