### 백준
### 16401번 과자 나눠주기

import sys
input = sys.stdin.readline

M, N = [ int(n) for n in input().split() ]
crackers = [ int(L) for L in input().split() ]

answer = 0
left, right = 1, max(crackers)
while left <= right:
    mid = (left + right) // 2
    cracker_num = sum([ L//mid for L in crackers ])
    if cracker_num < M:
        right = mid - 1
    else: # if cracker_num >= M:
        answer = mid
        left = mid + 1

print(answer)
