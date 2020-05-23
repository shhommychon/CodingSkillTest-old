### 소에아 3단계
### 2817번 부분 수열의 합

# 내가 받은 힌트는 "재귀"
def combination(input_list, make_this_num):
    ingredients = list(input_list)
    current_comb_num = 0

    i = 0
    while i in range(len(ingredients)):
        if ingredients[i] > make_this_num:
            del ingredients[i]
        else:
            break

    if sum(ingredients) == make_this_num:
        return 1
    elif sum(ingredients) < make_this_num:
        return 0
    elif make_this_num == 0:
        return 1
    else:
        while len(ingredients) > 0:
            max_list = ingredients.pop(0)
            current_comb_num += combination(ingredients, make_this_num - max_list)
        return current_comb_num

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    num_list = list(map(int, input().split()))

    num_list.sort(reverse=True)
    num_combination = 0
    while len(num_list) > 0:
        max_list = num_list.pop(0)
        num_combination += combination(num_list, K - max_list)

    print(f"#{test_case} {num_combination}")