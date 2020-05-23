### 프로그래머스 Level2
### 124 나라의 숫자 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3


def my_jaegwi(curr_num, curr_mod_rev=''):
    if curr_num == 0:
        return curr_mod_rev[::-1]

    next_num, check_mod = curr_num // 3, curr_num % 3

    if check_mod == 1:
        curr_mod_rev += '1'
        return my_jaegwi(next_num, curr_mod_rev)
    elif check_mod == 2:
        curr_mod_rev += '2'
        return my_jaegwi(next_num, curr_mod_rev)
    else:
        curr_mod_rev += '4'
        return my_jaegwi(next_num - 1, curr_mod_rev)


def solution(n):
    return my_jaegwi(n)


if __name__ == "__main__":
    answers = ("1", "2", "4", "11", "12", "14", "21", "22", "24", "41")

    my_answers = list()
    for n in range(1, 11):
        my_answers.append(solution(n))

    for m_a, a in zip(my_answers, answers):
        print(f"{m_a} : {m_a == a}")
