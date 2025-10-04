#include <stdio.h>
#include "../include/myAtoi.h"

int main() {
    printf("\n\nPROGRAM START...\n");
    printf("--------------------\n");
    int test = myAtoi("2");
    printf("\n%d\n", test);
    printf("\n--------------------\n");
    printf("PROGRAM END.\n\n");
    return 0;
}

int myAtoi(char *s) {
    int rslt = 0;
    rslt = (int)*s - 48;
    return rslt;
}
