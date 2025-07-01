//최적화된 코드
#include <iostream>
using namespace std;

// 한수 판별 함수
bool isHansoo(int n) {
	if (n < 100) // 1~99는 모두 한수
		return true;
	int a = n / 100; // 백의 자리
	int b = (n / 10) % 10; // 십의 자리
	int c = n % 10; // 일의 자리

	return (a - b) == (b - c); // 등차수열 확인
}
int main() {
	int limit;
	cin >> limit;

	int count = 0;
	for (int i = 1; i <= limit; i++) {
		if (isHansoo(i))
			count++;
	}
	cout << count;
	return 0;
}