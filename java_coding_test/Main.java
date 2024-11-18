package java_coding_test;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int dp[] = new int[11];

        dp[0] = 1;
        dp[1] = 2;
        dp[2] = 4;

        int n = sc.nextInt();
        int[] result = new int[n];

        for(int i = 0; i<n; i++) {
            int num = sc.nextInt();
            for(int j = 3; j<num; j++) {
                dp[j] = dp[j-1] + dp[j-2] + dp[j-3];
            }
            result[i] = dp[num-1];
        }
        
        for(int num: result) {
            System.out.println(num);
        }
        
        sc.close();
    }
}
