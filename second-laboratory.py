import threading
from multiprocessing import Process
import time

def compute_gwa(grades, doer : str):
    gwa = sum(grades) / len(grades)
    print(f"[{doer}]: Calculated GWA: {gwa}")

def do_threading(grades_list : list[float]):
    start_time = time.time()
    threads = []
    for grade in grades_list:
        t = threading.Thread(target=compute_gwa, args=([grade], "Thread",))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end_time = time.time()
    print(f"Total Threading Time: {end_time - start_time:.2f} seconds.")

def do_multiprocessing(grades_list : list[float]):
    start_time = time.time()
    processes = []
    for grade in grades_list:
        p = Process(target=compute_gwa, args=([grade], "Process",))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    end_time = time.time()
    print(f"Total Processing Time: {end_time - start_time:.2f} seconds.")

def main():
    grades_list = list(map(float, input("Enter grades separated by space: ").split()))
    do_threading(grades_list)
    do_multiprocessing(grades_list)

if __name__ == "__main__":
    main()