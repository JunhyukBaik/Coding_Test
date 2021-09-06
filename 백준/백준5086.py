# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:07:16 2021

@author: 백준혁
"""

while(True):
    n, m = map(int, input().split())
    if n == 0:
        break
    if m % n == 0:
        print("factor")
    elif n % m == 0:
        print("multiple")
    else:
        print("neither")
