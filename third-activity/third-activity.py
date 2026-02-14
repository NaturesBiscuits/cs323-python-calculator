#Part B
from concurrent.futures import ProcessPoolExecutor
import time
import os
from concurrent.futures import ThreadPoolExecutor
import threading

# Deduction functions
def compute_sss(salary):
    print(f"SSS running on thread: {threading.current_thread().name}")
    return salary * 0.045

def compute_philhealth(salary):
    print(f"PhilHealth running on thread: {threading.current_thread().name}")
    return salary * 0.025

def compute_pagibig(salary):
    print(f"Pag-IBIG running on thread: {threading.current_thread().name}")
    return salary * 0.02

def compute_tax(salary):
    print(f"Tax running on thread: {threading.current_thread().name}")
    return salary * 0.10


def task_parallelism_demo(name, salary):
    print(f"\n--- Task Parallelism for {name} (Salary: {salary}) ---")

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            "SSS": executor.submit(compute_sss, salary),
            "PhilHealth": executor.submit(compute_philhealth, salary),
            "Pag-IBIG": executor.submit(compute_pagibig, salary),
            "Tax": executor.submit(compute_tax, salary)
        }

        results = {}
        for key, future in futures.items():
            results[key] = future.result()

    total_deduction = sum(results.values())

    # Display results
    for k, v in results.items():
        print(f"{k}: {v:.2f}")

    print(f"Total Deduction: {total_deduction:.2f}")


if __name__ == "__main__":
    task_parallelism_demo("Alice", 32000)

def task(task_id):
    start = time.time()
    print(f'Task {task_id} START at {start:.2f} (PID {os.getpid()})')
    time.sleep(4)
    end = time.time()
    print(f";Task {task_id} END at {end:.2f} (PID {os.getpid()})")

print('Parallel execution')
start_all = time.time()

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(task, range(4))

end_all = time.time()
print(f"Total time: {end_all - start_all:.2f} seconds")
