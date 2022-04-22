### LeetCode
### 424. Longest Repeating Character Replacement https://leetcode.com/problems/longest-repeating-character-replacement/
### <파이썬 알고리즘 인터뷰> 77. 가장 긴 반복 문자 대체

# Wrong Answer

# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         s_list = list()
#         curr_count = 0
#         curr_alpha = 'init'
#         for c in s+'e': # 'e': end
#             if c != curr_alpha:
#                 if curr_count != 0:
#                     s_list.append((curr_count, curr_alpha))
#                 curr_count = 1
#                 curr_alpha = c
#             else:
#                 curr_count += 1
        
#         if len(s_list) >= 3:
#             seq_lengths = list()
#             idx = 0
#             while idx < len(s_list) - 2:
#                 left, mid, right = s_list[idx], s_list[idx+1], s_list[idx+2]
#                 if left[1] == right[1] and mid[0] <= k:
#                     seq_lengths.append(left[0]+k+right[0])
#                 idx += 1

#             if len(seq_lengths) != 0:
#                 return max(seq_lengths)
#             else:
#                 s_list = sorted(s_list)
#                 big = s_list[-1][0]
#                 small = sum([s[0] for s in s_list[:-1]])
#                 return big + (k if k < small else small)
        
#         elif len(s_list) == 2:
#             big, small = max(s_list)[0], min(s_list)[0]
#             return big + (k if k < small else small)

#         else: # if len(s_list) == 1:
#             return s_list[0][0]
