### LeetCode
### 240. Search a 2D Matrix II https://leetcode.com/problems/search-a-2d-matrix-ii/
### <파이썬 알고리즘 인터뷰> 69. 2D 행렬 검색 II

from typing import List

# # Runtime: 198 ms, faster than 72.78% of Python3 online submissions
# # Memory Usage: 20.5 MB, less than 43.54% of Python3 online submissions
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         for row in matrix:
#             if target in row:
#                 return True
#         return False

# 아래는 풀이 1 (p. 538)
# # Runtime: 178 ms, faster than 82.16% of Python3 online submissions for Search a 2D Matrix II.
# # Memory Usage: 20.3 MB, less than 85.51% of Python3 online submissions for Search a 2D Matrix II.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 예외 처리
        if not matrix:
            return False
        
        # 첫행의 맨 뒤
        row = 0
        col = len(matrix[0])-1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # 타겟이 작으면 왼쪽으로 이동
            elif target < matrix[row][col]:
                col -= 1
            # 타겟이 크면 아래로 이동
            elif target > matrix[row][col]:
                row += 1
        return False
