### 프로그래머스 Level1
### 정수 제곱근 판별 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12934?language=python3


def solution(n):
    sqrt = n ** 0.5
    if sqrt % 1 != 0:
        return -1
    else:
        return int((sqrt + 1) ** 2)


if __name__ == "__main__":
    answer1 = solution(121)
    answer2 = solution(3)

    print(f"{answer1} : {answer1 == 144}")
    print(f"{answer2} : {answer2 == -1}")
