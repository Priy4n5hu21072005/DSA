package JavaRevisionAndPractice;
// Method Overloading 
public class chapter1 {
    int a ;
    int b;
    int c;
    // Static Variable 
    String name ="Priyanshu Learning";
    public chapter1(int x, int y){
        this.a=x;
        this.b=y;
    }
    // Parametrized Constructor
    public chapter1(int x , int y , int z){
        this.a=x;
        this.b=y;
        this.c=z;
    }
    public int Addition(){
        System.out.println(name);
        return a+b;
    }
    public int Subtraction(){
        return a-b;
    }
    public static void main(String[] args) {
        chapter1 obj = new chapter1(36,3);
        System.out.println(obj.Addition());
        System.out.println(obj.Subtraction());
    }
}
