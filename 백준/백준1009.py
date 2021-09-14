# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:57:39 2021

@author: 백준혁
"""

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    tmp = a
    if b == 1:
        tmp = tmp % 10
    else:
        for _ in range(b - 1):
            tmp = (tmp * a) % 10
    if tmp == 0:
        tmp = 10
    print(tmp)
    