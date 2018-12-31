import java.io.*;
import java.math.*;
import java.lang.*;
import java.util.*;



abstract class AbstractFactory {
   abstract Car getCar(String cartype);
   abstract Bike getBike(String biketype);
}





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

class CarFactory extends AbstractFactory {
	public Car getCar(String cartype) {
		// if (cartype == null)
		// 	return null;

		if(cartype.equalsIgnoreCase("Ferrari"))
         	return new Ferrari();

        else if(cartype.equalsIgnoreCase("Bugatti"))
         	return new Bugatti();

        else if(cartype.equalsIgnoreCase("Lamborghini"))
         	return new Lamborghini();

        return null;
	}
	@Override
	Bike getBike(String biketype) {
		return null;
	}
}




interface Bike {
	void drive();
}

class BMW implements Bike {
	@Override
	public void drive() {
		System.out.println("BMW S 1000 RR is now driving.");
	}
}

class Ducati implements Bike {
	@Override
	public void drive() {
		System.out.println("Ducati SuperSport is now driving.");
	}
}

class Kawasaki implements Bike {
	@Override
	public void drive() {
		System.out.println("Kawasaki Ninja is now driving.");
	}
}

class BikeFactory extends AbstractFactory {
	public Bike getBike(String biketype) {
		// if (biketype == null)
		// 	return null;

		if(biketype.equalsIgnoreCase("BMW"))
         	return new BMW();

        else if(biketype.equalsIgnoreCase("Ducati"))
         	return new Ducati();

        else if(biketype.equalsIgnoreCase("Kawasaki"))
         	return new Kawasaki();

        return null;
	}
	@Override
	Car getCar(String cartype) {
		return null;
	}
}










class FactoryProducer {
   public static AbstractFactory getFactory(String choice){
   
      if(choice.equalsIgnoreCase("Car")){
         return new CarFactory();   
      }
      else if(choice.equalsIgnoreCase("Bike")){
         return new BikeFactory();
      }
      
      return null;
   }
}







class prog2 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Which car or bike brand would you like to try out?");
		String str = scan.next();
		String str2 = scan.next();

		AbstractFactory factory = FactoryProducer.getFactory("Car");

		Car car = factory.getCar(str);

		AbstractFactory factory2 = FactoryProducer.getFactory("Bike");

		Bike bike = factory2.getBike(str2);

		

		car.drive();
		bike.drive();

	}
}