### 소에아 2단계
### 2007번 패턴 마디의 길이

T = int(input())

for test_case in range(1, T + 1):
    target = input()

    # 패턴 마디의 길이는 반드시 1에서 10 사이에 있습니다.
    for i in range(1,11):
        if target[0:i] == target[i:2*i]:
            break

    print(f"#{test_case} {i}")