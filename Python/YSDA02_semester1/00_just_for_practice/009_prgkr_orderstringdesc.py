### 프로그래머스 Level1
### 문자열 내림차순으로 배치하기 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3


def solution(s):
    return ''.join(sorted(s, reverse = True))


if __name__ == "__main__":
    print(f"{solution('Zbcdefg')} : {solution('Zbcdefg') == 'gfedcbZ'}")
