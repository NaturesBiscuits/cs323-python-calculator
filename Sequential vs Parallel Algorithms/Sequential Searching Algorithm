#Sequential Searching Algorithm 

import random
import time

import multiprocessing as mp
import heapq



data = [random.randint(1, 1_000_000) for _ in range(100)]
# Same ra na datasets atong gamiton guys

def sequentialSearch(arr : list[int], x : int) -> int:
    n = len(arr)

    for i in range(0, n):
        if (arr[i] == x):
            return i
    
    return -1

def getInputNumber(prompt : str):
    while True:
        try: return float(input(prompt))
        except: print("Please enter a number.")

def main():
    while True:
        print("(1) Sequential Search")
        print("(0) Quit")

        myInput : int
        while True:
            myInput = int(getInputNumber("> "))
            if myInput >= 0 < 2: break
            print("Please choose a number from 0 to 1")
        
        if myInput == 0: break

        match myInput:
            case 1:
                x = int(getInputNumber("Enter integer to search: "))
                start = time.perf_counter()
                result = sequentialSearch(data, x)
                end = time.perf_counter()

                if result == -1: print(f"{x} does not exist in array.")
                else: print(f"{x} exists at index {result}.")
                print(f"Total Execution Time: {end - start:.4f}")

if __name__ == "__main__":
    main()
    print("Goodbye :)")


