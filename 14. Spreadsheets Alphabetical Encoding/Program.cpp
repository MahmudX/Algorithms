#include <iostream>
using namespace std;

char GetChar(int n)
{
    return (char)(64 + n);
}

string GetString(int n)
{
    string result = "";
    while (n > 26)
    {
        int temp = n / 26, rem = n % 26;
        if (rem == 0)
        {
            result += GetChar((n - 1) / 26);
            result += "Z";
        }
        else
            result += GetChar(temp);
        n = rem;
    }
    if (n != 0)
        result += GetChar(n);
    return result;
}

int main()
{
    for (int i = 1; i < 137; i++)
    {
        cout << GetString(i) << endl;
    }
}