import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		String C[] = new String[n];
		char ALL[][] = new char[50][50];
		// �Է¹ޱ�
		for(int i = 0; i<n; i++) {
			C[i] = sc.next();
		}
		
		// �и��Ͽ� �ٽ� �����ϱ�
		for(int i = 0; i<n; i++) {
			for(int j = 0; j<m; j++) {
				ALL[i][j] = C[i].charAt(j);
			}
		}
		
		//int num = 0;
		int change = 0;
		int c_flug = 0; // �������� change �� ��츦 üũ
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
