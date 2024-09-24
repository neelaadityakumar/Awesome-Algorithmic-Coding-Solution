#include <vector>
#include <iostream>
#include <cstring>
#include <utility>
#include <algorithm>
#include <queue>

using namespace std;

int T;
int n, m, in[200005], tp[200005];
vector<int> graph[200005];
vector<pair<int, int>> undirs;

bool topsort()
{
    // Use Kahn's algorithm
    int cnt = 0;
    queue<int> q;
    for (int i = 1; i <= n; i++)
        if (!in[i])
            q.push(i), tp[i] = ++cnt;

    while (!q.empty())
    {
        int n = q.front();
        q.pop();
        for (int i : graph[n])
        {
            if (!--in[i])
                q.push(i), tp[i] = ++cnt;
        }
    }

    return cnt == n;
}

int main()
{
    cin >> T;
    cin.ignore();

    while (T--)
    {
        cin >> n >> m;

        memset(in, 0, sizeof(in));
        for (int i = 1; i <= n; i++)
            graph[i].clear();
        undirs.clear();

        int d, x, y;
        for (int i = 1; i <= m; i++)
        {
            cin >> d >> x >> y;
            if (d)
            {
                graph[x].push_back(y);
                in[y]++;
            }
            else
                undirs.push_back({x, y});
        }

        if (topsort())
        {
            cout << "YES" << endl;
            for (int i = 1; i <= n; i++)
            {
                for (int j : graph[i])
                    cout << i << " " << j << endl;
            }

            // If node x appears before node y in the topsort ordering, x-->y. Otherwise orient y-->x
            for (auto [i, j] : undirs)
            {
                if (tp[i] < tp[j])
                    cout << i << " " << j << endl;
                else
                    cout << j << " " << i << endl;
            }
        }
        else
            cout << "NO" << endl;
    }
}