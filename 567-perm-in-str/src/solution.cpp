#include "../include/solution.hpp"

Solution::Solution(){}
Solution::~Solution(){}
bool Solution::checkInclusion(std::string s1, std::string s2) {
  std::map<char, size_t> charMap = initCharMap(s1);
  size_t left, right, len1, len2;
  len1 = s1.length();
  len2 = s2.length();
  if (len1 > len2) return false;
  left  = 0;
  right = s1.length()-1;
  
  initWindow(len1, s2, charMap);
  if (checkMap(charMap)) return true;

  while (right+1 < len2) {
    if(charMap.count(s2[left])) charMap[s2[left]]++;
    if(charMap.count(s2[right+1])) charMap[s2[right+1]]--;
    if (checkMap(charMap)) return true;
    ++right;
    ++left;
  }
  return false;
}

std::map<char, size_t> Solution::initCharMap(const std::string& str) const {
  std::map<char, size_t> rslt;
  for(char c : str) {
    rslt[c]++;
  }
  return rslt;
}

void Solution::initWindow(const size_t len, const std::string& word, std::map<char, size_t>& charMap) {
  for (size_t i = 0; i < len; ++i) {
    if(charMap.count(word[i])) charMap[word[i]]--;
  }
}

bool Solution::checkMap(const std::map<char, size_t>& charMap){
  for(const auto& [k,v] : charMap){
    if (v != 0) return false;
  }
  return true;
}