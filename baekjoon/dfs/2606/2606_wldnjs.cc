#include <iostream>
#include <vector>
using namespace std;

int n, m;
vector<int> v[101];
int visited[101];
int cnt = 0;

void dfs(int x)
{
	visited[x] = 1;
	for (int i = 0; i < v[x].size(); i++)
	{
		int y = v[x][i];
		if (!visited[y])
		{
			dfs(y);
			cnt++;
		}

	}
}
int main()
{
	cin >> n >> m;
	for (int i = 0; i < m; i++)
	{
		int f, s;
		cin >> f >> s;
		v[f].push_back(s);
		v[s].push_back(f);
	}
	dfs(1);
	cout << cnt;
}