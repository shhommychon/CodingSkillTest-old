### 백준
### 1697번 숨바꼭질

import sys
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())
if N == K:
    print(0)
else: 
    visited = [False] * 100001
    locs = deque()
    locs.append((N, 0))
    do = True
    while locs and do:
        loc, answer = locs.popleft()
        for l in (loc+1, loc-1, 2*loc):
            if l == K:
                print(answer+1); do = False; break
            if 0 <= l <= 100000 and visited[l] == 0:
                visited[l] = 1
                locs.append((l, answer+1))
        if not do: break
