#include "leet/solution.hpp"
#include <memory>
#include <iostream>

int main() {

    std::string input = "babad";

    leet::Solution sol0;
    leet::Solution *sol1 = new leet::Solution();
    auto sol2 = std::make_unique<leet::Solution>();

    std::string rslt0 = sol0.longestPalindrome(input);
    std::string rslt1 = sol1->longestPalindrome(input);
    std::string rslt2 = sol2->longestPalindrome(input);
    std::cout << "Result0: \"" << rslt0 << "\"" << std::endl;
    std::cout << "Result1: \"" << rslt1 << "\"" << std::endl;
    std::cout << "Result2: \"" << rslt2 << "\"" << std::endl;

    delete sol1;
    return 0;
}