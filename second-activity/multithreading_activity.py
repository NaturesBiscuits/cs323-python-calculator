import threading
import time
import random

def process_grade(grade, results, idx, lock):
    # Simulate independent processing per subject
    time.sleep(random.uniform(0.2, 1.0))
    with lock:
        results.append(grade)
        print(f"[Thread {idx}] processed grade: {grade}")

n = int(input("How many grades? "))
grades_list = [float(input(f"Enter grade {i+1}: ")) for i in range(n)]

results = []
lock = threading.Lock()
threads = []

start = time.perf_counter()

for i, grade in enumerate(grades_list, start=1):
    t = threading.Thread(target=process_grade, args=(grade, results, i, lock))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

final_gwa = sum(results) / len(results)
end = time.perf_counter()

print(f"\n[Multithreading] Final GWA (all grades): {final_gwa:.2f}")
print(f"[Multithreading] Total Execution Time: {end - start:.4f} seconds")
