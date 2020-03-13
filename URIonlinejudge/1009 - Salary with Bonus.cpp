#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    string s;
    float a, b;
    cin >> s;
    cin >> a;
    cin >> b;
    cout << "TOTAL = R$ "
         << fixed
         << setprecision(2)
         << (a + (b * 15 / 100))
         << endl;
}