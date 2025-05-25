#include <iostream>
#include <vector>
#include <algorithm> // find() 
using namespace std;

int main() {
    int n, v;
    int count = 0;
    cin >> n; // 숫자 개수
    vector<int> vec(n);
    for (int i = 0; i < n; i++)
        cin >> vec[i];

    cin >> v; // 찾는 수 

    for (int i = 0; i < n; i++) {
        if (vec[i] == v)
            count++;
    }
    cout << count;
    return 0;
}