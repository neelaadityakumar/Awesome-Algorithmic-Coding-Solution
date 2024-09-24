
#include "bits/stdc++.h"
#pragma GCC optimize("O3", "unroll-loops")
#define ll long long
#define ld long double
#define ff first
#define ss second
#define db double
#define time_begin() auto begin = chrono::high_resolution_clock::now()
#define time_end()                                                          \
	auto end = chrono::high_resolution_clock::now();                        \
	auto elapsed = chrono::duration_cast<chrono::nanoseconds>(end - begin); \
	auto sec = elapsed.count() * 1e-9;                                      \
	cerr << "\n\nExecution time: " << sec << " seconds";
#define check_time()                             \
	cerr << "\nStatus : ";                       \
	if (sec > 1)                                 \
		cerr << "Time Limit Exceeded 1!!!1!111"; \
	else                                         \
		cerr << "You good brother"
#define precision(x) fixed << setprecision((x))
#define check_ok(s) cout << s << " is aight" << '\n'
#define pii pair<int, int>
#define mp make_pair
using namespace std;

void setIO(string s = "")
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	if (!s.empty())
	{
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}
}

vector<vector<pii>> adj;
vector<int> deg;

int main()
{
	setIO("timeline");
	int n, m, c;
	cin >> n >> m >> c;
	vector<int> a(n);
	for (int i = 0; i < n; i++)
		cin >> a[i];
	vector<int> dp(n, -1);
	adj = vector<vector<pii>>(n, vector<pii>());
	deg = vector<int>(n, 0);
	for (int i = 1; i <= c; i++)
	{
		int u, v, w;
		cin >> u >> v >> w;
		adj[--u].push_back({--v, w});
		deg[v]++;
	}
	queue<int> q;
	for (int i = 0; i < n; i++)
	{
		if (deg[i] == 0)
		{
			q.push(i);
			dp[i] = a[i];
		}
	}
	while (!q.empty())
	{
		int u = q.front();
		q.pop();
		for (auto &[v, w] : adj[u])
		{
			if (--deg[v] == 0)
				q.push(v);
			dp[v] = max({dp[v], dp[u] + w, a[v]});
		}
	}
	for (int i = 0; i < n; i++)
		cout << dp[i] << '\n';
}
