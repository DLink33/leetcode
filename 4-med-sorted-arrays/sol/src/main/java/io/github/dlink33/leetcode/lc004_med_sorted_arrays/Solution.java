package io.github.dlink33.leetcode.lc004_med_sorted_arrays;
import java.util.Arrays;

public class Solution {

    public static void main(String[] args) {
        int[] arr1 = {1,3};
        int[] arr2 = {2,4};
        MergeTwoSortedArrays sol = new MergeTwoSortedArrays(arr1, arr2);
        int[] merged = sol.getMerged();
        double median = sol.getMedian();
        System.out.println(Arrays.toString(merged));
        System.out.println(median);
   }
}
