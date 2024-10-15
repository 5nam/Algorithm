package java_coding_test;

import java.util.Scanner;

/**
 * N 은 100, 시간복잡도 O(N)
 */
public class Main11720 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int number = Integer.parseInt(sc.nextLine());
        String[] numbers = sc.nextLine().split("");
        int result = 0;

        for (int i = 0; i<number; i++) {
            result += Integer.parseInt(numbers[i]);
        }

        System.out.println(result);

        sc.close();
    }
}