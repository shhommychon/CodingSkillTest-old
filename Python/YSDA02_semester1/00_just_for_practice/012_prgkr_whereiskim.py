### 프로그래머스 Level1
### 서울에서 김서방 찾기 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12919?language=python3


def solution(where_is_kim):
    return f"김서방은 {where_is_kim.index('Kim')}에 있다"


if __name__ == "__main__":
    answer1 = solution(["Jane", "Kim"])

    print(f"{answer1} : {answer1 == '김서방은 1에 있다'}")

