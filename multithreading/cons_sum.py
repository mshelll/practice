
import threading 

MAX_ELEM = 16
MAX_WORKERS = 4

factor = int(MAX_ELEM/MAX_WORKERS)

mux = threading.Lock()
cond = threading.Condition()

SUM = []

status = 0

def sum(arr):
    sum1 = 0
    for num in arr:
        sum1 += num
    return sum1
    
def get_slice(arr, part):
    a = factor*part
    b = factor*(part+1)
    return arr[a:b]

def task1(arr, part):
    global SUM
    arr1 = get_slice(arr, part)
    sum1 = sum(arr1)
    SUM.append(sum1)


def main():
    arr =[1, 2, 3, 4, 5, 6]
    t = list()
    for i in range(MAX_WORKERS):
        t.append(threading.Thread(target=task1, args=(arr, i)))
        t[i].start()

    for i in range(MAX_WORKERS):
        t[i].join()

    print(sum(SUM))

if __name__ == "__main__":
    main()