import random
import time
from multiprocessing import Process, Queue
import math

# Worker function (runs in each process)
def worker(sub_data, target, q, offset):
    for i, value in enumerate(sub_data):
        if value == target:
            q.put(offset + i)  # return global index
            return
    q.put(-1)  # not found in this chunk

# Parallel search function
def parallel_linear_search(data, target, num_processes=4):
    processes = []
    q = Queue()
    chunk_size = math.ceil(len(data) / num_processes)

    for i in range(num_processes):
        start = i * chunk_size
        end = start + chunk_size
        sub_data = data[start:end]

        p = Process(target=worker, args=(sub_data, target, q, start))
        processes.append(p)
        p.start()

    result = -1

    # Collect results
    for _ in processes:
        res = q.get()
        if res != -1:
            result = res

    # Ensure all processes finish
    for p in processes:
        p.join()

    return result


# ==========================
# MAIN PROGRAM
# ==========================
if __name__ == "__main__":
    # 1. Generate dataset (REQUIRED) :contentReference[oaicite:0]{index=0}
    N = 100000  # change to 1000, 100000, 1000000
    data = [random.randint(1, 1000000) for _ in range(N)]

    # 2. Choose target (guaranteed to exist)
    target = data[N // 2]

    # 3. Run parallel search
    start = time.time()
    index = parallel_linear_search(data, target)
    end = time.time()

    print("Target:", target)
    print("Found at index:", index)
    print("Execution time:", end - start)
