### 백준
### 2667번 단지번호붙이기
### DFS

N = int(input())
apartment = []
for _ in range(N):
    apartment.append(list(map(int, input())))

from typing import List
def coord_to_nums(coord: str) -> List[int]:
    return list(map(int, coord.split('_')))

def nums_to_coord(num1: int, num2: int) -> str:
    return f"{num1}_{num2}" if 0 <= num1 < N or 0 <= num2 < N else 'X'

all_coord = [0] * (N**2)
temp_idx = 0
for r in range(N):
    for c in range(N):
        all_coord[temp_idx] = nums_to_coord(r, c)
        temp_idx += 1

def dfs(curr_r, curr_c, cnt=1):
    for y, x in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        next_coord = nums_to_coord(curr_r+y, curr_c+x)
        if next_coord in all_coord and apartment[curr_r+y][curr_c+x] == 1:
            all_coord.remove(next_coord)
            cnt = dfs(curr_r+y, curr_c+x, cnt=cnt+1)
    return cnt

all_sizes = list()
while all_coord:
    next_coord = all_coord.pop(0)
    r, c = coord_to_nums(next_coord)
    if apartment[r][c] == 1:
        all_sizes.append(dfs(r, c))

print(len(all_sizes))
for ap_size in sorted(all_sizes):
    print(ap_size)