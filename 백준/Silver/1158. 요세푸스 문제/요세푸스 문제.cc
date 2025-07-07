#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main(void) {
	int K, N;
	queue<int> q;
	
	cin >> N >> K;

	vector<int> v;

	for (int i = 1; i <= N; i++) {
		q.push(i);
	}
	int token; 
	while (!q.empty()) {

			for (int i = 0; i < K-1; i++) {
				token = q.front();
				q.pop();
				q.push(token);
			}
			token = q.front(); 
			q.pop();
			v.push_back(token);
		
	}
	cout << "<";
	for (size_t i = 0; i < v.size(); i++) {
		cout << v[i];
		if (i != v.size() - 1)
			cout << ", ";
	}

	cout << ">";
	
	return 0;
}