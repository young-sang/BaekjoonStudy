T = int(input())

for i in range(0,T):
    try:
        s = input()
        print(s[0]+s[-1])
    except:
        break
