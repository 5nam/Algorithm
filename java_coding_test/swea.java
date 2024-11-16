package java_coding_test;

import java.util.Scanner;

public class swea {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] nums = new int[n];

        for(int i = 0; i<n; i++) {
            nums[i] = Integer.parseInt(sc.next());
        }

        int len = nums.length;
			
		//뒤에서부터 큰값이 나오면 리셋하기.맨뒤에 값이 무조건 큰값이라고 가정하기
		long max = Long.MIN_VALUE;
		int num = 0;
		long cost = 0L;
		long result = 0L;
		for (int i = nums.length-1 ;  i >= 0 ; i--) {
			// 더 큰 최댓값을 찾았다면? 호다닥 사자 ! 비용계산하기 : 사야할 애들의 갯수  * 판매가  - 구매가
			if( nums[i] > max ) {
				result += (max*num - cost);
				max = nums[i];
				//초기화
				cost = 0;		
				num = 0;
			} else {	//max 보다 작으면 사자
				cost+=nums[i];
				num++;
			}
		}
			
		//마지막에 한번 더 해주기
		result += (max*num - cost);
			
		System.out.println("#" + " " + result);
    }
}
