### 프로그래머스 Level1
### 문자열 내 p와 y의 개수 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3


def solution(s):
    return s.lower().count('p') == s.lower().count('y')


if __name__ == "__main__":
    print(f"{solution('pPoooyY')} : {solution('pPoooyY') == True}")
    print(f"{solution('Pyy')} : {solution('Pyy') == False}")
