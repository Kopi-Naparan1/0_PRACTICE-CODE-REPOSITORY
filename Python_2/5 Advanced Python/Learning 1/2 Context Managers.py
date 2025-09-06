
def exercise_1():
    class MyContext:
        def __enter__(self):
            print('--Entrance--')
            return 'I am the context'

        def __exit__(self, exc_type, exc_val, exc_tb):
            print('--Exit--')

    with MyContext() as obj:
        print(obj)


def exercise_2():
    with open("data.txt", "w") as f:
        f.write("hello")
        f.writelines('This is\n Hello\n World\n Okay?')


def exercise_3():
    with open("a.txt", 'w') as a, open('b.txt', "w") as b:
        a.write("hallo a")
        b.write('hello b')


def exercise_4():
    import time
    import random

    class Load:
        def __enter__(self):
            print('Entering...')
            return self #  ?

        def __exit__(self, exc_type, exc_val, exc_tb):
            print('Exiting...')

    with Load():
        start = time.time()
        time.sleep(random.uniform(1,5))
        end = time.time()
        result = end - start
        print(f'Loading time: {result:.4f} secs')


def exercise_5():
    from contextlib import contextmanager

    @contextmanager
    def open_file(path):
        f = open(path)
        try:
            yield f

        finally:
            f.close()


def exercise_6():
    with open('test_1.txt', 'r') as f:
        content = f.read()
        print(content)


def exercise_7():
    class MyManager:
        def __enter__(self):
            print('Entering...')
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            print('Exiting...')

    with MyManager():
        print('I am inside!')


def exercise_8():
    import time, random

    class LoadingTime:
        def __enter__(self):
            pass

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

    with LoadingTime():
        start = time.time()
        print('Fetching datas...')
        time.sleep(random.uniform(1, 4))
        end = time.time()
        result = end - start
        print(f'Total loading time: {result:.3f} secs')


def exercise_9():
    from contextlib import contextmanager

    @contextmanager
    def open_resource():
        print('--- Start ---')
        yield "Resource 1"
        print('--- End ---')

    with open_resource() as x:
        print(f'opened: {x}')


def exercise_10():
    with open('test_1.txt', "w") as f:
        f.writelines('Line 1\nLine 2\nLine 3 ')

    print('--- Lines ---')
    with open('test_1.txt' , 'r') as f:
        print(f.read())




def main():
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # exercise_5()
    # exercise_6()
    # exercise_7()
    # exercise_8()
    # exercise_9()
    # exercise_10()


if __name__ == "__main__":
    main()