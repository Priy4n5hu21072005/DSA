package JavaRevisionAndPractice;

public class chapter3 {
    void m1(){
        System.out.println("hi");
    }
}
// Single inheritance
class c2 extends chapter3{
    void m2(){
        System.out.println("kaise hai aap");
    }
}
class Telling{
    public static void main(String[] args) {
        c2 obj = new c2();
        obj.m1();
        obj.m2();
    }
}
// Multiple Inheritence 
 interface batting {
    void bat();
}
 interface bowling {
void ball();
}
class Hardik implements batting , bowling{
    public void bat(){
        System.out.println("rohit is batting");
    }
    public void ball(){
        System.out.println("bowling");
    }
}
class cricket{
    public static void main(String[] args) {
        Hardik obj = new Hardik();
        obj.bat();
        obj.ball();
    }
}
