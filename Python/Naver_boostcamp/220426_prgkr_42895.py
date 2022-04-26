### 프로그래머스 Level3
### 동적계획법(Dynamic Programming) | N으로 표현
### https://programmers.co.kr/learn/courses/30/lessons/42895?language=python3

# 테스트 케이스 3 / 4

# from collections import deque

# def makeq(q, N):
#     s = set()
#     while q:
#         num = q.popleft()
#         for x in (num+N, num-N, num*N, num//N):
#             if x > 0:
#                 s.add(x)
#         if not q:
#             s.add(int(str(num)+str(N)))
#     return deque(list(s))

# def solution(N, number):
#     answer = 1
#     if N == number:
#         return answer
    
#     q = deque([N])
#     while answer < 8:
#         answer += 1
        
#         q = makeq(q, N)
#         if number in q:
#             return answer
    
#     return -1