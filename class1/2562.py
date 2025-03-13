arr = []
for i in range(0,9):
    a = int(input())
    arr.append(a)

a = 0
ind = 0
for i in range(len(arr)):
    if(a <arr[i]):
        a = arr[i]
        ind = i + 1

print(a)
print(ind)

    