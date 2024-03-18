#include <iostream>
#include <queue>
using namespace std;

int n, m;
int arr[101][101];
int visited[101][101];

int dy[] = { -1,0,1,0 };
int dx[] = { 0,1,0,-1 };
int bfs(int x, int y)
{
	queue<pair<int,int>> q;
	q.push({ x,y });
	visited[y][x] = 1;
	while (q.size())
	{
		int y = q.front().second;
		int x = q.front().first;
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			int ny = y + dy[i];
			int nx = x + dx[i];
			if (ny < 0 || nx < 0 || ny >= n || nx >= m || arr[ny][nx]==0) continue;
			if (visited[ny][nx]) continue;
			visited[ny][nx] = visited[y][x] + 1;
			q.push({ nx,ny });
		}
	}
	return visited[n - 1][m - 1];
}

int main()
{
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
			scanf("%1d", &arr[i][j]);
	}
	cout << bfs(0, 0);
}