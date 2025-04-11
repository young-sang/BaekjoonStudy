def add(a , b):
    return (a + b)*(a - b)

x, y = map(int, input().split(' '))
print(add(x, y))
