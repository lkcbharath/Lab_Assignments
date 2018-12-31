import java.io.*;
import java.math.*;
import java.lang.*;
import java.util.Scanner;

class prog4 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int n,m,i,j,choice,key;
		System.out.println("Enter n and m for nxm 2D array");
		n = scan.nextInt();
		m = scan.nextInt();
		int[][] a = new int[n][m];
		System.out.println("Enter a 2D array of order n x m");

		for (i=0;i<n;i++) {
			for (j=0;j<m;j++) {
				a[i][j] = scan.nextInt();
			}
		}

		System.out.println("Enter your choice based on the following options:");
		System.out.println("1. Add two arrays\n2. Subtract two arrays\n3. Transpose of an array\n4. Search an element in an array");
		choice = scan.nextInt();

		int arr2d = 2;

		switch(choice) {
			case 1: arr2d = 0; break;
			case 2: arr2d = 1; break;

			case 3: for (i=0;i<n;i++) {
						for (j=0;j<m;j++) {
							System.out.printf(a[j][i] + " ");
						}
						System.out.println();
					}
					System.exit(0);break;

			case 4: System.out.println("Enter key to search for:");
					key = scan.nextInt();
					for (i=0;i<n;i++) {
						for (j=0;j<m;j++) {
							if (key==a[i][j]) {
								System.out.println("Found!");
								System.exit(0);
							}
						}
					}
					System.out.println("Not found");System.exit(0);break;

			default: System.out.println("Invalid choice");System.exit(0);
		}

		int[][] b = new int[n][m];

		System.out.println("Enter a second 2D array of order n x m");

		for (i=0;i<n;i++) {
			for (j=0;j<m;j++) {
				b[i][j] = scan.nextInt();
				if (arr2d==0)
					a[i][j] += b[i][j];
				else if (arr2d==1)
					a[i][j] -= b[i][j];
			}
		}

		System.out.println("Result of operation on 2D array:");

		for (i=0;i<n;i++) {
			for (j=0;j<m;j++) {
				System.out.printf(a[i][j] + " ");
			}
			System.out.println();
		}








	}
}
