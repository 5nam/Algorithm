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
        for(int i = 0; i<n; i++) {
            int num = sc.nextInt();
            for(int j = 3; j<num; j++) {
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
            }
        }
        
        
        System.out.println(dp[n-1]);
        sc.close();
    }
}
