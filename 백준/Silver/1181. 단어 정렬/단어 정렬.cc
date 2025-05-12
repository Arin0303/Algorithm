#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(string a, string b) {
    if (a.length() == b.length()) return a < b;
    return a.length() < b.length();
}

int main() {
    int n;
    cin >> n;
    vector<string> words(n);
    for (int i = 0; i < n; i++) cin >> words[i];
    sort(words.begin(), words.end(), compare);
    words.erase(unique(words.begin(), words.end()), words.end());
    for (auto& w : words) cout << w << '\n';
    return 0;
}
