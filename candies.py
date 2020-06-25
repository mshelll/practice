#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):

    m = {}

    m[0] = 1
    for i in range(1, n):

        if arr[i] > arr[i-1]:
            m[i] = m[i-1]+1
        else:
            m[i] = 1

    print("m1 :", m)

    for i in range(n-2, -1, -1):

        if arr[i] > arr[i+1] and m[i] <= m[i+1]:
            m[i] = m[i+1] + 1

    print("m2 :", m)

    return sum([val for _, val in m.items()])



if __name__ == '__main__':
    fptr = open("/Users/rift/Workspace/python/input1.txt", 'r')

    n = int(fptr.readline())

    arr = []

    for _ in range(n):
        arr_item = int(fptr.readline())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr = open("/Users/rift/Workspace/python/output1.txt", 'w')
    fptr.write(str(result) + '\n')

    fptr.close()
