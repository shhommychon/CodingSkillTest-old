### 소에아 3단계
### 4615번 재미있는 오셀로 게임

# import sys
# sys.stdin = open("input.txt", 'r')

def play(row, col, player):
    global N
    global board

    curr = 'B' if player == 1 else 'W'  # 현재 플레이어

    change = [(row, col)]       # 바꿀 좌표

    # 0, 45, 90, 135, 180, 225, 270, 315도 방향으로 체크
    # r, c는 대략 +, - 부호 역할
    for r, c in [(0, -1), (1, -1), (1, 0), (1, 1),
                 (0, 1), (-1, 1), (-1, 0), (-1, -1)]:
        visited = []    # 바꿀 좌표 후보
        i = 1
        R = row + r * i
        C = col + c * i
        while 0 <= C < N and 0 <= R < N:
            if board[C][R] == 0:        # 0을 만나거나 out of range인 경우 change에 더하지 않음
                break
            elif board[C][R] == curr:
                change += visited       # 자기 돌을 만날 경우에만 그 사이 좌표 change에 더함
                break
            else:
                visited.append((R, C))
                i += 1
                R = row + r * i
                C = col + c * i

    for R, C in change:
        board[C][R] = curr


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    board = [ [ 0 for _ in range(N)] for _ in range(N) ]
    board[N//2-1][N//2-1] = 'W'
    board[N//2][N//2-1] = 'B'
    board[N//2-1][N//2] = 'B'
    board[N//2][N//2] = 'W'

    for _ in range(M):
        row, col, player = map(int, input().split())
        row, col = map(lambda x: x - 1, (row, col))     # 인덱스 좌표에 맞춤
        play(row, col, player)

    countB = 0
    countW = 0
    for i in range(N):
        for j in range(N):
            test = board[i][j]
            if test == 'B':
                countB += 1
            elif test == 'W':
                countW += 1

    print(f"#{test_case} {countB} {countW}")
