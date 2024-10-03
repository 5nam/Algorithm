package list;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main1940 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // n 입력받기
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        // m 입력받기
        st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());

        // nums(n 개의 재료들) 입력받고, 정렬
        st = new StringTokenizer(br.readLine());
        long nums[] = new long[n];
        for(int i = 0; i<n; i++) {
            nums[i] = Long.parseLong(st.nextToken());
        }

        Arrays.sort(nums);

        // start, end, count 변수 초기화
        int start = 0;
        int end = n-1;
        int count = 0;

        while (start != end) {
            long sum = nums[start] + nums[end];
            if(sum > m) {
                end--;
            }
            else if(sum < m) {
                start++;
            }
            else {
                count++;
                start++;
                end--;
            }
        }

        System.out.println(count);

    }
}
