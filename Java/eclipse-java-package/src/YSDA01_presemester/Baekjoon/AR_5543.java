package YSDA01_presemester.Baekjoon;

// 백준 2단계 if문
// 5543번 상근날드
// 상근날드에서 가장 싼 세트를 찾는 문제

import java.util.Scanner;
import java.util.Arrays;

class AR_5543 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sangDuckBurger = sc.nextInt();
        int jungDuckBurger = sc.nextInt();
        int haDuckBurger = sc.nextInt();
        int coke = sc.nextInt();
        int cider = sc.nextInt();

        int[] burgers = {sangDuckBurger, jungDuckBurger, haDuckBurger};
        Arrays.sort(burgers);

        int cheapestBurger = burgers[0];
        int cheapestDrink = Math.min(coke, cider);
        // 참고: 자바의 Math.min(), Math.max() 함수들은 멍청해서 두개 인자만 비교 가능!

        System.out.println(cheapestBurger + cheapestDrink - 50);
    }
}
