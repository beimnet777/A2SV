#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    num = arr[n-1]
    for i in range(n-2,-1,-1):
        if arr[i]>num:
                arr[i+1]= arr[i]
        else:
            arr[i+1]=num
            for i in arr :
                print(i,end=" ")
            print()
            break
        
        for i in arr :
                print(i,end=" ")
        print()
        
    if(arr[0]>num):
        arr[0]=num
        for i in arr :
            print(i,end=" ")
        print()
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
