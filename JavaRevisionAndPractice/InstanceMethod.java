package JavaRevisionAndPractice;

// Instance Method means vo method jo object oriented hota hai aur kisi object ke liye bnya jata hai aur data pass karta hai 
class Instance{
    String n = "";
    public void Instance(String n){
        this.n=n;
    }
}
class Main{
    public static void main(String[] args){
        Instance obj = new Instance();
        obj.Instance("Aap ki Aise Taise");
        System.out.println(obj.n);
    }
}