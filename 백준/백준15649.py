# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 18:45:30 2021

@author: 백준혁
"""

N, M = map(int, input().split())
visited = [False] * N
outp = list()

def nnm(depth, m):
    if depth == m:
        print(' '.join(map(str, outp)))
        return
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            outp.append(i+1)
            nnm(depth+1, m)
            visited[i] = False
            outp.pop()

nnm(0, M)