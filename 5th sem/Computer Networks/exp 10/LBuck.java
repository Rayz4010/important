import java.util.*;

class LBuck {
    public static void main(String[] args) {
        int[] pk = new int[20];
        int rem = 0, cap = 4, rate = 3, sent, acc;
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter number of packets:");
        int n = sc.nextInt();

        System.out.println("Enter packet sizes:");
        for (int i = 1; i <= n; i++) pk[i] = sc.nextInt();

        System.out.println("Clock\tPkt\tAccept\tSent\tRemain");
        for (int i = 1; i <= n; i++) {

            if (pk[i] != 0) {
                if (rem + pk[i] > cap) acc = -1;
                else { acc = pk[i]; rem += pk[i]; }
            } else acc = 0;

            if (rem != 0) {
                if (rem < rate) { sent = rem; rem = 0; }
                else { sent = rate; rem -= rate; }
            } else sent = 0;

            if (acc == -1) System.out.println(i + "\t" + pk[i] + "\tdrop\t" + sent + "\t" + rem);
            else System.out.println(i + "\t" + pk[i] + "\t" + acc + "\t" + sent + "\t" + rem);
        }
    }
}
