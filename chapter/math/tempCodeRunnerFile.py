import sys

arr = [False] * (246912 + 1)
arr[0] = True
arr[1] = True
for i in range(2, 246912 + 1):
    for j in range(2, int(i**0.5 + 1)):
        if i % j == 0:
            arr[i] = True
            break
while True:
    a = int(sys.stdin.readline())
    if a == 0:
        break
    num =0
    for i in range(a, a*2 + 1):
        if arr[i] == False:
            num += 1
    print(num)
        