X = int(input())
count = 1
cnt = 1
cnt_one = 2
while X > cnt:
    count += 1
    cnt = cnt + cnt_one
    cnt_one += 1
mo = count
za = 1
for i in range(cnt-count+1,cnt+1):
    if count % 2 == 0:
      result = za / mo
      if i == X:
        print("{}/{}".format(za,mo))
        break
      mo += -1
      za += 1
    else:
      result = mo / za
      if i == X:
        print("{}/{}".format(mo,za))
        break
      mo += -1
      za += 1