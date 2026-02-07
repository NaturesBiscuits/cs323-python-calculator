from multiprocessing import Process, Manager
import time
import random

def process_grade_mp(grade, results, idx):
    time.sleep(random.uniform(0.2, 1.0))
    results.append(grade)
    print(f"[Process {idx}] processed grade: {grade}")

if __name__ == "__main__":
    n = int(input("How many grades? "))
    grades_list = [float(input(f"Enter grade {i+1}: ")) for i in range(n)]

    with Manager() as manager:
        results = manager.list()
        processes = []

        start = time.perf_counter()

        for i, grade in enumerate(grades_list, start=1):
            p = Process(target=process_grade_mp, args=(grade, results, i))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        final_gwa = sum(results) / len(results)
        end = time.perf_counter()

        print(f"\n[Multiprocessing] Final GWA (all grades): {final_gwa:.2f}")
        print(f"[Multiprocessing] Total Execution Time: {end - start:.4f} seconds")
