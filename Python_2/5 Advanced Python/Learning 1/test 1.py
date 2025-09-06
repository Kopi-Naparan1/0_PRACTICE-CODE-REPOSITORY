import time
import threading
import multiprocessing

COUNT = 100_000_000
BATCH_SIZE = 20_000_000


# =========================
# REGULAR LOOP
# =========================
def count_regular():
    start = time.perf_counter()
    for i in range(1, COUNT + 1):
        if i % BATCH_SIZE == 0:
            print(f"[REGULAR] Counted to: {i}")
    end = time.perf_counter()
    print(f"[REGULAR] Time taken: {end - start:.2f} seconds")


# =========================
# MULTITHREADING
# =========================
def thread_worker(start_i, end_i):
    for i in range(start_i, end_i + 1):
        if i % BATCH_SIZE == 0:
            print(f"[THREAD] Counted to: {i}")

def count_threading():
    start = time.perf_counter()
    threads = []
    num_threads = 4
    step = COUNT // num_threads

    for i in range(num_threads):
        t_start = i * step + 1
        t_end = (i + 1) * step
        t = threading.Thread(target=thread_worker, args=(t_start, t_end))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.perf_counter()
    print(f"[THREADING] Time taken: {end - start:.2f} seconds")


# =========================
# MULTIPROCESSING
# =========================
def process_worker(start_i, end_i):
    for i in range(start_i, end_i + 1):
        if i % BATCH_SIZE == 0:
            print(f"[PROCESS] Counted to: {i}")

def count_multiprocessing():
    start = time.perf_counter()
    processes = []
    num_processes = multiprocessing.cpu_count()
    step = COUNT // num_processes

    for i in range(num_processes):
        p_start = i * step + 1
        p_end = (i + 1) * step
        p = multiprocessing.Process(target=process_worker, args=(p_start, p_end))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.perf_counter()
    print(f"[MULTIPROCESSING] Time taken: {end - start:.2f} seconds")


# =========================
# MAIN EXECUTION
# =========================
if __name__ == "__main__":
    print("\n=== Regular For Loop ===")
    count_regular()

    print("\n=== Multithreading ===")
    count_threading()

    print("\n=== Multiprocessing ===")
    count_multiprocessing()
