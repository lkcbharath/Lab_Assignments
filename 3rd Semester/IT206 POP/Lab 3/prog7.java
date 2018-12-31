import java.io.*;
import java.math.*;
import java.lang.*;
import java.util.*;
import java.net.InetAddress;

 
class prog7 {
    public static void main(String args[]) throws Exception {
        InetAddress inetAddress = InetAddress.getLocalHost();
        System.out.println("IP Address:- " + inetAddress.getHostAddress());
        System.out.println("Host Name:- " + inetAddress.getHostName());
    }
}
