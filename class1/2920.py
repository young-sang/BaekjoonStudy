a = list(map(int, input().split(' ')))

b = a.copy()
c = a.copy()

b.sort()
c.sort(reverse=True)

if(a == b):
    print("ascending")
elif(a == c):
    print("descending")
else:
    print("mixed")