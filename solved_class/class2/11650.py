import sys
N = int(input())
arr = []
for i in range(N):
    x,y = map(int, sys.stdin.readline().split())
    arr.append((x,y))

res = sorted(arr, key=lambda x: (x[0] , x[1]))
for x, y in res:
    print(x, y)