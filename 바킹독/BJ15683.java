package 바킹독;

import java.io.*;
import java.util.*;

public class BJ15683 {
	static int[][] board;
	static ArrayList<int[]> target;
	static int[][] dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // 상, 하, 좌, 우 
	static int N;
	static int M;
	
	public static void main(String[] args) throws IOException {
		// System.setIn(new FileInputStream("src/input.txt"));

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		// 초기화
		target = new ArrayList<>();
		
		// 입력 받기
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		board = new int[N][M];
		for(int r = 0; r<N; r++) {
			st = new StringTokenizer(br.readLine());
			for(int c = 0; c<M; c++) {
				int num = Integer.parseInt(st.nextToken());
				
				if((0 < num) && (num < 6)) {
					target.add(new int[] {num, r, c});
				}
				
				board[r][c] = num;
			}
		}
		
		// 정렬
		target.sort((a, b) -> {
			return Integer.compare(b[0], a[0]);
		});
		
//		System.out.println(Arrays.deepToString(target.toArray()));
		
		// 로직 수행
		for(int i = 0; i<target.size(); i++) {
			solve(target.get(i)[0], target.get(i)[1], target.get(i)[2]);
		}
		
		int ans = 0;
		for(int i = 0; i<N; i++) {
			for(int j = 0; j<M; j++) {
				if(board[i][j] == 0) {
					ans += 1;
				}
			}
		}
				
		System.out.println(ans);

	}
	
	static void solve(int type, int r, int c) {
		
		int[] cnt = getCount(r, c); // 상하좌우 
		
		if(type == 5) {
			// 상하좌우 모두 해당. 그러므로 굳이 상하좌우 세서 비교할 필요 X
			// 바로 업데이트 수행.
			updateBoard(r, c, new int[] {0, 1, 2, 3});
		}
		else if(type == 4) {
			int[][] d = {{0, 1, 2}, {0, 1, 3}, {0, 2, 3}, {1, 2, 3}};
			// 4개 비교해보고, 가장 최댓값 방향들 배열로 넘기기.
			int max = 0;
			int[] max_i = d[0];
			for(int i = 0; i<d.length; i++) {
				int temp = 0;
				for(int j = 0; j<3; j++) {
					temp += cnt[d[i][j]];
				}
				
				if(max < temp) {
					max = temp;
					max_i = d[i];
				}
			}
			
			updateBoard(r, c, max_i);
			
		}
		else if(type == 3) {
			int[][] d = {{0, 2}, {0, 3}, {1, 2}, {1, 3}};
			// 4개 비교해보고, 가장 최댓값 방향들 배열로 넘기기.
			int max = 0;
			int[] max_i = d[0];
			for(int i = 0; i<d.length; i++) {
				int temp = 0;
				for(int j = 0; j<2; j++) {
					temp += cnt[d[i][j]];
				}
				
				if(max < temp) {
					max = temp;
					max_i = d[i];
				}
			}
			
			updateBoard(r, c, max_i);
			
		}
		else if(type == 2) {
			// 2개 비교해보고, 가장 최잿값 방향을 배열로 넘기기.
			int[][] d = {{0,1}, {2, 3}};
			// 4개 비교해보고, 가장 최댓값 방향들 배열로 넘기기.
			int max = 0;
			int[] max_i = d[0];
			for(int i = 0; i<d.length; i++) {
				int temp = 0;
				for(int j = 0; j<2; j++) {
					temp += cnt[d[i][j]];
				}
				
				if(max < temp) {
					max = temp;
					max_i = d[i];
				}
			}
			
			updateBoard(r, c, max_i);
		}
		else {
			// 상, 하, 좌, 우 중 가장 큰 것 방향 넘기기.
			int[] d = {0, 1, 2, 3};
			// 4개 비교해보고, 가장 최댓값 방향들 배열로 넘기기.
			int max = 0;
			int max_i = d[0];
			for(int i = 0; i<d.length; i++) {
				if(max < cnt[i]) {
					max = cnt[i];
					max_i = d[i];
				}
			}
			
			updateBoard(r, c, new int[] {max_i});
		}
	}
	
	static int[] getCount(int r, int c) {
		int[] result = new int[4]; // 상하좌우 count 담는 배열
		
		for(int i = 0; i<2; i++) { // 상하 
			int nr = r;
			int nc = c;
			for(int j = 0; j<N; j++) {
				nr += dir[i][0];
				nc += dir[i][1];
				
				// 벽이거나, 범위 밖에 있으면.
				if(!check(nr, nc) || board[nr][nc] == 6) {
					break;
				}
				
				if(board[nr][nc] == 0) {
					result[i] += 1;
				}
			}
		}
		
		for(int i = 2; i<4; i++) { // 좌우 
			int nr = r;
			int nc = c;
			for(int j = 0; j<N; j++) {
				nr += dir[i][0];
				nc += dir[i][1];
				
				// 벽이거나, 범위 밖에 있으면.
				if(!check(nr, nc) || board[nr][nc] == 6) {
					break;
				}
				
				if(board[nr][nc] == 0) {
					result[i] += 1;
				}
			}
		}
		
		return result;
		
	}
	
	static void updateBoard(int r, int c, int[] d) {
		// d 에 쓰여진 방향으로 유효 범위만큼 가서 -1 으로 바꿔주기. 방향 인덱스가 담겨있음.
		for(int i = 0; i<d.length; i++) {
			int nr = r;
			int nc = c;
			for(int j = 0; j<8; j++) {
				nr += dir[d[i]][0];
				nc += dir[d[i]][1];
				if(!check(nr, nc) || board[nr][nc] == 6) {
					break;
				}
				
				board[nr][nc] = -1;
			}
		}
	}
	
	static boolean check(int nr, int nc) {
		return 0<=nr && nr<N && 0<=nc && nc<M;
	}

}
