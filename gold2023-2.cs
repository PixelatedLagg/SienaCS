namespace Siena //6 minutes
{
    public class Program
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
        public static void Main()
        {
            int lower = Convert.ToInt32(Console.ReadLine() ?? "");
            int upper = Convert.ToInt32(Console.ReadLine() ?? "");
            int steps = Convert.ToInt32(Console.ReadLine() ?? "");
            for (int i = lower; i <= upper; i++)
            {
                if (Calc(i) == steps)
                {
                    Console.WriteLine(i);
                }
            }
        }
    }
}