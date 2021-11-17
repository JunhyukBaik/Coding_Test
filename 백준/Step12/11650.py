n = int(input())
jp = list()
for i in range(n):
    x, y = map(int, input().split())
    jp.append((x,y))
jp.sort()
for i in jp:
    print(i[0], i[1])