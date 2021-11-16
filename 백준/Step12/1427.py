n = int(input())
ns = list()
while n > 0:
    ns.append(n%10)
    n = n // 10
ns.sort(reverse=True)
for i in ns:
    print(i,end='')