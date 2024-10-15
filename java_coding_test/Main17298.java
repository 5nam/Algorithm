package java_coding_test;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main17298 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        Stack<Integer> stack = new Stack<>();

        // N 과 수열 받기
        int N = Integer.parseInt(st.nextToken());
        int result[] = new int[N];
        int nums[] = new int[N];
        st = new StringTokenizer(bf.readLine());
        for(int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        stack.push(0);
        for(int i = 1; i<N; i++) {
            while (!stack.empty() && nums[i] > nums[stack.peek()]) {
                result[stack.pop()] = nums[i]; 
            }
            stack.push(i);
        }

        while(!stack.empty()) {
            result[stack.pop()] = -1;
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (int i = 0; i<N; i++) {
            bw.write(result[i] + " ");
        }
        bw.write("\n");
        bw.flush();
    }
}