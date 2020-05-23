### 백준 11단계 재귀
### 11729번 하노이 탑 이동 순서
### 재귀적인 패턴을 재귀함수로 찍는 문제 2

# 해당 함수에 return 값이 있게 하는 방법??
def hanoi(disk_num, move_from=1, move_to=3):
    # 글로벌 변수를 쓰지 않고 함수를 만드는 방법??
    global counter
    global steps

    empty = 6 - (move_from + move_to)

    if disk_num != 1:
        # 맨 밑 디스크를 제외한 모든 디스크를 빈 공간에 'hanoi()' 한다
        hanoi(disk_num-1, move_from, empty)

        # 맨 밑 디스크를 목적 위치로 옮긴다
        counter += 1
        steps.append(f"{move_from} {move_to}")

        # 맨 밑 디스크를 제외한 모든 디스크를 빈 공간에 'hanoi()' 한다
        hanoi(disk_num-1, empty, move_to)

    else:   # disk_num == 1
        counter += 1
        steps.append(f"{move_from} {move_to}")

N = int(input())

counter = 0
steps = []

hanoi(N)

print(counter)
print("\n".join(steps))
