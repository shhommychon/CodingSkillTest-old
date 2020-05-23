### 소에아 3단계
### 1206번 [S/W 문제해결 기본] 1일차 - View

# import sys
# sys.stdin = open('input.txt', 'r')

# 총 10개의 테스트 케이스가 주어진다
for test_case in range(1, 11):
    land = int(input())
    buildings = list(map(int, input().split()))
    nice_views = 0

    for i in range(2, land - 2):
        check_views = buildings[i] - max(buildings[i - 2], buildings[i - 1], buildings[i + 1], buildings[i + 2])
        if check_views > 0:
            nice_views += check_views

    print(f"#{test_case} {nice_views}")