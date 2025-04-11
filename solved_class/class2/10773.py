K = int(input())
stack = []
for i in range(K):
    a = int(input())
    if a == 0:
        if len(stack) == 0:
            break
        stack.pop()
    else:
        stack.append(a)
res = 0

for i in range(len(stack)):
    res += stack[i]
print(res)