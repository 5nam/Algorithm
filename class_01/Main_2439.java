import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int j;
		for(int i = 0; i < num; i++) {
			for(j = num; j>i+1; j--) {
				System.out.print(" ");
			}
			for(int k =0; k< j;k++) {
				System.out.print("*");
			}
			System.out.println();
		}
		sc.close();
	}
}
