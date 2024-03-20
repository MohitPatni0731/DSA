#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    for (int j = 0; j < t; j++) {
        int a = 0, b = 0, c = 0;
        for (int i = 0; i < 3; i++) {
            string s;
            cin >> s;
            for (char c : s) {
                if (c == 'A')
                    a++;
                else if (c == 'B')
                    b++;
                else if (c == 'C')
                    c++;
            }
        }

        if (a != 3)
            cout << "A" << endl;
        else if (b != 3)
            cout << "B" << endl;
        else
            cout << "C" << endl;
    }

    return 0;
}
