### 백준
### 12015번 가장 긴 증가하는 부분 수열 2

# 시간초과

# import sys
# input = sys.stdin.readline

# from collections import deque

# N = int(input())
# nums = deque([ int(n) for n in input().split() ])

# ascending = [[nums.popleft()]]
# while nums:
#     curr_num = nums.popleft()
#     idx = 0
#     while idx < len(ascending):
#         if ascending[idx][-1] < curr_num:
#             ascending[idx].append(curr_num)
#             curr_num = None
#             break
#         idx += 1
#     if curr_num is not None:
#         ascending.append([curr_num])

# print(max([ len(a) for a in ascending ]))

### original code:
### https://letsbegin.tistory.com/50

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

arr = [0]

def binary_search(start, end, target):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid
        else:
            end = start = mid
    return end

for num in nums:
    if num > arr[-1]:
        arr.append(num)
    else:
        start = 1
        end = len(arr) - 1
        idx = binary_search(start, end, num)
        arr[idx] = num

print(len(arr) - 1)
