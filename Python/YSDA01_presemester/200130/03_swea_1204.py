### 소에아 2단계
### 1204번 [S/W 문제해결 기본] 1일차 - 최빈수 구하기

# import sys
# sys.stdin = open('test.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    test_case = int(input())    # ??

    scores = list(input().split())

    # 갯수를 키로, 값을 해당 갯수 만큼 있는 점수들의 리스트로 하는 사전입니다.
    scores_dict = {}

    for score in set(scores):
        if scores.count(score) not in scores_dict:
            scores_dict[scores.count(score)] = []
        scores_dict[scores.count(score)].append(score)

    # 최빈값이 하나라면 해당 점수값을 출력,
    if len(scores_dict[max(scores_dict)]) == 1:
        print(f"#{test_case} {scores_dict[max(scores_dict)][0]}")
    # 최빈값이 여러개라면 그들 중 최대값을 출력합니다.
    else:
        print(f"#{test_case} {max(scores_dict[max(scores_dict)])}")
