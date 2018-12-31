class RunnableDemo implements Runnable {

   private Thread t;
   private String threadName;
   private int count=0;
   
   RunnableDemo(String name) {
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
            for(int i = 0; i < 1000; i++) {
                count = count + 1;
                System.out.println("Current count: " + count);
                Thread.sleep(5);
            // Let the thread sleep for a while.
            // Thread.sleep(50);
         }
      } catch (Exception e) {
         System.out.println("Exception caught:" + e);
      }

      System.out.println("Thread " +  threadName + " exiting. Count is " + count);
   }
   
   
}

class prog2 {

   public static void main(String args[]) {
      RunnableDemo R1 = new RunnableDemo("Thread-1");
      R1.start();
      
      RunnableDemo R2 = new RunnableDemo("Thread-2");
      R2.start();

      RunnableDemo R3 = new RunnableDemo("Thread-3");
      R3.start();

      RunnableDemo R4 = new RunnableDemo("Thread-4");
      R4.start();
   }   
}