### 백준 2단계 if문
### 2884번 알람 시계
### 시간 뺄셈 문제

H, M = map(int, input().split())

new_minute = (60 + M - 45) % 60
new_hour = (24 + (H + (M - 45)//60)) % 24   # 식 제대로 세우고 제출할 것!

print(str(new_hour) + ' ' + str(new_minute))