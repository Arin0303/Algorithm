#include <iostream>
using namespace std;

int N, M;
int arr[10];        // M <= 8이므로 충분
bool visited[10];   // 1 ~ N까지 사용 여부

void dfs(int depth) {
    if (depth == M) {
        for (int i = 0; i < M; i++) {
            cout << arr[i] << " ";
        }
        cout << "\n";
        return;
    }

    for (int i = 1; i <= N; i++) {
        if (!visited[i]) {
            visited[i] = true;
            arr[depth] = i;
            dfs(depth + 1);
            visited[i] = false;  // 백트래킹
        }
    }
}

int main() {
    cin >> N >> M;
    dfs(0);  // 깊이 0부터 시작
    return 0;
}
