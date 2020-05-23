### 백준 1단계 입출력과 사칙연산
### 1001번 A-B
### 두 수를 입력받고 뺄셈을 한 결과를 출력하는 문제

fp = file("stdin", "r")
A = scan(file=fp, what=integer(), n=1)
B = scan(file=fp, what=integer(), n=1)
cat(A-B)