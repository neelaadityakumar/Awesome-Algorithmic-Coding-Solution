#include <bits/stdc++.h>
using namespace std;
#define int long long

const int MOD = 1e9 + 7;

// Fast modular exponentiation
int modPow(int base, int exp, int mod) {
    if (base == 0 && exp == 0) return 1; // 0^0 = 1 as per problem statement

    int result = 1;
    base %= mod;

    while (exp > 0) {
        if (exp & 1) result = (result * base) % mod;
        base = (base * base) % mod;
        exp >>= 1;
    }

    return result;
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;
    while (t--) {
        int a, b, c;
        cin >> a >> b >>c;
        cout << modPow(a, modPow(b, c, MOD-1),MOD) << "\n";
    }

    return 0;
}
