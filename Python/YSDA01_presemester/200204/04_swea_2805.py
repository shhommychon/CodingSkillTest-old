### 소에아 3단계
### 2805번 농작물 수확하기

T = int(input())

for test_case in range(1, T + 1):
    size = int(input())

    row_neglect_nums = []
    row_neglect_nums += [ i for i in range(size // 2, 0, -1) ]
    row_neglect_nums += [ i for i in range(0, size // 2 + 1) ]

    sum_list = 0
    for i in range(size):
        blank_num = row_neglect_nums[i]
        count_num = size - 2 * blank_num
        s = list(map(int, list(input())))
        sum_list += sum(s[blank_num:blank_num+count_num])

    print(f"#{test_case} {sum_list}")
