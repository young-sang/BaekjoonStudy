
while True:
    a = list(map(int, input()))
    c = a.copy()
    b = []
    12
    if a[0] == 0:
        break
    
    for i in range(0, len(a)):
        b.append(c.pop())
    
    res = "yes"
    for x in range(0, len(b)):
        if a[x] != b[x]:
            res = "no"
            break
    print(res)

        
    
