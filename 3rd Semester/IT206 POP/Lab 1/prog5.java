import java.io.*;
import java.math.*;
import java.lang.*;
import java.util.Scanner;

class prog5 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int i,n;
		System.out.println("Enter length of array:");
		n = scan.nextInt();
		System.out.println("Enter the array:")
		int[] a = new int[n];
		for (i=0;i<n;i++)
			a[n-1-i] = scan.nextInt();

		System.out.println("Array in reverse is:");

		for (i=0;i<n;i++) {
				System.out.printf(a[i] + " ");
		}
		System.out.println();
	}
}
