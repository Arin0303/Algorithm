#include <iostream>
using namespace std;

int main() {
	int h, m; // 00:00(자정)~23:59(다음날 자정 1분전)
	cin >> h >> m;
	// 45분 일찍 알람 설정하기
	if (m - 45 < 0) {
		h -= 1;
		if (h == 24)
			h = 0;
		else if (h == -1)
			h = 23;
		m = 60 - (45 - m);
	}
	else {
		m = m - 45;
	}

	cout << h << " " << m;
	
	return 0;
}


