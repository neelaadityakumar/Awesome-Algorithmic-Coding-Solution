#include <bits/stdc++.h>
using namespace std;

#define ll long long

void numberSpiral(ll y, ll x) {
    ll ans = 0;
    if (y > x) {
        ans = (y - 1) * (y - 1);
        if (y % 2 == 1) {
            ans += x;
        } else {
            ans += 2 * y - x;
        }
    } else {
        ans = (x - 1) * (x - 1);
        if (x % 2 == 0) {
            ans += y;
        } else {
            ans += 2 * x - y;
        }
    }
    cout << ans << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;
    while (t--) {
        ll y, x;
        cin >> y >> x;
        numberSpiral(y, x);
    }

    return 0;
}
