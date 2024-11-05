package java_coding_test;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] S = new long[n];

        for(int i = 0; i<n; i++) {
            S[i] = sc.nextLong();
        }

        for(int i = 0; i<n; i++) {
            if(solution(S[i])) {
                System.out.println("YES");
                continue;
            }
            System.out.println("NO");
        }

        sc.close();
    }

    public static boolean solution(long num) {
        boolean temp = true;
        for(long j = 2; j < num; j++) {
            if(num % j == 0) {
                if(j >= 1000000) {
                    System.out.println(j);
                    break;
                }
                temp = false;
                break;
            }
        }

        return temp;
    }
}