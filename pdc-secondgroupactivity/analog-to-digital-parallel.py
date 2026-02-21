from concurrent.futures import ThreadPoolExecutor
import time
import queue
import threading

class IceWrapper:
    def __init__(self, id):
        self.id = id
        self.filledWithWater = False
        self.isTied = False
        self.isInFreezer = False
        self.isFrozen = False

    def fillWithWater(self):
        time.sleep(2)  # simulate faucet delay
        self.filledWithWater = True
        print(f"IceWrapper {self.id}: Filled with water")

    def tie(self):
        time.sleep(1)
        self.isTied = True
        print(f"IceWrapper {self.id}: Tied")

    def putInFreezer(self):
        time.sleep(1)
        self.isInFreezer = True
        print(f"IceWrapper {self.id}: Placed in freezer")

    def takeFromFreezer(self):
        time.sleep(3)  # freezing time
        self.isFrozen = True
        self.isInFreezer = False
        print(f"IceWrapper {self.id}: Frozen and removed from freezer")


# Queues represent pipeline stages (Input Distribution)
fill_queue = queue.Queue()
tie_queue = queue.Queue()
freezer_queue = queue.Queue()
done_queue = queue.Queue()

def fill_worker():
    while True:
        ice = fill_queue.get()
        if ice is None:
            break
        ice.fillWithWater()
        tie_queue.put(ice)
        fill_queue.task_done()

def tie_worker():
    while True:
        ice = tie_queue.get()
        if ice is None:
            break
        ice.tie()
        freezer_queue.put(ice)
        tie_queue.task_done()

def freezer_worker():
    while True:
        ice = freezer_queue.get()
        if ice is None:
            break
        ice.putInFreezer()
        ice.takeFromFreezer()
        done_queue.put(ice)
        freezer_queue.task_done()


def run_parallel_pipeline(num_wrappers=5):
    # Create input
    for i in range(num_wrappers):
        fill_queue.put(IceWrapper(i))

    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(fill_worker)
        executor.submit(tie_worker)
        executor.submit(freezer_worker)

        fill_queue.join()
        tie_queue.join()
        freezer_queue.join()

    print("\nAll ice wrappers processed.")


if __name__ == "__main__":
    start = time.time()
    run_parallel_pipeline(5)
    end = time.time()

    print(f"\nTotal parallel execution time: {end - start:.2f} seconds")