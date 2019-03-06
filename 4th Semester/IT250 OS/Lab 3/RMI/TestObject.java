import java.rmi.*;  
import java.rmi.server.*;  
public class TestObject extends UnicastRemoteObject implements TestObjectInterface{  
    TestObject()throws RemoteException{  
super();  
}  
public String access(){ return "Object accessed";}  
}   