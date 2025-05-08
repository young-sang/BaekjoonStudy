n = int(input())
res = 0
for i in range(n, n*n):
    if i % n == i // n:
        res += i

print(res)