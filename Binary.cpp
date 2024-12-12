#include <iostream>
#include <math.h> 

using namespace std;

int main() {
    int n;
    cout << "Enter your number: ";
    cin >> n;

    int ans = 0;
    for (int i = 0; n != 0; i++) {
        int bit = n & 1;
        ans = (bit * pow(10, i)) + ans;
        n >>= 1;
    }

    cout << "Binary representation: " << ans << endl;

    return 0;
}
