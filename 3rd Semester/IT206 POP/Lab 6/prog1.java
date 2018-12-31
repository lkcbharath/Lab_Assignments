import java.awt.*;
import java.applet.*;
import java.awt.event.*;
import java.rmi.*
import java.rmi.server.*; 

public interface Adder extends Remote{  
    public int add(int x,int y)throws RemoteException;  
    }  







public class prog1 extends Applet implements ActionListener
{
Label l1,l2;
TextField t1,t2;
Button send,clear;

public void init()
{


l1=new Label("Enter your Text here");
add(l1);

t1=new TextField(30);
add(t1);

l2=new Label("Text is displayed here");
add(l2);

t2=new TextField(30);
add(t2);


send=new Button("Send!");
add(send);
send.addActionListener(this);

clear=new Button("Clear");
add(clear);
clear.addActionListener(this);


}

public void actionPerformed(ActionEvent e)
{
if(e.getSource()==send)
{
	String s = "Default message";
	t2.setText(s);
}


if(e.getSource()==clear)
{
t1.setText(" ");
t1.setText("");
t2.setText(" ");
t2.setText("");
}
}

}