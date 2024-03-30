import java.util.Scanner;

class Program
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        String attack = sc.nextLine();
        String defend = sc.nextLine();
        int d;
        int a;
        switch (defend)
        {
            case "MARSHAL":
                d = 9;
                break;
            case "GENERAL":
                d = 8;
                break;
            case "COLONEL":
                d = 7;
                break;
            case "CAPTAIN":
                d = 6;
                break;
            case "LIEUTENANT":
                d = 5;
                break;
            case "SERGEANT":
                d = 4;
                break;
            case "MINER":
                d = 3;
                break;
            case "SCOUT":
                d = 2;
                break;
            case "SPY":
                d = 1;
                break;
            default:
                d = 0;
                break;
        }
        switch (attack)
        {
            case "MARSHAL":
                a = 9;
                break;
            case "GENERAL":
                a = 8;
                break;
            case "COLONEL":
                a = 7;
                break;
            case "CAPTAIN":
                a = 6;
                break;
            case "LIEUTENANT":
                a = 5;
                break;
            case "SERGEANT":
                a = 4;
                break;
            case "MINER":
                a = 3;
                break;
            case "SCOUT":
                a = 2;
                break;
            case "SPY":
                a = 1;
                break;
            default:
                a = 0;
                break;
        }
        switch (defend)
        {
            case "FLAG":
                System.out.println("FLAG REMOVED");
                break;
            case "BOMB":
                if (attack.equals("MINER"))
                {
                    System.out.println("BOMB REMOVED");
                }
                else
                {
                    System.out.println(attack + " REMOVED");
                }
                break;
            case "MARSHAL":
                switch (attack)
                {
                    case "SPY":
                        System.out.println("MARSHAL REMOVED");
                        break;
                    case "MARSHAL":
                        System.out.println("BOTH REMOVED");
                        break;
                    default:
                        System.out.println(attack + " REMOVED");
                        break;
                }
                break;
            default:
                if (d > a)
                {
                    System.out.println(attack + " REMOVED");
                }
                if (a == d)
                {
                    System.out.println("BOTH REMOVED");
                }
                if (a > d)
                {
                    System.out.println(defend + " REMOVED");
                }
                break;
        }
    }
}