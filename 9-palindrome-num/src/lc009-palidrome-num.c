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

bool isPalindrome(int x) {
    if (x < 0) return false;
    unsigned char digits = numDigits(x);
    
}

int main() {return 0;}