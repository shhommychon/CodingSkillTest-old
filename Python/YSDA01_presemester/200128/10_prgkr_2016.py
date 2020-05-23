### 프로그래머스 Level1
### 2016년 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3


def num_to_dayname(day_in_num):
    # 2016년 1월 1일 금요일을 기준으로 나머지 계산
    if day_in_num == 1:
        return "FRI"
    elif day_in_num == 2:
        return "SAT"
    elif day_in_num == 3:
        return "SUN"
    elif day_in_num == 4:
        return "MON"
    elif day_in_num == 5:
        return "TUE"
    elif day_in_num == 6:
        return "WED"
    else:
        return "THU"


def solution(a, b):
    days = 0

    # a월 이전 월의 날짜 수를 days에 더함
    for month in range(1, a):
        if month <= 7:
            days += 30 + (month % 2)
            if month == 2:
                days -= 1
        else:
            days += 30 + (((month % 2) - 1) * (-1))

    # b일을 days에 더함
    days += b

    # days를 7로 나눈 나머지를 괜히 한번 작성해 본 num_to_dayname 함수로 보냄
    answer = num_to_dayname(days % 7)

    return answer