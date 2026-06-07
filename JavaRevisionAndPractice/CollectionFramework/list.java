package JavaRevisionAndPractice.CollectionFramework;

import java.util.*;

public class list {
    public static void main(String[] args) {

        List<String> names = Arrays.asList("Ankit", "Rohan");

        Iterator<String> it = names.iterator();

        while (it.hasNext()) {
            System.out.println(it.next());
        }
        // ArrayList
        ArrayList <String> l1=new ArrayList<>();
        l1.add("ankit");
        l1.add("ravi");
        System.out.println(l1);
        l1.remove(1);
    }
}
