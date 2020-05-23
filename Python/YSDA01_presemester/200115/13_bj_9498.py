### 백준 2단계 if문
### 9498번 시험 성적
### 시험 점수를 성적으로 바꾸는 문제

grade = int(input())

# >= , > 범위 잘 보고 제출 누를 것!
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")