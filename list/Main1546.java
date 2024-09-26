package list;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 시험 과목의 개수 1000개, 시간복잡도 : O(N), 제한시간 2초
 */
public class Main1546 {
    public static void main(String[] args) throws IOException {

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());

        int N = Integer.parseInt(stringTokenizer.nextToken());

        double[] scores = new double[N];
        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        for(int i = 0; i<N; i++) {
            scores[i] = Integer.parseInt(stringTokenizer.nextToken());
        }

        // 최댓값 구하면서 점수 총합 구하기
        double max = scores[0];
        double sum = scores[0];
        for (int i = 1; i<scores.length; i++) {
            if (max < scores[i]) {
                max = scores[i];
            }

            sum += scores[i];
        }

        System.out.println(sum / max * 100 / N);
    }
}
