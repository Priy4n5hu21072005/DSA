package JavaRevisionAndPractice.OOPSconcepts;
//Encapsulation
public class chapter2 {
    public class MBA{
        void study(){
            System.out.println("learning MBA");
        }
    }
    // Overriding
    class Financial extends MBA{
        void study(){
            System.out.println("good!");
            
        }
    }
    public static void main(String[] args) {
        chapter2 outer =new chapter2();
        MBA obj = outer.new Financial();
        obj.study();
    }
}
