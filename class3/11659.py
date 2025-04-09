import sys
N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
s = [0] * (len(arr)+1)

for i in range(N+1):
    
    if i == 0:
        s[0] = 0
    else:
        s[i] = arr[i-1] + s[i-1]


for i in range(M):
    a,b = map(int , sys.stdin.readline().split())

    print(s[b] - s[a-1])