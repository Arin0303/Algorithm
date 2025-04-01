#include <iostream>
#include <string>
using namespace std;

int main(void) {
	int n;
	int result = 0; 
	string num;

	cin >> n >> num;
	for (int i = 0; i <n; i++) {
		result += stoi(num.substr(i, 1));
	}
	cout << result;
	return 0;
}