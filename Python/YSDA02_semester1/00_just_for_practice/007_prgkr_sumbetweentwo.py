### 프로그래머스 Level1
### 두 정수 사이의 합 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3


def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b+1))


if __name__ == "__main__":
    print(f"{solution(3, 5)} : {solution(3, 5) == 12}")
    print(f"{solution(3, 3)} : {solution(3, 3) == 3}")
    print(f"{solution(5, 3)} : {solution(5, 3) == 12}")
