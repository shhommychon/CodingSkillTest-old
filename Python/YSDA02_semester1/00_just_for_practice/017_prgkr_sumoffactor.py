### 프로그래머스 Level1
### 약수의 합 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12928?language=python3


def solution(n):
    yaksu = set()
    for num in range(1, round(n ** 0.5) + 1):
        if num not in yaksu and n % num == 0:
            yaksu.update([num, n//num])

    return sum(yaksu)


if __name__ == "__main__":
    answer1 = solution(12)
    answer2 = solution(5)

    print(f"{answer1} : {answer1 == 28}")
    print(f"{answer2} : {answer2 == 6}")
