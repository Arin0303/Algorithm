#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
	int N, M;
	cin >> N;
	vector<int> v1(N);
	int low, high, mid;

	for (int i = 0; i < N; i++) {
		cin >> v1[i];
	}
	sort(v1.begin(), v1.end()); // 이진탐색을 위한 정렬 
	cin >> M;
	vector<int> v2(M);
	vector<int> vResult(M, 0); // 정답벡터 0으로 초기화 


	for (int i = 0; i < M; i++) {
		cin >> v2[i];
		low = 0;
		high = N - 1;

		while (low <= high) {
			mid = (low + high) / 2;

			if (v2[i] < v1[mid]) {
				high = mid - 1;
			}

			else if (v2[i] > v1[mid]) {
				low = mid + 1;
			}

			else{
				vResult[i] = 1;
				break;
			}
		}
	}

	for (int i = 0; i < M; i++) {
		cout << vResult[i] << '\n';
	}

	return 0;
}
