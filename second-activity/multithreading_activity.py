import threading
import time
import random

def compute_gwa_thread(grade, idx):
    time.sleep(random.uniform(0.3, 1.5))  # simulate variable work
    gwa = grade
    print(f"[Thread {idx}] GWA: {gwa}")

n = int(input("How many grades? "))
grades_list = [float(input(f"Enter grade {i+1}: ")) for i in range(n)]

start = time.perf_counter()

threads = []
for i, grade in enumerate(grades_list, start=1):
    t = threading.Thread(target=compute_gwa_thread, args=(grade, i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.perf_counter()
print(f"\n[Multithreading] Total Execution Time: {end - start:.4f} seconds")
