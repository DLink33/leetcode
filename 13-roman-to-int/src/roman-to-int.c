#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include "roman-to-int.h"

int roman2int(string s) {
    int rslt = 0;
    size_t i = 0;
    char currChar = ' ';
    while ((currChar=s[i]) != '\0') {
        switch (currChar) {
            case 'M':
                rslt += 1000;
                break;
            case 'D':
                rslt += 500;
                break;
            case 'C':
                if      (s[i+1] == 'D') {rslt += 400; i++;}
                else if (s[i+1] == 'M') {rslt += 900; i++;}
                else rslt += 100;
                break;
            case 'L':
                rslt += 50;
                break;
            case 'X':
                if      (s[i+1] == 'L') {rslt += 40; i++;}
                else if (s[i+1] == 'C') {rslt += 90; i++;}
                else rslt += 10;
                break;
            case 'V':
                rslt += 5;
                break;
            case 'I':
                if      (s[i+1] == 'V') {rslt += 4; i++;}
                else if (s[i+1] == 'X') {rslt += 9; i++;}
                else rslt += 1;
                break;
            default:
                printf("Non-valid Roman numeral found. Exiting program...");
                exit(1);
                break;
        }
        i++;
    } 
    return rslt;
}
