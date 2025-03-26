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
        minCount = 0
        wcount = 0
        bcount = 0
        print(arr[i][j])
        
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
                # print(arr[i+y][j+x])
                # print(numSpel)
                # print("=======")
                if arr[i+y][j+x] != numSpel:
                    bcount += 1

        if wcount >= bcount:
            minCount = bcount
        else:
            minCount = wcount
        resarr.append(minCount)

print(min(resarr))

        
