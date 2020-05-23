### 백준 11단계 재귀
### 10872번 팩토리얼
### 팩토리얼은 단순 for문으로도 구할 수 있지만, 학습을 위해 재귀를 써 봅시다.

def factorial(n):
    if n != 0:
        return factorial(n-1) * n
    else:
        return 1

print(factorial(int(input())))  # 괄호 조심!