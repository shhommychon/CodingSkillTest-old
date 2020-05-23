package YSDA01_presemester.Baekjoon;

// 백준 2단계 if문
// 1330번 두 수 비교하기
// 두 수를 비교한 결과를 출력하는 문제

import java.util.Scanner;

class AM_1330 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();

        if (A > B) {
            System.out.println('>');
        } else if (A < B) {
            System.out.println('<');
        } else {
            System.out.println("==");
        }
    }
}
