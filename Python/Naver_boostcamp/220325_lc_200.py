### LeetCode
### 200. Number of Islands https://leetcode.com/problems/number-of-islands/
### <파이썬 알고리즘 인터뷰> 32. 섬의 개수

from typing import List

class Solution:
    def __init__(self):
        self.grid = list()
    
    
    def dfs_alter_grid(self, i: int, j: int):
        if not (0 <= i < len(self.grid) and 0 <= j < len(self.grid[0])):
            return
        
        if self.grid[i][j] == '1':
            self.grid[i][j] = '0'
            for next_i, next_j in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                self.dfs_alter_grid(next_i, next_j)


    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        answer = 0
        for i, row in enumerate(self.grid):
            for j, element in enumerate(row):
                if element == '1':
                    answer += 1
                    self.dfs_alter_grid(i, j)
        
        return answer
