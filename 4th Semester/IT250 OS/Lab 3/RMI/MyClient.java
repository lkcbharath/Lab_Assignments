import java.rmi.*;
import java.util.Scanner;  
public class MyClient{  
public static void main(String args[]){  
    System.out.println("Fetching object...");
try{  
TestObjectInterface stub=(TestObjectInterface)Naming.lookup("rmi://localhost:5000/sonoo");  

System.out.println(stub.access());  
}catch(Exception e){}  
}  
}  