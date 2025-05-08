queue = []

N, K = map(int, input().split())
for i in range(N):
    queue.append(i+1)

count = 1
res = []
while True:
    if len(queue) == 0:
        break
    if count % K == 0:
        a = queue.pop(0)
        res.append(a)
    else:
        a = queue.pop(0)
        queue.append(a)
    count += 1
print("<", end="")
for i in range(len(res)):
    if i == len(res)-1:
        print(res[i], end="")
    else:
        print(res[i], end=", ")
    
print(">")