import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Objects;
import java.util.StringTokenizer;

public class graph_10026 {
  public static int n;
  public static String[][] graph;
  public static String[][] graphAbnormal;
  public static int[] dx = { 0, 0, -1, 1 };
  public static int[] dy = { 1, -1, 0, 0 };
  public static boolean[][] visited;
  public static boolean[][] visitedAbnormal;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int ans = 0;
    int ansAbnormal = 0;

    n = Integer.parseInt(st.nextToken());
    graph = new String[n][n];
    graphAbnormal = new String[n][n];
    visited = new boolean[n][n];
    visitedAbnormal = new boolean[n][n];

    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      String a = st.nextToken();
      String[] tmp = a.split("");
      for (int j = 0; j < n; j++) {
        // G인 경우, 적록색맹 환자 그래프에만 R로 넣음
        if (tmp[j].equals("G")) {
          graph[i][j] = tmp[j];
          graphAbnormal[i][j] = "R";
        } else {
          graph[i][j] = tmp[j];
          graphAbnormal[i][j] = tmp[j];
        }
      }
    }

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (!visited[i][j]) {
          dfs(i, j);
          ans++;
        }
      }
    }

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (!visitedAbnormal[i][j]) {
          dfsAbnormal(i, j);
          ansAbnormal++;
        }
      }
    }

    System.out.println(ans + " " + ansAbnormal);

  }

  private static void dfsAbnormal(int x, int y) {
    visitedAbnormal[x][y] = true;
    for (int k = 0; k < 4; k++) {
      int nx = dx[k] + x;
      int ny = dy[k] + y;
      if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visitedAbnormal[nx][ny]) {
        if (Objects.equals(graphAbnormal[x][y], graphAbnormal[nx][ny])) {
          dfsAbnormal(nx, ny);
        }
      }
    }
  }

  private static void dfs(int x, int y) {
    visited[x][y] = true;
    for (int k = 0; k < 4; k++) {
      int nx = dx[k] + x;
      int ny = dy[k] + y;
      if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]) {
        if (Objects.equals(graph[x][y], graph[nx][ny])) {
          dfs(nx, ny);
        }
      }
    }
  }
}
