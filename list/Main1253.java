package list;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(st.nextToken());

        // 숫자 배열 입력받기
        long nums[] = new long[n];
        st = new StringTokenizer(bf.readLine());
        for(int i = 0; i<n; i++) {
            nums[i] = Long.parseLong(st.nextToken());
        }

        // count 변수 선언
        int count = 0;

        // 숫자 배열 정렬
        Arrays.sort(nums);

        // 결과 구하기
        for(int i = 0; i<n; i++) {
            int s = 0;
            int e = n-1;
            long target = nums[i];

            while (s != e) {
                long sum = nums[s] + nums[e];
                if(i == s) {
                    s++;
                    continue;
                }
                else if(i == e) {
                    e--;
                    continue;
                }

                if(target > sum) {
                    s++;
                }
                else if(target < sum) {
                    e--;
                }
                else {
                    count++;
                    break;
                }
            }
        }

        System.out.println(count);
    }
}
