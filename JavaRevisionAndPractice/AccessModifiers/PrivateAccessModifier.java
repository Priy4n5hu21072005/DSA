package JavaRevisionAndPractice.AccessModifiers;

class Person {
    public int Aukat;
    public void setAukat(int Aukat){
        this.Aukat=Aukat;
    }     
    public int getAukat(){return Aukat;}
}
public class PrivateAccessModifier{
    public static void main(String[] args){
    Person p = new Person();
    p.setAukat(100000);
    System.out.println(p.getAukat());
}
}