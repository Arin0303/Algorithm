#include <iostream>
#include <vector>
using namespace std;
// 9개의 서로 다른 자연수 중에서 최댓값 찾기, 해당 최댓값이 몇번째인지 찾기


int main(void) {
    vector<int> v(9);
    int max = 0;

    for (int i = 0; i < v.size(); i++) {
        cin >> v[i];
    }

    for (int i = 1; i < v.size(); i++) {
        if (v[max] < v[i])
            max = i;
    }
    cout << v[max] << '\n' << max+1;

    return 0;
}
