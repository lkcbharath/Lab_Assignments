//method overriding

class Thought {

      int a = 5;
    public void message() {
        System.out.println("1+1 = 11, I don't know how it makes sense otherwise.");
    }
}

class Advice extends Thought {

      int a = 6;
    public void message() {
        System.out.println("1+1 = 2, because of how we count numbers.");
    }
}

class prog3 {
	 public static void main(String args[]) { 
       Advice therefore = new Advice();
       Thought ithink = new Thought();

       ithink.message();
       System.out.println("But the truth is...");
       therefore.message();

       System.out.println("Five = " + ithink.a);
       System.out.println("Six = " + therefore.a);

    }
}