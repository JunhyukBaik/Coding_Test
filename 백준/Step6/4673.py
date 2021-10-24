def selfnum(n):
    sum = 0
    newn = str(n)
    for i in range(len(newn)):
        sum += int(newn[i])
    return n + sum
arr = list()
for i in range(10000):
    arr.append(i+1)

for i in range(10000):
    sel = selfnum(i)
    if sel in arr:
        arr.remove(sel)
for i in range(len(arr)):
    print(arr[i])