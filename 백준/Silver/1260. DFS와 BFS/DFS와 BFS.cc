#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

vector<vector<int>> graph;
vector<bool> visited;

void dfs(int v) {
    visited[v] = true;
    cout << v << ' ';
    for (int u : graph[v]) {
        if (!visited[u])
            dfs(u);
    }
}

void bfs(int start) {
    queue<int> q;
    vector<bool> visited(graph.size(), false);
    q.push(start);
    visited[start] = true;
    while (!q.empty()) {
        int v = q.front(); q.pop();
        cout << v << ' ';
        for (int u : graph[v]) {
            if (!visited[u]) {
                visited[u] = true;
                q.push(u);
            }
        }
    }
}

int main() {
    int n, m, start;
    cin >> n >> m >> start;
    graph.resize(n + 1);
    visited.resize(n + 1, false);

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for (int i = 1; i <= n; i++)
        sort(graph[i].begin(), graph[i].end());

    dfs(start);
    cout << '\n';
    fill(visited.begin(), visited.end(), false);
    bfs(start);
    cout << '\n';
    return 0;
}
