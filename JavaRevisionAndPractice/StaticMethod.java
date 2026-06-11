// Static Method means vo method jo kisi bhi object se belong nahi karta hai and koi bhi new instance create nahi karta hai 
package JavaRevisionAndPractice;
class StaticMethod{
    public static void Namste(){
        System.out.println("Namaste sabhi! Namste sabhi");
    }
    public static void main(String[] args) {
        StaticMethod.Namste();
    }
}
