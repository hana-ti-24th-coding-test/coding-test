package dfs.Baekjoon;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class hr_2606 {
    static int N;
    static int M;
    static Scanner scanner = new Scanner(System.in);
    static Boolean[] visited;
    static Boolean[][] Graph;
    static int count = 0;
    public static void main(String[] args) {
        N = scanner.nextInt(); //정점
        M = scanner.nextInt(); //간선

        visited = new Boolean[N+1];
        Graph = new Boolean[N+1][N+1];

        Arrays.fill(visited, false);
        for(int i = 0; i < N; i++) {
            Arrays.fill(Graph[i], false);
        } //이렇게 초기화 하면 runtime 에러 발생... 다른 방법 찾아보기

        for (int i = 1; i <= M; i++) {
            int U = scanner.nextInt();
            int V = scanner.nextInt();
            Graph[U][V] = Graph[V][U] = true;
        }

        System.out.println(bfs(1));
    }

    public static int bfs(int node) {
        Queue<Integer> queue = new LinkedList<>();

        visited[node] = true;
        queue.offer(node);

        while(!queue.isEmpty()) {
            int curr = queue.poll();

            for (int i = 0; i < N; i++) {
                if(!visited[i] && Graph[curr][i]) {
                    queue.offer(i);
                    visited[i] = true;
                    count++;
                }
            }
        }

        return count;
    }
}
