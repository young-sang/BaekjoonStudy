A = int(input())
R, S = input().split()
R = int(R)
S = str(S)

for j in range(0, A):
    for i in S:
        print(i*R, end="")
    print()
