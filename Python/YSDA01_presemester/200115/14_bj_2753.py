### 백준 2단계 if문
### 2753번 윤년
### 윤년을 판별하는 문제

year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)