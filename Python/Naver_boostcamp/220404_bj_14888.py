### 백준
### 14888번 연산자 끼워넣기
###
### original code:
### https://github.com/HeoSeokYong/BoostCampAlgorithmStudy_LEVEL2_CV11/blob/main/week5/Mon/selim_dfs.py

import sys
input = sys.stdin.readline

N = int(input())
nums = [ int(n) for n in input().split() ]
ops = [ int(n) for n in input().split() ]

min_max = [float("inf"), float("-inf")]
def dfs(num_idx, result):
    if sum(ops) == 0:
        min_max[0] = min(min_max[0], result)
        min_max[1] = max(min_max[1], result)
        return
    
    if ops[0] >= 1:
        ops[0] -= 1 
        newsum = result + nums[num_idx]
        dfs(num_idx+1, newsum)
        ops[0] += 1
    if ops[1] >= 1:
        ops[1] -= 1
        newsum = result - nums[num_idx]
        dfs(num_idx+1, newsum)
        ops[1] += 1
    if ops[2] >= 1:
        ops[2] -= 1 
        newsum = result * nums[num_idx]
        dfs(num_idx+1, newsum)
        ops[2] += 1
    if ops[3] >= 1:
        ops[3] -= 1
        newsum = -1 * ((-result) // nums[num_idx]) if result < 0 else result // nums[num_idx]
        dfs(num_idx+1, newsum)
        ops[3] += 1
    
dfs(1, nums[0])
print(min_max[1])
print(min_max[0])
