import java.util.Scanner;

public class Password{
 public static void main(String[] args){
 Scanner input = new Scanner(System.in);
 
System.out.println("Enter password");
String  userInput = input.nextLine();

if(userInput.length() <= 10 && userInput.length() > 6){
System.out.print("Medium");
}else if(userInput.length() < 6){
System.out.println("weak");
}else if(userInput.length() > 10){
System.out.println("Strong");
}else if(userInput.length() < 1)
System.out.println("This code is invalid");
}
}














