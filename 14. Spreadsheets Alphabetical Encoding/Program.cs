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
                s.Add(GetColumn(i));
            }
            Console.WriteLine(string.Join(", ", s));
        }
        static string GetColumn(int n)
{
    string result = "";

    while (n > 0)
    {
        int rem = (n - 1) % 26;
        result = char(rem + 'A') + result;
        n = (n - 1) / 26;
    }

    return result;
}
    }
}
