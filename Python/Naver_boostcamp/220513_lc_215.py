### LeetCode
### 215. Kth Largest Element in an Array https://leetcode.com/problems/kth-largest-element-in-an-array/
### <파이썬 알고리즘 인터뷰> 55. 배열의 K번째 큰 요소

from typing import List
import heapq

class Solution:
    def findKthLargest_sort(self, nums: List[int], k: int) -> int:
        """
        Runtime: 86 ms
        Memory Usage: 14.7 MB
        """
        return sorted(nums, reverse=True)[k-1]
    
    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        """
        Runtime: 99 ms
        Memory Usage: 14.8 MB
        """
        nums = [ -n for n in nums ]
        heapq.heapify(nums)
        for _ in range(k):
            answer = heapq.heappop(nums)
        return -answer

if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest_sort(
        nums = [3,2,1,5,6,4],
        k = 2
    ))
    print(s.findKthLargest_sort(
        nums = [3,2,3,1,2,4,5,5,6],
        k = 4
    ))
