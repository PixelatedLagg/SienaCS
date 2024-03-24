import java.util.Scanner;
import java.lang.Math;

class Program
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        sc.close();
        for (int i = 0; i < number; i++)
        {
            if (Math.pow(2, i) > number)
            {
                break;
            }
            System.out.println(Math.pow(2, i));
        }
    }
}