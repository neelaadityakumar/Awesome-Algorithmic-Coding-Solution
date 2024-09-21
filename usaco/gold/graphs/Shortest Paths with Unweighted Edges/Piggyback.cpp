#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define int ll
#define NAME "piggyback"
#define file                         \
    freopen(NAME ".in", "r", stdin); \
    freopen(NAME ".out", "w", stdout);
#define sdf                  \
    ios::sync_with_stdio(0); \
    cin.tie(0);              \
    cout.tie(0);

const int N = 4e4 + 5, INF = 1e18;
vector<vector<int>> adj(N);
int b, e, p, n, m;

void bfs(int s, vector<int> &dis, int cost)
{
    dis.assign(n + 2, INF);
    dis[s] = 0;
    queue<int> q;
    q.push(s);
    while (!q.empty())
    {
        int u = q.front();
        q.pop();

        for (auto v : adj[u])
        {
            if (dis[v] != INF)
                continue;
            if (dis[v] > dis[u] + cost)
            {
                dis[v] = dis[u] + cost;
                q.push(v);
            }
        }
    }
}

int32_t main()
{
    sdf
            file
                cin >>
        b >> e >> p >> n >> m;
    for (int i = 1; i <= m; ++i)
    {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    vector<int> disB, disE, disP;
    bfs(1, disB, b);
    bfs(2, disE, e);
    bfs(n, disP, p);

    int ans = INF;
    for (int i = 1; i <= n; ++i)
    {
        ans = min(disB[i] + disE[i] + disP[i], ans);
    }
    cout << ans;
    return 0;
}