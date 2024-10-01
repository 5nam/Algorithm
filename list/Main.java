package list;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bufferedReader.readLine());

        // n, m 받기
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // 합 배열 선언
        long s_arr[] = new long[n+1];
        int count = 0;

        // 합 배열 만들기
        st = new StringTokenizer(bufferedReader.readLine());
        for(int i = 1; i<s_arr.length; i++) {
            s_arr[i] = s_arr[i-1] + Integer.parseInt(st.nextToken());
        }

        // m 으로 나누어지는 구간합 구하기
        for(int i = 1; i<s_arr.length; i++) {
            for(int j = i; j<s_arr.length; j++) {
                long num = s_arr[j] - s_arr[i-1];
                if(num % m == 0) {
                    count++;
                }
            }
        }

        System.out.println(count);
        
    }
    
}
