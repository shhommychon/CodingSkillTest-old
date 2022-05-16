### 프로그래머스 Level2
### 완전탐색 | 카펫
### https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3

def solution(brown, yellow):
    # (w-1) + (h-1) == brown // 2
    # (w-2) * (h-2) == yellow
    
    h, w = 1, yellow
    while h <= w:
        if yellow % h:
            h += 1; continue
        w = yellow // h
        if (w+1) + (h+1) == brown // 2:
            return [w+2, h+2]
        h += 1
