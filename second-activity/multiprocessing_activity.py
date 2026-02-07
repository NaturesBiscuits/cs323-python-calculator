from multiprocessing import Process
import time
import random

def compute_gwa_process(grade, idx):
    time.sleep(random.uniform(0.3, 1.5))
    gwa = grade
    print(f"[Process {idx}] GWA: {gwa}")

if __name__ == "__main__":
    n = int(input("How many grades? "))
    grades_list = [float(input(f"Enter grade {i+1}: ")) for i in range(n)]

    start = time.perf_counter()

    processes = []
    for i, grade in enumerate(grades_list, start=1):
        p = Process(target=compute_gwa_process, args=(grade, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.perf_counter()
    print(f"\n[Multiprocessing] Total Execution Time: {end - start:.4f} seconds")
