#include <bits/stdc++.h>
using namespace std;
using ll = long long;

signed main()
{
    int n, m;
    cin >> n >> m;

    vector<ll> v(n + 1), diff(n + 2);
    for (int i = 1; i <= n; i++)
        cin >> v[i];

    while (m--)
    {
        int l, r;
        cin >> l >> r;
        diff[l]++;
        diff[r + 1]--;
    }

    for (int i = 2; i <= n; i++)
        diff[i] += diff[i - 1];

    sort(v.begin() + 1, v.end());
    sort(diff.begin() + 1, diff.end() - 1);

    ll ans = 0;
    for (int i = 1; i <= n; i++)
        ans += v[i] * diff[i];
    cout << ans << '\n';
    return 0;
}