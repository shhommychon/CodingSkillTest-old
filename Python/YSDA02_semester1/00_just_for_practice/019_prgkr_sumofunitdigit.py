### 프로그래머스 Level1
### 자릿수 더하기 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12931?language=python3

# 소프트웨어 아카데미 3750번 참고


def solution(n):
    return sum(map(int, str(n)))


if __name__ == "__main__":
    answer1 = solution(123)
    answer2 = solution(987)

    print(f"{answer1} : {answer1 == 6}")
    print(f"{answer2} : {answer2 == 24}")
