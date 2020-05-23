### 소에아 3단계
### 1244번 [S/W 문제해결 응용] 2일차 - 최대 상금

import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    number, change = input().split()

    number = list(number)
    target = sorted(number, reverse=True)

    change = int(change)
    i = 0
    while change:
        if number[i] == target[i]:
            i += 1
        elif i < len(target)-2:
            t = target[i]
            t_i = number.index(t)
            number[i], number[t_i] = number[t_i], number[i]
            i += 1
            change -= 1
        elif i == len(target)-2:
            number[i], number[i+1] = number[i+1], number[i]
            change -= 1

    print(f"#{test_case} {int(''.join(number))}")