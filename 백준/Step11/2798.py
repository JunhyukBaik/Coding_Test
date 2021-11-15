n,m = map(int, input().split())
card = list(map(int, input().split()))
summ = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if card[i] + card[j] +card[k] > m:
                continue
            else:
                summ = max(summ, card[i]+card[j]+card[k])
print(summ)