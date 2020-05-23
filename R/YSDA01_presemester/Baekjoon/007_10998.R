### 백준 1단계 입출력과 사칙연산
### 10998번 A×B
### 곱셈 문제

# 덧셈, 뺄셈은 똑같이 해서 통과하는데 이건 왜 런타임 에러 뜨냐...
fp = file("stdin", "r")
A = scan(file=fp, what=integer(), n=1)
B = scan(file=fp, what=integer(), n=1)
cat(A*B)