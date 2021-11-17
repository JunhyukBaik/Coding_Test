# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 21:40:58 2021

@author: 백준혁
"""

N = int(input())

X = list(map(int, input().split()))

for i in range(N):
    X[i] = [X[i],i]

X.sort(key=lambda x:x[0])
#print(X)
num = 0
tmp = 0
cnt = 0

for i in range(len(X)):
    if i == 0:
        tmp = X[i][0]
        X[i][0] = num
        
    else:
        if X[i][0] == tmp:
            X[i][0] = num

        else:
            cnt += 1
            tmp = X[i][0]
            X[i][0] = cnt
            num = cnt


X.sort(key=lambda x:x[1])
for i in X:
    print(i[0], end=' ')