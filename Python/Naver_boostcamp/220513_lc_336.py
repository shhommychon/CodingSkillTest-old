### LeetCode
### 336. Palindrome Pairs https://leetcode.com/problems/palindrome-pairs/
### <파이썬 알고리즘 인터뷰> 57. 팰린드롬 페어

from typing import List

class Solution:
    def is_palindrome(self, merged_string: str) -> bool:
        left, right = 0, len(merged_string)-1
        while left < right:
            if merged_string[left] == merged_string[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        Time Limit Exceeded
        Trie 자료구조를 쓰지 않으면 시간내로 풀 수 없는 문제
        """
        answer = list()
        for idx1 in range(len(words)):
            for idx2 in range(len(words)):
                if idx1 == idx2: continue
                if self.is_palindrome(words[idx1] + words[idx2]):
                    answer.append([idx1, idx2])
        return answer

if __name__ == "__main__":
    s = Solution()
    print(s.palindromePairs(
        words = ["abcd","dcba","lls","s","sssll"]
    ))
    print(s.palindromePairs(
        words = ["bat","tab","cat"]
    ))
    print(s.palindromePairs(
        words = ["a",""]
    ))
