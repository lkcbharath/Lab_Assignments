import java.awt.*;
import java.applet.*;
import java.awt.event.*;

public class prog2 extends Applet implements ActionListener
{
int oper = 1;

// add threads with runnable

Button anim1,anim2,anim3,clear;
Button auto_anim;

public void init()
{
anim1=new Button("animate 1");
add(anim1);
anim1.addActionListener(this);

anim2=new Button("animate 2");
add(anim2);
anim2.addActionListener(this);

anim3=new Button("animate 3");
add(anim3);
anim3.addActionListener(this);

auto_anim=new Button("Automatically Animate!");
add(auto_anim);
auto_anim.addActionListener(this);

clear=new Button("Clear");
add(clear);
clear.addActionListener(this);

}


public void paint(Graphics g)
{
	Dimension d = getSize();
	//oper is for operation

	if (oper==1) {
		g.clearRect(0, 0, d.width, d.height);

			g.drawArc(100,100,100,100,0,360); //head
	g.drawLine(150,200,150,400); //body

	g.drawArc(125,130,15,15,0,360); //eye 1
	g.drawArc(165,130,15,15,0,360); //eye 2

	g.drawArc(125,150,55,30,180,180); //smile

		g.drawLine(150,300,250,250); //arm1
		g.drawLine(150,300,50,250); //arm2

		g.drawLine(150,400,200,450); //LEG1
		g.drawLine(150,400,100,450); //LEG2
	}

	else if (oper==2) {
		g.clearRect(0, 0, d.width, d.height);

			g.drawArc(100,100,100,100,0,360); //head
	g.drawLine(150,200,150,400); //body

	g.drawArc(125,130,15,15,0,360); //eye 1
	g.drawArc(165,130,15,15,0,360); //eye 2

	g.drawArc(125,150,55,30,180,180); //smile

		g.drawLine(150,300,250,300); //arm1
		g.drawLine(150,300,50,300); //arm2

		g.drawLine(150,400,220,450); //LEG1
		g.drawLine(150,400,80,450); //LEG2
	}

	else if (oper==3) {
		g.clearRect(0, 0, d.width, d.height);

			g.drawArc(100,100,100,100,0,360); //head
	g.drawLine(150,200,150,400); //body

	g.drawArc(125,130,15,15,0,360); //eye 1
	g.drawArc(165,130,15,15,0,360); //eye 2

	g.drawArc(125,150,55,30,180,180); //smile

		g.drawLine(150,300,250,325); //arm1
		g.drawLine(150,300,50,325); //arm2

		g.drawLine(150,400,240,450); //LEG1
		g.drawLine(150,400,60,450); //LEG2
	}

	else if (oper==4) {
		g.clearRect(0, 0, d.width, d.height);
	}

}


public void actionPerformed(ActionEvent e)
{


	if(e.getSource()==anim1)
	{
		oper = 1;
		repaint();
	}
	
	if(e.getSource()==anim2)
	{
		oper = 2;
		repaint();
	}

	if(e.getSource()==anim3)
	{
		oper = 3;
		repaint();
	}

	if(e.getSource()==clear)
	{
		oper = 4;
		repaint();
	}

}

}