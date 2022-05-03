### 프로그래머스 Level2
### 연습문제 | 다음 큰 숫자
### https://programmers.co.kr/learn/courses/30/lessons/12911?language=python3

def solution(n):
    one_count = bin(n).count('1')
    n += 1
    while bin(n).count('1') != one_count:
        n += 1
    return n
