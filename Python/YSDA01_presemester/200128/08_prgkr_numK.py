### 프로그래머스 Level1
### K번째수 (정렬)
### https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        subarray = array[i-1:j]
        answer.append(sorted(subarray)[k-1])
    return answer

if __name__ == "__main__":
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))