using System;
using System.Linq;

namespace Siena //27 minutes
{
    public class Program
    {
        public static void Main()
        {
            int[] dice = new int[5];
            for (int i = 0; i < 5; i++)
            {
                dice[i] = Convert.ToInt32(Console.ReadLine() ?? "");
            }
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
                Console.WriteLine(1000 + dice[0] * 5);
                return;
            }
            if (max == 4) //4 match
            {
                Console.WriteLine(600 + roll * 4);
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
                    Console.WriteLine(400 + dice[0] + dice[1] + dice[2] + dice[3] + dice[4]);
                    return;
                }
                Console.WriteLine(300 + roll * 3); //3 match only
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
                    Console.WriteLine(200 + roll * 2 + subRoll * 2);
                    return;
                }
                Console.WriteLine(100 + roll * 2); //2 match
                return;
            }
            if ((dice.Contains(1) && dice.Contains(2) && dice.Contains(3) && dice.Contains(4) && dice.Contains(5)) || (dice.Contains(2) && dice.Contains(3) && dice.Contains(4) && dice.Contains(5) && dice.Contains(6))) //straight
            {
                Console.WriteLine(500 + dice[0] + dice[1] + dice[2] + dice[3] + dice[4]);
                return;
            }
            Console.WriteLine(dice[0] + dice[1] + dice[2] + dice[3] + dice[4]); //nothing
        }
    }
}