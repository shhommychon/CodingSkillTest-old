package YSDA01_presemester.Baekjoon;

// 백준 2단계 if문
// 2753번 윤년
// 윤년을 판별하는 문제

import java.util.Scanner;

class AO_2753 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();

        if ((year % 4 == 0) && (year % 100 != 0) || (year % 400 == 0))  {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}
