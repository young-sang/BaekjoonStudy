N = int(input())

for i in range(1, 1000000):
    res = i
    for j in str(i):
        res += int(j)
    if(res == N):
        print(i)
        break
else:
    print(0)

# ---------------------

n=int(input())
print([*[i for i in range(n)if n==i+sum(map(int,str(i)))],0][0])

# --------------------------

n=int(input())

for i in range(1,n+1):
    if i+sum(map(int,str(i)))==n:
        break

print(i if i!=n else 0)