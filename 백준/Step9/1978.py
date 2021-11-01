n = int(input())
count = 0

arr = list(map(int, input().split()))
for i in arr:
    sosuc = 0
    if i > 1:
        for t in range(2, i+1):
            if i % t == 0:
                sosuc += 1
        if sosuc == 1:
            count += 1
print(count)