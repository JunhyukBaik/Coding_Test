C = int(input())
percent = list()
for i in range(C):
    score = list(map(int, input().split()))
    sum = 0
    count = 0
    for j in range(len(score)):
        if j==0:
            continue
        sum += score[j]
    avg = sum / score[0]
    for j in range(len(score)):
        if j==0:
            continue
        if score[j] > avg:
            count = count + 1
    percent.append(count/score[0]*100)
for i in range(C):
    print("%.3f"%(percent[i]) + '%')