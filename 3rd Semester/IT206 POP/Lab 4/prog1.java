import java.io.*;
import java.math.*;
import java.lang.*;
import java.util.*;

interface Car {
	void drive();
}

class Ferrari implements Car {
	@Override
	public void drive() {
		System.out.println("Ferrari 450 Italia is now driving.");
	}
}

class Bugatti implements Car {
	@Override
	public void drive() {
		System.out.println("Bugatti Veyron is now driving.");
	}
}

class Lamborghini implements Car {
	@Override
	public void drive() {
		System.out.println("Lamborghini Huracan is now driving.");
	}
}

class VWFactory {
	public Car getCar(String cartype) {
		if (cartype == null)
			return null;

		if(cartype.equalsIgnoreCase("Ferrari"))
         	return new Ferrari();

        else if(cartype.equalsIgnoreCase("Bugatti"))
         	return new Bugatti();

        else if(cartype.equalsIgnoreCase("Lamborghini"))
         	return new Lamborghini();

        return null;
	}
}

class prog1 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Which car brand would you like to try out?");
		String str = scan.next();
		VWFactory belgium = new VWFactory();
		Car veyron = belgium.getCar(str);

		veyron.drive();

	}
}