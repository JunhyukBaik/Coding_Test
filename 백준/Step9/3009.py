xs = list()
ys = list()
for _ in range(3)
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
xs.sort()
ys.sort()
if xs.count(xs[0]) == 1
    a = xs[0]
elif xs.count(xs[2]) == 1
    a = xs[2]
if ys.count(ys[0]) == 1
    b = ys[0]
elif ys.count(ys[2]) == 1
    b = ys[2]
print(a, b)