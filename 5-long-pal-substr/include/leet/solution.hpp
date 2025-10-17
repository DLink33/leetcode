#pragma once
#include <string>

namespace leet {
class Solution {
public:
    std::string str_;
    Solution() = default;
    Solution(std::string);
    ~Solution() = default;
    std::string longestPalindrome(const std::string);
    std::pair<size_t, size_t> checkHelper(long long, long long, const std::string&);
};
}