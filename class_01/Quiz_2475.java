import java.util.Scanner;

public class Quiz_2475 {
	public static void main(String[] args) {
		int num = 0;
		int sum = 0;
		Scanner sc = new Scanner(System.in);
		for(int i = 0; i<5; i++) {
			num = sc.nextInt();
			sum += num*num;
		}
		System.out.print(sum%10);
		sc.close();
	}
}

// 백준 사이트에서 컴파일 에러 남 -> 자바 클래스 명을 Main 으로 설정해주어야 백준에서 오류가 안남!
// error: ‘import’ does not name a type
// error: expected unqualified-id before ‘public’