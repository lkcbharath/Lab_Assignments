import java.io.*; 
import java.math.*;

class ASingleton {

	private static ASingleton instance = null;

	private ASingleton() {
	}

	public static ASingleton getInstance() {
		if (instance == null) {
			instance = new ASingleton();
			System.out.println("New Instance created");
		}
		return instance;
	}

}

class SingletonDemo implements Runnable {

   private Thread t;
   private String threadName;
   private ASingleton aSingleton;
   
   SingletonDemo(String name) {
      threadName = name;
      System.out.println("Creating " +  threadName );
   }

   public void start() {
      System.out.println("Starting " +  threadName );
      if (t == null) {
         t = new Thread(this, threadName);
         t.start();
      }
   }
   
   public void run() {
      System.out.println("Running " +  threadName );
      
      try {
      		aSingleton.getInstance();
            Thread.sleep(1);
            // Let the thread sleep for a while.
            // Thread.sleep(50);
         
      } catch (Exception e) {
         System.out.println("Exception caught:" + e);
      }

      System.out.println("Thread " +  threadName + " exiting.");
   }
   
   
}

class prog2 {

   public static void main(String args[]) {
      SingletonDemo R1 = new SingletonDemo("Thread-1");
      R1.start();
      
      SingletonDemo R2 = new SingletonDemo("Thread-2");
      R2.start();

      SingletonDemo R3 = new SingletonDemo("Thread-3");
      R3.start();
      
      SingletonDemo R4 = new SingletonDemo("Thread-4");
      R4.start();
   }   
}