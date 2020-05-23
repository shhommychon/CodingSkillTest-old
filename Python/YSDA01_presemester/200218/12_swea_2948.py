### 소에아 3단계
### 2948번 문자열 교집합

# import sys
# sys.stdin = open("input.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    strsetA = set(input().split())
    strsetB = set(input().split())

    answer = N - len(strsetA.difference(strsetB))

    print(f"#{test_case} {answer}")