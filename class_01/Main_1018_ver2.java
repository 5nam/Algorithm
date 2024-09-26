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
		
		// idea : 전체 탐색을 하는 것, 한칸씩 이동하면서 
		//int num = 0;
		int change = 0;
		int c_flug = 0; // 이전것이 change 일 경우를 체크
		
		for(int i = 0; i < (n/8)+(n%8); i++) {
			for(int j = 0; j < (m/8) + (m%8); j++) {
				int change_flug = 0;
				for(int k = i; k<i+8; k++) {
					for(int q = j+7; q>=j; q--) {
						if(q == 0) {
							c_flug = 0;
							continue;
						}
						else if(ALL[k][q] == ALL[k][q-1] && ALL[k][q-1] == ALL[k][q+1] && c_flug == 0) {
							c_flug = 1;
							change_flug++;
						}
						else {
							c_flug = 0;
							continue;
						}
					}
				}
				if(change == 0 || change > change_flug) {
					change = change_flug;
				}
			}
		}
		
		/*
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
		*/
		System.out.println(change);
		//System.out.println(num);
	}
}
