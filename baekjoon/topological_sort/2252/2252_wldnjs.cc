#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int v, e;
vector<int> adj[100001]; // 간선 정보
int indegree[100001]; //진입차수

void tosort() {
	vector<int> result;
	queue<int> q;

	//진입차수가 0인 노드를 큐에 삽입
	for (int i = 1; i <= v; i++) {
		if (indegree[i] == 0) {
			q.push(i);
		}
	}

	while (!q.empty()) {
		int now = q.front();
		q.pop();
		result.push_back(now);

		for (int i = 0; i < adj[now].size(); i++) {
			indegree[adj[now][i]] -= 1;
			if (indegree[adj[now][i]] == 0) {
				q.push(adj[now][i]);
			}
		}
	}
	for (int i = 0; i < result.size(); i++) {
		cout << result[i] << " ";
	}
}
int main()
{
	cin >> v >> e;
	for (int i = 0; i < e; i++) {
		int a, b;
		cin >> a >> b;
		adj[a].push_back(b);
		indegree[b] += 1;
	}
	tosort();
}