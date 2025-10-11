#include <stdio.h>
#include "test_roman2int.h"

int main(void) {
    /* Count cases using the sentinel (input == (void*)0) */
    size_t num = 0;
    while (test_cases[num].input != (void*)0) ++num;

    roman2int_test_suite suite = { test_cases, num };
    bool passed = run_test(&suite, roman2int);
    if (passed) puts("All tests passed!");
    else puts("Some tests failed.");
    return passed ? 0 : 1;
}
