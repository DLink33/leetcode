#include <iostream>
#include "../include/solution.hpp"

int main() {
  std::cout << "Hello, World!" << std::endl;
  Solution sol;
  bool rslt = sol.checkInclusion("ab", "eidbaooo");
  std::cout << rslt << std::endl;
  return 0;
}