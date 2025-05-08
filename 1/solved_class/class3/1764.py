import sys
N, M = map(int, sys.stdin.readline().split())
set1 = set([])
set2 = set([])

for i in range(N):
    a = sys.stdin.readline().strip()
    set1.add(a)

for j in range(M):
    a = sys.stdin.readline().strip()
    set2.add(a)


res = set1 & set2
li = list(res)
li.sort()
print(len(li))
for i in li:
    print(i)
