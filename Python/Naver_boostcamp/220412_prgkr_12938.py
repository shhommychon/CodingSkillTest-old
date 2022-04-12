### 프로그래머스 Level3
### 이분탐색 | 입국심사
### https://programmers.co.kr/learn/courses/30/lessons/12938?language=python3


def solution(n, s):
    if s < n:
        return [-1]
    
    mok = s // n
    answer = [ mok ] * n
    
    namoji = s % n
    for i in range(len(answer)-1, len(answer)-1-namoji, -1):
        answer[i] += 1
    
    return answer
