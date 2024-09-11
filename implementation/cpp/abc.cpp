#include <iostream>
using namespace std;

#define TxtIO                                \
    freopen("../_test/test.in", "r", stdin); \
    freopen("../_test/test.out", "w", stdout);

int main()
{
    TxtIO int X, Y, M;
    cin >> X >> Y >> M;
    cout << X << Y << M << endl;
    return 0;
}
