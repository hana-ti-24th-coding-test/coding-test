#include <iostream>
#include <vector>
using namespace std;

int n;
vector<int> v[100001];
int visited[100001];
int arr[100001];
void dfs(int x)
{
	visited[x] = 1;
	for (int i = 0; i < v[x].size(); i++)
	{
		int y = v[x][i];
		if (!visited[y])
		{
			arr[y] = x;
			dfs(y);
		}
	}
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int x, y;
		cin >> x >> y;
		v[x].push_back(y);
		v[y].push_back(x);
	}
	dfs(1);
	for (int i = 2; i <= n; i++)
	{
		cout << arr[i] << "\n";
	}
}