### 소에아 3단계
### 4843번 [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬

# import sys
# sys.stdin = open("input.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    print(f"#{test_case} ", end='')
    N = int(input())
    a_list = sorted(list(map(int, input().split())))

    for ai, aj in zip(a_list[-1::-1], a_list[:5]):
        print(f"{ai} {aj} ", end='')
    print()