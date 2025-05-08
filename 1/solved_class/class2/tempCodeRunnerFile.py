import sys
M, N = map(int, sys.stdin.readline().split())


for i in range(M, N+1):
    res = False
    if i == 1:
        continue
    if i == 2:
        print(2)
        continue
    for j in range(2, i):
        if i % j == 0:
            res = True
            break
    if res == False:
        print(i)