import java.io.*;
import java.math.*;
import java.lang.*;
import java.util.*;

class prog5 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int n;
		System.out.println("Enter choice based on geometric figure for area calculation:");
		System.out.println("1. Triangle");
		System.out.println("2. Square or Rhombus");
		System.out.println("3. Rectangle or Parallelogram");
		System.out.println("4. Trapezium");
		System.out.println("5. Circle");
		n = scan.nextInt();

		int b,h,r;
		int longside,shortside;
		double result=0;

		switch(n) {
			case 1:
				System.out.println("Enter Triangle base and height");
				b = scan.nextInt();
				h = scan.nextInt();
				result = (double)(0.5*b*h);
				break;
			case 2:
				System.out.println("Enter Square/Rhombus side length");
				r = scan.nextInt();
				result = (double)(r*r);
				break;
			case 3:
				System.out.println("Enter Rectangle/Parallelogram base and height");
				b = scan.nextInt();
				h = scan.nextInt();
				result = (double)(b*h);
				break;
			case 4:
				System.out.println("Enter Trapezium parallel side lengths and height");
				longside = scan.nextInt();
				shortside = scan.nextInt();
				h = scan.nextInt();
				result = (double)(0.5*(longside+shortside)*h);
				break;
			case 5:
				System.out.println("Enter Circle radius");
				r = scan.nextInt();
				result = (double)(3.1415*r*r);
				break;
			default:
				System.out.println("Invalid option entered.");
				System.exit(0);
		}

		System.out.println("Result is: " + result);
	}

}