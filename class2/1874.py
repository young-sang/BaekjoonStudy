n = int(input())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

resarr = []
plusnim = []
success = True
prevnum = 0
popMaxnum = 0
for i in arr:
    if i > prevnum:
        for j in range(popMaxnum + 1, i+1):
            resarr.append(j)
            plusnim.append("+")
        plusnim.append("-")
        popMaxnum = resarr.pop()
        prevnum = i
    else:
        b = resarr.pop()
        if b == i:
            plusnim.append("-")
            prevnum = i
        else:
            success = False
            break

if success == False:
    print("NO")
else:
    for i in plusnim:
        print(i)