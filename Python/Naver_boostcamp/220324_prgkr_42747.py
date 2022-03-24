### 프로그래머스 Level2
### 정렬 | H-index
### https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3

def solution(citations):
    citations = sorted(citations, reverse=True)
    
    answer = 0
    for i, c in enumerate(citations):
        h = i+1
        if h <= c:
            answer = h
        else:
            break
    
    return answer
