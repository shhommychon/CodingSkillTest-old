### 프로그래머스 Level1
### 이상한 문자 만들기 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3


def solution(s):
    words = s.split(' ')

    answer = ''
    for word in words:
        for i, c in enumerate(word):
            if i % 2 == 0:
                answer += c.upper()
            else:
                answer += c.lower()
        answer += ' '

    return answer[:-1]


if __name__ == "__main__":
    answer1 = solution("try hello world")
    answer2 = solution("said  hello   world")

    print(f"{answer1} : {answer1 == 'TrY HeLlO WoRlD'}")
    print(f"{answer2} : {answer2 == 'SaId  HeLlO   WoRlD'}")