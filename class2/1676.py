N = int(input())
res = 1
for i in range(N):
    res *=i+1

count = 0
for i in reversed(str(res)):
    if i == "0":
        count += 1
    else:
        break

print(count)