package list;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int s = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());

        // 임의로 만든 dna 문자열 받기
        st = new StringTokenizer(bf.readLine());
        String[] dna = (st.nextToken()).split("");

        // 부분 문자열에 포함되어야 할 ACGT 최소 개수 받기
        st = new StringTokenizer(bf.readLine());
        int[] acgtMin = {Integer.parseInt(st.nextToken()),
                        Integer.parseInt(st.nextToken()),
                        Integer.parseInt(st.nextToken()),
                        Integer.parseInt(st.nextToken())};

        // 해당하는 문자열 몇 개인지 담는 변수
        int count = 0;

        for(int i = 0; i<s-p+1; i++) {
            // 부분 문자열 ACGT 개수 저장할 배열 초기화
            int[] result = new int[4];
            int start = i;
            int end = i + p - 1;

            while (start != end+1) {
                if(dna[start].equals("A")) {
                    result[0]++;
                    start++;
                }
                else if(dna[start].equals("C")) {
                    result[1]++;
                    start++;
                }
                else if(dna[start].equals("G")) {
                    result[2]++;
                    start++;
                }
                else {
                    result[3]++;
                    start++;
                }
            }

            // 부분 문자열이 비밀번호로 사용 가능한지 확인
            boolean success = result[0] >= acgtMin[0] && result[1] >= acgtMin[1] && result[2] >= acgtMin[2] && result[3] >= acgtMin[3];
            if(success) {
                count++;
            }

            
        }

        System.out.println(count);
        bf.close();
    }
    
}
