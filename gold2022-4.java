import java.util.Scanner;

class Program
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        String target = sc.nextLine();
        int num = sc.nextInt();
        String[] guesses = new String[num];
        for (int i = num - 1; i >= 0; i--)
        {
            guesses[i] = sc.nextLine();
        }
        sc.close();
        for (int i = 0; i < num; i++)
        {
            if (guesses[i] == target)
            {
                System.out.println("GGGGG");
                return;
            }
            Boolean[] filled = new Boolean[5];
            for (int j = 0; j < 5; j++)
            {
                Boolean output = false;
                if (guesses[i].charAt(j) == target.charAt(j))
                {
                    System.out.print("G");
                    filled[j] = true;
                    continue;
                }
                for (int k = 0; k < 5; k++)
                {
                    if (filled[k])
                    {
                        continue;
                    }
                    if (target.charAt(k) == guesses[i].charAt(j))
                    {
                        if (target.charAt(k) == guesses[i].charAt(j))
                        {
                            continue;
                        }
                        System.out.print("Y");
                        filled[k] = true;
                        output = true;
                        break;
                    }
                }
                if (!output)
                {
                    System.out.print("D");
                }
            }
            System.out.println();
        }
    }
}