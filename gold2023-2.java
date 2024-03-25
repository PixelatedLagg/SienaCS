import java.util.Scanner;

class Program
{
    static int Calc(int i)
    {
        int steps = 0;
        while (i != 1)
        {
            if (i % 2 == 0)
            {
                i /= 2;
            }
            else
            {
                i = 3 * i + 1;
            }
            steps++;
        }
        return steps;
    }

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int lower = Integer.parseInt(sc.nextLine());
        int upper = Integer.parseInt(sc.nextLine());
        int steps = Integer.parseInt(sc.nextLine());
        for (int i = lower; i <= upper; i++)
        {
            if (Calc(i) == steps)
            {
                System.out.print(i);
            }
        }
        sc.close();
    }
}