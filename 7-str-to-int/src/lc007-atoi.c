#include <stdio.h>
#include <stdbool.h>
#include "../include/myAtoi.h"

int main() {
    unsigned char numTests = 4;
    char* str0 = "20000000000000000000";
    char* str1 = "   -000042yay!";
    char* str2 = "4193 with words";
    char* str3 = "+1";
    char* tests[4] = {str0, str1, str2, str3};
    int rslt;
    printf("\n\nPROGRAM START...\n");
    printf("--------------------\n");
    for (int i = 0; i < numTests; i++) {
        printf("Test %d: \"%s\"\n", i + 1, tests[i]);
        rslt = myAtoi(tests[i]);
        printf("Result: %d\n", rslt);
        printf("--------------------\n");
    }
    printf("\n--------------------\n");
    printf("PROGRAM END.\n\n");
    return 0;
}

// HELPER FUNCTIONS

// Check if the string starts with a negative sign
bool isNeg(char *s){
    return *s && *s == '-';
}

// Remove leading whitespace characters
char* rmLdWhtSpace(char *s){
    if (!s) return s;
    while (*s && (
              *s == ' ' ||
              *s == '\t' ||
              *s == '\n' ||
              *s == '\v' ||
              *s == '\f' ||
              *s == '\r')) s++;

    return s;
}

// Remove leading zeros
char* rmLdZeros(char *s){
    if (!s) return s;
    while(*s && *s == '0') s++;
    return s;
}

// Convert a character digit to its integer value
int charToInt(char c){
    return (int)c - 48;
}

// solution function
int myAtoi(char *s) {
    s = rmLdWhtSpace(s);

    bool isNegative = isNeg(s);
    if (isNegative || (*s && *s == '+')) s++;
    s = rmLdZeros(s);

    int r = 0;
    while (*s && *s >= '0' && *s <= '9') {
        int d = charToInt(*s);  // assumes '0'..'9'
        if (!isNegative) {
            if (r > 214748364 || (r == 214748364 && d > 7)) return 2147483647;   // INT_MAX
            r = r * 10 + d;
        } else {
            if (r < -214748364 || (r == -214748364 && d > 8)) return -2147483648; // INT_MIN
            r = r * 10 - d;
        }
        s++;
    }
    return r;  // already signed correctly
}
