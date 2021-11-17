n = int(input())
nl = list()
for i in range(n):
    age, wd = map(str, input().split())
    nl.append((int(age),wd, i))

nl.sort(key=lambda x: (x[0], x[2]))
for i in nl:
    print(i[0], i[1])