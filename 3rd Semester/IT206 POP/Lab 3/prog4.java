import java.io.*;
import java.math.*;
import java.lang.*;
import java.util.*;

class prog4 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		String str;
		char c;
		String ci;

		str = scan.next();

		int i,j;
		int[] a = new int[26];

		for (i=0;i<26; ++i)
			a[i] = 0;


		for (i=0;i<str.length();++i) {
			c = str.charAt(i);
			j = c;
			j -= 97;
			++a[j];
		}
		System.out.println("Duplicate character details shown below. If blank, no duplicate characters present:");
		for (i=0;i<26;++i) {
			if(a[i]>1) {
				c = (char)(i+97);

				System.out.println(c + " has occurred " + a[i] + " times.");
			}
		}
	}
}