package list;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 수의 개수 N(최대 100,000), 합을 구하는 횟수 M(최대 100,000)
 * 시간 복잡도 : O(N+M)
 */
public class Main11659 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());

        int N = Integer.parseInt(stringTokenizer.nextToken());
        int M = Integer.parseInt(stringTokenizer.nextToken());

        // long[] nums = new long[N];
        long[] s_nums = new long[N];

        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        for(int i = 0; i<N; i++) {            
            if(i == 0) {
                s_nums[i] = Integer.parseInt(stringTokenizer.nextToken());
                continue;
            }

            s_nums[i] = s_nums[i-1] + Integer.parseInt(stringTokenizer.nextToken());
        }

        long[] result = new long[M];
        for(int i = 0; i<M; i++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            int start = Integer.parseInt(stringTokenizer.nextToken())-2; // 인덱스로 변환하기 위해 -1, 구간합을 구하기 위해 -1
            int end = Integer.parseInt(stringTokenizer.nextToken())-1; // 인덱스로 변환하기 위해 -1

            if(start < 0) {
                result[i] = s_nums[end];
                continue;
            }

            result[i] = s_nums[end] - s_nums[start];
        }

        for(int i = 0; i<M; i++) {
            System.out.println(result[i]);
        }
    }
}
