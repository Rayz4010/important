import java.util.*;

class Ford {
    static final int INF = 999999;

    static void bellman(int n, int src, int[][] w) {
        int[] d = new int[n];
        Arrays.fill(d, INF);
        d[src] = 0;

        for (int k = 0; k < n - 1; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if (w[i][j] != INF && d[i] != INF && d[j] > d[i] + w[i][j])
                        d[j] = d[i] + w[i][j];

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (w[i][j] != INF && d[i] != INF && d[j] > d[i] + w[i][j]) {
                    System.out.println("Negative weight cycle detected");
                    return;
                }

        for (int i = 0; i < n; i++)
            System.out.println(src + " → " + i + " = " + d[i]);
    }

    public static void main(String[] a) {
        Scanner s = new Scanner(System.in);
        System.out.print("Vertices: ");
        int n = s.nextInt();
        int[][] g = new int[n][n];

        System.out.println("Adjacency matrix (0 = no edge):");
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                g[i][j] = (i == j) ? 0 : (s.nextInt() == 0 ? INF : s.nextInt());

        System.out.print("Source: ");
        bellman(n, s.nextInt(), g);
    }
}
