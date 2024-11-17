package java_coding_test;

import java.util.Scanner;

public class Main1748 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int result = 0;
        int divisor = 10;

        for(int i = 1; i<1_000_000_000; i++) {
            if(n == 0) {
                break;
            }

            if(n < divisor) {
                if((n + (divisor/10-1)) % divisor == 0) {
                    result += i+1;
                    n -= 1;
                } 
                result += n * i;
                n -= n;
                divisor *= 10;
            }
            else {
                int temp = (divisor-1) - (divisor/10 - 1);
                result += temp * i;
                n -= temp;
                divisor *= 10;
            }
        }

        System.out.println(result);
        sc.close();
    }
}
