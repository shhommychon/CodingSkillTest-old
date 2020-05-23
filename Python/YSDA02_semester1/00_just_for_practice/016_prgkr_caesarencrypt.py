### 프로그래머스 Level1
### 시저 암호 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12926?language=python3


def push_chr(c, n):
    if c == ' ':
        return ' '
    elif c.isupper():
        return chr(ord(c) + n - 26) if ord(c) + n > ord('Z') else chr(ord(c) + n)
    else:
        return chr(ord(c) + n - 26) if ord(c) + n > ord('z') else chr(ord(c) + n)


def solution(s, n):
    return ''.join(map(lambda c: push_chr(c, n), s))


if __name__ == "__main__":
    answer1 = solution("AB", 1)
    answer2 = solution("z", 1)
    answer3 = solution("a B z", 4)

    print(f"{answer1} : {answer1 == 'BC'}")
    print(f"{answer2} : {answer2 == 'a'}")
    print(f"{answer3} : {answer3 == 'e F d'}")

    # 주의! 대문자 글자의 ord에 n을 더해서 소문자 범위의 ord가 되는 경우 있음
    # print(solution("Hello World", 25))