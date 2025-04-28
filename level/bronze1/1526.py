a = input()
b = [0]*len(a)

for i in range(len(a)):
    i = len(a) - i - 1
    if int(a[i]) >= 7:
        b[i] = '7'
    elif int(a[i]) < 4:
        if i == len(a) - 1:
            b[i] = '0'
        else:
            b[i] = '0'
            b[i+1] = '7'
    else:
        b[i] = '4'
print(int(''.join(b)))


# N = int(input())
# for number in range(N,1,-1):
#     word = str(number)
#     cnt = 0
#     for w in word :
#         if w == '7' :
#             cnt += 1
#         elif w == '4' :
#             cnt += 1
#     if cnt == len(word) :
#         print(number)
#         break
#     else :
#         continue