import java.util.Scanner;
import java.util.Random;

public class NumberGuessingGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        
        int randomNumber = random.nextInt(100) + 1;
        int maxAttempts = 10;
        int numberOfTries = 0;
        int guess = 0;
        
        System.out.println("Welcome to the Number Guessing Game!");
        System.out.println("Guess a number between 1 and 100.");
        System.out.println("You have " + maxAttempts + " attempts.");
        
        while (guess != randomNumber && numberOfTries < maxAttempts) {
            System.out.println("Enter your guess:");
            guess = scanner.nextInt();
            numberOfTries++;
            
            if (guess < randomNumber) {
                System.out.println("Too low!");
            } else if (guess > randomNumber) {
                System.out.println("Too high!");
            } else {
                System.out.println("Congratulations! You guessed the correct number.");
                System.out.println("It took you " + numberOfTries + " tries.");
                break;
            }
            
            if (numberOfTries == maxAttempts) {
                System.out.println("Sorry, you've reached the maximum number of attempts.");
                System.out.println("The correct number was " + randomNumber + ".");
            }
        }
        
        scanner.close();
    }
}
