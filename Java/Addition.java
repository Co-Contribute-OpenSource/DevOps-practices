import java.util.Scanner;
public class Addition
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        // for addition of two numbers we need to have two nuumbers A adn B
        int a  = sc.nextInt();
        int b = sc.nextInt();
        int sum = a+b;
        System.out.println(sum);
    }
}