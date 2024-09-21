#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int mod = 998244353;
const int maxn = 5e5 + 5;

ll dp[maxn + 5];

int main()
{
    int n, m;
    cin >> n >> m;

    vector<int> L(m), R(m);
    for (int i = 0; i < m; i++)
        cin >> L[i] >> R[i];

    dp[1] = 1;
    for (int i = 1; i <= n; i++)
    {
        if (i > 2)
            dp[i] = (dp[i] + dp[i - 1]) % mod;
        for (int j = 0; j < m; j++)
        {
            dp[i + L[j]] = (dp[i + L[j]] + dp[i]) % mod;
            dp[i + R[j] + 1] = (dp[i + R[j] + 1] - dp[i] + mod) % mod;
        }
    }

    cout << dp[n] << '\n';
    return 0;
}