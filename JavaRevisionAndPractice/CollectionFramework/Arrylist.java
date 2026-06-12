import java.util.ArrayList;
class Arraylist{
    public static void main(String[] args){
        ArrayList <Integer> al = new ArrayList<>();
        al.add(12);
        al.add(13);
        al.add(14);
        System.out.println("The Array after adding value" +al);
        al.add(2,15);
        System.out.println("after adding the specific value:"+al);
        al.set(2, 16);
        System.out.println("update the value" +al);
    }
}