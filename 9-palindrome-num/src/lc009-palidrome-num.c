#include <stdio.h>
#include <stdbool.h>
#include "../include/lc009.h"

unsigned char numDigits(int x) {
    unsigned char rslt = 1;
    while (x >= 10) {
        x /=10;
        rslt++;
    }
    return rslt;
}

int power(int base, int exp) {
    int rslt = base; 
    while (--exp > 0) {
        rslt *= base;
    }
    return rslt;
}

bool isPalindrome(int x) {
    if (x < 0) return false;
    unsigned char digits = numDigits(x);
    unsigned char lsd = 0;
    unsigned char msd  = 0;
    unsigned char remain = digits;

    while (remain > 1) {
        int d = power(10, remain-1);
        lsd = x % 10;
        msd = x / d;
        if (lsd != msd) return false;
        x /= 10;
        x %= (d/10);
        remain -= 2;
    }
    return true;
}

int main() {
    bool r = isPalindrome(561828165);
    printf("%u\n", r);
    return 0;
}