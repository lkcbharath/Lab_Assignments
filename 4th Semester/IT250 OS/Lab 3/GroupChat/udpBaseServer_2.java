// Java program to illustrate Server side 
// Implementation using DatagramSocket 
import java.io.IOException; 
import java.net.DatagramPacket; 
import java.net.DatagramSocket; 
import java.net.InetAddress; 
import java.util.Scanner;
import java.net.SocketException; 

public class udpBaseServer_2 
{ 
	public static void main(String[] args) throws IOException 
	{ 
		// Scanner sc = new Scanner(System.in); 
		// Step 1 : Create a socket to listen at port 1234 
		DatagramSocket ds_server = new DatagramSocket(1234); 
		DatagramSocket ds_client = new DatagramSocket();

		InetAddress ip = InetAddress.getLocalHost(); 

		byte buf[] = null; 
		byte[] receive = new byte[65535]; 

		DatagramPacket DpReceive = null; 

		while (true) 
		{ 

			// Step 2 : create a DatgramPacket to receive the data. 
			DpReceive = new DatagramPacket(receive, receive.length); 

			// Step 3 : revieve the data in byte buffer. 
			ds_server.receive(DpReceive); 

			System.out.println("Client:-" + data(receive)); 

			// Exit the server if the client sends "bye" 
			if (data(receive).toString().equals("bye")) 
			{ 
				System.out.println("Client sent bye.....EXITING"); 
				break; 
			} 

			// Clear the buffer after every message. 
			receive = new byte[65535]; 

			// String inp = sc.nextLine(); 

			// // convert the String input into the byte array. 
			// buf = inp.getBytes(); 

			// // Step 2 : Create the datagramPacket for sending 
			// // the data. 
			// DatagramPacket DpSend = 
			// 	new DatagramPacket(buf, buf.length, ip, 4321); 

			// // Step 3 : invoke the send call to actually send 
			// // the data. 
			// ds_client.send(DpSend); 

			// // break the loop if user enters "bye" 
			// if (inp.equals("bye")) 
			// 	break; 
		} 
	} 

	// A utility method to convert the byte array 
	// data into a string representation. 
	public static StringBuilder data(byte[] a) 
	{ 
		if (a == null) 
			return null; 
		StringBuilder ret = new StringBuilder(); 
		int i = 0; 
		while (a[i] != 0) 
		{ 
			ret.append((char) a[i]); 
			i++; 
		} 
		return ret; 
	} 
} 
