N = int(input())
for i in range(N) :
    a = input()
    stack = []

    for i in a :
        if i == '(' :
            stack.append(i)
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 :
        print('YES')
    else :
        print('NO')