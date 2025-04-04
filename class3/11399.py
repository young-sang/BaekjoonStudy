N = int(input())
B = list(map(int, input().split()))
B.sort()
res = 0
add = 0
for i in range(N):
    add += B[i]
    res += add
print(res)