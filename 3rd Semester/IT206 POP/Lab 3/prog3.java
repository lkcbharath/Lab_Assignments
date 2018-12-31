class ThreadDemo extends Thread {

   private Thread t;
   private String threadName;
   public static int count=0;
   
   ThreadDemo(String name) {
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
   
   public synchronized void run() {
      System.out.println("Running " +  threadName );
      {
      try {
            for(int i = 0; i < 100; i++) {
                count = count + 1;
                System.out.println("Current count: " + count);
                Thread.sleep(5);
            // Let the thread sleep for a while.
            // Thread.sleep(50);
         }
      } catch (Exception e) {
         System.out.println("Exception caught:" + e);
      }
      }

      System.out.println("Thread " +  threadName + " exiting. Count is " + count);
   }
   
   
}

class prog3 {

   public static void main(String args[]) {
      ThreadDemo T1 = new ThreadDemo("Thread-1");
      T1.start();
      
      ThreadDemo T2 = new ThreadDemo("Thread-2");
      T2.start();

      ThreadDemo T3 = new ThreadDemo("Thread-3");
      T3.start();
      
      ThreadDemo T4 = new ThreadDemo("Thread-4");
      T4.start();
   }   
}
