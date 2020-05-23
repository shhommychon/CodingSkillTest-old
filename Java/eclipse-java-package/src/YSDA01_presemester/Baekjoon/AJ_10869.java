package YSDA01_presemester.Baekjoon;

// 백준 1단계 입출력과 사칙연산
// 10869번 사칙연산
// 모든 연산 문제

import java.util.Scanner;

class AJ_10869 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();

        System.out.println(A+B);
        System.out.println(A-B);
        System.out.println(A*B);
        System.out.println(A/B);
        System.out.println(A%B);
    }
}
