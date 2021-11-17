n = int(input())
wl = list()
for _ in range(n):
    wd = input()
    wl.append((wd,len(wd)))
wlc = list(set(wl))

wlc.sort(key=lambda x: (x[1], x[0]))
for i in wlc:
    print(i[0])