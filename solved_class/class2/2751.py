import sys

N = int(input())
arr = []
for i in range(N):
    a = int(sys.stdin.readline())
    arr.append(a)

arr.sort()

for i in arr:
    print(i)