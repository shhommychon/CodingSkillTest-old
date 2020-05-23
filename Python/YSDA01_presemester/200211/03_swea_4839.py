### 소에아 2단계
### 4839번 [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색

import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    La, Lb = 1, 1
    Ra, Rb = P, P
    Ca, Cb = int((La+Ra)/2), int((Lb+Rb)/2)

    while Ca != Pa and Cb != Pb:
        if Ca < Pa:
            La = Ca
        else:
            Ra = Ca
        if Cb < Pb:
            Lb = Cb
        else:
            Rb = Cb
        Ca, Cb = int((La + Ra) / 2), int((Lb + Rb) / 2)
    else:
        if Ca == Pa and Cb != Pb:
            print(f"#{test_case} A")
        elif Ca != Pa and Cb == Pb:
            print(f"#{test_case} B")
        else:
            print(f"#{test_case} 0")
