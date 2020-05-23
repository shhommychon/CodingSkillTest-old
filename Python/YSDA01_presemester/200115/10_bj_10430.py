### 백준 1단계 입출력과 사칙연산
### 10430번 나머지
### 네 개의 계산식을 계산하는 문제. 이 문제를 푼 다음에는 직접 입력을 만들어서 넣어 봅시다. 어떤 사실을 관찰할 수 있나요?

A, B, C = map(int, input().split())
print((A+B)%C)
print((A%C + B%C)%C)
print((A*B)%C)
print((A%C * B%C)%C)