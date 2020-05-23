### 프로그래머스 Level1
### 정수 내림차순으로 배치하기 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12933?language=python3


def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))


if __name__ == "__main__":
    answer1 = solution(118372)

    print(f"{answer1} : {answer1 == 873211}")
