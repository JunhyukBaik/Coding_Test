sen = input()
abcz = "abcdefghijklmnopqrstuvwxyz"
res = list()
for i in range(len(abcz)):
    if abcz[i] in sen:
        res.append(sen.index(abcz[i]))
    else:
        res.append(-1)
for i in range(len(res)):
    print(res[i], end= ' ')