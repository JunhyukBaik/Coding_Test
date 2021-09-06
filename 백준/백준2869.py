# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:16:32 2021

@author: 백준혁
"""

A, B, V = map(int, input().split())

day = 0
high = 0

oned = A - B
tmp = V - A

if (tmp % oned == 0):
    print(tmp // oned + 1)
else:
    print(tmp // oned + 2)