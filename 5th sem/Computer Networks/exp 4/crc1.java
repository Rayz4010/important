import java.util.*;

public class crc1 {
    static void divide(int[] d, int[] g) {
        for (int i = 0; i <= d.length - g.length; i++)
            if (d[i] == 1)
                for (int j = 0; j < g.length; j++)
                    d[i + j] ^= g[j];
    }

    public static void main(String[] a) {
        Scanner s = new Scanner(System.in);

        System.out.print("Msg: "); String msg = s.nextLine();
        System.out.print("Gen: "); String gen = s.nextLine();

        int[] g = gen.chars().map(c -> c - '0').toArray();
        int[] data = new int[msg.length() + g.length - 1];
        for (int i = 0; i < msg.length(); i++) data[i] = msg.charAt(i) - '0';

        int[] temp = data.clone(); divide(temp, g);
        for (int i = msg.length(); i < data.length; i++) data[i] = temp[i];

        System.out.print("Codeword: "); for (int x : data) System.out.print(x); System.out.println();

        System.out.print("Received: ");
        int[] recv = s.nextLine().chars().map(c -> c - '0').toArray();
        divide(recv, g);

        System.out.println(Arrays.stream(recv).anyMatch(x -> x == 1) ? "Error detected" : "Valid");
    }
}
