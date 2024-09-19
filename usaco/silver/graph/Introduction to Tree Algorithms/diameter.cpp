#include <bits/stdc++.h>
using namespace std;

const int mxN = 2e5;

int N, dis, e;
vector<int> adj[mxN];

void dfs(int u, int p, int depth)
{
    for (int v : adj[u])
    {
        if (v == p)
            continue;
        dfs(v, u, depth + 1);
    }

    if (depth > dis)
    {
        dis = depth;
        e = u;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;

    for (int i = 0; i < N - 1; i++)
    {
        int a, b;
        cin >> a >> b;
        a--;
        b--;

        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    dfs(0, -1, 0);
    dis = 0;

    dfs(e, -1, 0);
    cout << dis << '\n';

    return 0;
}