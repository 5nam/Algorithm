package java_coding_test;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main12891 {
    static int[] acgtMin = new int[4];
    static char[] dna;
    // 부분 문자열 ACGT 개수 저장할 배열 초기화
    static int[] result = new int[4];
    // 해당하는 문자열 몇 개인지 담는 변수
    static int count = 0;

    public static void main(String args[]) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int s = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());

        // 임의로 만든 dna 문자열 받기
        st = new StringTokenizer(bf.readLine());
        dna = st.nextToken().toCharArray();

        // 부분 문자열에 포함되어야 할 ACGT 최소 개수 받기
        st = new StringTokenizer(bf.readLine());
        for(int i = 0; i<4; i++) {
            acgtMin[i] = Integer.parseInt(st.nextToken());
        }
        
        int start = 0;
        int end = start + p - 1;
        int pointer = start;
        
        // 가장 처음 부분 문자열이 비밀번호 조건에 맞는지 확인
        checkFirstSubString(start, end, pointer);

        // 가장 처음 부분 문자열을 판단한 데이터를 기반으로 처음 인덱스와 끝 인덱스의 다음 인덱스를 통해
        // 나머지 부분 문자열 비밀번호 조건 충족 여부 구하기
        checkAllSubString(start, end, s, p);

        System.out.println(count);
        bf.close();
    }
    
    static void checkFirstSubString(int start, int end, int pointer) {
        while (pointer != end+1) {
            switch (dna[pointer]) {
                case 'A':
                    result[0]++;
                    pointer++;
                    break;
                    
                case 'C':
                    result[1]++;
                    pointer++;
                    break;
                
                case 'G':
                    result[2]++;
                    pointer++;
                    break;
                
                default:
                    result[3]++;
                    pointer++;
                    break;
            }
        }

        // 부분 문자열이 비밀번호로 사용 가능한지 확인
        boolean success = result[0] >= acgtMin[0] && result[1] >= acgtMin[1] && result[2] >= acgtMin[2] && result[3] >= acgtMin[3];
        if(success) {
            count++;
        }
    }

    static void checkAllSubString(int start, int end, int s, int p) {
        for(int i = 0; i<s-p; i++) {

            switch (dna[start]) {
                case 'A':
                    result[0]--;
                    break;
                
                case 'C':
                    result[1]--;
                    break;
                
                case 'G':
                    result[2]--;
                    break;
                
                default:
                    result[3]--;
                    break;
            }

            // end 는 하나 늘어난 것 카운트 해줘야함
            switch (dna[++end]) {
                case 'A':
                    result[0]++;
                    break;
                
                case 'C':
                    result[1]++;
                    break;
                
                case 'G':
                    result[2]++;
                    break;
                
                default:
                    result[3]++;
                    break;
            }

            // 부분 문자열이 비밀번호로 사용 가능한지 확인
            boolean success = result[0] >= acgtMin[0] && result[1] >= acgtMin[1] && result[2] >= acgtMin[2] && result[3] >= acgtMin[3];
            if(success) {
                count++;
            }

            start++; // start 이제 다음으로 넘어갔으므로
        }
    }

}
