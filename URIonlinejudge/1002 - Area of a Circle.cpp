#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    double n = 3.14159;
    double R;
    cin >> R;
    cout << "A="
         << fixed
         << setprecision(4)
         << n * R * R
         << endl;
}