N = int(input())
a = list(map(int, input().split()))

max = a[0]
min = a[0]

for i in a:
    if (min > i):
        min = i
    if(max < i):
        max = i

print(min, max)