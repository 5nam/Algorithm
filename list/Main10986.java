package list;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main10986 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bufferedReader.readLine());

        // n, m 받기
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // 합 배열 선언
        long s_arr[] = new long[n+1];

        // 나머지 연산 수행한 합 배열 생성
        st = new StringTokenizer(bufferedReader.readLine());
        for(int i = 1; i<s_arr.length; i++) {
            s_arr[i] = (s_arr[i-1] + Integer.parseInt(st.nextToken())) % m;
        }

        long count[] = new long[m];
        // 나머지를 반영한 합 배열의 같은 값들 개수 세기
        for(int i = 1; i<s_arr.length; i++) {
            count[(int)s_arr[i]]++;
        }


        // count 배열로 공통된 인덱스 수로 경우의 수 구하기
        long result = count[0];
        for(int i = 0; i<m; i++) {
            // count[i] 개 중에 2개를 뽑는 경우의 수 계산 공식 count[i] * (count[i] - 1) / 2
            result += count[i] * (count[i] - 1) / 2;
        }

        System.out.println(result);
        
    }
}
