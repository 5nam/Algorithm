import java.util.Scanner;
public class Main_11654 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		char m = 0;
		for(int i = 0; i<s.length(); i++) {
			m = s.charAt(i);
		}
		System.out.println((int)m);
		sc.close();
	}
}
