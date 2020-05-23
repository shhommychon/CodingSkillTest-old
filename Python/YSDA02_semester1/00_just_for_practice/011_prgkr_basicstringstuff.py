### 프로그래머스 Level1
### 문자열 다루기 기본 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12918?language=python3


def solution(s):
    if len(s) not in (4, 6):
        return False

    try:
        int(s)
    except ValueError:
        return False

    return True


if __name__ == "__main__":
    answer1 = solution("a234")
    answer2 = solution("1234")

    print(f"{answer1} : {answer1 == False}")
    print(f"{answer2} : {answer2 == True}")

