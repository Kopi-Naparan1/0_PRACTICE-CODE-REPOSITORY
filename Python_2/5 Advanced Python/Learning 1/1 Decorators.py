

def exercise_1():
    def logger(function):
        def wrapper():
            print("Calling function...")
            function()
        return wrapper


    @logger
    def greet():
        print("Hello from greet!")

    def exercise_1_main():
        greet()
    exercise_1_main()


def exercise_2():
    import time
    import random

    def time_decorator(function):
        def wrapper():
            start = time.time()
            function()
            end = time.time()
            total = end - start
            print(f'Start: {start:.2f}\nEnd: {end:.2f}\n\tTotal time: {total:.2f}')
        return wrapper

    @time_decorator
    def greet():
        time.sleep(random.uniform(1,5))
        print('Hi I am from greet! ')


    def exercise_2_main():
        greet()
    exercise_2_main()


def exercise_3():
    def repeat(times):
        def decorator(function):
            def wrapper():
                for i in range(times):
                    function(i)
            return wrapper
        return decorator

    @repeat(times=3)
    def greet(i):
        print(f"Hi this is a greeting from ({i+1})")

    def exercise_3_main():
        greet()
    exercise_3_main()


def exercise_4():
    def log_action(function):
        def wrapper():
            print('Action Started')
            function()
            print('Action Finished')
        return wrapper

    @log_action
    def doing_something():
        print('Doing something important')

    doing_something()


def exercise_5():
    def log_action(function):
        def wrapper(*args, **kwargs):
            print('Start')
            function(*args, **kwargs)
            print('End')
        return wrapper

    @log_action
    def greet(name):
        print(f"Hi there {name}")

    @log_action
    def add(a, b):
        print(f"Sum is {a + b}")

    greet("Kopi")
    greet("Nyro")
    greet("Kophalem")

    add(5,5)


def exercise_6():
    def log(function):
        def wrapper(*args, **kwargs):
            print('Start')
            result = function(*args, **kwargs)
            print('End')
            return result
        return wrapper

    @log
    def greet(name, mood="happy"):
        return f'Hi {name}!, You are {mood} '

    message = greet("Nyro", "Excited")
    print(f'Returned: {message}')


def exercise_7():
    def log(function):
        def wrapper(*args, **kwargs):
            print(f"Calling function {function.__name__} with args: {args} and kwargs: {kwargs}")
            result = function(*args, **kwargs)
            print(f"Function {function.__name__} returned: {result}")
            return result

        return wrapper

    @log
    def multiply(x, y):
        return x * y
    multiply(5,5)


def exercise_8():
    import time
    import random

    def timer(function):
        def wrapper(*args, **kwargs):
            print(f"Calling function {function.__name__} with args: {args} and kwargs: {kwargs}")
            start = time.time()
            product = function(*args, **kwargs)
            end = time.time()
            print(f'Total loading time: {end - start:.4f} seconds')
            print(f"Function {function.__name__} returned: {product}")
            return product
        return wrapper

    @timer
    def multiply(x, y, z):
        time.sleep(random.uniform(1,5))
        return x * y * z
    multiply(5, 5, 5)













def main():
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # exercise_5()
    # exercise_6()
    # exercise_7()
    exercise_8()


if __name__ == "__main__":
    main()