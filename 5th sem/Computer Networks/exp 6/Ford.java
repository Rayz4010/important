import java.util.*;

public class Ford {
    static final int INF = 999999;

    static void bellmanFord(int n, int src, int[][] w) {
        int[] dist = new int[n];
        Arrays.fill(dist, INF);
        dist[src] = 0;

        // Relax edges n-1 times
        for (int k = 0; k < n - 1; k++)
            for (int u = 0; u < n; u++)
                for (int v = 0; v < n; v++)
                    if (w[u][v] != INF && dist[u] != INF && dist[v] > dist[u] + w[u][v])
                        dist[v] = dist[u] + w[u][v];

        // Check negative cycle
        for (int u = 0; u < n; u++)
            for (int v = 0; v < n; v++)
                if (w[u][v] != INF && dist[u] != INF && dist[v] > dist[u] + w[u][v]) {
                    System.out.println("Graph contains a negative weight cycle");
                    return;
                }

        // Print distances
        for (int i = 0; i < n; i++)
            System.out.println("Distance from " + src + " to " + i + " = " + dist[i]);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of vertices: ");
        int n = sc.nextInt();
        int[][] A = new int[n][n];

        System.out.println("Enter adjacency matrix (0 = no edge):");
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                A[i][j] = sc.nextInt();
                if (i == j) A[i][j] = 0;
                else if (A[i][j] == 0) A[i][j] = INF;
            }

        System.out.print("Enter source vertex (0 to " + (n - 1) + "): ");
        int source = sc.nextInt();

        bellmanFord(n, source, A);
        sc.close();
    }
}
