#include <stdio.h>
#include "test_roman2int.h"

size_t getStrLen(string);

roman2int_test_case test_cases[] = {
    {"III", 3},
    {"IV", 4},
    {"IX", 9},
    {"LVIII", 58},
    {"MCMXCIV", 1994},
    {"MMMDCCXLIX", 3749},
    {"CDXLIV", 444},
    {"CMXCIX", 999},
    {"MMXXIV", 2024},
    {"XLII", 42},
    {"XCIX", 99},
    {(void*)0, 0} // Sentinel value to mark the end of the array
};

size_t getStrLen(string s) {
    size_t len = 0;
    while(s[len] != '\0'){len++;}
    return len;
}

bool run_test(roman2int_test_suite *suite, roman2int_func func) {
    roman2int_test_case currTestCase = {(void*)0, 0};
    int rslt = 0;
    for (size_t i=0; i < suite->numCases; ++i) {
        currTestCase = suite->cases[i];
        rslt = func(currTestCase.input);
        if (rslt != currTestCase.expected) return false;
    }
    return true;
}
