import math
N = int(input())

a = list(map(int, input().split(' ')))

top = max(a)
res = 0
for i in a:
    res += float(i / top) * 100

print(res / len(a))