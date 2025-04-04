import sys
N, M = map(int, sys.stdin.readline().split())
dic = {}
for i in range(N):
    a = sys.stdin.readline().strip().split()
    dic[a[0]] = a[1]

for j in range(M):
    a = input()
    print(dic[a])