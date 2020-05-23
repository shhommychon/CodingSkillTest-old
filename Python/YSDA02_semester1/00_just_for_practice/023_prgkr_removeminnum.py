### 프로그래머스 Level1
### 제일 작은 수 제거하기 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3


def solution(arr):
    arr.remove(min(arr))
    return arr if len(arr) else [-1]


if __name__ == "__main__":
    answer1 = solution([4,3,2,1])
    answer2 = solution([10])

    print(f"{answer1} : {answer1 == [4,3,2]}")
    print(f"{answer2} : {answer2 == [-1]}")
