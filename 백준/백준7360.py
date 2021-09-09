# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 03:37:55 2021

@author: 백준혁
"""
while(True):
    N = int(input())
    if N == 0:
        break
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = 0
    b = 0
    for i in range(N):
        if A[i] == B[i]:
            continue
        elif A[i] > B[i]:
            if A[i] - B[i] == 1:
                if A[i] == 2 and B[i] == 1:
                    b += 6
                else:
                    b += (A[i] + B[i])
            else:
                a += A[i]
        elif A[i] < B[i]:
            if B[i] - A[i] == 1:
                if B[i] == 2 and A[i] == 1:
                    a += 6
                else:
                    a += (A[i] + B[i])
            else:
                b += B[i]
    print("A has", a , "points. B has" , b , "points.\n")
                