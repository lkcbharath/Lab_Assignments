// simple inheritance

import java.io.*;
import java.math.*;
import java.lang.*;
import java.util.Scanner;

class properties {


	String name;
	int age;

	public static void displaytest() {
		System.out.println("Base class called successfully!");
	}
}

class details extends properties {
	//data fields extended
	int salary; 
}

class prog1{

	

	public static void main(String args[]) {

		details test = new details();
		test.name = "ME";
		test.age = 19;
		test.salary = 12000;
		System.out.println(test.name);
		System.out.println(test.age);
		System.out.println(test.salary);
		test.displaytest();

	}
}
	