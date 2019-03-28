import java.io.*;
import java.util.Scanner;
import java.util.*;

class Monitor
{
private volatile int readers; //specifies number of readers reading
private volatile boolean writing; //specifies if someone is writing
private volatile Condition OK_to_Read, OK_to_Write;

 public Monitor()
{
    readers = 0;
    writing = false;
    OK_to_Read = new Condition();
    OK_to_Write = new Condition();
}

public synchronized void Start_Read(int n)
{

     System.out.println("wants to read " + n);
    if(writing || OK_to_Write.is_non_empty())
    {
        try{
            System.out.println("reader is waiting " + n);
            OK_to_Read.sleep_();
        }
        catch(InterruptedException e){}
    }
    readers += 1;
    OK_to_Read.release_all();

}

public synchronized void End_Read(int n)
{

        System.out.println("finished reading " + n);
        readers -= 1;

        if(OK_to_Write.is_non_empty())
        {
            OK_to_Write.release_one();
        }
        else if(OK_to_Read.is_non_empty())
        {
            OK_to_Read.release_one();
        }
        else
        {
            OK_to_Write.release_all();
        }

}

public synchronized void Start_Write(int n)
{
    System.out.println("wants to write " + n);
    if(readers != 0 || writing)
    {
        try{
            System.out.println("Writer is waiting " + n);
            OK_to_Write.sleep_();
                }catch(InterruptedException e){}
    }

    writing = true;

}

public synchronized void End_Write(int n)
{

    System.out.println("finished writing " + n);
    writing = false;
    if(OK_to_Read.is_non_empty())
    {
        OK_to_Read.release_one();
    }
    else if(OK_to_Write.is_non_empty())
    {
        OK_to_Write.release_one();
    }
    else
    {
        OK_to_Read.release_all();
    }

}

}

class Condition
{
private int number;//specifies the number of readers/writers waiting

public Condition()
{ 
    number = 0; 
}

public synchronized boolean is_non_empty()  
{ 
    if(number == 0)
        return false; 
    else
        return true;
}

public synchronized void release_all()
{ 
number = 0;
notifyAll(); 
}


public synchronized void release_one()
{ 
number -=1;
notify(); 
}   

public synchronized void wait_() throws InterruptedException
{  
    number++;
    wait();
}
public synchronized void sleep_() throws InterruptedException
{  
    Thread.sleep(1000);
}

}


class Reader extends Thread
{
private Monitor M;
private String value;
public Reader(String name,Monitor c)
{
    super(name);
    M=c;
}

public void run()
{
    for(int i = 0; i < 10; i++){
            M.Start_Read(i);
            //System.out.println("Reader "+getName()+" is retreiving data...");
            System.out.println("Reader is reading " + i);
            M.End_Read(i);
    }

}
}

class Writer extends Thread
{
private Monitor M;
private int value;
public Writer(String name, Monitor d)
{
    super(name);
    M = d;
}

public void run()
{
    for(int j = 0; j < 10; j++){
            M.Start_Write(j);
            //System.out.println("Writer "+getName()+" is writing data...");
            System.out.println("Writer is writing " + j);
            M.End_Write(j);
    }

}
}

public class Demo
{
public static void main(String [] args)
{
    Monitor M = new Monitor();
    // int n1,n2,i;
    // Scanner scan = new Scanner(System.in);
    // n1 = scan.nextInt();
    // n2 = scan.nextInt();
    Reader reader = new Reader("1",M);
    Writer writer = new Writer("1",M);
    reader.start();
    writer.start();
         
} }