### 백준 2단계 if문
### 10817번 세 수
### 세 정수 중에 두 번째로 큰 정수를 찾는 문제

A, B, C = map(int, input().split())

if A <= B:
    if A <= C:
        if B <= C:
            print(B)
        else:
            print(C)
    else:
        print(A)
else:
    if A <= C:
        print(A)
    else:
        if B <= C:
            print(C)
        else:
            print(B)