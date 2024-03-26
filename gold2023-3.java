import java.util.Scanner;

class Program
{
    static int[] dice = new int[5];
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 5; i++)
        {
            dice[i] = sc.nextInt();
        }
        sc.close();
        int max = 0, roll = 0;
        for (int r = 1; r < 7; r++) //1 - 6
        {
            int matches = 0;
            for (int i = 0; i < 5; i++) //iterate array
            {
                if (dice[i] == r)
                {
                    matches++;
                }
            }
            if (matches > max)
            {
                max = matches;
                roll = r;
            }
        }
        if (max == 5) //all match
        {
            System.out.println(1000 + dice[0] * 5);
            return;
        }
        if (max == 4) //4 match
        {
            System.out.println(600 + roll * 4);
            return;
        }
        if (max == 3) //3 match
        {
            int subMax = 0;
            for (int r = 1; r < 7; r++) //1 - 6
            {
                if (r == roll)
                {
                    continue;
                }
                int matches = 0;
                for (int i = 0; i < 5; i++) //iterate array
                {
                    if (dice[i] == r)
                    {
                        matches++;
                    }
                }
                if (matches > subMax)
                {
                    subMax = matches;
                }
            }
            if (subMax == 2) //3 match and 2 match
            {
                System.out.println(400 + dice[0] + dice[1] + dice[2] + dice[3] + dice[4]);
                return;
            }
            System.out.println(300 + roll * 3); //3 match only
            return;
        }
        if (max == 2) //2 match
        {
            int subMax = 0, subRoll = 0;
            for (int r = 1; r < 7; r++) //1 - 6
            {
                if (r == roll)
                {
                    continue;
                }
                int matches = 0;
                for (int i = 0; i < 5; i++) //iterate array
                {
                    if (dice[i] == r)
                    {
                        matches++;
                    }
                }
                if (matches > subMax)
                {
                    subMax = matches;
                    subRoll = r;
                }
            }
            if (subMax == 2) //2 match and 2 match
            {
                System.out.println(200 + roll * 2 + subRoll * 2);
                return;
            }
            System.out.println(100 + roll * 2); //2 match
            return;
        }
        if ((Contains(1) && Contains(2) && Contains(3) && Contains(4) && Contains(5)) || (Contains(2) && Contains(3) && Contains(4) && Contains(5) && Contains(6))) //straight
        {
            System.out.println(500 + dice[0] + dice[1] + dice[2] + dice[3] + dice[4]);
            return;
        }
        System.out.println(dice[0] + dice[1] + dice[2] + dice[3] + dice[4]); //nothing
    }

    static Boolean Contains(int n)
    {
        for (int i = 0; i < 6; i++)
        {
            if (dice[i] == n)
            {
                return true;
            }
        }
        return false;
    }
}