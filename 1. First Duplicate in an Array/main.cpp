#include <math.h>
#include <vector>
#include <iostream>
using namespace std;

int firstDuplicate(vector<int> intArr)
{
    for (int i = 0; i < sizeof(intArr); i++)
    {
        int index = abs(intArr[i]) - 1;
        if (intArr[index] < 0)
            return abs(intArr[i]);
        intArr[index] *= -1;
    }
    return -1;
}

int main()
{
    vector<int> intArr = {8, 8, 6, 2, 6, 4, 7, 9, 5, 8};
    cout << firstDuplicate(intArr);
    return 0;
}