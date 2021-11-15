n = int(input())
res = 0
for i in range(1,n):
    strr = str(i)
    summ = i
    for j in range(len(strr)):
        summ += int(strr[j])
    if summ == n:
        res = i
        break
print(res)