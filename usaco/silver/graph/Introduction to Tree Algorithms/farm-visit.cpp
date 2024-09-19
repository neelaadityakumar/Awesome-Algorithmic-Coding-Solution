#include <bits/stdc++.h>

using namespace std;

vector<int> adj[100000], farm(100000), comp(100000);

bool visited[100000];

int curComp;

// Generate the connected components using DFS

void DFS(int curCow)
{
    if (visited[curCow])
    {
        return;
    }
    comp[curCow] = curComp;
    visited[curCow] = true;
    for (int adjCow : adj[curCow])
    {
        if (farm[curCow] == farm[adjCow])
        {
            DFS(adjCow);
        }
    }
}

int main()
{
    freopen("milkvisits.in", "r", stdin);
    freopen("milkvisits.out", "w", stdout);
    int n, m;
    cin >> n >> m;
    string cows;
    cin >> cows;
    for (int i = 0; i < n; i++)
    {
        farm[i] = (cows[i] == 'H');
    }
    for (int i = 0; i < n - 1; i++)
    {
        int x, y;
        cin >> x >> y;
        --x, --y;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }
    curComp = 1;
    for (int i = 0; i < n; i++)
    {
        if (!comp[i])
        {
            DFS(i);
            ++curComp;
        }
    }
    for (int i = 0; i < m; i++)
    {
        int a, b;
        char c;
        cin >> a >> b >> c;
        int curType = (c == 'H');
        --a, --b;
        /* If the first condition is true then there will
            be both an 'H', and 'G' in the current path.
           The latter condition checks if the current path consists of all "c"s.
        */
        if ((comp[a] != comp[b]) || (farm[a] == curType))
        {
            cout << 1;
        }
        else
        {
            cout << 0;
        }
    }
    cout << endl;
}