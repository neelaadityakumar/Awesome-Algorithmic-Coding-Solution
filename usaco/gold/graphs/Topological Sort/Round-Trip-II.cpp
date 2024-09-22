#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define pb push_back
#define mp make_pair
#define fir first
#define sec second
#define all(a) a.begin(), a.end()

const int maxn = 200010;
const ll MOD = 1e9 + 7;
const int INF = 1e9;
const ll LINF = 1e18;
ll n, m, a[maxn];
map<int, int> M, N;
string s, ss;
set<int> S;

vector<int> adj[maxn];
int col[maxn], p[maxn];
int cycle_start = -1, cycle_end = -1;

void dfs(int s)
{
    col[s] = 1;
    for (auto u : adj[s])
    {
        if (col[u] == 0)
            p[u] = s, dfs(u);
        else if (col[u] == 1)
            cycle_start = u, cycle_end = s;
    }
    col[s] = 2;
}

void print_cycle(int s, int d)
{
    vector<int> cycle;
    cycle.pb(s);
    for (int i = d; i != s; i = p[i])
        cycle.pb(i);
    cycle.pb(s);
    reverse(all(cycle));
    cout << cycle.size() << "\n";
    for (auto u : cycle)
        cout << u << " ";
}

int main()
{
    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        adj[a].pb(b);
        // adj[b].pb(a);
    }
    fill(col, col + maxn, 0);
    fill(p, p + maxn, -1);
    for (int i = 1; i <= n; i++)
    {
        if (col[i] != 0)
            continue;
        cycle_start = -1, cycle_end = -1;
        dfs(i);
        if (cycle_start == -1)
            continue;
        print_cycle(cycle_start, cycle_end);
        return 0;
    }
    cout << "IMPOSSIBLE\n";
}