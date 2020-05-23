### 프로그래머스 Level1
### 소수 찾기 (연습문제)
### https://programmers.co.kr/learn/courses/30/lessons/12921?language=python3

# 소프트웨어 아카데미 3131번 참고


def solution(n):
    num_list = [ n_ for n_ in range(2, n+1) ]
    prime_list = []

    for num in num_list:
        is_prime = True
        for prime in prime_list:
            # ★★★★★ 에라토스테네스 ★★★★★
            if prime > num ** 0.5:
                break
            elif num % prime == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)

    return len(prime_list)


if __name__ == "__main__":
    answer1 = solution(10)
    answer2 = solution(5)

    print(f"{answer1} : {answer1 == 4}")
    print(f"{answer2} : {answer2 == 3}")

