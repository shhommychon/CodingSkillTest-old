### 프로그래머스 Level3
### 단어 변환 (깊이/너비 우선 탐색(DFS/BFS))
### https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

def bfs_word_search(begin, target, words):
    if target not in words:
        return 0

    queue = [begin]
    queue_temp = list()
    visited = [begin]

    distance = 1

    while queue:
        v = queue.pop(0)

        # visited에 없는 모든 단어에 대하여,
        for w in words:
            if w not in visited:
                one_diff = False
                more_diff = False
                # 기준 단어 v와 대조 단어 w 간 알파벳 비교
                for w0, v0 in zip(w, v):
                    if w0 != v0:
                        if one_diff:        # 이미 알파벳 1개 차이가 난다면,
                            more_diff = True
                            break
                        one_diff = True     # 알파벳 1개 차이 남
                if one_diff and not more_diff:
                    if w == target:         # w가 target과 동일 시 바로 함수 종료
                        return distance
                    queue_temp.append(w)
                    visited.append(w)

        if len(queue) == 0:
            queue += queue_temp
            queue_temp.clear()
            distance += 1

    return 0    # BFS를 마쳤으나 target에 도달하지 못함

def solution(begin, target, words):
    return bfs_word_search(begin, target, words)

# test
if __name__ == "__main__":
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))

    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log"]
    print(solution(begin, target, words))