#include "leet/solution.hpp"

leet::Solution::Solution(std::string s){
    this->str_ = std::move(s);
}

std::string leet::Solution::longestPalindrome(const std::string s) {
    size_t len = s.length();
    size_t bestL = 0;
    size_t bestR = 0;
    for (size_t i = 0; i < len; ++i) {
        auto [l1, r1] = checkHelper(static_cast<long long>(i), static_cast<long long>(i), s);
        auto [l2, r2] = checkHelper(static_cast<long long>(i), static_cast<long long>(i+1), s);
        
        const size_t len1 = (r1 >= l1) ? r1-l1+1 : 0; // check to prevent underflows from the helper func
        const size_t len2 = (r2 >= l2) ? r2-l2+1 : 0; // check to prevent underflows from the helper func

        size_t candL, candR;
        if (len1 >= len2)   { candL = l1; candR = r1; }
        else                { candL = l2; candR = r2; }

        const size_t bestLen = bestR - bestL + 1;
        const size_t candLen = candR >= candL ? candR - candL + 1 : 0; //check to pre

        if (candLen > bestLen) {
            bestL = candL;
            bestR = candR;
        }
    }
    return s.substr(bestL, bestR-bestL+1);
}

std::pair<size_t, size_t> leet::Solution::checkHelper(long long left, long long right, const std::string& s) {
    const long long len = static_cast<long long>(s.length());
    while(left >= 0 && right < len) {
        if (s[static_cast<size_t>(left)]  != s[static_cast<size_t>(right)] ) break;
        --left;
        ++right;
    }
    return {static_cast<size_t>(left+1), static_cast<size_t>(right-1)};
}