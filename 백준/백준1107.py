# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 01:05:28 2021

@author: 백준혁
"""
bts = {str(i) for i in range(10)}  # 0, 1, 2 ... 9 (가능한 수)

# input
N = int(input())  # 원하는 채널
M = int(input())  # 고장난 버튼 수
if M != 0:
    bts -= set(map(str, input().split()))  # 고장난 버튼 리스트 제거

# 100번에서 +, - 로만 움직이는 경우
min_cnt = abs(100 - N)

# 1,000,000 채널까지 브루트 포스 진행
for num in range(1000001):
    num = str(num)
    for j in range(len(num)):
        if num[j] not in bts:
            break
        elif j == len(num) - 1:
            min_cnt = min(min_cnt, abs(N - int(num)) + len(str(num)))
print(min_cnt)
