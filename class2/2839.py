N = int(input())


def a():
    A = N // 5
    maxi = 0
    for i in range(A+1):
        if (N - (i * 5)) % 3 == 0:
            maxi = i
    return maxi

b = a()

if b == 0:
    if N % 3 == 0:
        print(N // 3)
    else:
        print(-1)
else:
    print(b + ((N - (b*5)) // 3))