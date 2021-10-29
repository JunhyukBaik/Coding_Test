d = dict()
n = input()
n = n.upper()
for i in n:
    if i in d:
        d[i] += 1
    else:
        d[i] = 0
sd = sorted(d.items(), key=lambda x: x[1], reverse=True)
if len(sd) > 1:
    if sd[0][1] == sd[1][1]:
        print('?')
    else:
        print(sd[0][0])
else:
    print(sd[0][0])
