import java.io.*;
import java.math.*;
import java.lang.*;
import java.util.Scanner;

class prog2 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		String str;
		System.out.println("Enter two integers");
		int a = scan.nextInt();
		int b = scan.nextInt();
		System.out.println("Enter an arithmetic operator to perform as operation on integers");
		str = scan.next();
		char op = str.charAt(0);
		int res = 0;

		switch(op) {
			case '+': res = a+b; break;
			case '-': res = a-b; break;
			case '*': res = a*b; break;
			case '/': res = a/b; break;
			case '%': res = a%b; break;
			default: System.out.println("Invalid operation");System.exit(0);
		}
		System.out.println("Result of operation is " + res);
	}
}