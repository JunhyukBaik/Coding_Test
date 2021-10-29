N = int(input())
count = 0
for i in range(N):
    error = 0
    sen = input()
    for j in range(len(sen)-1):
        if sen[j] != sen[j+1]:
            nsen = sen[j+1:]
            if nsen.count(sen[j]) > 0:
                error += 1
    if error == 0:
        count += 1
print(count)