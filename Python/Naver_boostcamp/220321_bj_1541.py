### 백준
### 1541번 잃어버린 괄호

equation = '0' + input()

answer = 0

eqs = equation.split('-')
for i, eq in enumerate(eqs):
    nums = list(map(int, eq.split('+')))
    if i == 0:
        answer += sum(nums)
    else:
        answer -= sum(nums)

print(answer)