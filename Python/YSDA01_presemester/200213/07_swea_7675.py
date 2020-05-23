### 소에아 3단계
### 7675번 통역사 성경이

# import sys
# sys.stdin = open("input.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    words = input().split()
    count_name = [0 for _ in range(N)]
    i = 0
    is_name = True
    end_sen = False

    for w in words:
        w = list(w)

        # 소문자로 시작해도 구두점 체크 했어야 함
        if len(w) != 0 and w[-1] in ('.', '!', '?'):
            end_sen = True  # 문장 마지막
            w.pop()  # 구두점 제거

        if 'A' <= w[0] <= 'Z':
            w.pop(0)  # 대문자 버림
            for c in w:
                if c < 'a' or c > 'z':
                    is_name = False  # 소문자가 아니면 이름이 아님
                    break
            if is_name:
                count_name[i] += 1
            else:
                is_name = True  # 초기화

        if end_sen:
            i += 1  # 문장 마지막이면 인덱스 옮김
            end_sen = False  # 초기화

    print(f"#{test_case} {' '.join(map(str, count_name))}")