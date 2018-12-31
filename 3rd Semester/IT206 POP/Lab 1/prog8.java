import java.io.*;
import java.math.*;
import java.lang.*;
import java.util.Scanner;

class prog8 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int i,state=0;
		int wc=0;
		System.out.println("Enter a string:");
		String str = scan.nextLine();
		for (i=0; i<str.length(); i++)
        {
            if (str.charAt(i) == ' ' || str.charAt(i) == '\n' || str.charAt(i) == '\t')
                state = 0;

            else if (state==0)
            {
                state = 1;
                wc = wc+1;
                continue;
            }
        }

        System.out.println("Number of words in string: " + wc);

	}
}





		