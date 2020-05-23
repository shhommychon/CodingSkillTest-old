### 백준 2단계 if문
### 1330번 두 수 비교하기
### 두 수를 비교한 결과를 출력하는 문제

A, B = map(int, input().split())

if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")