import sys
N, M = map(int, (input().split()))
arr = []
for i in range(N):
    a = sys.stdin.readline()
    row = []
    for j in range(M):
        row.append(a[j])
    arr.append(row)
alpa = ['W', 'B']

resarr = []
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        wcount = 0
        bcount = 0
        
        for y in range(8):
            for x in range(8):
                numSpel = ''
                if y % 2 == 0:
                    if x % 2 == 0:
                        numSpel = alpa[0]   
                    else:
                        numSpel = alpa[1]
                else:
                    if x % 2 == 0:
                        numSpel = alpa[1]   
                    else:
                        numSpel = alpa[0]
                if arr[i+y][j+x] != numSpel:
                    wcount += 1
    
        for y in range(8):
            for x in range(8):
                numSpel = ''
                if y % 2 == 0:
                    if x % 2 == 0:
                        numSpel = alpa[1]   
                    else:
                        numSpel = alpa[0]
                else:
                    if x % 2 == 0:
                        numSpel = alpa[0]   
                    else:
                        numSpel = alpa[1]
                if arr[i+y][j+x] != numSpel:
                    bcount += 1

        if wcount >= bcount:
            resarr.append(bcount)
        else:
            resarr.append(wcount)
        

print(min(resarr))

        
