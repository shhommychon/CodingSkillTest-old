### 프로그래머스 Level1
### 수박수박수박수박수박수? (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12922?language=python3


def solution(n):
    return "수박" * (n // 2) + "수" * (n % 2)


if __name__ == "__main__":
    answer1 = solution(3)
    answer2 = solution(4)

    print(f"{answer1} : {answer1 == '수박수'}")
    print(f"{answer2} : {answer2 == '수박수박'}")
