package list;

import java.util.Scanner;

/**
 * 시험 과목의 개수 1000개, 시간복잡도 : O(N), 제한시간 2초
 */
public class Main1546 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        double[] scores = new double[N];

        // 점수 입력받기
        for (int i = 0; i<scores.length; i++) {
            scores[i] = sc.nextInt();
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
        
        sc.close();
    }
}
