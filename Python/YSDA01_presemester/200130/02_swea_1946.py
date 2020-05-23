### 소에아 2단계
### 1946번 간단한 압축 풀기

T = int(input())

for test_case in range(1, T + 1):
    print(f"#{test_case}")

    N = int(input())
    C = []  # 문자
    K = []  # 갯수

    # 빈 스트링에다가 문자 Ci를 Ki번 빈 스트링에 더해줍니다.
    string = ''
    for i in range(N):
        Ci, Ki = input().split()
        string += Ci * int(Ki)

    # string을 10의 길이로 나누어 인덱싱을 사용하여 한 조각씩 출력합니다.
    for i in range(len(string) // 10 + (N % 10 != 0)):
        print(string[0 + i*10 : 10 + i*10])
