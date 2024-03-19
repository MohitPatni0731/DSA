class Solution {
public:
    bool isValid(string s) {
        int n = s.size(); 
        stack<char> Stack;
        bool answer = true;
        
        for (int i = 0; i < n; i++) { 
            if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
                Stack.push(s[i]);
            } else {
                if (Stack.empty()) {
                    answer = false;
                    break;
                }
                char top = Stack.top();
                Stack.pop();
                if ((s[i] == ')' && top != '(') ||
                    (s[i] == ']' && top != '[') ||
                    (s[i] == '}' && top != '{')) {
                    answer = false;
                    break;
                }
            }
        }
        
        if (!Stack.empty()) {
            answer = false;
        }
        
        return answer;
    }
};
