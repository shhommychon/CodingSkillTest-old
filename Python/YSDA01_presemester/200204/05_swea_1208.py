### 소에아 3단계
### 1208번 [S/W 문제해결 기본] 1일차 - Flatten

# import sys
# sys.stdin = open('input.txt', 'r')

# 총 10개의 테스트 케이스가 주어진다
for test_case in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    boxes.sort()

    short_idx = 0       # sort() 직후 제일 낮은 박스의 인덱스
    tall_idx = 99       # sort() 직후 제일 높은 박스의 인덱스
    shortest = boxes[0]     # sort() 직후 제일 낮은 박스의 높이
    tallest = boxes[99]     # sort() 직후 제일 높은 박스의 높이
    while dump:
        # 평탄화가 모두 끝났을 때의 편차가 0이라면,
        # 그 때 가능한 0을 제외한 최소 편차는 2
        # 따라서 편차가 0, 1일때 무조건 끝
        if tallest - shortest in (0, 1):
            break

        else:
            # 평탄화
            boxes[tall_idx] -= 1
            boxes[short_idx] += 1
            dump -= 1

            # 가장 높았던 박스 왼쪽의 박스 높이가 이전 tallest와 동일하다면,
            if boxes[tall_idx-1] == tallest:
                tall_idx -= 1
            # 아니라면, 더이상 tallest 높이를 가진 박스 없음 - 초기화
            else:
                tallest = boxes[tall_idx]
                tall_idx = 99

            # 가장 낮았던 박스 왼쪽의 박스 높이가 이전 shortest와 동일하다면,
            if boxes[short_idx+1] == shortest:
                short_idx += 1
            # 아니라면, 더이상 shortest 높이를 가진 박스 없음 - 초기화
            else:
                shortest = boxes[short_idx]
                short_idx = 0

    print(f"#{test_case} {tallest - shortest}")

