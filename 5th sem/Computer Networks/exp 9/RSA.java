import java.util.*;

public class RSA {
    static int gcd(int a,int b){ while(b!=0){int r=a%b; a=b; b=r;} return a; }

    public static void main(String[] a) {
        Scanner s=new Scanner(System.in);

        System.out.println("Enter the message to be encrypted:");
        String msg=s.nextLine();

        System.out.println("Enter p and q:");
        int p=s.nextInt(), q=s.nextInt();
        int n=p*q, phi=(p-1)*(q-1), e=0, d=0;

        for(int i=2;i<phi;i++) if(gcd(i,phi)==1){ e=i; break; }
        for(int i=2;i<phi;i++) if((e*i-1)%phi==0){ d=i; break; }

        int len=msg.length();
        int[] num=new int[len], enc=new int[len], dec=new int[len];

        for(int i=0;i<len;i++) num[i]=msg.charAt(i)-96;

        for(int i=0;i<len;i++){
            enc[i]=1;
            for(int j=0;j<e;j++) enc[i]=(enc[i]*num[i])%n;
        }

        System.out.println("\nEncrypted message:");
        for(int i=0;i<len;i++){
            System.out.print(enc[i]);
            System.out.print((char)(enc[i]+96));
        }

        for(int i=0;i<len;i++){
            dec[i]=1;
            for(int j=0;j<d;j++) dec[i]=(dec[i]*enc[i])%n;
        }

        System.out.println("\n\nDecrypted message:");
        for(int i=0;i<len;i++) System.out.print((char)(dec[i]+96));
    }
}