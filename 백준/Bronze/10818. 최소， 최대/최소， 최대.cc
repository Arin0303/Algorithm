#include <iostream>
#include <vector>
using namespace std;

int main(void) {
    int n;// 입력 개수
    cin >> n;
    vector<int> v(n); // 크기 n의 벡터 생성

    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    int min = v[0];
    int max = v[0];
    for (int i = 1; i < n; i++) {
        if (min > v[i])
            min = v[i];
        if (max < v[i])
            max = v[i];
    }

    cout << min << " " << max << '\n';
    return 0;
}
