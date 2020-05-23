### 소에아 3단계
### 5607번 [Professional] 조합

T = int(input())

for test_case in range(1, T + 1):
    N, R = map(int, input().split())

    combi = 1

    n = N
    for _ in range(R):
        combi *= n
        n -= 1

    r = R
    for _ in range(R):
        combi //= r
        r -= 1

    while combi >= 1234567891:
        combi -= 1234567891
    print(f"#{test_case} {combi}")
