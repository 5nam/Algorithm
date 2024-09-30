package list;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main11660 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());

        // n, m 받기
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int m = Integer.parseInt(stringTokenizer.nextToken());
        
        // 기본 배열, 합 배열 선언
        int arr[][] = new int[n+1][n+1];
        long s_arr[][] = new long[n+1][n+1];

        // 기본 배열 받기
        for(int i = 1; i<arr.length; i++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            for(int j = 1; j<arr.length; j++) {
                arr[i][j] = Integer.parseInt(stringTokenizer.nextToken());
            }
        }

        // 합 배열
        for(int i = 1; i<s_arr.length; i++) {
            for(int j = 1; j<s_arr.length; j++) {
                s_arr[i][j] = s_arr[i-1][j] + s_arr[i][j-1] - s_arr[i-1][j-1] + arr[i][j];
            }
        }

        long[] result = new long[m];
        // 합 배열로 구간합 구하기
        for(int i = 0; i<m; i++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            
            int x1 = Integer.parseInt(stringTokenizer.nextToken());
            int y1 = Integer.parseInt(stringTokenizer.nextToken());
            int x2 = Integer.parseInt(stringTokenizer.nextToken());
            int y2 = Integer.parseInt(stringTokenizer.nextToken());

            result[i] = s_arr[x2][y2] - s_arr[x2][y1-1] - s_arr[x1-1][y2] + s_arr[x1-1][y1-1];

        }

        for(long num: result) {
            System.out.println(num);
        }
    }
}
