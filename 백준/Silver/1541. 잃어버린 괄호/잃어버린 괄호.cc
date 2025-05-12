#include <iostream>
#include <sstream>
using namespace std;

int main() {
    string s;
    cin >> s;
    stringstream ss(s);
    string token;
    int result = 0;
    bool minus = false;

    while (getline(ss, token, '-')) {
        int temp = 0;
        stringstream part(token);
        string num;
        while (getline(part, num, '+')) {
            temp += stoi(num);
        }
        if (minus) result -= temp;
        else {
            result += temp;
            minus = true;
        }
    }
    cout << result << '\n';
    return 0;
}
