#include <iostream>
using namespace std;
int GetPisanoPeriod(int m)
{
    int a = 0;
    int b = 1;
    int c = a + b;
    for (int i = 0; i < m * m; i++)
    {
        c = (a + b) % m;
        cout << "c: " << c << endl;
        a = b;
        b = c;
        cout << "a: " << a << endl
             << "b: " << b << endl
             << endl;
        if (a == 0 && b == 1)
            return i + 1;
    }
    return 0;
}
int main()
{
    cout << GetPisanoPeriod(3) << endl;
}