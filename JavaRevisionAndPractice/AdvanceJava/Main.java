// Comparable is used when we need to default sorting in a class
import java.util.*;
class Student implements Comparable<Student>
{
    int RollNo ;
    String name ;
    Student(int RollNo,String name){
        this.RollNo = RollNo;
        this.name=name ;
    }
    @Override
    public int compareTo(Student s){
        return this.RollNo-s.RollNo ;
    }
}
public class Main{
    public static void main(String[] args) {
        ArrayList <Student> list = new ArrayList<>();
        list.add(new Student(3, "Priyanshu"));
        list.add(new Student(5, "Ankit"));
        list.add(new Student(2, "P"));
        list.add(new Student(6, "Priya"));
        list.add(new Student(1, "Anshu"));
        Collections.sort(list);
        for(Student s : list){
            System.out.println(s.RollNo+" "+s.name);
        }
    }
}