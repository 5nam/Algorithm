package SAFFY;

import java.io.*;
import java.util.*;

class BJ_17298 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());

        int[] ans = new int[N];

        Stack<Integer> origin = new Stack<>();
        Stack<Integer> temp = new Stack<>();

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i<N; i++) {
            origin.push(Integer.parseInt(st.nextToken()));
        }

        for(int i = N-1; i>=0; i--) {

            if (temp.empty()) {
                ans[i] = -1;
                temp.push(origin.pop());
                continue;
            }
            int nowOrigin = origin.pop();
            int nowTemp = temp.pop();

            if (nowOrigin >= nowTemp) {
                while (true) {
                    if(temp.empty()) {
                        ans[i] = -1;
                        break;
                    }
                    
                    int newNum = temp.peek();
                    if(newNum > nowOrigin) {
                        ans[i] = newNum;
                        break;
                    }

                    temp.pop();
                }
                temp.push(nowOrigin);
            }
            else {
                ans[i] = nowTemp;
                temp.push(nowTemp);
                temp.push(nowOrigin);
            }
        }

        StringBuilder sb = new StringBuilder();

        for(int i = 0; i<ans.length; i++) {
            sb.append(ans[i] + " ");
        }

        System.out.print(sb.toString());
    }
}