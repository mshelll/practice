# Program to print integers in sequence

from threading import Thread, Condition
import time

MAX_THREADS = 5

COUNT = 0

cond = Condition()


def display(num):
    global COUNT

    while(1):
        with cond:
            while(COUNT != num):
                cond.wait()

            print("Thread num :", num)
            COUNT = (COUNT+1)%(MAX_THREADS)
            cond.notifyAll()
            time.sleep(1)

def main():
    arr =[1, 2, 3, 4, 5, 6]
    t = list()
    for i in range(MAX_THREADS):
        t.append(Thread(target=display, args=(i,)))
        t[i].start()

    for i in range(MAX_THREADS):
        t[i].join()

if __name__ == "__main__":
    main()