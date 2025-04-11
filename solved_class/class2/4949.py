arrin = {"[": "]", "(": ")"}
while True:

    N = input()
    if(N == "."):
        print(".")
        break
    res = ""
    arr = []
    for i in N:
        if i in arrin.keys():
            arr.append(arrin[i])
        elif i in arrin.values():
            if len(arr) == 0 or arr.pop() != i:
                res = "no"
                break

    if len(arr) != 0:
        res = "no"
    if(res != "no"):
        res = "yes"
    print(res)
# -----------------
while True :
    a = input()
    stack = []

    if a == "." :
        break

    for i in a :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')