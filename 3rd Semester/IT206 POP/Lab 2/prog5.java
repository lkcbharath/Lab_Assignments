// multiple inheritance



interface Airplane {

    default void show(){
        System.out.println("Airplanes can move forward and backward easily, so I was called via interface.");
    }
}

interface Helicopter {

    default void show(){
        System.out.println("Helicopters can move up and down easily, so I was called via interface.");
    }
}


class VTOL implements Airplane,Helicopter{

    public void show(){
        Airplane.super.show();
        Helicopter.super.show();
        System.out.println("The advantage of VTOLs are that it can both act as an Airplane and as a Helicopter!!!");
    }
}

class prog5 {
    public static void main(String args[]){
        VTOL Hydra = new VTOL();
        Hydra.show();
    }
}
