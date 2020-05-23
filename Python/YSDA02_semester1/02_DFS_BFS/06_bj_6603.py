### 백준
### 6603번 로또
### k(k>6)개의 숫자가 있는 집합 S가 주어졌을 때, 6개의 수를 고르는 모든 방법

# 이거 백트래킹인거 같은데

def dfs_combination(num_list, prev=[], counter=0):
    global combinations     # visited

    if counter == 6:
        combinations.append(prev)
        return

    counter += 1

    for i in range(len(num_list)):
        if len(prev) + len(num_list[i:]) < 6:
            continue        # 예) 1 2 3 4 5 6 7 에서 3이 첫번째 원소일 경우
        if len(prev) != 0 and int(num_list[i]) < int(prev[-1]):
            continue        # 예) 1 2 3 4 5 6 7 에서 1 2 3 4 6 5, 2 1 4 3 5 6 등 경우
        if num_list[i] not in prev:
            dfs_combination(num_list, prev + [num_list[i]], counter)

while True:
    num_list = input().split()
    N = int(num_list.pop(0))

    if N == 0:
        break

    combinations = list()
    dfs_combination(num_list)

    for c in combinations:
        print(' '.join(c))
    print()