### 백준
### 11724번 연결 요소의 개수
### 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

import sys
# sys.stdin = open("input.txt", 'r')

# DFS 알고리즘을 사용하여 global graph 내
# start_node에서 시작하여 각 node 까지
# 갈 수 있는 모든 node 체크하는 함수
def my_dfs(start_node):
    global N
    global graph
    global visited

    if visited[start_node]:
        return 0

    v = start_node
    stack = [v]

    w_is_next = False

    while stack:
        v = stack[-1]

        for w, w_val in enumerate(graph[v]):
            if w_val == 1 and not visited[w]:
                w_is_next = True
                break

        if w_is_next:
            stack.append(w)
            visited[w] = True
            v = w
            w_is_next = False
        else:
            stack.pop()

    return 1    # DFS 완료 후 counter에 1 증가

# 이 문제 input() 쓰면 시간 초과됨
N, M = map(int, sys.stdin.readline().split())

graph = [ [ 0 for _ in range(N) ] for _ in range(N) ]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u-1][v-1] = 1
    graph[v-1][u-1] = 1

visited = [ False for _ in range(N) ]

counter = 0
for start_node in range(N):
    counter += my_dfs(start_node)

print(counter)