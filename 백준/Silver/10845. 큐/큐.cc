#include <iostream>
#include <queue>
using namespace std;

queue<int> q;
 void calculate_queue(string cmd, int token) {
	if (cmd == "push") {
		q.push(token);
	}
	else if (cmd == "pop") {
		if (q.empty()) { 
			cout << -1 << '\n';
			return;
		}
		cout << q.front() << '\n';
		q.pop();
	}
	else if (cmd == "size") {
		cout << q.size() << '\n';
	} 
	else if (cmd == "empty") {
		if (q.empty())
			cout << 1 << '\n'; 
		else
			cout << 0 << '\n'; 
	}
	else if (cmd == "front") {
		if (q.empty()) { 
			cout << -1 << '\n';
			return;
		}
		cout << q.front() << "\n";
		
	}
	else if (cmd == "back") {
		if (q.empty()) { 
			cout << -1 << '\n';
			return;
		}
		cout << q.back() << "\n";
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
		calculate_queue(cmd, token);
	}
	
	return 0;
}
