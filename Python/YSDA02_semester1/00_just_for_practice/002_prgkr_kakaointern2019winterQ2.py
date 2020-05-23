### 프로그래머스 Level2
### 튜플 (2019 카카오 개발자 겨울 인턴십 코딩 테스트 실전 모의고사)
### https://programmers.co.kr/competitions/145/kakao-internship-test
### https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3


def solution(s):
    set_list = s[2:-2].split("},{")

    ordered_sets = [ [] for _ in range(len(set_list)) ]
    for set_in_string in set_list:
        set_in_list = set_in_string.split(',')
        ordered_sets[len(set_in_list)-1] += set_in_list

    answer = []
    for ordered_set in ordered_sets:
        for element in ordered_set:
            if int(element) not in answer:
                answer.append(int(element))
                break

    return answer


if __name__ == "__main__":
    my_answer = list()
    my_answer.append(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    my_answer.append(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
    my_answer.append(solution("{{20,111},{111}}"))
    my_answer.append(solution("{{123}}"))
    my_answer.append(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))

    kakao_answer = ([2, 1, 3, 4], [2, 1, 3, 4], [111, 20], [123], [3, 2, 4, 1])
    for m_a, a in zip(my_answer, kakao_answer):
        print(f"{m_a} : {m_a == a}")