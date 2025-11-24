import java.util.Scanner;

public class RandomNumber{
public static void main(String[] args){
 Scanner input = new Scanner(System.in);
 int fixed_value = 20;

 System.out.println("Enter a number: ");
  int input_number = input.nextInt();
  
 while(input_number != fixed_value){
  if(input_number > fixed_value){
  System.out.println("Too high");
  }else if(input_number < fixed_value){
  System.out.println("Too low");
 }else if(input_number == fixed_value){
  System.out.println("you are correct" + fixed_value + "is the correct number");
 }
 System.out.println("Enter a number: ");
   input_number = input.nextInt();
  }
  


}

}
