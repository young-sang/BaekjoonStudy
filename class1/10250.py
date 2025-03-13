T = int(input())

for i in range(0, T):
    H ,W, P= input().split(' ')
    H = int(H)
    W = int(W)
    P = int(P)
    a = 0
    for x in range(0+1, W+1):
        for y in range(1, H+1):
            a = a + 1
            if(a == P):
                print(str(y)+ str(x).zfill(2))