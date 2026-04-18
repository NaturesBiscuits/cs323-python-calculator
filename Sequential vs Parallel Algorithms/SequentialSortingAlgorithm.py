# Sequential Sorting Algorithm

import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

def run_test(dataset_name, data):
    print(f"\nRunning test for: {dataset_name}")
    print("Number of elements:", len(data))

    start = time.time()
    insertion_sort(data)
    end = time.time()

    print("Time taken:", end - start, "seconds")


small_data = [random.randint(1, 1_000_000) for _ in range(1000)]
run_test("Small Dataset (1,000 elements)", small_data)


medium_data = [random.randint(1, 1_000_000) for _ in range(100000)]
run_test("Medium Dataset (100,000 elements)", medium_data)


large_data = [random.randint(1, 1_000_000) for _ in range(1000000)]
run_test("Large Dataset (1,000,000 elements)", large_data)


sorted_data = list(range(1000))
run_test("Special Case — Already Sorted Data", sorted_data)
