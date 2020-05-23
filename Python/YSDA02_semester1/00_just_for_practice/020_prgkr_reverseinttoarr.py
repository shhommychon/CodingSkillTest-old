### 프로그래머스 Level1
### 자연수 뒤집어 배열로 만들기 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12932?language=python3


def solution(n):
    return list(map(int, str(n)[::-1]))


if __name__ == "__main__":
    answer1 = solution(12345)

    print(f"{answer1} : {answer1 == [5, 4, 3, 2, 1]}")
