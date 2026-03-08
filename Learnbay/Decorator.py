def decorator_function(original_function):

    def wrapper():
        print("print the fucntion Calling")
        original_function()
        print("after the function calling")

    return wrapper


@decorator_function
def hello():
    print("Hello function calling")


hello()