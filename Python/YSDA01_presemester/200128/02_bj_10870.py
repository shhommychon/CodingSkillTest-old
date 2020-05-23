### 백준 11단계 재귀
### 10870번 피보나치 수 5
### 피보나치 수 역시 단순 for문으로도 구할 수 있지만, 학습을 위해 재귀를 써 봅시다.

def fibonacci(n):
    if n != 0 and n != 1:
        return fibonacci(n-1) + fibonacci(n-2)
    elif n == 1:
        return 1
    else:
        return 0

print(fibonacci(int(input())))