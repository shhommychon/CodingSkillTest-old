### 소에아 3단계
### 4831번 [파이썬 S/W 문제해결 기본] 1일차 - 전기버스

# import sys
# sys.stdin = open("input.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())

    station = [ 0 for _ in range(N+1) ]

    m = list(map(int, input().split()))
    for i in range(M):
        station[m[i]] = 1

    bus_at = 0
    gas = 0
    answer = 0
    while bus_at < N-K:     # N-K 이상은 충전 없어도 가능
        i = K
        while i > 0:
            if station[bus_at+i] == 1:
                bus_at = bus_at + i
                gas += 1
                break
            else:
                i -= 1
        if i == 0:
            break   # answer = 0

        if bus_at >= N-K:
            answer = gas
            break

    print(f"#{test_case} {answer}")