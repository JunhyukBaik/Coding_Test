A = int(input())
B = int(input())
C = int(input())
counts = [0 for i in range(10)]
result = A*B*C
while(result):
    r = result % 10
    counts[r] = counts[r] + 1
    result = result // 10
for i in range(10):
    print(counts[i])
    