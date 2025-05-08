N = int(input())
arr = []
for i in range(N):
    x, y = map(int,input().split())
    arr.append((x,y))
res = [1] * N
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            res[i] += 1
    

for i in res:
    print(i, end=' ')
    

