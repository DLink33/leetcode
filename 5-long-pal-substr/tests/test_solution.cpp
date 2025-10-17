#include <catch2/catch_test_macros.hpp>
#include "leet/solution.hpp"

TEST_CASE("longestPalindrome - smoke") {
    leet::Solution s;
    auto out = s.longestPalindrome("");
    REQUIRE(out.size() >= 0);
}

TEST_CASE("longestPalindrome - basics") {
    leet::Solution s;
    REQUIRE( (s.longestPalindrome("babad") == "bab" || s.longestPalindrome("babad") == "aba") );
    REQUIRE( s.longestPalindrome("cbbd") == "bb" );
    REQUIRE( s.longestPalindrome("a") == "a" );
    REQUIRE( (s.longestPalindrome("ac") == "a" || s.longestPalindrome("ac") == "c") );
}
