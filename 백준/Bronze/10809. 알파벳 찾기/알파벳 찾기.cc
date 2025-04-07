#include <iostream>
#include <vector>
#include <string> // String 클래스를 사용하기 위해 포함  

using namespace std;

int main(void) {
	string word;
	cin >> word;
	bool exist = false; 

	vector<char> vec(word.begin(), word.end()); // word의 처음부터 끝까지 문자들을 하나씩 복사해서 
												// vec이라는 vector<char>에 넣는다. 
	for (char i = 'a'; i <= 'z'; i++) {
	

		for (int j = 0; j<vec.size(); j++) { // 벡터의 요소의 길이는 size()내장함수 사용 
			if (vec[j] == i) {
				cout << j << ' ';
				exist = true;
				break;
			}
		}
		if (exist == false) {
			cout << -1 << ' ';
		}
		exist = false;
	}
	return 0;
} 