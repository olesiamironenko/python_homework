# Task 2: A Decorator that Takes an Argument
# 2.2: Declare a decorator called type_converter. It has one argument called type_of_output
def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

# 2.3: Write a function return_int() that 
#   takes no arguments and 
#   returns the integer value 5. 
# Decorate that function with type-decorator. 
# Pass str as the parameter to type_decorator.
@type_converter(str)
def return_int():
    return 5

# 2.4: Write a function return_string() that 
#   takes no arguments and 
#   returns the string value "not a number". 
# Decorate that function with type-decorator. 
# Pass int as the parameter to type_decorator
@type_converter(int)
def return_string():
    return "not a number"

if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__) # This should print "str"
    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!") # This is what should happen