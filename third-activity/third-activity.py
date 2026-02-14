#Part B
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import time
import os
import threading

# Deduction functions
def compute_sss(salary):
    thread = threading.current_thread().name
    print(f"SSS running on thread: {thread}")
    return salary * 0.045

def compute_philhealth(salary):
    thread = threading.current_thread().name
    print(f"PhilHealth running on thread: {thread}")
    return salary * 0.025

def compute_pagibig(salary):
    thread = threading.current_thread().name
    print(f"Pag-IBIG running on thread: {thread}")
    return salary * 0.02

def compute_tax(salary):
    thread = threading.current_thread().name
    print(f"Tax running on thread: {thread}")
    return salary * 0.10



def task_parallelism_demo(name, salary):
    print(f"\n--- Task Parallelism for {name} (Salary: {salary}) ---")

    tasks = {
        "SSS": compute_sss,
        "PhilHealth": compute_philhealth,
        "Pag-IBIG": compute_pagibig,
        "Tax": compute_tax
    }

    with ThreadPoolExecutor(max_workers=len(tasks)) as executor:
        futures = {label: executor.submit(func, salary) for label, func in tasks.items()}
        results = {label: future.result() for label, future in futures.items()}

    total_deduction = sum(results.values())

    for label, amount in results.items():
        print(f"{label}: {amount:.2f}")

    print(f"Total Deduction: {total_deduction:.2f}")


if __name__ == "__main__":
    task_parallelism_demo("Edward", 35000)

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
