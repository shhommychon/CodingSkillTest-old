### 프로그래머스 Level1
### 문자열 내 마음대로 정렬하기 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3


def solution(strings, n):
    strings = sorted(list(map(lambda s: s[n] + s, strings)))
    return list(map(lambda s: s[1:], strings))


if __name__ == "__main__":
    answer1 = solution(['sun', 'bed', 'car'], 1)
    answer2 = solution(['abce', 'abcd', 'cdx'], 2)

    print(f"{answer1} : {answer1 == ['car', 'bed', 'sun']}")
    print(f"{answer2} : {answer2 == ['abcd', 'abce', 'cdx']}")

