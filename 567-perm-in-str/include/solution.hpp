#include <string>
#include <map>

class Solution {
public:
  Solution();
  ~Solution();
  bool checkInclusion(std::string, std::string);

private:
std::map<char, size_t> initCharMap(const std::string&) const;
void initWindow(const size_t, const std::string&, std::map<char, size_t>&);
bool checkMap(const std::map<char, size_t>&);
};