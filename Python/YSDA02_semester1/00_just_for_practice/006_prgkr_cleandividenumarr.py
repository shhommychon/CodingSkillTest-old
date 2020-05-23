### 프로그래머스 Level1
### 나누어 떨어지는 숫자 배열 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3


def solution(arr, divisor):
    clean_divide = list()

    for num in arr:
        if num % divisor == 0:
            clean_divide.append(num)

    if len(clean_divide) == 0:
        clean_divide.append(-1)
    return sorted(clean_divide)


if __name__ == "__main__":
    print(f"{solution([5, 9, 7, 10], 5)} : {solution([5, 9, 7, 10], 5) == [5, 10]}")
    print(f"{solution([2, 36, 1, 3], 1)} : {solution([2, 36, 1, 3], 1) == [1, 2, 3, 36]}")
    print(f"{solution([3, 2, 6], 10)} : {solution([3, 2, 6], 10) == [-1]}")