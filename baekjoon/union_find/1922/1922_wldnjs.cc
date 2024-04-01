#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, m;
int parent[100001];
vector<pair<int, pair<int, int>>> v;
int result = 0;

int findParent(int x) {
	if (x == parent[x]) return x;
	return parent[x] = findParent(parent[x]);
}

void unionParent(int a, int b) {
	a = findParent(a);
	b = findParent(b);
	if (a < b) parent[b] = a;
	else parent[a] = b;
}
int main()
{
	cin >> n;
	cin >> m;
	for (int i = 1; i <= n; i++) {
		parent[i] = i;
	}
	for (int i = 0; i < m; i++) {
		int a, b, cost;
		cin >> a >> b >> cost;
		v.push_back({ cost,{a,b} });
	}
	sort(v.begin(), v.end());

	for (int i = 0; i < v.size(); i++) {
		int cost = v[i].first;
		int a = v[i].second.first;
		int b = v[i].second.second;
		if (findParent(a) != findParent(b))
		{
			unionParent(a, b);
			result += cost;
		}
	}

	cout << result << "\n";
}