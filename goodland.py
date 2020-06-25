#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pylons function below.
def pylons(k, arr):

    plants = []
    j = k
    k -= 1

    i = 0
    while(i < len(arr)):
        print("i :", i)
        found = False
        if i+k < len(arr):
            for p in range(i+k, i-1, -1):
                if arr[p] == 1:
                    plants.append(p)
                    i = p+k+1
                    found = True
                    break

        if found: continue

        elif i-k >= 0:
            for p in range(i, i-k-1, -1):
                if arr[p] == 1:
                    plants.append(p)
                    i = p+k+1
                    found = True
                    break

        if not found:
            return -1

    print("plants :", plants)
    return len(set(plants))

if __name__ == '__main__':
    fptr = open("/Users/rift/Workspace/python/input1.txt", 'r')

    nk = fptr.readline().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, fptr.readline().rstrip().split()))

    result = pylons(k, arr)

    fptr = open("/Users/rift/Workspace/python/output1.txt", 'w')
    fptr.write(str(result) + '\n')

    fptr.close()
