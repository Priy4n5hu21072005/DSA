package JavaRevisionAndPractice;

public class chapter1 {
    int a ;
    int b;
    public chapter1(int x, int y){
        this.a=x;
        this.b=y;
    }
    public int Addition(){
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
