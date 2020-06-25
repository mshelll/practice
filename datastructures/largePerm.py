#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestPermutation function below.
def largestPermutation(k, arr):
  N = len(arr)
  n = N

  start = N
  end = N - k

  print("N :", N)

  m = {}
  for i in range(len(arr)):
    m[arr[i]] = i

  i = 0
  swaps = 0
  while(i < N and swaps < k and n > 0):
      if arr[i] == n:
        i += 1
        n -= 1
        continue
      index = m[n]
      print("i :", i)
      print("n :", n)
      print("index :", index)

      if index < 0 or index > N:
        break
      arr[index] = arr[i]
      m[arr[i]] = index
      arr[i] = n
      m[n] = i
      n -= 1
      i += 1
      swaps += 1
  
  return arr

if __name__ == '__main__':
  fptr = open("/Users/rift/Workspace/python/input1.txt", 'r')

  nk = fptr.readline().split()

  n = int(nk[0])

  k = int(nk[1])

  arr = list(map(int, fptr.readline().rstrip().split()))

  result = largestPermutation(k, arr)

  fptr = open("/Users/rift/Workspace/python/output1.txt", 'w')
  fptr.write(' '.join(map(str, result)))
  fptr.write('\n')

  fptr.close()