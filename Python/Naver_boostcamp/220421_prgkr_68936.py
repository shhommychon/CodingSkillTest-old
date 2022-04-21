### 프로그래머스 Level3
### 월간 코드 챌린지 시즌1 | 쿼드압축 후 개수 세기
### https://programmers.co.kr/learn/courses/30/lessons/68936?language=python3


import numpy as np
from collections import deque

def solution(arr):
    arr = np.array(arr)
    arrs = deque([arr])
    zeros, ones = 0, 0
    
    while arrs:
        a = arrs.popleft()
        if 0 not in a:
            ones += 1
        elif 1 not in a:
            zeros += 1
        elif len(arr) > 1:
            arrs.append(a[:len(a)//2, :len(a)//2])
            arrs.append(a[:len(a)//2, len(a)//2:])
            arrs.append(a[len(a)//2:, :len(a)//2])
            arrs.append(a[len(a)//2:, len(a)//2:])
    
    return [zeros, ones]
