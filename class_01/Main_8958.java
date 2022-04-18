import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		String[] str = new String[num];
		char[][] answer = new char[num][80];
		for(int i = 0; i<num; i++) {
			str[i] = sc.next();
		}
		
		int score = 0;
		int flug = 0; // 정답이 연속된 횟수, 0이면 연속 x
		for(int i = 0; i<num; i++) {
			score = 0;
			flug = 0;
			for(int j = 0; j<str[i].length(); j++) {
				answer[i][j] = str[i].charAt(j);
				if(answer[i][j] == 'O') {
					if(flug == 0) {
						score++;
						flug++;
					}
					else if(flug > 0) {
						flug++;
						score += flug;
					}
				}
				else if(answer[i][j] == 'X') {
					flug = 0;
				}
			}
			System.out.println(score);
		}
		sc.close();
	}
}
