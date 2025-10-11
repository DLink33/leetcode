#ifndef TEST_ROMAN2INT_H
#define TEST_ROMAN2INT_H

#include <stddef.h>
#include <stdbool.h>
#include "roman-to-int.h"

typedef struct { string input; int expected; } roman2int_test_case;

typedef struct { roman2int_test_case *cases; size_t numCases; } roman2int_test_suite;

typedef int (*roman2int_func)(char *string);

extern roman2int_test_case test_cases[];
extern bool run_test(roman2int_test_suite*, roman2int_func);

#endif /* TEST_ROMAN2INT_H */
