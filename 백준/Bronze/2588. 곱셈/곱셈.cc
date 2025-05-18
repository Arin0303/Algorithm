#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;

    int B1 = B % 10;
    int B2 = (B / 10) % 10;
    int B3 = B / 100;

    cout << A * B1 << '\n';
    cout << A * B2 << '\n';
    cout << A * B3 << '\n';
    cout << A * B << '\n';

    return 0;
}
