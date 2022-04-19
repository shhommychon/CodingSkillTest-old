### 프로그래머스 Level2
### 탐욕법(Greedy) | 조이스틱
### https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3

# 정확성 6 / 27


# def moves(alphabet: str) -> int:
#     # assert len(alphabet) == 1, len(alphabet)
#     if alphabet <= 'N':
#         return ord(alphabet) - 65
#     else:
#         return 26 - (ord(alphabet) - 65)


# def solution(name):
#     answer = -1
    
#     # A가 가장 많이 연속되는 구간 찾음
#     a_len, max_a_len, a_continuous = 0, 0, False
#     is_end_a_continous = False
#     for i, c in enumerate(name+'_'):
#         if c != 'A' and c != '_':
#             if a_continuous:
#                 a_continuous = False
#                 max_a_len = max(max_a_len, a_len+1)
#                 a_len = 0
#             answer += 1 + moves(c)
#         elif c == 'A':
#             a_len += 1
#             answer += 1
#         else: # if c == '_'
#             max_a_len = max(max_a_len, a_len)
#             if a_len == max_a_len:
#                 is_end_a_continous = True
    
#     answer -= max_a_len
    
#     if is_end_a_continous:
#         return answer
    
#     else:
#         return answer + min(len(name)-max_a_len, max_a_len)
