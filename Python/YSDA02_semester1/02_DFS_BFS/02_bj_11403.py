### 백준
### 11403번 경로 찾기
### 가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

# import sys
# sys.stdin = open("input.txt", 'r')

# DFS 알고리즘을 사용하여 global graph 내
# start_node에서 시작하여 각 node 까지
# 갈 수 있는지 여부 리스트로 return
def reachable(start_node):
    global N
    global graph

    v = start_node
    stack = [v]

    visited = [ '0' for _ in range(N) ]

    w_is_next = False

    while stack:
        v = stack[-1]

        # v의 인접 node 중 방문 안 한 w 찾기
        for w, w_val in enumerate(graph[v]):
            if w_val == '1' and visited[w] != '1':   # 연결 여부 확인 후 방문 여부 확인
                w_is_next = True
                break

        if w_is_next:
            stack.append(w)
            visited[w] = '1'
            v = w
            w_is_next = False
        else:
            stack.pop()

    return visited

N = int(input())

graph = []
for _ in range(N):
    graph.append(input().split())

graph_connected = []
for start_node in range(N):
    graph_connected.append(reachable(start_node))

for i in range(N):
    print(' '.join(graph_connected[i]))