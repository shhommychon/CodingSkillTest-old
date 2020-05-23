package YSDA01_presemester.Baekjoon;

// 백준 2단계 if문
// 10817번 세 수
// 세 정수 중에 두 번째로 큰 정수를 찾는 문제

import java.util.Scanner;
import java.util.Arrays;

class AQ_10817 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        int[] arr = {A, B, C};
        Arrays.sort(arr);

        System.out.println(arr[1]);
    }
}
