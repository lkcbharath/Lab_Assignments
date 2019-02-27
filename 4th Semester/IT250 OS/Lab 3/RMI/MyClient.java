import java.rmi.*;
import java.util.Scanner;  
public class MyClient{  
public static void main(String args[]){  
    int a, b;
    Scanner scan = new Scanner(System.in);
    System.out.println("Enter two integers:");
    a = scan.nextInt();
    b = scan.nextInt();
    System.out.print("The sum is: ");
try{  
Adder stub=(Adder)Naming.lookup("rmi://localhost:5000/sonoo");  

System.out.println(stub.add(a,b));  
}catch(Exception e){}  
}  
}  