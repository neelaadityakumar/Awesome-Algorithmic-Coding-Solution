#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

int n, m;
vector<int> a;
int memo[101][100001]{};


int dp(int i, int prev) {
    if (memo[prev][i] != 0) return memo[prev][i];
    if (i == n) return 1;
    if (a[i] != 0 && abs(prev - a[i]) > 1) return 0;
    if (a[i] != 0) return dp(i + 1, a[i]);

    int count = 0;
    for (int k = prev - 1; k <= prev + 1; k++) {
        if (k >= 1 && k <= m) {
            count += dp(i + 1, k);
            if (count >= MOD) count -= MOD;
        }
    }
    return memo[prev][i] = count;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n >> m;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int ans = 0;
    if (a[0] == 0) {
        for (int i = 1; i <= m; i++) {
            ans += dp(1, i);
            if (ans > MOD) ans -= MOD;
        }
    } else {
        ans = dp(1, a[0]);
    }
    cout << ans;

    return 0;
}

