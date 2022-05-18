### 프로그래머스 Level2
### 2021 Dev-Matching: 웹 백엔드 개발자(상반기) | 행렬 테두리 회전하기
### https://programmers.co.kr/learn/courses/30/lessons/77485?language=python3

import numpy as np

def process_matrix(m, qy1, qx1, qy2, qx2):
    qy1, qx1, qy2, qx2 = qy1-1, qx1-1, qy2-1, qx2-1
    
    curr_min = 100 * 100
    top = m[qy1, qx1:qx2].copy(); curr_min = min(curr_min, top.min())
    right = m[qy1:qy2, qx2].copy(); curr_min = min(curr_min, right.min())
    bot = m[qy2, qx1+1:qx2+1].copy(); curr_min = min(curr_min, bot.min())
    left = m[qy1+1:qy2+1, qx1].copy(); curr_min = min(curr_min, left.min())
    
    m[qy1, qx1+1:qx2+1] = top
    m[qy1+1:qy2+1, qx2] = right
    m[qy2, qx1:qx2] = bot
    m[qy1:qy2, qx1] = left
    
    return m, curr_min

def solution(rows, columns, queries):
    matrix = np.array([ [ c+r*columns for c in range(1, columns+1) ] for r in range(0, rows) ])
    answer = []
    for q in queries:
        matrix, this_min = process_matrix(matrix, *q)
        answer.append(int(this_min)) 
    return answer
