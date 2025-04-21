N = input()
num = int(input())
res = {}
for i in range(num):
    x = input()
    L = N.count("L") + x.count("L")
    O = N.count("O") + x.count("O")
    V = N.count("V") + x.count("V")
    E = N.count("E") + x.count("E")
    res[x] = (L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E) % 100

print(max(res, key=res.get))