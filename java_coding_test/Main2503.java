package java_coding_test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// A가 정답으로 생각할 수 있는 모든 수를 넣어보기
// B가 도전한 내용에 맞는지 확인하기
public class Main2503 {
    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int num = Integer.parseInt(st.nextToken());

        int[][] hint = new int[num][3];
        int answer = 0;

        for(int i = 0; i<num; i++) {
            st = new StringTokenizer(bf.readLine());
            for(int j = 0; j<3; j++) {
                hint[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i = 1; i<10; i++) {
            for(int j = 1; j<10; j++) {
                for(int k = 1; k<10; k++) {
                    if(i == j || j == k || i == k) {
                        continue;
                    }

                    // 숫자가 정해졌다면
                    int cnt = 0;
                    for(int h = 0; h<num; h++) {
                        int number = hint[h][0];
                        int strike = hint[h][1];
                        int ball = hint[h][2];

                        int ball_count = 0;
                        int strike_count = 0;

                        String[] numbers = Integer.toString(number).split("");
                        for(int o = 0; o<3; o++) {
                            int temp = Integer.parseInt(numbers[o]);
                            if((o == 0 && i == temp) ||
                                (o == 1 && j == temp) ||
                                (o == 2 && k == temp)) {

                                    strike_count++;
                                    continue;
                            }
                            else if((i==temp) ||
                                    (j==temp) ||
                                    (k==temp)) {
                                        ball_count++;
                                        continue;
                            }
                        }

                        if(ball == ball_count && strike == strike_count) {
                            cnt++;
                            continue;
                        }
                        break;
                    }

                    if(cnt == num) {
                        answer += 1;
                    }
                }
            }
        }

        System.out.println(answer);
    }
}
