### LeetCode
### 76. Minimum Window Substring https://leetcode.com/problems/minimum-window-substring/
### <파이썬 알고리즘 인터뷰> 76. 부분 문자열이 포함된 최소 윈도우

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         elements = { c: s.count(c) for c in t }
#         init_idx = [ s.index(c) for c in t ]
#         if len(init_idx) != len(elements):
#             temp_s = str(s)
#             for element in elements:
#                 num_count = elements[element]
#                 if num_count > 1:
#                     temp_s[temp_s.index(element)] = '_'
#                     if element not in temp_s:
#                         return ''
#                     init_idx.append(temp_s.index(element))
#                     num_count -= 1
                    
#         left, right = min(init_idx), max(init_idx)
#         if right == len(s) - 1:
#             return 
#         answer = s[left:right+1] if right < len(s) else 
#         answer_len = right - left + 1
#         left += 1
#         if left > right:
#             right += 1
        
#         is_proper_substr = False
#         while right < len(s):
#             raise KeyboardInterrupt

# if __name__ == "__main__":
#     s = Solution()
#     print(s.searchMatrix(
#         matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
#         target = 5
#     ))
