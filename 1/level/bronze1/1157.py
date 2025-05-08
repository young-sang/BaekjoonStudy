a = input()
a = a.upper()
res = {}
for i in range(len(a)):
    if a[i] not in res.keys():
        res[a[i]] = 1
    else:
        res[a[i]] = res[a[i]] + 1

key = max(res.values())
max_keys = [k for k, v in res.items() if v == key]
if len(max_keys) > 1:
    print("?")
else:
    print(max_keys[0])