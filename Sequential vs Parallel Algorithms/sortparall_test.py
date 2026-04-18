# One Parallel Sorting Algorithm 

import multiprocessing as mp
import heapq
import random
import time


# ---------- Worker ----------
def sort_chunk(chunk, queue):
    chunk.sort()
    queue.put(chunk)


# ---------- Parallel Sort ----------
def parallel_sort(data, num_processes=4):
    if len(data) == 0:
        return data

    chunk_size = len(data) // num_processes
    chunks = [
        data[i:i + chunk_size]
        for i in range(0, len(data), chunk_size)
    ]

    processes = []
    queue = mp.Queue()

    for chunk in chunks:
        p = mp.Process(target=sort_chunk, args=(chunk, queue))
        processes.append(p)
        p.start()

    sorted_chunks = [queue.get() for _ in processes]

    for p in processes:
        p.join()

    return list(heapq.merge(*sorted_chunks))


# ---------- Benchmark Runner ----------
def run_parallel_sort_test(N):
    print(f"\n=== DATASET SIZE: {N} ===")

    # Generate dataset
    data = [random.randint(1, 1_000_000) for _ in range(N)]
    data_copy = data.copy()

    # Measure time
    start = time.time()
    result = parallel_sort(data_copy)
    end = time.time()

    # Validate correctness
    is_correct = result == sorted(data)

    print(f"Parallel Sort Time: {end - start:.6f} seconds")
    print(f"Correctly Sorted: {is_correct}")


# ---------- Main ----------
if __name__ == "__main__":
    run_parallel_sort_test(1_000)
    run_parallel_sort_test(100_000)
    run_parallel_sort_test(1_000_000)
