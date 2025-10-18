package leet;

import java.lang.Math;

public class Solution {
    private int getDigits(int x) {
        if (x == 0) return 1;
        int n = 0;
        while (x != 0) {
            x/=10;
            ++n;
        }
        return n;
    }
    public int reverse(int x) {
        boolean neg = false;
        if (x < 0) {
            x = x*-1;
            neg = true;
        }
        int rslt = 0;
        int popped = 0;
        while (x != 0){
            popped = x % 10;
            x /= 10;
            if (rslt < Integer.MIN_VALUE/10 || (rslt == Integer.MIN_VALUE/10 && popped < -8)) return 0;
            if (rslt > Integer.MAX_VALUE/10 || (rslt == Integer.MAX_VALUE/10 && popped >  7)) return 0;
            rslt = rslt * 10 + popped; 
        }
        if (neg) rslt*=-1;
        return rslt;
    }
}

