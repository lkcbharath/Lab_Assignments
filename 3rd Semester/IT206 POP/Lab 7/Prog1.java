import java.awt.*;
import javax.swing.*;
import java.applet.*;
import java.awt.event.*;
import java.io.*;
import java.math.*;
import java.lang.*;
import java.util.*;

public class Prog1 extends Applet implements ActionListener
{
int oper = 4;

// add threads with runnable

Button circle,square,rectangle,clear;
ShapeFactory shapeFactory = new ShapeFactory();
Shape shape;

public void init()
{
circle=new Button("Circle");
add(circle);
circle.addActionListener(this);

square=new Button("Square");
add(square);
square.addActionListener(this);

rectangle=new Button("Rectangle");
add(rectangle);
rectangle.addActionListener(this);

clear=new Button("Clear");
add(clear);
clear.addActionListener(this);

}


public void paint(Graphics g)
{
	Dimension d = getSize();
	//oper is for operation
	if (oper==1) {
		g.drawArc(0, 0, d.width, d.height,0,360);
	}
	if (oper==2) {
		g.drawRect(20,20, 100, 100);
	}
	if (oper==3) {
		g.drawRect(20,20,100,300);
	}
	if (oper==4) {
		g.clearRect(0, 0, d.width, d.height);
	}

}


public void actionPerformed(ActionEvent e)
{
	if(e.getSource()==clear)
	{
		oper = 4;
		repaint();
	}
	else{

	if(e.getSource()==circle)
		shape = shapeFactory.getShape("Circle");
	if(e.getSource()==square)
		shape = shapeFactory.getShape("Square");
	if(e.getSource()==rectangle)
		shape = shapeFactory.getShape("Rectangle");

	oper = shape.draw();
	repaint();
	}

}
}

interface Shape {
	int draw();
}

class Circle extends Prog1 implements Shape {
	
	@Override
	public int draw() {
		System.out.println("Circle 450 Italia is now driving.");
		return 1;
	}
}

class Square extends Prog1 implements Shape {
	

	@Override
	public int draw() {
		System.out.println("Square Veyron is now driving.");
		return 2;
	}
}

class Rectangle extends Prog1 implements Shape {
	
	@Override
	public int draw() {
		System.out.println("Rectangle Huracan is now driving.");
		return 3;
	}
}

class ShapeFactory {
	public Shape getShape(String cartype) {
		if (cartype == null)
			return null;

		if(cartype.equalsIgnoreCase("Circle"))
         	return new Circle();

        else if(cartype.equalsIgnoreCase("Square"))
         	return new Square();

        else if(cartype.equalsIgnoreCase("Rectangle"))
         	return new Rectangle();

        return null;
	}
}

