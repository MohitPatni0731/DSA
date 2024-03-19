#include <iostream>
#include <vector>
#include <utility>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::pair<int, int> result = {-1, -1};
        for (int i = 0; i < nums.size(); i++)
        {
            for (int j = i+1; j < nums.size(); i++)
            {
                if (nums[i] + nums[j] ==  target) {
                    result.first = i;
                    result.second = j;
                    return result;
                }
            }
        }
    }
};