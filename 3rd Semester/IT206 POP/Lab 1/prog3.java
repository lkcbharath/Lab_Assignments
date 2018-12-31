import java.io.*;
import java.math.*;
import java.lang.*;
import java.util.Scanner;

class prog3 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter number of integers to be inputted");
		int n = scan.nextInt();
		int[] a = new int[n];
		int i,x;
		System.out.println("Enter the array");
		for (i=0;i<n;i++) {
			x = scan.nextInt();
			a[i] = (x%2);
		}
		System.out.println("New array is: ");	
		for (i=0;i<n;i++) {
			System.out.printf(a[i] + " ");
		}
		System.out.println();

	}
}