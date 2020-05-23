### 프로그래머스 Level1
### 완주하지 못한 선수 (해시)
### https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

def solution(participant, completion):
    loser = set(participant) - set(completion)
    if len(loser) == 1:
        return list(loser)[0]
    else:
        for c in completion:
            if participant.count(c) != completion.count(c):
                return c

# 탈락자는 반드시 한명
solution(["marina", "josipa", "josipa", "nikola", "vinko", "filipa"],
         ["josipa", "filipa", "marina", "nikola"])