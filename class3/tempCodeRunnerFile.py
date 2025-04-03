import sys
N, M = map(int, sys.stdin.readline().split())
dic = {}
dic2 = {}
for i in range(N):
    a = sys.stdin.readline()
    dic[str(i+1)] = a
    dic[a] = i + 1

for j in range(M):
    a = sys.stdin.readline()
    if a.isdecimal():
        print(dic.get(a))
    else:
        print(dic2.get(a))
