### 소에아 3단계
### 5208번 [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2

# import sys
# sys.stdin = open("input.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    Mi = list(map(int, input().split()))
    N = Mi.pop(0)

    visited = 0
    bus_at = 0
    while bus_at + Mi[bus_at] < N-1:
        # bus_at에서 출발 시 교체 가능한 경우의 수만큼 원소 생성
        comparison = []     # 각 원소는 다음 번에 가게되는 거리

        for if_bus_at in range(Mi[bus_at]):
            # 이미 if_bus_at 만큼 (현재 배터리를 사용하여) 움직였기 때문에 거리에 더해줌
            comparison.append(Mi[bus_at + if_bus_at + 1] + if_bus_at)

        bus_at += comparison.index(max(comparison)) + 1
        visited += 1

    print(f"#{test_case} {visited}")