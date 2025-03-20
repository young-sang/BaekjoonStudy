# A, B, V = map(int, input().split())
# height = 0
# day = 0
# while True:
#     day += 1
#     height += A
#     if height >= V:
#         break
#     else:
#         height -= B
# print(day)

# #  시간 오래걸림, 단축 필요
import math

A, B, V = map(int, input().split())
day = math.ceil((V - B) / (A - B))
print(day)