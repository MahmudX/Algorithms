#include <iostream>
using namespace std;

string GetColumn(int n)
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

int main()
{
    for (int i = 1; i < 1000; i++)
    {
        cout << GetColumn(i) << ", ";
    }
}
