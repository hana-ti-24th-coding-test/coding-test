#include <iostream>
#include <vector>
#include <queue>
#define INF 1e9

using namespace std;

int n, m, start;
vector<pair<int, int> > graph[100001];
int d[100001];

void dijkstra(int start) {
	priority_queue<pair<int, int> > pq;
	pq.push({ 0, start });
	d[start] = 0;
	while (!pq.empty()) {
		int dist = pq.top().first;
		int now = pq.top().second;
		pq.pop();
		if (d[now] < dist) continue;
		for (int i = 0; i < graph[now].size(); i++) {
			int cost = dist + graph[now][i].second;
			int nx = graph[now][i].first;
			if (d[nx] > cost) {
				pq.push({ cost,nx });
				d[nx] = cost;
			}
		}
	}
}

int main(void) {
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		graph[a].push_back({ b, c });
	}

	fill(d, d + 100001, INF);


	int st, end;
	cin >> st >> end;
	dijkstra(st);
	cout << d[end];

	return 0;
}