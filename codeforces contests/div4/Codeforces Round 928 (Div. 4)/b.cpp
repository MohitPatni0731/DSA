#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t;
    
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        vector<int> count;
        for (int j = 0; i < n; i++)
        {
            int c = 0;
            string s;
            cin >> s;
            c.count('1')
            if (c==0) {
                continue;
            }
            count.append(c);
        }
        if (max(count)==min(count)) {
            cout<<"SQUARE"
        } else {
            cout<<"TRIANGLE"
        }
        
    }