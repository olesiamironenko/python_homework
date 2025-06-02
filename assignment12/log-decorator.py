# one time setup
import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

# Task 1: Writing and Testing a Decorator
# 1.2: Declare a decorator called logger_decorator. 
# This should log 
#   the name of the called function (func.__name__), 
#   the input parameters of that were passed, and 
#   the value the function returns, to a file ./decorator.log
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        # To write a log record:
        logger.log(logging.INFO, 
           f"function: {func.__name__}\n" 
           f"positional parameters: {list(args) if args else 'none'}\n" 
           f"keyword parameters: {dict(kwargs) if kwargs else 'none'}\n" 
           f"return: {result}\n"
        )

        return result
    return wrapper

# 1.3: Declare a function that takes no parameters and returns nothing. Maybe it just prints "Hello, World!"
@logger_decorator
def hello_world():
    print("Hello, World!")

# 1.4: Declare a function that takes a variable number of positional arguments and returns True
@logger_decorator
def accept_positional_args(*args):
    return True

# 1.5: Declare a function that takes no positional arguments and a variable number of keyword arguments, and that returns logger_decorator
@logger_decorator
def accept_kw_args(**kwargs):
    return logger_decorator

# 1.6: Within the mainline code, call each of these three functions, passing parameters for the functions that take positional or keyword arguments.
if __name__ == "__main__":
    hello_world()
    accept_positional_args(2,3,4)
    accept_kw_args(a='1', b='2', c='3')
