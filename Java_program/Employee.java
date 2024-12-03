import java.util.*;
public class Employee{
    int id;
    String name;
    double salary;
    public Employee(int id, String name, double salary){
        this.id = id;
        this.name = name;
        this.salary = salary;
    }
    void display(){
        System.out.println("Id: "+id+" Name: "+name+" Salary: "+salary);
    }
    void increase(percentage){
        salary = salary + salary*percentage/100;
    }
    public static void main(String[] args){
        Scanner in =new Scanner(System.in);
        System.out.println("Enter the name ");
        String name = in.nextLine();
        System.out.println("Enter the id");
        int id = in.nextInt();
        System.out.println("Enter the salary");
        double salary= in.nextDouble();
        Employee e = new Employee(id, name, salary);
        e.display();    
        System.out.println("Enter the percentage to increase the salary");
        double percentage = in.nextDouble();
        e.increase(percentage);
        e.display();
    }
}