import random
import threading
import time
import multiprocessing


def exercise_1():
    def say_hello():
        print('Hello world')
    thread_1 = threading.Thread(target=say_hello)
    thread_2 = threading.Thread(target=say_hello)
    thread_3 = threading.Thread(target=say_hello)
    thread_4 = threading.Thread(target=say_hello)
    thread_5 = threading.Thread(target=say_hello)

    threads = [thread_1, thread_2, thread_3, thread_4, thread_5]
    for thread in threads:
        thread.start()
        thread.join()


def exercise_2():
    def api_loader(api_num):
        start = time.time()
        time.sleep(random.uniform(1,3))
        print(f'API {api_num} is loaded')
        end = time.time()
        print(f"Loading time: {end - start:.2f} secs\n")

    threads = []
    for i in range(10):
        t = threading.Thread(target=api_loader, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    print('\nAll APIs are loaded\n')


def raise_10(n):
    return n ** 10


def exercise_3():

    with multiprocessing.Pool() as pool:
        results = pool.map(raise_10, range(20))
    print(list(results))


COUNT_LIMIT = 1_000_000  # adjust if your CPU can't handle this
THREADS = 5
PROCESSES = 5


def count():
    total = 0
    for i in range(COUNT_LIMIT // THREADS):  # divide work across threads or procs
        total += i
    return total


def exercise_4():
    print("Regular loop:")
    start = time.perf_counter()
    count()  # just once
    end = time.perf_counter()
    print(f'→ Time: {end - start:.2f} seconds\n')


def exercise_5():
    print("Multithreading:")

    def thread_target():
        count()

    threads = []
    start = time.perf_counter()

    for _ in range(THREADS):
        t = threading.Thread(target=thread_target)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end = time.perf_counter()
    print(f'→ Time: {end - start:.2f} seconds\n')


def exercise_6():
    print("Multiprocessing:")

    def process_target():
        count()

    processes = []
    start = time.perf_counter()

    for _ in range(PROCESSES):
        p = multiprocessing.Process(target=process_target)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    end = time.perf_counter()
    print(f'→ Time: {end - start} seconds\n')


def exercise_7():
    def file_downloader(i):
        print('-' * 30)
        print(f'\nFile {i+1} is downloading...')
        start = time.perf_counter()
        time.sleep(random.uniform(1, 5))
        end = time.perf_counter()
        print(f'File {i+1} is downloaded...')
        print(f'Downloading time:{end - start:.2f} seconds...')
        print('-' * 30)
        print('')

    threads = []
    for i in range(9):
        t = threading.Thread(target=file_downloader, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print('====All file are downloaded...====')


def main():
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # exercise_5()
    # exercise_6()
    exercise_7()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
