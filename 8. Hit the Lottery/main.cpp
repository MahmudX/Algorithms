#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int notes = 0;
    if (n >= 100)
    {
        notes += n / 100;
        n = n % 100;
    }
    if (n >= 20)
    {
        notes += n / 20;
        n = n % 20;
    }

    if (n >= 10)
    {
        notes += n / 10;
        n = n % 10;
    }

    if (n >= 5)
    {
        notes += n / 5;
        n = n % 5;
    }

    if (n >= 1)
    {
        notes += n;
    }
    cout << notes << endl;
}