import java.util.Scanner;

public class FatherAndSon{
public static void main(String[] args){
 Scanner input = new Scanner(System.in);

 System.out.println("Enter Father Age");
 int fatherAge = input.nextInt();
 
 System.out.println("Enter Son Age");
 int sonAge = input.nextInt();


 int twiceAge = (2 * sonAge) - fatherAge;

if((fatherAge >= 80 || fatherSon < 1) && (sonAge >= 80 || sonAge < 1)){
System.out.println("You are out of range");
}else{
System.out.println("The father is twice older than the son in " +  twiceAge + " years");
}

}
}
