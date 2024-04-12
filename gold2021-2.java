import java.util.Scanner;

class Program
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int speed1 = sc.nextInt();
        int position1 = sc.nextInt();
        int speed2 = sc.nextInt();
        int position2 = sc.nextInt();
        int speed3 = sc.nextInt();
        int position3 = sc.nextInt();
        sc.close();
        double time1 = (100 - position1) / speed1;
        double time2 = (100 - position2) / speed2;
        double time3 = (100 - position3) / speed3;
        int[] place = new int[3];
        if (time1 == time2 && time2 == time3) //all equal
        {
            if (position1 == position2 && position2 == position3 || (position1 < position2 && position2 < position3))
            {
                place[0] = 1;
                place[1] = 2;
                place[2] = 3;
                //DONE
            }
            if (position1 < position3 && position3 < position2)
            {
                place[0] = 1;
                place[1] = 3;
                place[2] = 2;
                //DONE
            }
            if (position2 < position1 && position1 < position3)
            {
                place[0] = 2;
                place[1] = 1;
                place[2] = 3;
                //DONE
            }
            if (position2 < position3 && position3 < position1)
            {
                place[0] = 2;
                place[1] = 3;
                place[2] = 1;
                //DONE
            }
            if (position3 < position1 && position1 < position2)
            {
                place[0] = 3;
                place[1] = 1;
                place[2] = 2;
                //DONE
            }
            if (position3 < position2 && position2 < position1)
            {
                place[0] = 3;
                place[1] = 2;
                place[2] = 1;
                //DONE
            }
        }
        else if (time1 == time2 && time3 > time2)
        {
            place[2] = 1;
            if (position1 < position2 || position1 == position2)
            {
                place[0] = 1;
                place[1] = 2;
                //DONE
            }
            if (position1 > position2)
            {
                place[0] = 2;
                place[1] = 1;
                //DONE
            }
        }
        else if (time1 == time3 && time2 > time1)
        {
            place[2] = 2;
            if (position1 < position3 || position1 == position3)
            {
                place[0] = 1;
                place[1] = 3;
                //DONE
            }
            if (position1 > position3)
            {
                place[0] = 3;
                place[1] = 1;
                //DONE
            }
        }
        else if (time2 == time3 && time1 > time2)
        {
            place[2] = 2;
            if (position1 < position3 || position1 == position3)
            {
                place[0] = 1;
                place[1] = 3;
                //DONE
            }
            if (position1 > position3)
            {
                place[0] = 3;
                place[1] = 1;
                //DONE
            }
        }
        if (time1 == time2)
        {
            if (time3 < time1)
            {
                place[0] = 3;
            }
            else
            {
                place[2] = 3;
            }
            if (position1 < position2 || position1 == position2)
            {
                place[0] = 1;
                place[1] = 2;
            }
            if (position1 > position2)
            {
                place[0] = 2;
                place[1] = 1;
            }
        }
    }
}