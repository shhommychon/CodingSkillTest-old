### 소에아 2단계
### 4871번 [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로

# import sys
# sys.stdin = open("input.txt", 'r')

# DFS 알고리즘을 사용하여 주어진 graph에서
# start_node -> target_node 가능 여부 return
def is_reachable(graph, start_node, target_node):
    visited = list()
    stack = []

    v = start_node - 1
    t = target_node - 1

    w_is_next = False

    stack.append(v)             # v를 stack에 push

    while len(stack):
        v = stack[-1]           # v는 stack 맨 끝 원소 (peak)
        visited.append(v)

        # v의 인접 node 중 방문 안 한 w 찾기
        for w, w_val in enumerate(graph[v]):
            if w not in visited:
                if graph[v][w] == 1:
                    w_is_next = True
                    break

        if w_is_next:
            if w == t:          # target_node 도달 시 dfs 즉시 종료
                return 1
            stack.append(w)     # v를 stack에 push
            v = w               # v <- w
            w_is_next = False

        # 해당 v node는 인접 node가 없으므로 stack에서 삭제
        else:
            stack.pop()

    return 0

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    graph = [ [ 0 for _ in range(V) ] for _ in range(V) ]

    for _ in range(E):
        S, G = map(int, input().split())
        graph[S-1][G-1] = 1

    S, G = map(int, input().split())
    print(f"#{test_case} {is_reachable(graph, S, G)}")