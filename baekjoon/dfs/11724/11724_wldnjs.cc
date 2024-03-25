#include <iostream>
#include <vector>
using namespace std;

int n, m, cnt = 0;
vector<int> v[1001];
int visited[1001];
void dfs(int x)
{
	visited[x] = 1;
	for (int i = 0; i < v[x].size(); i++)
	{
		int y = v[x][i];
		if (!visited[y])
		{
			dfs(y);
		}
	}
}

int main()
{
	cin >> n >> m;
	for (int i = 0; i < m; i++)
	{
		int x, y;
		cin >> x >> y;
		v[x].push_back(y);
		v[y].push_back(x);
	}
	for (int i = 1; i <= n; i++)
	{
		if (!visited[i])
		{
			cnt++;
			dfs(i);
		}
	}
	cout << cnt;
}