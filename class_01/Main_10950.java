import java.util.Scanner;
public class Main_10950 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int[] result = new int[num];
		
		for(int i = 0; i<num; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			result[i] = a+b;
		}
		for(int i = 0; i<num; i++) {
			System.out.println(result[i]);
		}
		sc.close();
	}
}
