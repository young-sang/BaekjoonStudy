import sys

N = int(input())

A = sys.stdin.readline().rstrip().split(' ')

v = int(input())
count = 0
for i in A:
    if(int(i) == v):
        count += 1

print(count)