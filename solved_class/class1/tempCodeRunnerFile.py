S = input()

alpabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

count = 0
for i in S:
    if i in alpabet:
        print(count, end=' ')
    else:
        print(-1, end=' ')
    count += 1