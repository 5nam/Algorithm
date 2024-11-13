package java_coding_test;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] height = new int[9];
        int[] not_answer = new int[2];
        int[] answer = new int[7]; // 포함되지 않는 인덱스 골라내기
        

        for(int i = 0; i<9; i++) {
            height[i] = sc.nextInt();
        }

        // 만약에 9명 중에 7명을 뽑는 것이고 순서는 고려하지 않는다고 하면, 9C7 의 경우의 수를 찾아보면 된다
        // 0 부터 7 따지고, 1 부터 8 따지고, 2부터 다시 0 부터 따지고 ... 이렇게 돌면 전체 경우의 수를 볼 수 있나?
        // 9명 중 2명을 제외하는 걸로 생각하면, 이중 for 문으로 돌려서 모든 경우의 수를 찾을 수 있음
        int total = 0;

        for(int i = 0; i<9; i++) {
            total += height[i];
        }
        
        for(int i = 0; i<9; i++) {
            for(int j = i+1; j<9; j++) {
                if(total - height[i] - height[j] == 100) {
                    not_answer[0] = i;
                    not_answer[1] = j;
                    i = 10; // 정답을 찾으면 2중 for 문을 빠져나가기 위해
                    break;
                }
            }
        }

        int index = 0;
        for(int i = 0; i<9; i++) {
            if(i == not_answer[0] || i == not_answer[1]) {
                continue;
            }
            answer[index] = height[i];
            index++;
        }

        Arrays.sort(answer);
        
        for(int result: answer) {
            System.out.println(result);
        }

        sc.close();
    }
}
