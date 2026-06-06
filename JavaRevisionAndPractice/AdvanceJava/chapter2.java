package JavaRevisionAndPractice.AdvanceJava;

public class chapter2 {
    // final block 
    public static void main(String[] args) {
        try{
            int a[]=new int[7];
            System.out.println(a[8]);
        }
        catch(ArrayIndexOutOfBoundsException e){
            System.out.println(e);
        }
        finally{
            int a[] = new int[7];
            a[2]=7;
            System.out.println(a[2]);
        }
    }
    
}
