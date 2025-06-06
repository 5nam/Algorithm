package java_coding_test;

public class Main1090 {
    public static void main(String[] args) {
        // 모든 위치에서
        // 모든 친구들의 거리를 계산해서
        // 가장 적은 값을 알려주면 됨

        // 1번 아이디어
        // X, Y 를 구분해서 계산해준 뒤에 합쳐서
        // 최솟값을 알려주면 됩니다!


        // 2번 아이디어
        // 우리가 한 곳에서 모일 때, 비용을 최소화 하기 위해서는
        // 우리의 집 중 한 곳에서 모이면 된다.
        // 이 방법은 구성원의 집만 방문하면 된다. 즉 3명이라면 3*3 의 좌표만 방문해보면 된다. 엄청나게 경우의 수를 줄임

        // 3번 아이디어
        // 최소 거리를 계산하고 싶다.
        // 그리고 2명이 모여야 한다.
        // 그 점에서, 가까운 두명의 거리만 더해주면 되지 않을까?
        // 최소거리를 계산하고 싶을 때, 그냥 먼저 점을 정하고 
        // 가까운 사람의 순서대로 1명 2명 3명 4명의 값을 구해서 더해주면 됨
    }
}
