### 백준 28단계 DFS와 BFS
### 1260번 DFS와 BFS
### DFS와 BFS를 다루는 문제

# import sys
# sys.stdin = open("input.txt", 'r')

def my_dfs(start_node):
    global N
    global graph

    v = start_node
    stack = [v]
    visited = [str(v)]

    w_is_next = False

    while stack:
        v = stack[-1]

        for w_idx, w_val in enumerate(graph[v-1]):
            if w_val == 1 and str(w_idx+1) not in visited:
                w_is_next = True
                break

        if w_is_next:
            v = w_idx + 1
            stack.append(v)
            visited.append(str(v))
            w_is_next = False
        else:
            stack.pop()

    return visited

def my_bfs(start_node):
    global N
    global graph

    v = start_node
    queue = [v]
    visited = [str(v)]

    while queue:
        v = queue.pop(0)

        for w_idx, w_val in enumerate(graph[v-1]):
            if w_val == 1 and str(w_idx+1) not in visited:
                queue.append(w_idx+1)
                visited.append(str(w_idx+1))

    return visited

N, M, V = map(int, input().split())

graph = [ [ 0 for _ in range(N) ] for _ in range(N) ]
for _ in range(M):
    i, j = map(int, input().split())
    graph[i-1][j-1], graph[j-1][i-1] = 1, 1

print(' '.join(my_dfs(V)))
print(' '.join(my_bfs(V)))