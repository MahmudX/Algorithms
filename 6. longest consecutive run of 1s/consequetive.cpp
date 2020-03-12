#include <iostream>
#include <bitset>
using namespace std;
int main(){
    int decNumber = 156;
    // Decimal to binary
    string binary = bitset<8>(decNumber).to_string();
    int ones, temp = 0; // var ones is the required answer
    for (int i = 0; i < binary.length(); i++){
        if (binary[i] == '1') temp++;
        else{
            if (temp > ones){
                ones = temp; temp = 0;
            }
        }
    }
    cout << ones;
}
