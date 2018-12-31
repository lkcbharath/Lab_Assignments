import java.io.*;
import java.math.*;
import java.lang.*;
import java.util.*;

class BubbleSort 
{
  public static <T extends Comparable<T>> void bubbleSort (T[] list, int size) 
  {
    int swapOccurred = 1, outCounter, inCounter; 
    T temp;
    // swapOccurred helps to stop iterating if the array gets sorted before 
    // outCounter reaches to size
    for (outCounter = size - 1; outCounter > 0 && swapOccurred == 1; outCounter--)
    {
      swapOccurred = 0;
      for (inCounter = 0; inCounter < outCounter; inCounter++)
      {
        if (list[inCounter].compareTo(list[inCounter+1]) > 0)
        {
          temp = list[inCounter];
          list[inCounter] = list[inCounter+1];
          list[inCounter+1] = temp;
          swapOccurred = 1;
        }
      }
    }
  }
}
 
public class prog3
{
	public static void main (String[] args)
	{
	  	Scanner scan = new Scanner(System.in);

	  	int i,n,c;
	  	String str;
	  	System.out.println("Enter length of array");
	  	n = scan.nextInt();

	  	System.out.println("Choose between choices for arrays: 1) Integer, 2) Float, 3) Double, then enter array elements");
	  	c = scan.nextInt();
	  	if (c==1) {
	  		Integer arr[] = new Integer[n];
	  		for (i=0;i<n;++i) {
	  			arr[i] = scan.nextInt();
	  		}
	   		BubbleSort.bubbleSort(arr, arr.length);
	     

	    	System.out.println("Sorted Array: ");
	    	for(Integer x : arr)
	    	{
	      		System.out.println(x);
	    	}
	    }
	    if (c==2) {
	  		Float arr[] = new Float[n];
	  		for (i=0;i<n;++i) {
	  			arr[i] = scan.nextFloat();
	  		}
	   		BubbleSort.bubbleSort(arr, arr.length);
	     

	    	System.out.println("Sorted Array: ");
	    	for(Float x : arr)
	    	{
	      		System.out.println(x);
	    	}
	    }
	    if (c==3) {
	  		Double arr[] = new Double[n];
	  		for (i=0;i<n;++i) {
	  			arr[i] = scan.nextDouble();
	  		}
	   		BubbleSort.bubbleSort(arr, arr.length);
	     

	    	System.out.println("Sorted Array: ");
	    	for(Double x : arr)
	    	{
	      		System.out.println(x);
	    	}
	    }
	  	
	}
}
 
   