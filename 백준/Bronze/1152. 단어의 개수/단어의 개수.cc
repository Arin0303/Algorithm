#include <iostream>
#include <string>
using namespace std;

int main() {
	string str;
	getline(cin, str);

	int count = 0;
	bool inWord = false;

	for (char c : str) {
		if (c != ' ') {
			if (!inWord) {
				inWord = true;
				count++;
			}
		} else {
			inWord = false;
		}
	}

	cout << count << '\n';
	return 0;
}
