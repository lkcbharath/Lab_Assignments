import java.io.*;
import java.math.*;
import java.lang.*;
import java.util.*;

class prog1 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		String str;
		int res = 0;
		try {
			System.out.println("Enter two integers");
			int a = scan.nextInt();
			int b = scan.nextInt();
			System.out.println("Enter an arithmetic operator to perform as operation on integers");
			str = scan.next();
			char op = str.charAt(0);
			

			switch(op) {
				case '+': res = a+b; break;
				case '-': res = a-b; break;
				case '*': res = a*b; break;
				case '/': res = a/b; break;
				case '%': res = a%b; break;
				default: System.out.println("Invalid operation entered!");System.exit(0);
			}
		}
		catch (java.util.InputMismatchException e) {
			System.out.println("Enter a valid integer within range! " + e);
			System.exit(0);
		}
		catch (ArithmeticException e) {
			System.out.println("Dividing by 0 is not possible! " + e);
			System.exit(0);
		}

		catch (Exception e) {
			System.out.println("Add this exception: " + e);
			System.exit(0);
		}

		System.out.println("Result of operation is " + res);
	}
}