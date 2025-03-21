
arr = []
for i in range(3):
    a = input()
    arr.append(a)
b  = 0
for i in range(len(arr)):
    if str(arr[i]).isdecimal():
        b = int(arr[i])
        b += (3- i)
        break

if b % 3 == 0:
    if b % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
else:
    if b% 5 == 0:
        print("Buzz")
    else:
        print(b)