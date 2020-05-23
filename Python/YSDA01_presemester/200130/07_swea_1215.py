### 소에아 3단계
### 1215번 [S/W 문제해결 기본] 3일차 - 회문1

# import sys
# sys.stdin = open('test.txt', 'r')

for test_case in range(1, 11):
    unit = int(input())

    grid = [ [] for _ in range(8) ]
    answer = 0

    # 8*8인 기존 그리드에서 전치된 그리드가 grid[0:7]에,
    # 원래 그리드가 grid[8:15]에 저장됩니다.
    for _ in range(8):
        new_list = list(input())
        grid.append(new_list)
        for i in range(8):
            grid[i].append(new_list[i])

    for target in grid:
        half_unit = unit // 2
        is_odd = unit % 2       # 홀수와 짝수일 경우 모두 동일한 코드를 적용시키기 위한 발버둥입니다.
        i = 0
        while i+2*half_unit+is_odd <= 8:    # IndexOutOfRange를 방지합니다.
            front = target[i:i+half_unit]
            back = target[i+half_unit+is_odd:i+2*half_unit+is_odd]
            back.reverse()      # back.reverse()의 반환값은 None입니다.
            if front == back:   # front == back.reverse() 할 수 없습니다.
                answer += 1
            i += 1

    print(f"#{test_case} {answer}")     # #을 빼먹으면 안됩니다.