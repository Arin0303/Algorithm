
#include <iostream>
using namespace std;

int n, d;
int count_d = 0;

void dfs(int current) {
    
    if (current > n)
        return;
    // d가 current 안에 몇 번 들어있는지 %과 /를 이용하여 세기
    int tmp = current;
    while (tmp > 0) {
        if (tmp % 10 == d) 
            count_d++; // tmp 마지막 자리에 d가 있으면 count_d++
        tmp /= 10; // tmp 마지막 자리 없애기 
    }
    for (int i = 0; i < 10; i++) {
        dfs(current * 10 + i);
    }
}

int main() {
    
    cin >> n >> d;
    // 1~n까지 d의 빈도 

    // 1~9로 시작하는 트리 생성
    for (int i = 1; i <= 9; i++) {
        dfs(i);
    }

    cout << count_d << '\n';
    return 0;
}
