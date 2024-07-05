import asyncio
import random
from typing import Any

QUEUE_MAX_SIZE = 10
PRODUCE_INTERVAL = 0.1
CONSUME_INTERVAL = 0.15
RUN_DURATION = 10

shared_queue: asyncio.Queue = asyncio.Queue(maxsize=QUEUE_MAX_SIZE)

async def producer() -> None:
    item = 0
    end_time: float = asyncio.get_running_loop().time() + RUN_DURATION
    while asyncio.get_running_loop().time() < end_time:
        try:
            shared_queue.put_nowait(item)
            print(f"Produced: {item}")
            item += 1
        except asyncio.QueueFull:
            print("Queue is full, producer is waiting.")
        await asyncio.sleep(PRODUCE_INTERVAL)

async def consumer() -> None:
    end_time: float = asyncio.get_running_loop().time() + RUN_DURATION
    while asyncio.get_running_loop().time() < end_time:
        try:
            item: Any = shared_queue.get_nowait()
            print(f"Consumed: {item}")
        except asyncio.QueueEmpty:
            print("Queue is empty, consumer is waiting.")
        await asyncio.sleep(CONSUME_INTERVAL)

async def main() -> None:
    # Create tasks for producer and consumer coroutines
    producer_task = asyncio.create_task(producer())
    consumer_task = asyncio.create_task(consumer())
    
    # Wait for tasks to finish
    await asyncio.gather(producer_task, consumer_task)
    
    print("Finished running producer-consumer scenario.")

if __name__ == "__main__":
    asyncio.run(main())
