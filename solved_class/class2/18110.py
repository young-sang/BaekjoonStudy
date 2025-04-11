
def rs(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

import sys


n = int(input())
arr = []
result = 0
if n != 0:
    for i in range(n):
        a = int(sys.stdin.readline())
        arr.append(a)

    arr.sort()
    sum1 = 0
    minus = rs(n*0.15)
    
    for i in range(minus, n-minus):
        sum1 += arr[i]
    result = rs(sum1 / (n - 2*minus))
print(result)
