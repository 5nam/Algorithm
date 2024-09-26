import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] num = new int[n];
		
		for(int i = 0; i<n; i++) {
			num[i] = sc.nextInt();
		}
		
		int big = num[0];
		int small = num[0];
		
		
		for(int i = 1; i<n; i++) {
			if(big < num[i]) {
				big = num[i];
			}
			if(small > num[i]) {
				small = num[i];
			}
		}
		
		System.out.print(small + " " + big);
		
		sc.close();
	}
}
