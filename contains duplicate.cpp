class Solution
{
public:
    bool containsDuplicate(vector<int> &nums)
    {
        for (int pointer = 0; pointer < nums.size(); pointer++)
        {
            for (int i = pointer + 1; i < nums.size(); i++)
            {
                if (nums[pointer] == nums[i])
                {
                    return true;
                }
            }
        }
        return false;
    }
};
