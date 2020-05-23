### 소에아 3단계
### 3131번 100만 이하의 모든 소수

num_list = [ i for i in range(2, 1000000 + 1) ]
prime_list = []

for num in num_list:
    is_prime = True
    for prime in prime_list:
        if num % prime == 0:
            is_prime = False
            break
        # ★★★★★ 에라토스테네스 ★★★★★
        elif prime > num ** 0.5:
            break
    if is_prime:
        prime_list.append(num)
        print(num, end=' ')
