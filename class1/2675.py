A = int(input())


for j in range(0, A):
    R, S = input().split()
    R = int(R)
    S = str(S)
    for i in S:
        print(i*R, end="")
    print()
