# Program to demonstrate producer consumer problem
# Note we deliberately havent used sophisticated collections
# or sync mechanisms and thats the way it should be

from threading import Thread, Condition

work_queue = []
MAX_ITEMS = 5

cond = Condition()

def is_not_empty():
    return len(work_queue) > 0

def is_not_full():
    return len(work_queue) != MAX_ITEMS

def get_front(work_queue):
    val = work_queue[0]
    work_queue.remove(val)
    return val

def producer():
    for i in range(MAX_ITEMS):
        with cond:
            cond.wait_for(is_not_full)
            work_queue.append(i)
            print("Produce :", i)
            cond.notifyAll()

def consumer():
    for i in range(MAX_ITEMS):
        with cond:
            cond.wait_for(is_not_empty)
            val = get_front(work_queue)
            print("consume :", val)
            cond.notifyAll()

def main():

    producer_thread = Thread(target=producer)
    consumer_thread = Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

if __name__ == "__main__":
    main()