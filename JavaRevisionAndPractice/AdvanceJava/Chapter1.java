package JavaRevisionAndPractice.AdvanceJava;
import java.util.*;
public class Chapter1 {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println("enter your first number");
        int a = sc.nextInt();
        System.out.println("next Number");
        int b = sc.nextInt();
        try{
            b=a/0;
        }
        catch(ArithmeticException e){
            System.out.println("dhang se daal number daal chutiye" +e);
        }
        catch(NullPointerException e){
            System.out.println("arrey kitni jaldi hai re tere ko");
        }
           b = a / b;
        System.out.println("the output=" +b);
        sc.close();
    }
}
