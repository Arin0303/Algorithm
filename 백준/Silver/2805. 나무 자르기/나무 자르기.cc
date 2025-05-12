#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool canCut(const vector<int>& trees, int height, long long m) {
    long long total = 0;
    for (int h : trees)
        if (h > height) total += (h - height);
    return total >= m;
}

int main() {
    int n;
    long long m;
    cin >> n >> m;
    vector<int> trees(n);
    for (int i = 0; i < n; i++) cin >> trees[i];

    int left = 0, right = *max_element(trees.begin(), trees.end()), ans = 0;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (canCut(trees, mid, m)) {
            ans = mid;
            left = mid + 1;
        } else right = mid - 1;
    }
    cout << ans << '\n';
    return 0;
}
