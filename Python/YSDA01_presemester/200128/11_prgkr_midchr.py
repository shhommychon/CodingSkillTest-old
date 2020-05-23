### 프로그래머스 Level1
### 가운데 글자 가져오기 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3


def solution(s):
    return s[len(s)//2] if len(s) % 2 else s[len(s)//2-1:len(s)//2+1]


if __name__ == "__main__":
    print(f"{solution('abcde')} : {solution('abcde') == 'c'}")
    print(f"{solution('qwer')} : {solution('qwer') == 'we'}")