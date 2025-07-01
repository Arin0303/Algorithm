#include <iostream>
using namespace std;


int main() {
    int limit, result;
    int count = 0;
    cin >> limit;
    // 1보다 크고 limit보다 작거나 같은 수 중에서 각 자리가 등차수열인 수의 개수 구하기
    for (int n = 1; n <= limit; n++) {
        if (n < 100) { // 일의자리, 십의자리
            count++;
        }
        else if ((n >= 100) && (n < 1000)) { // 백의자리
            int first, second, third; // 일의자리, 십의자리, 백의자리
            first = n % 10;

            second = (n / 10) % 10;

            third = n / 100;

            int interval = third - second;
            if ((second - first) == interval)
                count++;
        }
    }

    cout << count;
    return 0;
}
