package java_coding_test;

import java.util.Scanner;

public class swea {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] nums = new int[n];

        for(int i = 0; i<n; i++) {
            nums[i] = Integer.parseInt(sc.next());
        }

        int left = 0;
        int right = n-1;
        long total = 0;
        long quantity = 0;
        long purchase = 0;

        while (true) {
            if(left == right) {
                total += quantity * nums[right] - purchase;
                break;
            }

            if(nums[left] > nums[right]) {
                if(quantity > 0) {
                    total += quantity * nums[left] - purchase;
                    quantity = 0;
                    purchase = 0;
                    left++;
                }
                else {
                    right--;
                }
            }
            else if(nums[left] < nums[right]) {
                quantity++;
                purchase += nums[left];
                left++;
            }
        }

        System.out.println("#" + test_case + " " + total);

        sc.close();
    }
}
