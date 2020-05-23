### 소에아 2단계
### 1859번 백만 장자 프로젝트

# import sys
# sys.stdin = open('test.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    maymayga = list(map(int, input().split()))

    # 기본 예제들은 통과를 하는데 자꾸 제출하면 시간 초과가 나서
    # 2시간을 헤매다가 for문, len 함수, append 메서드의 사용을
    # 최소한으로 줄이기 위해 리스트의 뒤에서부터 비교를 하는 방식으로
    # 변경해야 했습니다.

    # 그리고 초반에 증가할 때만 매매하는 방식으로 코딩을 했다가,
    # 2 1 2 6 과 같은 예시처럼 매매가가 떨어져도 사야할 경우를
    # 계산하지 못하는 문제점이 발생했습니다.

    counter = 0
    profit = 0
    buy_price = 0

    # 매매가 리스트의 길이가 0이 아닐 때 계속 실행됩니다.
    while len(maymayga):
        # 리스트의 맨 뒤 값을 pop()하여 판매가으로 설정합니다.
        sell_price = maymayga.pop()
        while len(maymayga):
            # 리스트의 맨 뒤 값이 판매가보다 작을 경우,
            if maymayga[-1] < sell_price:
                # 구매가에 해당 값을 더하고,
                buy_price += maymayga.pop()
                # 산 횟수를 1 증가시킵니다.
                counter += 1
            else:
                # 판매가보다 높은 가격이 나타나면 break 합니다.
                break
        # 판매가 * 현재까지 저장된 산 횟수 - 현재까지 합쳐진 구매가
        profit += sell_price * counter - buy_price
        counter = 0     # 산 횟수 초기화
        buy_price = 0   # 구매가 초기화

    print(f"#{test_case} {profit}")
