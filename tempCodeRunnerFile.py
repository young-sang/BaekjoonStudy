N = int(input())
arr = []
for i in range(N):
    x, y = map(int,input().split())
    arr.append((x,y))
res = [0] * N
for i in range(N):
    count = N
    for j in range(N):
        if i == j:
            continue
        if arr[i][0] > arr[j][0] or arr[i][1] > arr[j][1]:
            count -= 1
    
    res[i] = count

for i in res:
    print(i, end=' ')
    

