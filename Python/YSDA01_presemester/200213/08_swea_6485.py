### 소에아 3단계
### 6485번 삼성시의 버스 노선

# import sys
# sys.stdin = open("input.txt", 'r')

# 풀기 전에 명한이형 풀이를 컨닝해버린 문제

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    A_B = [ 0 for _ in range(5000) ]
    for _ in range(N):
        Ai, Bi = map(int, input().split())
        for n in range(Ai, Bi+1):
            A_B[n-1] += 1

    P = int(input())
    C = []
    for _ in range(P):
        Ci = int(input())
        C.append(str(A_B[Ci-1]))

    print(f"#{test_case} {' '.join(C)}")