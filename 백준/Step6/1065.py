def cdcsy(n):
    if n < 100:
        return 1
    else:
        n = str(n)
        cha = int(n[0]) - int(n[1])
        for i in range(1,len(n)):
            num = int(n[i]) - int(n[i+1])
            if num != cha:
                return 0
            else:
                return 1
            
N = int(input())
count = 0
for i in range(N):
    count += cdcsy(i+1)
print(count)