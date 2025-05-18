#include <iostream>
using namespace std;

int main() {
    double A, B;
    cin >> A >> B;
    cout.precision(10);       // 소수점 아래 9자리 이상 출력
    cout << A / B << '\n';
    return 0;
}
