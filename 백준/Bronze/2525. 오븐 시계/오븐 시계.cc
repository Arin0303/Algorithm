#include <iostream>
using namespace std;

int main() {
	int a, b, c;
	cin >> a >> b >> c;

	if ((b + c) >= 60) {
		int n = (b + c) / 60;
		a += n;
		if (a >= 24)
			a = a - 24;

		b = (b + c) - 60 * n;
	}

	else {
		b = b + c;
	}

	cout << a << " " << b;

	return 0;
}


