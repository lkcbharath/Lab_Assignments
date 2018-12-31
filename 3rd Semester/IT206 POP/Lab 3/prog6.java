import java.io.*;
import java.math.*;
import java.lang.*;
import java.util.*;

class prog6 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int i,j,k;
		int num,cube;
		int count = 0;

		for (i=0;i<10;++i) {
			for (j=0;j<10;++j) {
				for (k=0;k<10;++k) {
					num = i*100 + j*10 + k;
					cube = (i*i*i) + (j*j*j) + (k*k*k);
					if (num==cube){
						System.out.println(num);
					}
				}
			}
		}
	}

}