//abstract class

abstract class Default {

    Default() { 
    	System.out.println("Original Abstract Class Constructor is accessed!"); 
    }

    abstract void fun();
}

class Derived extends Default {

    Derived() { 
    	System.out.println("Derived Constructor is accessed!"); 
    }
        

    void fun() { 
    	System.out.println("Derived fun() is accessed!"); 
    }
}

class prog2 {
    public static void main(String args[]) { 
       Derived d = new Derived();
       d.fun();
    }
}