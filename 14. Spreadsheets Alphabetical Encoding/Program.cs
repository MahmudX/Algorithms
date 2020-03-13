using System;
using System.Collections.Generic;
namespace Spreadsheets_Alphabetical_Encoding
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> s = new List<string>();
            for (int i = 1; i < 137; i++)
            {
                s.Add(GetString(i));
            }
            Console.WriteLine(string.Join(", ", s));
        }
        static string GetString(int n)
        {
            string result = "";
            while (n > 26)
            {
                int temp = n / 26, rem = n % 26;
                if (rem == 0)
                    result += GetChar((n - 1) / 26) + "Z";
                else
                    result += GetChar(temp);
                n = rem;
            }
            if (n != 0)
                result += GetChar(n);
            return result;
        }
        static char GetChar(int n)
        {
            return (char)(64 + n);
        }
    }
}
