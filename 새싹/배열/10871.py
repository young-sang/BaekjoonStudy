import sys

N, X = map(int, input().split(' '))

A = sys.stdin.readline().strip().split(' ')
for i in A:
    if int(i) < X:
        print(i, end=" ")
        