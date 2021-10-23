n = int(input())
results = list()
for i in range(n):
    result = 0
    sent = input()
    for j in range(len(sent)):
        if j == 0:
            if sent[j] == 'O':
                num = 1
            else:
                num = 0
            result = result + num
        else:
            if sent[j] == 'O':
                num = num + 1
            else:
                num = 0
            result = result + num
    results.append(result)
for i in range(n):
    print(results[i])
                