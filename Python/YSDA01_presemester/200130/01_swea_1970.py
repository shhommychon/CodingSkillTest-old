### 소에아 2단계
### 1970번 쉬운 거스름돈

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    jandons = []

    for money in (50000, 10000, 5000, 1000, 500, 100, 50, 10):
        jandons.append(str(N // money))
        N = N % money

    print("#" + str(test_case))
    print(" ".join(jandons))