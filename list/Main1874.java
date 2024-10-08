package list;

import java.util.Scanner;
import java.util.Stack;

public class Main1874 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        StringBuffer sb = new StringBuffer();

        Stack<Integer> stack = new Stack<>();

        int N = sc.nextInt();

        int nums[] = new int[N];
        for(int i = 0; i<N; i++) {
            nums[i] = sc.nextInt();
        }

        // 수열 반환 가능 여부
        boolean possible = true;

        int num = 1;
        for(int i = 0; i<N; i++) {
            if(nums[i] >= num) {
                while (nums[i] >= num) {
                    stack.push(num);
                    num++;
                    sb.append("+\n");
                }
                stack.pop();
                sb.append("-\n");
            }
            else {
                int temp = stack.pop();
                if(temp > nums[i]) {
                    System.out.println("NO");
                    possible = false;
                    break;
                } else {
                    sb.append("-\n");
                }
            }
        }

        if(possible) System.out.println(sb.toString());

        sc.close();
    }
}