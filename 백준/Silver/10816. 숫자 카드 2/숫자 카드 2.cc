#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
	int N, M;
	
	// 시간 초과 방지용
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin >> N;

	vector<int> ans(N);

	for (int i = 0; i < N; i++) {
		cin >> ans[i];
	}

	sort(ans.begin(), ans.end()); // upper_bound와 lower_bound를 쓰기 위해서는 정렬 필수

	cin >> M;

	for (int i = 0; i < M; i++) {
		int x;
		cin >> x;
		// lower_bound: iterator(주소)반환
		// ans.begin(): 주소 반환
		// 인덱스 번호를 알아야하기 때문에 주소-주소 = 인덱스(거리)를 구한다
		int lower = lower_bound(ans.begin(), ans.end(), x) - ans.begin(); // lower인덱스
		int upper = upper_bound(ans.begin(), ans.end(), x) - ans.begin(); // upper 인덱스

		cout << upper - lower << " "; // 출현 개수
	}

	
	/*
	count->시간초과!
	for (int i = 0; i < M; i++) {
		int result = count(ans.begin(), ans.end(), pred[i]);
		cout << result << " ";
	}
	*/



	return 0;
}

