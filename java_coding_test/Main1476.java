package java_coding_test;

import java.util.Scanner;

public class Main1476 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        final int E_CONSTANT = 15;
        final int S_CONSTANT = 28;
        final int M_CONSTANT = 19;

        int e = Integer.parseInt(sc.next());
        int s = Integer.parseInt(sc.next());
        int m = Integer.parseInt(sc.next());

        int count_e = 1;
        int count_s = 1;
        int count_m = 1;
        
        int result = 1;

        while(true) {
            if(e == count_e && s == count_s && m == count_m) {
                break;
            }

            count_e = count_e % E_CONSTANT == 0 ? 1:(count_e % E_CONSTANT)+1;
            count_s = count_s % S_CONSTANT == 0 ? 1:(count_s % S_CONSTANT)+1;
            count_m = count_m % M_CONSTANT == 0 ? 1:(count_m % M_CONSTANT)+1;

            result++;
        }

        System.out.println(result);
        
        sc.close();
    }
}
