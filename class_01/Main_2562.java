import java.util.Scanner;
public class Main_2562 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] num = new int[9];
		for(int i = 0; i<9; i++) {
			num[i] = sc.nextInt();
		}
		
		int big = num[0];
		int index = 0;
		for(int j = 1; j<9; j++) {
			if(big < num[j]) {
				big = num[j];
				index = j;
			}
		}
		System.out.println(big);
		System.out.println(index+1);
	}
}
