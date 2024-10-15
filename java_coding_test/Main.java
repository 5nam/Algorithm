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
            if(S[i] % 2 == 0) {
                System.out.println("NO");
                continue;
            } else {
                int devision = 3;
                while(devision < S[i]) {
                    if(S[i] % devision == 0) {
                        System.out.println("NO");
                        break;
                    }
                    devision += 2;
                }
                if(devision >= S[i]) {
                    System.out.println("YES");
                }
            }
        }

        sc.close();
    }
}
