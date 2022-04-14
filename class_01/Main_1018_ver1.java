// 문제를 잘못 이해함 : 체스판 전체가 아닌 8*8 로 잘라서 제일 최적화 된 부분만 잘라내는 것
import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		String C[] = new String[n];
		char ALL[][] = new char[50][50];
		// 입력받기
		for(int i = 0; i<n; i++) {
			C[i] = sc.next();
		}
		
		// 분리하여 다시 저장하기
		for(int i = 0; i<n; i++) {
			for(int j = 0; j<m; j++) {
				ALL[i][j] = C[i].charAt(j);
			}
		}
		
		//int num = 0;
		int change = 0;
		int c_flug = 0; // 이전것이 change 일 경우를 체크
		for(int i = 0; i<n; i++) {
			for(int j = m-1; j>=0; j--) {
				//num++;
				//c_flug = 0;
				if(j == 0) {
					c_flug = 0;
					continue;
				}
				else if(ALL[i][j] == ALL[i][j-1] && ALL[i][j-1] == ALL[i][j+1] && c_flug == 0) {
					c_flug = 1;
					change++;
				}
				else {
					c_flug = 0;
					continue;
				}
			}
		}
		System.out.println(change);
		//System.out.println(num);
	}
}
