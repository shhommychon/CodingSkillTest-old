### 소에아 2단계
### 1979번 어디에 단어가 들어갈 수 있을까

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    grid = []
    for _ in range(N):
        grid.append(list(input().split()))

    # 1이 연속되는 수를 모두 이 리스트에 넣습니다.
    possible_word_lengths = []

    # 행에서 검색
    for i in range(N):
        target_row = ''.join(grid[i])
        possible_word_lengths += list(map(len, target_row.split('0')))

    # 열에서 검색
    for i in range(N):
        target_col = ''
        for j in range(N):
            target_col += grid[j][i]
        possible_word_lengths += list(map(len, target_col.split('0')))

    print(f"#{test_case} {possible_word_lengths.count(K)}")
