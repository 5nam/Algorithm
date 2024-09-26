import java.util.Scanner;

public class Main_2884 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int H, M;
		H = sc.nextInt();
		M = sc.nextInt();
		int M_num = M-45;
		
		if(H == 0) {
			if(M_num < 0) {
				H = 23;
				M = 60 + M_num;
			}
			else if(M_num >= 0) {
				M = M_num;
			}
		}
		else if(H != 0) {
			if(M_num < 0) {
				H--;
				M = 60 + M_num;
			}
			else if(M_num >= 0) {
				M = M_num;
			}
		}
		
		System.out.println(H + " " + M);
		sc.close();
	}
}
