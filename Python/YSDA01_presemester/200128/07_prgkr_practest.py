### 프로그래머스 Level1
### 모의고사 (완전탐색)
### https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3


def solution(answers):
    answers = ''.join(map(str, answers))

    mathdumb1 = ('12345' * (len(answers) // 5 + 1))[:len(answers)]
    mathdumb2 = ('21232425' * (len(answers) // 8 + 1))[:len(answers)]
    mathdumb3 = ('3311224455' * (len(answers) // 10 + 1))[:len(answers)]

    mathdumbs_score = [0, 0, 0]
    for a, da1, da2, da3 in zip(answers, mathdumb1, mathdumb2, mathdumb3):
        if a == da1:
            mathdumbs_score[0] += 1
        if a == da2:
            mathdumbs_score[1] += 1
        if a == da3:
            mathdumbs_score[2] += 1

    max_mds = max(mathdumbs_score)
    max_md = list()
    for i in range(len(mathdumbs_score)):
        if mathdumbs_score[i] == max_mds:
            max_md.append(i+1)

    return max_md


if __name__ == "__main__":
    print(f"{solution([1,2,3,4,5])} : {solution([1,2,3,4,5]) == [1]}")
    print(f"{solution([1,3,2,4,2])} : {solution([1,3,2,4,2]) == [1,2,3]}")