#include <bits/stdc++.h>
using namespace std;

// BeginCodeSnip{DSU}
struct DSU
{
	vector<int> e;
	DSU(int N) : e(N, -1) {}

	// get representive component (uses path compression)
	int get(int x) { return e[x] < 0 ? x : e[x] = get(e[x]); }

	bool same_set(int a, int b) { return get(a) == get(b); }

	int size(int x) { return -e[get(x)]; }

	// union by size
	bool unite(int x, int y)
	{
		x = get(x), y = get(y);
		if (x == y)
			return false;
		if (e[x] > e[y])
			swap(x, y);
		e[x] += e[y];
		e[y] = x;
		return true;
	}
};
// EndCodeSnip

int main()
{
	freopen("closing.in", "r", stdin);
	int n, m;
	cin >> n >> m;

	vector<vector<int>> adj(n);
	for (int i = 0; i < m; i++)
	{
		int u, v;
		cin >> u >> v;
		u--;
		v--;
		adj[u].push_back(v);
		adj[v].push_back(u);
	}

	// conn[i] = whether the ith farm is closed
	vector<bool> conn(n);
	vector<int> rev(n);
	for (int i = 0; i < n; i++)
	{
		cin >> rev[i];
		rev[i]--;
	}

	DSU dsu(n);
	reverse(rev.begin(), rev.end());

	conn[rev[0]] = 1;
	// one node is always connected
	vector<string> ans = {"YES"};

	// connected components
	int cc = 1;
	for (int i = 1; i < n; i++)
	{
		cc++;
		conn[rev[i]] = 1;
		for (int j : adj[rev[i]])
		{
			if (conn[j])
			{
				if (dsu.unite(j, rev[i]))
				{
					cc--;
				}
			}
		}
		ans.push_back(cc == 1 ? "YES" : "NO");
	}
	reverse(ans.begin(), ans.end());

	freopen("closing.out", "w", stdout);
	for (const string &i : ans)
	{
		cout << i << '\n';
	}
}