### 백준 1단계 입출력과 사칙연산
### 2588번 곱셈
### 빈 칸에 들어갈 수는?

# 두 줄 연속으로 받을 때
num1 = int(input())
num2 = int(input())

num3 = num2 % 10
num4 = num2 // 10 % 10
num5 = num2 // 100 % 10

print(num1 * num3)
print(num1 * num4)
print(num1 * num5)
print(num1 * num2)