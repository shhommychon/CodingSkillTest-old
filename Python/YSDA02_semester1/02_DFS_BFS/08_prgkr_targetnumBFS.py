### 프로그래머스 Level2
### 타겟 넘버 (깊이/너비 우선 탐색(DFS/BFS))
### https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3

target_hit = 0

# DFS?
def dfs_sum_combination(numbers, target, idx=0, sum=0):
    if idx == len(numbers):
        if sum == target:
            global target_hit
            target_hit += 1
        return

    for n in (numbers[idx], -numbers[idx]):
        dfs_sum_combination(numbers, target, idx+1, sum+n)

def solution(numbers, target):
    dfs_sum_combination(numbers, target)
    return target_hit

# test
if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target))
