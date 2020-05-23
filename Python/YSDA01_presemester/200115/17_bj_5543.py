### 백준 2단계 if문
### 5543번 상근날드
### 상근날드에서 가장 싼 세트를 찾는 문제

burgers = list()
for _ in range(3):
    burgers.append(int(input()))
cheapest_burger = min(burgers)

coke = int(input())
cider = int(input())
cheapest_drink = coke if coke < cider else cider

print(cheapest_burger + cheapest_drink - 50)