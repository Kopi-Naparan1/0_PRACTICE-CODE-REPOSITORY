
def exercise_1():
    nums = [1, 2, 3]
    it = iter(nums)
    print(next(it))
    print(next(it))
    print(next(it))


def exercise_2():
    class HiNTimes:
        def __init__(self, n):
            self.count = 0
            self.n = n

        def __iter__(self):
            return self

        def __next__(self):
            if self.count < self.n:
                self.count += 1
                return f"Hi {self.count}"

            else:
                raise StopIteration

    greeter = HiNTimes(5)

    for greet in greeter:
        print(greet)


def exercise_3():
    class Countdown:
        def __init__(self, n):
            self.n = n

        def __iter__(self):
            return self

        def __next__(self):
            if self.n > 0:
                current = self.n
                self.n -= 1
                return current
            else:
                raise StopIteration

    count = Countdown(10)
    for num in count:
        print(f'Countdown: {num}')


def exercise_4():

    for i in range(10, 0, -1):
        print(f'Count:{i}')


def exercise_5():
    def countdown(n):
        for i in range(n, 0, -1):
            yield i

    for num in countdown(10):
        print(f"Countdown: {num}")


def exercise_6():
    def infinite_counter():
        i = 1
        while True:
            yield i
            i += 1

    for num in infinite_counter():
        print(f"Number: {num}")
        if num >= 10:
            break


def exercise_7():
    def even_stream():
        i = 2
        while True:
            yield i
            i += 2

    for num in even_stream():
        print(f"Even Number: {num}")
        if num >= 10:
            break


def exercise_8():
    def fetch_data():
        page = 1
        while True:
            print(f"Fetching page {page}...")
            yield [f"Item {i}" for i in range((page - 1) * 5 + 1, page * 5 + 1)]
            page += 1

    for items in fetch_data():
        print(items)
        if "Item 20" in items:
            break


def exercise_9():
    def batch_numbers(batch_size):
        batch_num = 1
        while True:
            print(f'Batch: {batch_num}')
            yield [f"Item: {i}" for i in range((batch_num - 1) * batch_size + 1, batch_num * batch_size + 1)]
            batch_num += 1

    for item in batch_numbers(batch_size=4):
        print(item)
        if "Item: 25" in item:
            break


def exercise_10():
    list_comprehension = [i for i in range(10)]
    print(list_comprehension)

    generator = (i for i in range(10))
    for num in generator:
        print(num)


def exercise_11():
    import sys

    print(sys.getsizeof([i for i in range(1000)]))  # large
    print(sys.getsizeof((i for i in range(1))))  # tiny


def exercise_12():
    def log_yielded(function):
        def wrapper(*args, **kwargs):
            for value in function(*args, **kwargs):
                print(f"[LOG]: {value}")
                yield value
        return wrapper

    @log_yielded
    def numbers():
        for i in range(1, 6):
            yield i

    for num in numbers():
        print(f'Received: {num}')



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
    # exercise_11()
    exercise_12()

if __name__ == "__main__":
    main()