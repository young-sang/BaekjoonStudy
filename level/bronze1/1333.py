# N, L, D = map(int, input().split())

# # 전체 시간
# total_time = N * L + (N - 1) * 5

# time = 0
# while True:
#     time += D  # 전화는 D초 간격으로 울림

#     if time > total_time:
#         print(time)
#         break

#     # 현재 전화 울린 시각이 노래 재생 중인지 체크
    
#     time_Left = time % (L + 5)

#     if time_Left > L or time_Left == 0:
#         print(time)
#         break


n,l,d=map(int,input().split())
l+=5
num=0
time=d
for i in range(n):
    num+=l
    while True:
        if time<num-5: time+=d
        else: break
    if num-5<=time<num: break
print(time)