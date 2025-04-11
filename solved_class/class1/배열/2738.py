N, M = map(int, input().split(' '))

A = [[0 for col in range(M)] for row in range(N)]
B = [[0 for col in range(M)] for row in range(N)]

for i in range(0,N):
    x = input().split(' ')
    for j in range(0, M):
        A[i][j] = int(x[j])


for i in range(0,N):
    x = input().split(' ')
    for j in range(0, M):
        B[i][j] = int(x[j])


for i in range(0,N):
    for j in range(0, M):
        print(A[i][j] + B[i][j], end=" ")
    print()

