#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int n; // 계단의 개수

	cin >> n;

	int stair[301] = { 0 };
	int dp[301] = { 0 };

	for (int i = 1; i <= n; i++) {
		cin >> stair[i];
	}

	//dp[3] = max(stair[1] + stair[3], stair[2] + stair[3]);
	//dp[4] = max(stair[1] + stair[2] + stair[4], stair[2] + stair[4], stair[1] + stair[3] + stair[4]); 
	//dp[4] = max(dp[2] + stair[4], dp[1] + stair[3] + stair[4]);


	for (int i = 1; i < n + 1; i++) {
		if (i == 1) 
			dp[i] = stair[1]; 
		else if (i == 2)
			dp[i] = stair[1] + stair[2];  
		else
			dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i]);   
	} 

	cout << dp[n];  
	return 0;
}