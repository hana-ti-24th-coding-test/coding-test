#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

int n, m, k, x, y;
int arr[51][51];
int visited[51][51];
int dy[] = { -1,0,1,0 };
int dx[] = { 0,1,0,-1 };

void bfs(int x, int y)
{
	queue<pair<int, int>> q;
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
			if (ny < 0 || nx < 0 || ny >= n || nx >= m || arr[ny][nx] == 0) continue;
			if (visited[ny][nx]) continue;
			visited[ny][nx] = 1;
			q.push({ nx,ny });
		}
	}
}

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		memset(arr, 0, sizeof(arr));
		memset(visited, 0, sizeof(visited));
		int ret = 0;
		cin >> n >> m >> k;
		for (int i = 0; i < k; i++)
		{
			cin >> y >> x;
			arr[y][x] = 1;
		}
		for (int i = 0; i < n; i++)
		{
			for (int j=0;j<m;j++)
				if (arr[i][j] == 1 && !visited[i][j])
				{
					bfs(j, i);
					ret++;
				}
		}
		cout << ret << "\n";
	}
}