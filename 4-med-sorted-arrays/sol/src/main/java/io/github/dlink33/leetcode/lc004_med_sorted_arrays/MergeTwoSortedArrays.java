package io.github.dlink33.leetcode.lc004_med_sorted_arrays;

public class MergeTwoSortedArrays {
    private int[] arr1, arr2, merged;
    private double median;

    public MergeTwoSortedArrays(int[] inArr1, int[] inArr2) {
        // Deep Copy of array for no side effects outside of this class 
        this.arr1 = MergeTwoSortedArrays.cpyIntArr(inArr1);
        this.arr2 = MergeTwoSortedArrays.cpyIntArr(inArr2);
        this.mergeArrys();
        this.calcMedian();
    }

    public int[] getArr1(){
        return this.arr1;
    }
    
    public int[] getArr2(){
        return this.arr2;
    }

    public void setArr1(int[] arr){
        this.arr1 = arr;
    }
    
    public void setArr2(int[] arr){
        this.arr2 = arr;
    }

    public int[] getMerged(){
        return this.merged;
    }

    public double getMedian(){
        return this.median;
    }

    private static int[] cpyIntArr(int[] arr) {
        int[] rslt = new int[arr.length];
        for(int i=0; i<arr.length; i++){
            rslt[i] = arr[i];
        }
        return rslt;
    }

    private void mergeArrys() {
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
        while(i<len1){
            rslt[k] = this.arr1[i];
            i++;
            k++;
        }
        while(j<len2){
            rslt[k] = this.arr2[j];
            j++;
            k++;
        }
        this.merged = rslt;
    }

    private void calcMedian(){
        int len = this.merged.length;
        if (len % 2 != 0) {  
            //Odd
            this.median = (double)this.merged[len/2];
        }
        else {  
            //Even
            this.median = (double)((this.merged[len/2]) + (this.merged[(len/2)-1])) / 2.0;
        }
    }

}
