T = int(input())
for i in range(1, T+ 1):
    for J in range(0, T):
        if(J < T - i):
            print(' ', end="")
        else:
            print("*", end="")
    print()
