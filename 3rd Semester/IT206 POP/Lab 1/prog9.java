import java.io.*;
import java.math.*;
import java.lang.*;
import java.util.Scanner;

class prog9 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter a string");
		String str1 = scan.nextLine();
		String str2 = "";

		for(int i=0;i<str1.length();i++)
			str2 += str1.charAt(i);
		System.out.println("Copied string is: " + str2);
	}
}
