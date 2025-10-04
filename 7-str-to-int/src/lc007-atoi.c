#include <stdio.h>
#include <stdbool.h>
#include "../include/myAtoi.h"

int main() {
    printf("\n\nPROGRAM START...\n");
    printf("--------------------\n");
    int test = myAtoi("   -000042yay!");
    printf("\n%d\n", test);
    printf("\n--------------------\n");
    printf("PROGRAM END.\n\n");
    return 0;
}

bool isNeg(char *s){
    return *s && *s == '-';
}
char* rmLdWhtSpace(char *s){
    while(*s && *s == ' '){
        s++;
    }
    return s;
}
char* rmLdZeros(char *s){
    while(*s && *s == '0'){
        s++;
    }
    return s;
}

int charToInt(char c){
    return (int)c - 48;
}

int myAtoi(char *s) {
    s = rmLdWhtSpace(s);
    bool isNegative = isNeg(s);
    if(isNegative) s++;
    s = rmLdZeros(s);
    int rslt = 0;
    while(*s && *s >= '0' && *s <= '9'){
        rslt = rslt * 10 + charToInt(*s);
        s++;
    }
    if(isNegative) rslt = -rslt;
    return rslt;
}
