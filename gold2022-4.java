import java.util.Scanner;

class Program
{
    public static void main(String[] args)
    {
        /*Scanner sc = new Scanner(System.in);
        //String target = sc.nextLine();
        String target = "SCOUT";
        int num = 3;
        //int num = sc.nextInt();
        String[] guesses = new String[num];
        System.out.println(num);
        for (int i = 0; i < num; i++)
        {
            guesses[i] = sc.nextLine();
        }
        sc.close();
        for (int i = 0; i < num; i++) //iterate over all guesses
        {
            if (guesses[i].equals(target)) //guess equals target
            {
                System.out.println("GGGGG");
                continue;
            }
            for (int j = 0; j < 5; j++) //iterate over chars in guess
            {
                if (guesses[i].charAt(j) == target.charAt(j)) //char is in right position
                {
                    System.out.print("G");
                    continue;
                }
                else if (target.indexOf(guesses[i].charAt(j)) != -1) //char is contained in target
                {
                    
                }
            }
        }*/
        Scanner sc = new Scanner(System.in);
        String target = sc.nextLine();
        while (guess.Length > 5)
        {
            Console.CursorTop = cursorTopText;
            Console.Write($"Guess: {new string(' ', guess.Length)}");
            Console.CursorLeft -= guess.Length;
            guess = Console.ReadLine() ?? "";
        }
        Console.CursorTop = cursorTop + i;
        if (guess == target)
        {
            correct = true;
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine($"  {guess[0]}    {guess[1]}    {guess[2]}    {guess[3]}    {guess[4]}");
            Console.ForegroundColor = ConsoleColor.Gray;
            Console.WriteLine($"You've guessed the word in {i + 1} {(i == 0 ? "try" : "tries")}!");
            return;
        }
        bool[] filled = new bool[5];
        for (int j = 0; j < 5; j++)
        {
            bool output = false;
            if (guess[j] == target[j])
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.Write($"  {guess[j]}  ");
                Console.ForegroundColor = ConsoleColor.Gray;
                filled[j] = true;
                continue;
            }
            for (int k = 0; k < 5; k++)
            {
                if (filled[k])
                {
                    continue;
                }
                if (target[k] == guess[j])
                {
                    if (target[k] == guess[k])
                    {
                        continue;
                    }
                    Console.ForegroundColor = ConsoleColor.Yellow;
                    Console.Write($"  {guess[j]}  ");
                    Console.ForegroundColor = ConsoleColor.Gray;
                    filled[k] = true;
                    output = true;
                    break;
                }
            }
            if (!output)
            {
                Console.Write("  #  ");
            }
        }
        Console.WriteLine();
    }
}