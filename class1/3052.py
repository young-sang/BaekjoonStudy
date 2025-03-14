a = []
count = 0
for i in range(0, 10):
    b = int(input())
    c = b % 42
    if c not in a:
        count += 1
    a.append(c)
    
print(count)
