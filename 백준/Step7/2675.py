T = int(input())
arr = list()
for i in range(T):
    news = ''
    R, S = map(str, input().split())
    R = int(R)
    for j in range(len(S)):
        a = S[j]*R
        news = news+a
    arr.append(news)
for i in range(T):
    print(arr[i])
        
