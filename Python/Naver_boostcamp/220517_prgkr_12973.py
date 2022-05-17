### 프로그래머스 Level2
### 2017 팁스타운 | 짝지어 제거하기
### https://programmers.co.kr/learn/courses/30/lessons/12973?language=python3

def solution(s):
    stack = ['_']
    for c in s:
        if c != stack[-1]:
            stack.append(c)
        else:
            stack.pop()
    return int(len(stack) == 1)
