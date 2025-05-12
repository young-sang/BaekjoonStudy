import sys
N = int(sys.stdin.readline())
arr = []
for i in range(N):
    d = int(sys.stdin.readline())
    arr.append(d)

res = []
arr = arr[::-1]
for i in arr:
    if len(res) == 0:
        res.append(i)
    if i > res[-1]:
        res.append(i)

print(len(res))