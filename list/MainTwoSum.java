package list;

import java.util.Arrays;

// two_sum 문제 변형
public class MainTwoSum {

    public static void main(String[] args) {
        int[] arr = { 2,7,11,15 };
        // int[] arr = { 1,2,3,5 };
        int target = 9;
        System.out.println(twoSum(arr, target));
    }

    public static boolean twoSum(int[] nums, int target) {
        
        Arrays.sort(nums);

        int start_index = 0;
        int end_index = nums.length - 1;
        
        while(start_index != end_index) {
            int sum = nums[start_index] + nums[end_index];
            if (sum > target) {
                end_index--;
            } else if (sum < target) {
                start_index++;
            } else {
                return true;
            }
        }

        return false;
    }
}
