// ��� ���� ��ȣ ��ġ�� ġȯ�Ͽ� �ڵ� �ۼ�
public class Main_10171 {
	public static void main(String[] args) {
		// i �� �� j �� ��
		for(int i = 0; i<4; i++) {
			for(int j = 0; j<8; j++) {
				if((i==1 && j==1) || (i==1 && j==7) || (i==2 && j==6)||(i==3 && j==5)) {
					System.out.print(")");
				}
				else if((i==0 && j==0)||(i==0 && j==6)||(i==3&&j==1)) {
					System.out.print('\\');
				}
				else if((i==0 && j==5)||(i==2 &&j==3)) {
					System.out.print("/");
				}
				else if((i==1 && j==4)||(i==2&&j==0)||(i==3&&j==2)) {
					System.out.print("(");
				}
				else if((i==3&&j==3)||(i==3&&j==4)) {
					System.out.print("_");
				}
				else if(i==1 && j==6) {
					System.out.print("'");
				}
				else if(i==3&&j==6) {
					System.out.print("|");
				}
				else {
					System.out.print(" ");
				}
			}
			System.out.println();
		}
	}
}
