### 소에아 4단계
### 1218번 [S/W 문제해결 기본] 4일차 - 괄호 짝짓기

# import sys
# sys.stdin = open("input.txt", 'r')

for test_case in range(1, 11):
    length = int(input())
    string = input()

    stack = []
    is_string = 1

    for s in string:
        if s in ('{', '[', '(', '<'):
            stack.append(s)
        elif (stack.pop(), s) not in (('{', '}'), ('[', ']'), ('(', ')'), ('<', '>')):
            is_string = 0
            break

    print(f"#{test_case} {is_string}")