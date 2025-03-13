H, M = input().split(' ')
H = int(H)
M = int(M)
if(M < 45):
    a = 60+(M - 45)
    if(H == 0):
        print(23, a)
    else:
        print(H-1, a)
else:
    print(H, M-45)
    
