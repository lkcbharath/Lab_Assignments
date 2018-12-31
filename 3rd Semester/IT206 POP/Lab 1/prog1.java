import java.io.*;
import java.math.*;
import java.lang.*;
import java.util.Scanner;

class prog1 {
	public static void main(String args[]) {
		
		char a;
		String str;
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter a character");
		str = scan.next();
		a = str.charAt(0);
		a = Character.toLowerCase(a);
		boolean charr = Character.isLetter(a);
		if (charr) {
			switch(a) {
				case 'a':case 'e': case 'i': case 'o': case 'u': System.out.println("Vowel"); break;
				default: System.out.println("Consonant"); break;
			}
		}
		else
			System.out.println("Character is not a letter");
	}
}