#include <vector>
#include <iterator>
#include <iostream>

class Solution {
private:
  std::vector<int> nums;
public:
  Solution();
  Solution(std::vector<int>);
  ~Solution();
  int removeDuplicates(std::vector<int>&);
  int removeDuplicates();
  const std::vector<int>& getNums() const;
  void printNums() const;
};s