### 백준
### 1389번 케빈 베이컨의 6단계 법칙
### 케빈 베이컨의 수가 가장 작은 사람을 찾는 게임

# import sys
# sys.stdin = open("input.txt", 'r')

# BFS 알고리즘을 통해 start_node에서부터 각 원소까지의 거리를
# visited에 저장 후 visited 리스트 원소들의 합을 return.
# 이 함수에서 queue는 start_node로부터 같은 거리에 있는 원소들이
# 모두 pop된 후에야 그 다음 거리에 있는 원소들을 한번에 저장
def kevinbacon(graph, start_node):
    v = start_node
    queue = [v]
    queue_temp = list()
    visited = [v]
    kb = [ 0 for _ in range(len(graph)) ]

    distance = 1

    while queue:
        v = queue.pop(0)

        for w_idx, w_val in enumerate(graph[v]):
            if w_val == 1 and w_idx not in visited:
                queue_temp.append(w_idx)
                visited.append(w_idx)
                kb[w_idx] = distance

        if len(queue) == 0:
            queue += queue_temp
            queue_temp.clear()
            distance += 1

    return sum(kb)

N, M = map(int, input().split())

graph = [ [ 0 for _ in range(N) ] for _ in range(N) ]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A-1][B-1], graph[B-1][A-1] = 1, 1

kb = list()
for start_node in range(N):
    kb.append(kevinbacon(graph, start_node))

print(f"{kb.index(min(kb))+1}")