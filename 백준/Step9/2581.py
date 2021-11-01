m = int(input())
n = int(input())
summ = 0
miin = 10000
for i in range(m, n+1):
  cnt = 0
  for j in range(2, i+1):
    if i % j == 0:
      cnt += 1
  if cnt == 1:
    summ += i
    if i < miin:
      miin = i
if miin == 10000:
    print("-1")
else:
    print(summ)
    print(miin)