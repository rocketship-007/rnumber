using System;
namespace numberGussingGame;

class Program
{
    static int Askforrandom()
        {
            Console.WriteLine("Enter a number from 1-100:");
            string usernumber = Console.ReadLine(); 
            int yournum = Convert.ToInt32(usernumber);
            return yournum;
        }
    static void Main()
        {
        Console.WriteLine("Welcome to the guess the number game!");
        Random rand = new();
        int mynumber = rand.Next(1,100);
        int usersumber = Askforrandom();
        int tries = 0;
        while (usersumber != mynumber)
        {
        tries++;
        if (mynumber<usersumber)
        {
            Console.WriteLine("Its less than the random number");
            usersumber = Askforrandom();
        }
        else if (mynumber>usersumber)
        {
            Console.WriteLine("Its grater than the random number");
            usersumber = Askforrandom();
        }
       }
        Console.WriteLine($"YAY! You're correct! It took you {tries+1} tries!");
    }
}
