import java.util.Scanner;

class Program
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        sc.nextLine();
        if (sc.nextLine().equals("MPH"))
        {
            if (num == 0)
            {
                System.out.println("CALM");
            }
            if (bet(num, 1, 3))
            {
                System.out.println("LIGHT-AIR");
            }
            if (bet(num, 4, 7))
            {
                System.out.println("LIGHT-BREEZE");
            }
            if (bet(num, 8, 12))
            {
                System.out.println("GENTLE-BREEZE");
            }
            if (bet(num, 13, 18))
            {
                System.out.println("MODERATE-BREEZE");
            }
            if (bet(num, 19, 24))
            {
                System.out.println("FRESH-BREEZE");
            }
            if (bet(num, 25, 31))
            {
                System.out.println("STRONG-BREEZE");
            }
            if (bet(num, 32, 38))
            {
                System.out.println("NEAR-GALE");
            }
            if (bet(num, 39, 46))
            {
                System.out.println("GALE");
            }
            if (bet(num, 47, 54))
            {
                System.out.println("SEVERE-GALE");
            }
            if (bet(num, 55, 63))
            {
                System.out.println("STORM");
            }
            if (bet(num, 64, 72))
            {
                System.out.println("VIOLENT-STORM");
            }
            if (num >= 73)
            {
                System.out.println("CALM");
            }
        }
        else
        {
            if (num == 0)
            {
                System.out.println("CALM");
            }
            if (bet(num, 1, 3))
            {
                System.out.println("LIGHT-AIR");
            }
            if (bet(num, 4, 6))
            {
                System.out.println("LIGHT-BREEZE");
            }
            if (bet(num, 7, 10))
            {
                System.out.println("GENTLE-BREEZE");
            }
            if (bet(num, 11, 16))
            {
                System.out.println("MODERATE-BREEZE");
            }
            if (bet(num, 17, 21))
            {
                System.out.println("FRESH-BREEZE");
            }
            if (bet(num, 22, 27))
            {
                System.out.println("STRONG-BREEZE");
            }
            if (bet(num, 28, 33))
            {
                System.out.println("NEAR-GALE");
            }
            if (bet(num, 34, 40))
            {
                System.out.println("GALE");
            }
            if (bet(num, 41, 47))
            {
                System.out.println("SEVERE-GALE");
            }
            if (bet(num, 48, 55))
            {
                System.out.println("STORM");
            }
            if (bet(num, 56, 63))
            {
                System.out.println("VIOLENT-STORM");
            }
            if (num >= 64)
            {
                System.out.println("CALM");
            }
        }
        sc.close();
    }
    static Boolean bet(int number, int lower, int upper)
    {
        return number >= lower && number <= upper;
    }
}