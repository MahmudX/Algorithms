#include <iostream>
using namespace std;

int main()
{
    double R;
    cin >> R;
    if (R < 0 || R > 100)
    {
        cout << "Fora de intervalo" << endl;
    }
    else if (R >= 0.00 && R <= 25.00)
    {
        cout << "Intervalo [0,25]" << endl;
    }
    else if (R > 25.00 && R <= 50.00)
    {
        cout << "Intervalo (25,50]" << endl;
    }
    else if (R > 50.00 && R <= 75.00)
    {
        cout << "Intervalo (50,75]" << endl;
    }
    else if (R > 75.00 && R <= 100.00)
    {
        cout << "Intervalo (75,100]" << endl;
    }
}