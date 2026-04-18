#Sequential Searching Algorithm 

import random
import time

def sequentialSearch(arr : list[int], target : int) -> int:
    n = len(arr)

    for i in range(0, n):
        if (arr[i] == target):
            return i
    
    return -1

def run_sequentialSearch(datasetSize : int):
    data = [random.randint(1, 1_000_000) for _ in range(datasetSize)]
    target = random.randint(1, 1_000_000)
    print(f"Running Test: {datasetSize}-element array, searching for {target}")

    start = time.perf_counter()
    result = sequentialSearch(data, target)
    end = time.perf_counter()

    if result == -1: print(f"{target} does not exist in array.")
    else: print(f"{target} exists at index {result}.")
    print(f"Time Taken: {end - start:.4f} seconds")
    print()
    print()

if __name__ == "__main__":
    run_sequentialSearch(100)
    run_sequentialSearch(1000)
    run_sequentialSearch(10000)
    run_sequentialSearch(100000)
    run_sequentialSearch(1000000)