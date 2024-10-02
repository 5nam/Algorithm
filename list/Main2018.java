package list;

import java.util.Scanner;

public class Main2018 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        long num = sc.nextInt();
        long count = 1;
        long sum = 1;
        long start_index = 1;
        long end_index = 1;

        while(end_index != num) {
            if (sum > num) {
                sum = sum - start_index;
                start_index++;
            } else if(sum < num) {
                end_index++;
                sum = sum + end_index;
            } else {
                sum = sum - start_index;
                start_index++;
                count++;
            }
        }

        System.out.println(count);

        sc.close();
    }
}
