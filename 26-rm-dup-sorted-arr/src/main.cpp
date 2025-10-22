#include "../include/solution.hpp"

int main(){
  std::vector<int> nums = {0,0,1,1,1,2,2,3,3,4};
  Solution sol {nums};
  sol.printNums();
  int rslt = sol.removeDuplicates();
  std::cout << "Result: " << rslt << std::endl;
  sol.printNums();
  return 0;
}
