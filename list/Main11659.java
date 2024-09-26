package list;

import java.util.Scanner;

/**
 * 수의 개수 N(최대 100,000), 합을 구하는 횟수 M(최대 100,000)
 * 시간 복잡도 : O(N+M)
 */
public class Main11659 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        long[] nums = new long[N];
        long[] s_nums = new long[N];

        for(int i = 0; i<N; i++) {
            nums[i] = sc.nextInt();
            
            if(i == 0) {
                s_nums[i] = nums[i];
                continue;
            }

            s_nums[i] = s_nums[i-1] + nums[i];
        }

        long[] result = new long[M];
        for(int i = 0; i<M; i++) {
            int start = sc.nextInt()-2; // 인덱스로 변환하기 위해 -1, 구간합을 구하기 위해 -1
            int end = sc.nextInt()-1; // 인덱스로 변환하기 위해 -1

            if(start < 0) {
                result[i] = s_nums[end];
                continue;
            }

            result[i] = s_nums[end] - s_nums[start];
        }

        for(int i = 0; i<M; i++) {
            System.out.println(result[i]);
        }
        sc.close();
    }
}
