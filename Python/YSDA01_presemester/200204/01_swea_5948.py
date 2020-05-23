### 소에아 3단계
### 5948번 새샘이의 7-3-5 게임

T = int(input())

for test_case in range(1, T + 1):
    a, b, c, d, e, f, g = sorted(list(map(int, input().split())))
    possible_fifth = {g+f+c, g+e+d, g+f+b, g+e+c, f+e+d, g+f+a, g+e+b, g+d+c, f+e+c}     # 중복 방지
    possible_fifth = sorted(list(possible_fifth))   # 크기 순
    possible_fifth.reverse()    # 순서 큰 > 작은
    print(f"#{test_case} {possible_fifth[2]}")