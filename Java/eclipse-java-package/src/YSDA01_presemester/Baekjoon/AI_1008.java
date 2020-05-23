package YSDA01_presemester.Baekjoon;

// 백준 1단계 입출력과 사칙연산
// 1008번 A/B
// 나눗셈 문제. 이 문제에는 "스페셜 저지" 표시가 붙어 있는데, 이것은 예제 출력과 꼭 똑같이 출력할 필요는 없고 조건에 맞는 답을 출력하면 된다는 뜻입니다.

import java.util.Scanner;

class AI_1008 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // float로 하니까 틀렸다고 뜸
        double A = sc.nextDouble();
        double B = sc.nextDouble();
        System.out.println(A/B);
    }
}
