package io.github.dlink33.leetcode.lc004_med_sorted_arrays;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;

class SolutionTest {

    private static int[] parse(String s) {
        if (s == null || s.isBlank()) return new int[0];
        return Arrays.stream(s.split(","))
                     .map(String::trim)
                     .mapToInt(Integer::parseInt)
                     .toArray();
    }

    @ParameterizedTest
    @CsvFileSource(
        resources = "/merge_test_cases.csv",
        numLinesToSkip = 1,
        delimiter = ';',
        encoding = "UTF-8"
    )
    void testMedianOfSortedArrays(String a, String b, double expected) {
        int[] arr1 = parse(a);
        int[] arr2 = parse(b);
        double exp = expected;
        MergeTwoSortedArrays sol = new MergeTwoSortedArrays(arr1, arr2);
        assertEquals(sol.getMedian(), exp);
    }

}