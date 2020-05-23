### 프로그래머스 Level1
### 체육복 (탐욕법(Greedy))
### https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3

def solution(n, lost, reserve):
    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 때, 이 학생은 다른 학생에게 체육복을 빌려줄 수 없다.
    lost, reserve = list(set(lost)-set(reserve)), list(set(reserve)-set(lost))

    # 주의: for 루프에서 사용되고 있는 리스트에서 원소를 remove() 하면 인덱싱이 이상해진다.
    borrowed = list()
    for loser in lost:      # 리스트 lost에서 loser 원소를 하나 빼면 그 다음 loser에 그 다음다음 원소가 온다.
        if loser-1 in reserve:
            borrowed.append(loser)
            reserve.remove(loser-1)
        elif loser+1 in reserve:
            borrowed.append(loser)
            reserve.remove(loser+1)

    return n - len(lost) + len(borrowed)

if __name__ == "__main__":
    print(solution(5, [2, 4], [1, 3, 5]))
    print(solution(5, [2, 4], [3]))
    print(solution(3, [3], [1]))

    print(solution(10, [3,8,9], [3,9,10]))