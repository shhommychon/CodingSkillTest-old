package YSDA01_presemester.Baekjoon;

// 백준 2단계 if문
// 2884번 알람 시계
// 시간 뺄셈 문제

import java.util.Scanner;

class AP_2884 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int M = sc.nextInt();

        if (M >= 45) {
            M -= 45;
        } else {
            M += 15;
            if (H == 0) {
                H = 23;
            } else {
                H -= 1;
            }
        }

        // H + ' ' + M 을 하니 ' '의 아스키코드 값 32로 계산이 됨!
        System.out.println(H + " " + M);
    }
}
