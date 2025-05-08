N = int(input())
if N == 1:
    print(1)    
else:
    x = 1
    while N > 1 + 3* x * (x - 1):
        x = x + 1
    print(x)