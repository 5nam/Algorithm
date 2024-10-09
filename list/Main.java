package list;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int N = Integer.parseInt(st.nextToken());
        int result[] = new int[N];
        int nums[] = new int[N];
        st = new StringTokenizer(bf.readLine());
        for(int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        for(int i = 0; i<N; i++) {
            for(int j = i+1; j<N+1; j++) {
                if(i == N-1) {
                    result[i] = -1;
                    break;
                }
                if (nums[i] < nums[j]) {
                    result[i] = nums[j];
                    break;
                }
                else if(nums[i] > nums[j]) {
                    if (j == N-1) {
                        result[i] = -1;
                        break;
                    }
                }
            }
        }

        for (int i = 0; i<N; i++) {
            System.out.print(result[i] + " ");
        }
        
    }
}