### 프로그래머스 Level1
### 크레인 인형뽑기 게임 (2019 카카오 개발자 겨울 인턴십 코딩 테스트 실전 모의고사)
### https://programmers.co.kr/competitions/145/kakao-internship-test
### https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3


def board_to_queues(board):
    list_of_queues = [ [] for _ in range(len(board)) ]
    for row in board:
        for i in range(len(row)):
            if row[i] != 0:
                list_of_queues[i].append(row[i])

    return list_of_queues


def solution(board, moves):
    board_queues = board_to_queues(board)
    bucket = []     # stack

    hit = 0

    for m in moves:
        if len(board_queues[m-1]):
            doll = board_queues[m-1].pop(0)
            if len(bucket):
                if bucket[-1] == doll:
                    bucket.pop()
                    hit += 2
                    continue
            bucket.append(doll)

    return hit


if __name__ == "__main__":
    my_answer = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
    print(f"{my_answer} : {my_answer == 4}")
