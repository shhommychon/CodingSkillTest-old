### 프로그래머스 Level2
### 2021 카카오 채용연계형 인턴십 | 거리두기 확인하기
### https://programmers.co.kr/learn/courses/30/lessons/81302?language=python3

# 정확성 19 / 31


# def dfs(place, r, c, original=None, level=0):
#     if r < 0 or r >= 5 or c < 0 or c >= 5 or level >= 2:
#         return 1
    
#     if original is None:
#         original = (r,c)
    
#     for y, x in ((1, 0), (-1, 0), (0, 1), (0, -1)):
#         if not(r+y == original[0] and c+x == original[1]) \
#             and 0 <= r+y < 5 and 0 <= c+x < 5:
#             z = place[r+y][c+x]
#             if z == 'O':
#                 result = dfs(place, r+y, c+x, original=original, level=level+1)
#                 if result == 0:
#                     return 0
#             elif z == 'P':
#                 return 0
    
#     return 1
    

# def solution(places):
#     answer = []
    
#     for p in places:
#         continue_ = True
#         for r in range(5):
#             for c in range(5):
#                 if p[r][c] == 'P':
#                     result = dfs(p, r, c)
#                     if result == 0:
#                         continue_ = False
#             if not continue_:
#                 break
#         answer.append(result)
    
#     return answer
