import sys
import math
N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

B = list(map(int, sys.stdin.readline().split()))

def bin(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = math.floor((left + right) /2)

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return -1

A.sort()

for i in B:
    if bin(A, i) == -1:
        print(0)
    else:
        print(1)

