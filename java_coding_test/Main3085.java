package java_coding_test;

import java.util.Scanner;

public class Main3085 {
    public static void main(String[] args) {
        // 한 칸씩 탐색하기
        // 만약 지금 선택한 칸이 (x, y) 라고 하면
        // x 축, y 축 기준으로 인접한 요소랑 같으면 바꾸지 않고, 같지 않으면 바꾼다.

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int max = 0;

        // 입력받기
        // String[][] input = new String[n][n];
        String[][] tetris = new String[n][n];

        for(int i = 0; i<n; i++) {
            String line = sc.next();
            tetris[i] = line.split("");
        }

        // 가장 처음 Max 찾기
        for(int k = 0; k<n; k++) {
            int count_x = 1;
            int count_y = 1;
            for(int l = 1; l<n; l++) {
                if(tetris[k][l-1].equals(tetris[k][l])) {
                    count_x++;
                }
                if(tetris[l-1][k].equals(tetris[l][k])) {
                    count_y++;
                }
            }

            if(count_x > max) {
                max = count_x;
            }
            if(count_y > max) {
                max = count_y;
            }
        }

        // x축, y축 기준으로 인접한 요소 하나씩 바꿔보기
        for(int x = 0; x<n; x++) {
            for(int y = 0; y<n-1; y++) {
                // x 축 전환
                if(!tetris[x][y].equals(tetris[x][y+1])) {
                    String temp = tetris[x][y];
                    tetris[x][y] = tetris[x][y+1];
                    tetris[x][y+1] = temp;

                    for(int k = 0; k<n; k++) {
                        int count_x = 1;
                        int count_y = 1;
                        for(int l = 1; l<n; l++) {
                            if(tetris[k][l-1].equals(tetris[k][l])) {
                                count_x++;
                            }
                            if(tetris[l-1][k].equals(tetris[l][k])) {
                                count_y++;
                            }
                        }

                        if(count_x > max) {
                            max = count_x;
                        }
                        if(count_y > max) {
                            max = count_y;
                        }
                    }

                    // 원래 배열로 원상복구
                    temp = tetris[x][y];
                    tetris[x][y] = tetris[x][y+1];
                    tetris[x][y+1] = temp;
                }

                // y 축 전환
                if(!tetris[x][y].equals(tetris[y+1][x])) {
                    String temp = tetris[x][y];
                    tetris[x][y] = tetris[y+1][x];
                    tetris[y+1][x] = temp;

                    for(int k = 0; k<n; k++) {
                        int count_x = 1;
                        int count_y = 1;

                        for(int l = 1; l<n; l++) {
                            if(tetris[k][l-1].equals(tetris[k][l])) {
                                count_x++;
                            }
                            if(tetris[k][l-1].equals(tetris[l][k])) {
                                count_y++;
                            }
                        }

                        if(count_x > max) {
                            max = count_x;
                        }
                        if(count_y > max) {
                            max = count_y;
                        }
                    }

                    temp = tetris[x][y];
                    tetris[x][y] = tetris[y+1][x];
                    tetris[y+1][x] = temp;
                }
            }
        }

        System.out.println(max);
        sc.close();
    }
}
