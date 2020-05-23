### 소에아 3단계
### 3750번 Digit sum

T = int(input())

answer = []

for test_case in range(1, T + 1):
    f_n = int(input()) % 9
    answer.append( f_n if f_n != 0 else 9 )

# 황호의 도움 (아니 이게 왜 됨)
for test_case in range(1, T + 1):
    print(f"#{test_case} {answer[test_case-1]}")
