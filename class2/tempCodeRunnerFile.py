def fec(a):
    res = 1
    for i in range(1, a+1):
        res *= i
    return res

N, K = map(int, input().split())

print(fec(N) / (fec(K) * fec(N-K)))