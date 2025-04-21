import java.util.*;
public class Add{
    public static void main(String args[])
    {
        Scanner in =new Scanner(System.in);
        System.out.println("Eneter the n of the matrix");
        int n=in.nextInt();
        int i,j;
        int m1[][]=new int[n][n];
        int m2[][]=new int[n][n];
        int sm[][]=new int[n][n];
        System.out.println("Enter the elements of the first matrix");
        for (i=0;i<n;i++){
            for (j=0;j<n;j++){
                m1[i][j]=in.nextInt();
            }
        }
        System.out.println("Enter the elements of the second matrix");
        for (i=0;i<n;i++){
            for (j=0;j<n;j++){
                m2[i][j]=in.nextInt();
            }
        }
        for (i=0;i<n;i++){
            for (j=0;j<n;j++){
                sm[i][j]=m1[i][j]+m2[i][j];
            }
        }
        System.out.println("Matrix after addition");
        for (i=0;i<n;i++){
            for (j=0;j<n;j++){
                System.out.println(sm[i][j]);
            }
            System.out.print("");
        }
    }
}