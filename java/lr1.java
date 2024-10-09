import java.util.Scanner;

public class lr1 
{

    public static void main (String args[]){

        Scanner scanner = new Scanner(System.in);

        int number = scanner.nextInt();
        boolean n_three = (number %3 ==0);
        boolean n_five = (number %5 ==0);
        boolean n_seven = (number %7 ==0); 
        
        if (n_three) {
            System.out.println("Число делится на 3");
        }

        else if (n_five) {
            System.out.println("Число делится на 5");
        }
        
        else if (n_seven) {
            System.out.println("Число делится на 7");
        }
        else {
            System.out.println("Число не делится на 3,5,7");
        }
        
        scanner.close();
    }
}

