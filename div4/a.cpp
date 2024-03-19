#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        string s;
        cin >> s; 
        int num_a = 0;
        int num_b = 0;
        for (char c : s) {
            if (c == 'A') {
                num_a += 1;
            } else {
                num_b +=1;
            }
        }
    if (num_a > num_b) {
        cout << "A" << endl;
    } else {
        cout << "B" << endl;
    }
    }
    

    return 0;
}
