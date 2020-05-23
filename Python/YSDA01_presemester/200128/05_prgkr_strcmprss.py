### 프로그래머스 Level1
### 문자열 압축 (2020 KAKAO BLIND RECRUITMENT)
### https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def apeach_compression(s, unit):
    s_list = list(s)

    i = 0
    while i < len(s_list):
        search = s_list[i:i+unit]
        if s_list[i+unit:i+2*unit] == search:
            counter = 1
            while s_list[i+unit:i+2*unit] == search:
                del s_list[i+unit:i+2*unit]
                counter += 1
                if i+unit >= len(s_list):
                    break
            s_list.insert(i, str(counter))
            i += 1
        i += unit

    return "".join(s_list)

def solution(s):
    possible_compression = []

    # 제출 예제 5번 스트링 길이 1 대비, 무압축 원본도 리스트에 append
    possible_compression.append(s)

    # 최대 문자열의 반(소수점 버림)의 단위로만 압축 가능
    for i in range(1, len(s) // 2 + 1):
        possible_compression.append(apeach_compression(s, i))

    len_possible_compression = list(map(len, list(possible_compression)))

    answer = min(len_possible_compression)
    return answer

solution("a")