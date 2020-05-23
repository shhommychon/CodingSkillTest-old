### 프로그래머스 Level1
### 같은 숫자는 싫어 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3


def solution(arr):
    check_num = None
    arr_new = list()

    for a in arr:
        if check_num != a:
            check_num = a
            arr_new.append(a)

    return arr_new


if __name__ == "__main__":
    print(f"{solution([1,1,3,3,0,1,1])} : {solution([1,1,3,3,0,1,1]) == [1,3,0,1]}")
    print(f"{solution([4,4,4,3,3])} : {solution([4,4,4,3,3]) == [4,3]}")