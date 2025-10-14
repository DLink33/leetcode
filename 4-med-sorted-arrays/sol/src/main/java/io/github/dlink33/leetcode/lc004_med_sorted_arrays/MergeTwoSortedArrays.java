package io.github.dlink33.leetcode.lc004_med_sorted_arrays;

public class MergeTwoSortedArrays {
    private
    int[] arr1;
    int[] arr2;
    int[] merged;
    float median;

    public MergeTwoSortedArrays(int[] inArr1, int[] inArr2) {
        // Deep Copy of array for no side effects
        this.arr1 = this.cpyIntArr(inArr1);
        this.arr2 = this.cpyIntArr(inArr2);
    }

    private int[] cpyIntArr(int[] arr) {
        int[] rslt = new int[arr.length];
        for(int i=0; i<arr.length; i++){
            rslt[i] = arr[i];
        }
        return rslt;
    }

    public int[] mergeArrys() {
        int len1 = this.arr1.length;
        int len2 = this.arr2.length;
        int[] rslt = new int[len1+len2];
        int i = 0, j = 0, k = 0;

        while(i < len1 && j < len2){
            if(this.arr1[i] <= this.arr2[j]){
                rslt[k] = this.arr1[i];
                i++;
            } else {
                rslt[k] = this.arr2[j];
                j++;
            }
            k++;
        }
        while(){}
        while(){}

        return rslt;
    }

}
