package YSDA01_presemester.Baekjoon;

// 백준 2단계 if문
// 9498번 시험 성적
// 시험 점수를 성적으로 바꾸는 문제

import java.util.Scanner;

class AN_9498 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int score = sc.nextInt();

        switch(score/10){
            case 10:
                System.out.println('A');
                break;
            case 9:
                System.out.println('A');
                break;
            case 8:
                System.out.println('B');
                break;
            case 7:
                System.out.println('C');
                break;
            case 6:
                System.out.println('D');
                break;
            default:
                System.out.println('F');
                break;
        }
    }
}