import threading
import queue
import random
import time
from typing import Any

QUEUE_MAX_SIZE = 10
PRODUCE_INTERVAL = 0.1
CONSUME_INTERVAL = 0.15
RUN_DURATION = 10

shared_queue: queue.Queue = queue.Queue(maxsize=QUEUE_MAX_SIZE)

# Lock for demonstrating thread-safe operations (optional, queue.Queue is already thread-safe)
lock: threading.Lock = threading.Lock()

def producer() -> None:
    end_time: float = time.time() + RUN_DURATION
    while time.time() < end_time:
        item: int = random.randint(1, 100)
        with lock:
            if not shared_queue.full():
                shared_queue.put(item)
                print(f"Produced: {item}")
            else:
                print("Queue is full, producer is waiting.")
        time.sleep(PRODUCE_INTERVAL)

def consumer() -> None:
    end_time: float = time.time() + RUN_DURATION
    while time.time() < end_time:
        with lock:
            if not shared_queue.empty():
                item: Any = shared_queue.get()
                print(f"Consumed: {item}")
            else:
                print("Queue is empty, consumer is waiting.")
        time.sleep(CONSUME_INTERVAL)

# Main function to start threads
def main() -> None:
    # Create producer and consumer threads
    producer_thread: threading.Thread = threading.Thread(target=producer)
    consumer_thread: threading.Thread = threading.Thread(target=consumer)
    
    # Start threads
    producer_thread.start()
    consumer_thread.start()
    
    # Wait for threads to finish
    producer_thread.join()
    consumer_thread.join()
    
    print("Finished running producer-consumer scenario.")

if __name__ == "__main__":
    main()

