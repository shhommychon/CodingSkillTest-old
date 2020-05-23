package YSDA01_presemester.Baekjoon;

// 백준 1단계 입출력과 사칙연산
// 2588번 곱셈
// 빈 칸에 들어갈 수는?

import java.util.Scanner;

class AL_2588 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i1 = sc.nextInt();
        int i2 = sc.nextInt();

        int i3 = i2 % 10;
        int i4 = i2 / 10 % 10;
        int i5 = i2 / 100 % 10;

        System.out.println(i1 * i3);
        System.out.println(i1 * i4);
        System.out.println(i1 * i5);
        System.out.println(i1 * i2);
    }
}
