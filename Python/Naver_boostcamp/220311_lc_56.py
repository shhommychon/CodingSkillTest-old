### LeetCode
### 56. Merge Intervals https://leetcode.com/problems/merge-intervals/
### <파이썬 알고리즘 인터뷰> 59. 구간 병합

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = list()
        for interval in sorted(intervals):
            if len(answer) == 0 or answer[-1][-1] < interval[0]:
                answer.append(interval)
            elif answer[-1][-1] >= interval[1]:
                continue
            else: # if interval[0] <= answer[-1][-1] < interval[1]:
                answer[-1][-1] = interval[1]
        
        return answer
