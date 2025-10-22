#include "../include/solution.hpp"

Solution::Solution() = default;
Solution::Solution(std::vector<int> nums) {
  this->nums = nums;
}
Solution::~Solution() = default;

int Solution::removeDuplicates(std::vector<int>& nums) {
  if (nums.size() == 0) return 0;
  std::size_t i, w, len;
  len = nums.size();
  i = w = 1;
  for( ; i < len; ++i) {
    if (nums[i] != nums[w-1]) nums[w++] = nums[i];
  }
  return static_cast<int>(w);
}

int Solution::removeDuplicates(){
  if (this->nums.empty()) return -1;
  int rslt = Solution::removeDuplicates(this->nums);
  return rslt;
}

const std::vector<int>& Solution::getNums() const {
  return this->nums;
}

void Solution::printNums() const {
  std::cout << "{";
  if (!this->nums.empty()) {
    std::copy(this->nums.begin(), this->nums.end() - 1, std::ostream_iterator<int>(std::cout, ", "));
    std::cout << this->nums.back();
  }
  std::cout << "}\n";
}