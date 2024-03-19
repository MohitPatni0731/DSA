#include <algorithm>
class Solution {
public:
    int scoreOfParentheses(string s) {
        int n = s.size(); 
        stack<char> Stack;
        int score = 0;
        
        for (int i = 0; i < n; i++){
            if (s[i] == '(') {
                Stack.push(score);
                score = 0;
            }
            else {
                score = Stack.top() + max(2*score, 1);
                Stack.pop();
            }
        
        }
        return score;
    }
};
