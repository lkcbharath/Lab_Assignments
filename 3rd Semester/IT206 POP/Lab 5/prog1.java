import java.awt.*;
import java.applet.*;
import java.awt.event.*;

public class prog1 extends Applet implements ActionListener
{
Label l1,l2,l3;
TextField t1,t2,t3;
Button addi,subt,mult,divi,clear;

public void init()
{
println("Testing");


l1=new Label("First Number");
add(l1);

t1=new TextField(10);
add(t1);

l2=new Label("Second Number");
add(l2);

t2=new TextField(10);
add(t2);

l3=new Label("Result");
add(l3);

t3=new TextField(10);
add(t3);

addi=new Button("+");
add(addi);
addi.addActionListener(this);

subt=new Button("-");
add(subt);
subt.addActionListener(this);

mult=new Button("*");
add(mult);
mult.addActionListener(this);

divi=new Button("/");
add(divi);
divi.addActionListener(this);

clear=new Button("Clear");
add(clear);
clear.addActionListener(this);



}

public void actionPerformed(ActionEvent e)
{
if(e.getSource()==addi)
{
Double sum=Double.parseDouble(t1.getText()) + Double.parseDouble(t2.getText());
t3.setText(Double.toString(sum));
}

if(e.getSource()==subt)
{
Double sub=Double.parseDouble(t1.getText()) - Double.parseDouble(t2.getText());
t3.setText(String.valueOf(sub));
}


if(e.getSource()==mult)
{
Double mul=Double.parseDouble(t1.getText()) * Double.parseDouble(t2.getText());
t3.setText(String.valueOf(mul));
}


if(e.getSource()==divi)
{
Double div=Double.parseDouble(t1.getText()) / Double.parseDouble(t2.getText());
t3.setText(String.valueOf(div));
}

if(e.getSource()==clear)
{
t1.setText(" ");
t1.setText("");
t2.setText(" ");
t2.setText("");
t3.setText(" ");
t3.setText("");
}
}

}