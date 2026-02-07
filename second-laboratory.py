import threading
import json
import os

def compute_gwa(grades):
    gwa = sum(grades) / len(grades)
    print(f"[Thread]: Calculated GWA: {gwa}")

def main():
    print(os.getcwd())
    grades_list = list(map(float, input("Enter grades separated by space: ").split()))
    threads = []
    for grade in grades_list:
        t = threading.Thread(target=compute_gwa, args=([grade],))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()