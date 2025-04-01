namespace Siena //4 minutes
{
    public class Program
    {
        public static void Main()
        {
            int number = Convert.ToInt32(Console.ReadLine() ?? "");
            for (int i = 0; i < number; i++)
            {
                if (Math.Pow(2, i) > number)
                {
                    break;
                }
                Console.WriteLine(Math.Pow(2, i));
            }
        }
    }
}