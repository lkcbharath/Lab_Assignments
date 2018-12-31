import java.io.*; 
import java.math.*; 

class RunnableDemo implements Runnable {

   private Thread t;
   private String threadName;
   private int offset = 0;
   
   RunnableDemo(String name, int offset) {
      threadName = name;
      System.out.println("Creating " +  threadName );
      this.offset += offset*1000;
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
            for(int i = this.offset; i < (this.offset + 1000); i++) {
                if(isPrime(i))
                	System.out.println( i+ " is prime");
                Thread.sleep(1);
            // Let the thread sleep for a while.
            // Thread.sleep(50);
         }
      } catch (Exception e) {
         System.out.println("Exception caught:" + e);
      }

      System.out.println("Thread " +  threadName + " exiting.");
   }

    boolean isPrime(int n) 
    { 
        // Corner cases 
        if (n <= 1) return false; 
        if (n <= 3) return true; 
      
        // This is checked so that we can skip  
        // middle five numbers in below loop 
        if (n % 2 == 0 || n % 3 == 0) return false; 
      
        for (int i = 5; i * i <= n; i = i + 6) 
            if (n % i == 0 || n % (i + 2) == 0) 
            return false; 
      
        return true; 
    } 
   
   
}

class prog3 {

   public static void main(String args[]) {
      RunnableDemo R1 = new RunnableDemo("Thread-1",1);
      R1.start();
      
      RunnableDemo R2 = new RunnableDemo("Thread-2",2);
      R2.start();

      RunnableDemo R3 = new RunnableDemo("Thread-3",3);
      R3.start();

      RunnableDemo R4 = new RunnableDemo("Thread-4",4);
      R4.start();
   }   
}