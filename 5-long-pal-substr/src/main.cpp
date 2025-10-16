#include "leet/solution.hpp"
#include <memory>

int main() {
    leet::Solution sol0;
    leet::Solution *sol1 = new leet::Solution();
    auto sol2 = std::make_unique<leet::Solution>();
    delete sol1;
    return 0;
}