#include <iostream>
#include <vector>
using namespace std;

int d(int n) {
    int sum = n;
    while (n!=0) {
        sum += n % 10; // 맨 뒷자리 더하기
        n /= 10; // 맨 뒷자리 제거
    }
    return sum;
}
int main() {
    vector<bool> isInitNum(10001, true);
    // 1~10000까지의 생성자에 대한 배열 세팅
    for (int n = 1; n < 10000; n++) {
        int num = d(n);
        if(num <= 10000)
            isInitNum[num] = false;
    }
    for (int i = 1; i < 10000; i++) { // 셀프넘버인지 판단할 숫자들(1~10000)
        if (isInitNum[i])
            cout << i << '\n';
    }

    return 0;
}
