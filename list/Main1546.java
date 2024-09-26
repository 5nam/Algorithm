package list;

import java.util.Scanner;

public class Main1546 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        double[] scores = new double[N];

        // 점수 입력받기
        for (int i = 0; i<scores.length; i++) {
            scores[i] = sc.nextInt();
        }

        // 최댓값 구하기
        double max = scores[0];
        for (int i = 1; i<scores.length; i++) {
            if (max < scores[i]) {
                max = scores[i];
            }
        }

        // 점수 조작
        double sum = 0;
        for (int i = 0; i<scores.length; i++) {
            sum += scores[i]/max*100;
        }

        System.out.println(sum/N);
        
        sc.close();
    }
}
