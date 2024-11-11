package java_coding_test;

import java.util.Scanner;

public class Main1816 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] S = new long[n];

        for(int i = 0; i<n; i++) {
            S[i] = sc.nextLong();
        }

        for(int i = 0; i<n; i++) {
            for(long j = 2; j<1000001; j++) {
                if(S[i]%j == 0) {
                    // 100만 이하의 약수가 존재한다
                    System.out.println("NO");
                    break;
                }
                if (j == 1000000) {
                    // 100만 이하의 약수가 존재하지 않는다
                    System.out.println("YES");
                }
            }
        }  

        sc.close();
    }
}