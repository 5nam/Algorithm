package list;

import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        long num = sc.nextInt();
        int count = 1;
    

        for(long i = num/2+1; i>=1; i--) {
            /**
             * 1부터 i 까지의 합이 num 을 못 넘는 순간에는 아래 연산을 수행해도 의미가 없으므로 break;
             */
            if(i*(i+1) < 2*num) {
                break;
            }
            long temp = i;
            for(long j = i-1; j>=1; j--) {
                temp += j;
                if(temp > num) {
                    break;
                }
                else if(temp == num) {
                    count++;
                    break;
                }
                else if(temp < num) {
                    continue;
                }
            }
        }

        System.out.println(count);
        sc.close();
    }
}
