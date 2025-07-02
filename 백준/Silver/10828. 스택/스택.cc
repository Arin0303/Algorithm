#include <iostream>
#include <vector>
using namespace std;

vector <int>stack;

 void calculate_stack(string cmd, int token) {
	if (cmd == "push") {
		stack.push_back(token);
	}
	else if (cmd == "pop") {
		if (stack.empty()) { // 스택이 비어있으면 -1 출력
			cout << -1 << '\n';
			return;
		}
		cout << stack.back() << '\n'; // 마지막 원소 출력
		stack.pop_back(); // 마지막 원소 제거
	}
	else if (cmd == "size") {
		cout << stack.size() << '\n'; // 스택에 들어있는 원소의 개수 출력 
	} 
	else if (cmd == "empty") {
		if (stack.empty())
			cout << 1 << '\n'; // 스택이 비어있으면 1 출력
		else
			cout << 0 << '\n'; // 비어있지 않으면 0 출력 
	}
	else if (cmd == "top") {
		if (stack.empty()) {
			cout << -1 << '\n';
			return;
		}
		cout << stack.back() << '\n'; // 가장 위에 있는 정수 출력 
	}
}


int main(void) {
	int N;
	int token = 0;
	cin >> N;
	for (int i = 0; i < N; i++) {
		string cmd;
		cin >> cmd;
		if (cmd == "push")
			cin >> token;
		calculate_stack(cmd, token);
	}
	
	return 0;
}
