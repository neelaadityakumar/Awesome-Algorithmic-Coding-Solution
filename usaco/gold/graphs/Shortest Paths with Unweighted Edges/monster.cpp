#include <bits/stdc++.h>
using namespace std;

#define forn(i, a, n) for (int i = a; i < int(n); i++)
#define ll long long
#define db double
#define pb push_back
#define all(v) v.begin(), v.end()
#define F first
#define S second
#define INF 1000000007
#define popcount(x) __builtin_popcountll(x)
#define pll pair<ll, ll>
#define pii pair<int, int>
#define nl "\n"
#define PI 3.1415926536
#define mp make_pair
const int N = 1e3 + 5;

int dx[4]{1, -1, 0, 0}, dy[4]{0, 0, 1, -1};
int fx[] = {-1, 1, 0, 0};
int fy[] = {0, 0, 1, -1};
char go[] = {'U', 'D', 'R', 'L'};
int nex[1005][1005];

void solve()
{
    int n, m;
    cin >> n >> m;
    vector<string> grid(n);
    for (auto &i : grid)
        cin >> i;
    queue<pair<int, int>> q;
    int x, y;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (grid[i][j] == 'M')
                q.push({i, j});
            else if (grid[i][j] == 'A')
                x = i, y = j;
    q.push({x, y});
    nex[x][y] = -1;
    // reduce distances from all monsters and then human
    while (!q.empty())
    {
        auto it = q.front();
        x = it.F;
        y = it.S;
        q.pop();
        if (grid[x][y] == 'A' && (x == 0 || x == n - 1 || y == 0 || y == m - 1))
        {
            cout << "YES" << endl;
            string ans;
            int d = nex[x][y];
            while (d != -1)
            {
                ans += go[d];
                x -= fx[d];
                y -= fy[d];
                d = nex[x][y];
            }
            reverse(ans.begin(), ans.end());
            cout << ans.size() << endl;
            cout << ans;
            return;
        }
        for (int i = 0; i < 4; i++)
        {
            int xx = x + fx[i],
                yy = y + fy[i];
            if (xx < 0 || xx >= n || yy < 0 || yy >= m || grid[xx][yy] != '.')
                continue;
            else
            {
                grid[xx][yy] = grid[x][y];
                if (grid[xx][yy] == 'A')
                    nex[xx][yy] = i;
                q.push({xx, yy});
            }
        }
    }
    cout << "NO";
}

int32_t main()
{

#ifndef ONLINE_JUDGE

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int T = 1; // cin >> T;
    while (T--)
        solve();

#ifdef DEBUG
    cerr << "Runtine is: " << clock() * 1.0 / CLOCKS_PER_SEC << endl;
#endif

    return 0;
}