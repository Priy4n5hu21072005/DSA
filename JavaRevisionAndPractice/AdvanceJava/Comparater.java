import java.util.*;

class Student {
    int RollNo;
    String name;

    Student(int RollNo, String name) {
        this.RollNo = RollNo;
        this.name = name;
    }
}
class NameOperator implements Comparator<Student>{
    public int compare(Student s1 , Student s2){
        return s1.name.compareTo(s2.name);
    }
}
public class Comparater{
    public static void main(String[] args){
        ArrayList<Student> list = new ArrayList<>();
        list.add(new Student(2, "Priyanshu"));
        list.add(new Student(3, "Ankit"));
        list.add(new Student(1, "Rohit"));
        list.add(new Student(5, "Ansh"));
        list.add(new Student(4, "Priya"));
        Collections.sort(list,new NameOperator());
        for(Student s : list){
            System.out.println(s.RollNo+" "+s.name);
        }
    }
}