// method overloading/polymorphism
// based on no of same parameters, different parameters, order of diff para, return type of method

class overload {

	int add(int a)
	{
		System.out.println("1 Integer entered!");
		return a;
	}

	int add(int a, int b)
	{
		System.out.println("2 Integers entered!");
		return a+b;
	}

	int add(int a, int b, int c)
	{
		System.out.println("3 integers entered!");
		return a+b+c;
	}

	float add(float a, float b)
	{
		System.out.println("Float returned");
		return a+b;
	}

	void check(int a, float b)
	{
		System.out.println("Integer is entered first!");
	}

	void check(float a, int b)
	{
		System.out.println("Float is entered first!");
	}
}




class prog4 {
	 public static void main(String args[]) { 
       overload test = new overload();
       float a = 1;
       float b = 2;
       System.out.println(test.add(1));
       System.out.println(test.add(1,2));
       System.out.println(test.add(1,2,3));
       System.out.println(test.add(a,b));
       test.check(1,a);
       test.check(a,1);


    }
}