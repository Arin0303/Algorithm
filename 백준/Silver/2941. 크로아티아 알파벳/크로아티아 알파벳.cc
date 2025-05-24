#include <iostream>
#include <string>
using namespace std;

int main(void) {
	string s;
	cin >> s;

	string croatia[8] = { "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=" };

	for (int i = 0; i < 8; i++) {
		size_t pos = s.find(croatia[i]);
		while (pos != string::npos) {
			s.replace(pos, croatia[i].length(), "*"); // 인덱스 pos 에서 croatia[i]의 길이만큼 *로 치환
			pos = s.find(croatia[i]);
		}
	}

	cout << s.length(); // 남은 문자열의 길이가 곧 문자 수 
	return 0;
}
