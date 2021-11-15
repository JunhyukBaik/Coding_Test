n = int(input())
man = list()
for _ in range(n):
    x, y = map(int, input().split())
    man.append([x,y,1])
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if man[i][0] < man[j][0] and man[i][1] < man[j][1]:
            man[i][2] += 1

for k in range(n):
    print(man[k][2], end=' ')
    