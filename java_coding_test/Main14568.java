package java_coding_test;

import java.util.Scanner;

public class Main14568 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int candy = sc.nextInt();
        int reuslt = 0;

        for (int A = 0; A<candy+1; A++) {
            for(int B = 0; B<candy+1; B++) {
                for(int C = 0; C<candy+1; C++) {
                    if(A+B+C == candy) {
                        if (A >= B+2) {
                            if (A != 0 && B !=0 && C!=0) {
                                if (C%2==0) {
                                    reuslt++;
                                }
                            }
                        }
                    }
                }
            } 
        }

        System.out.println(reuslt);
        sc.close();
    }
}
