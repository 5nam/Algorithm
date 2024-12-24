package EUREKA;

class Solution {

    public static void main(String[] args) {
        int[][] H = {{1,1},{1,21},{1,22},{1,23},{3,1},{5,5},{5,27},{6,6},{8,15},{9,28},{9,29},{9,30},{10,3},{10,9},{12,25}};
        
        int[] result = solution(7, H, 28);
        for(int i = 0; i<result.length; i++) {
            System.out.println(result[i]);
        }
    }
    public static int[] solution(int X, int[][] H, int Y) {
        Calendar calendar = new Calendar(X);

        calendar.setHoliday(H);

        // int answer = calendar.getAllWeekendNum() + calendar.getHoliday();
        int[] answer = calendar.getPayDay(Y);
        
        return answer;
    }

    public static class Calendar {

        int[][] month = new int[12][31];
        int[] days = {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334};
        int[] day = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    
        public Calendar(int start) {

            for(int i = 0; i<12; i++) {
                for(int d = 0; d<day[i]; d++) {
                    int result = (start + days[i] + d) % 7;

                    month[i][d] = result;
                }
            }
        }

        public int[] getPayDay(int Y) {
            int[] result = {Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y};

            for(int i = 0; i<12; i++) {
                if(isHoliday(i+1, Y) || isWeekend(i+1, Y)) {
                    // 우선 이전 날 중에 월급날이 될 수 있는 날이 있는지 살펴보기
                    int index = 1;
                    boolean cont = true;

                    while(cont) {
                        if(Y-index < 1 && Y+index > 28) {
                            break;
                        }

                        if(Y-index >= 1 && !isHoliday(i+1, Y-index) && !isWeekend(i+1, Y-index)) {
                            result[i] = Y-index;
                            cont = false;
                        }
                        else if(Y+index <= 28 && !isHoliday(i+1, Y+index) && !isWeekend(i+1, Y+index)) {
                            result[i] = Y+index;
                            cont = false;
                        }
                        index++;
                    }
                }
                
            }

            return result;
        }

        public int getHoliday() {

            int count = 0;

            for(int i = 0; i<12; i++) {
                for(int j = 0; j<day[i]; j++) {
                    if(isHoliday(i+1, j+1)) {
                        count++;
                    }
                }
            }

            return count;
        }

        private boolean isHoliday(int m, int d) {
            return month[m-1][d-1] == -1;
        }

        public void setHoliday(int[][] H) {
            for(int i = 0; i < H.length; i++) {
                int m = H[i][0];
                int d = H[i][1];

                if(isWeekend(m, d) && month[m-1][d-1] == 6) {
                    int index = 2;

                    // 가장 가까운 평일이 나올 때까지 while 문을 돈다. 5일 이내로 나올 것이므로...? 주말은 예외 처리 하지 않음.
                    while(true) {
                        if(month[m-1][d-index] != -1) {
                            month[m-1][d-index] = -1;
                            break;
                        }

                        index++;
                    }
                } 
                
                else if(isWeekend(m, d) && month[m-1][d-1] == 0) {
                    int index = 2;

                    while(true) {
                        // 년도를 넘어갈 때
                        if(m == 12 && d > 31) {
                            break;
                        }

                        if(month[m-1][d+index] != -1) {
                            month[m-1][d+index] = -1;
                            break;
                        }
                    }
                } else {
                    month[m-1][d-1] = -1;
                }
            }
            
        }
        

        public int getAllWeekendNum() {

            int count = 0;
            for(int i = 0; i<12; i++) {
                for(int j = 0; j<day[i]; j++) {
                    if(isWeekend(i+1, j+1)) {
                        count++;
                    }
                }
            }

            return count;
        }

        private boolean isWeekend(int m, int d) {
            return ((month[m-1][d-1] == 0) || (month[m-1][d-1] == 6));
        }
        
    }
}

