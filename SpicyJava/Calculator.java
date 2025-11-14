import java.util.Scanner;

public class Calculator{
public static void main(String[] args){
 Scanner input = new Scanner(System.in);

 System.out.println("Enter Operation");
 
int firstNumber = input.nextInt();

String operators = input.next();

int secondNumber = input.nextInt();

if(operators.equals("+")){
int add = firstNumber + secondNumber;
System.out.println("This is addition: " + add);
}else if(operators.equals("-")){
int difference = firstNumber - secondNumber;
System.out.println("This is Subtraction" + difference);
}else if(operators.equals("*")){
int multiplication = firstNumber * secondNumber;
System.out.println("This is multiplication" + multiplication);
}else if(operators.equals("/")){
int division = firstNumber / secondNumber;
System.out.println("This is division " + division);
}

}
}
