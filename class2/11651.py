import sys
N = int(input())
arr = []
for i in range(N):
    x,y = map(int, sys.stdin.readline().split())
    arr.append((x,y))

res = sorted(arr, key=lambda x: (x[1] , x[0]))
for x, y in res:
    print(x, y)