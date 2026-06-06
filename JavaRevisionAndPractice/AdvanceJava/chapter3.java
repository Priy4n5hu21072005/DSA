package JavaRevisionAndPractice.AdvanceJava;
import java.util.*;
public class chapter3 {
    // Throw and Throws 
        void sqare(int a){
            if (a<1){
                throw new ArithmeticException("Enter greater number");
            }
            else{
                System.out.println("square value is"+a+"is ="+(a*a));
            }
        }
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            int a = sc.nextInt();
            chapter3 obj = new chapter3();
            obj.sqare(a);
        }
}
