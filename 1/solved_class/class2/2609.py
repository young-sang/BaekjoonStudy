a = list(map(int, input().split()))

b = 1
res1 = []
while True:
    if b == min(a) + 1:
        break
    if a[0] % b == 0 and a[1] % b == 0:
        res1.append(b)
    b += 1
print(max(res1))
print(a[0]*a[1] // max(res1))

# # -----------
# a, b = map(int, input().split())
# lcm = a* b
# while (a%b != 0):
#     tmp = a
#     a = b
#     b = tmp%b
# print(b)
# print(lcm // b)