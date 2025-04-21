import java.util.*;
public class Stack{
    int s[]=new int [10];
    int top=-1;
    int size=10;
    void push(e){
        if (top==size-1)
        System.out.println("Stack Overflow");
        else{
            s[++top]=e;
            System.out.println("Element pushed");
        }
    }
    void pop(){
        if (top==-1)
        System.out.println("Stack Underflow");
        else{
            System.out.println("Element popped is "+s[top]);
            top--;
        }
    }
    void display(){
        if (top==-1)
        System.out.println("Stack is empty");
        else{
            System.out.println("Stack elements are:");
            for (int i=top;i>=0;i--){
                System.out.println(s[i]);
            }
    }
    public static void main(String args[]){
        Scanner in = new Scanner (System.in);
        System.out.println("1.Push 2.pop 3.display 4.exit");
        int ch;
        System.out.println("Enter your choice");
        ch=in.nextInt();
     for(;;){
     switch(ch):
        case 1:{
            System.out.println("Enter the element to be pushed");
            int x=in.nextInt();
            push(x);
            break;
        }
        case 2:{
            pop();
            break;
        }
        case 3:{
            display();
            break;
        }
        case 4:{
            System.exit(0);
            break;
        }
        default: System.out.println("Invalid choice");
    }
    }
}