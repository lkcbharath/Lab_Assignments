import java.rmi.*; 
public interface TestObjectInterface extends Remote 
{ 
	public String access() throws RemoteException; 
} 
