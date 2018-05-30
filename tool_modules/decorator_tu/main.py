'''
Created on May 31, 2018
'''


def my_decorator_decorator(*args, **kwargs):

    arg1 = args[0]
    arg2 = args[1]

    def my_decorator(some_function):

        def wrapper(*args, **kwargs):
            print(arg1, arg2)
            print("Something is happening before some_function() is called.")
            original_fun = some_function(*args, **kwargs)
            print("Something is happening after some_function() is called.")
            return original_fun

        return wrapper

    return my_decorator


@my_decorator_decorator("arg1", "arg2")
def just_some_function(a: int):
    print("Wheee!")
    print(a)

# Syntactic Sugar as @my_decorator
# just_some_function = my_decorator(just_some_function)


just_some_function(1)

if __name__ == '__main__':
    pass
