import math
N = int(input())
a = list(map(int, input().split(' ')))
T , P = list(map(int, input().split(' ')))

count = 0
for i in a:
    count += math.ceil(i / T)

print(count)
print(math.floor(N / P), N % P)