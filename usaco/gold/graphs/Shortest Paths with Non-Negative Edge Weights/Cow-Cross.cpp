#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
#define ss second

// Possible directions Bessie can go to eat grass
int dx[] = {1, 0, -1, 0, 3, 0, -3, 0, 2, 2, 1, 1, -1, -1, -2, -2};
int dy[] = {0, 1, 0, -1, 0, 3, 0, -3, 1, -1, 2, -2, 2, -2, 1, -1};

int main()
{
    ifstream fin("visitfj.in");

    int n, t;
    fin >> n >> t;
    vector<vector<int>> field(n, vector<int>(n));
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            fin >> field[i][j];
        }
    }

    // 2d integer grid initialized with max values for distance
    vector<vector<int>> dist(n, vector<int>(n, INT_MAX));
    // 2d boolean grid initialized with false for tracking visits
    vector<vector<bool>> visited(n, vector<bool>(n));
    // {distance, {row, col}}
    priority_queue<pair<int, pii>> dijkstra;
    dijkstra.push(make_pair(0, make_pair(0, 0)));
    dist[0][0] = 0;
    while (!dijkstra.empty())
    {
        int x, y;
        tie(x, y) = dijkstra.top().ss;
        dijkstra.pop();

        // check if this coordinate has already been visited
        if (visited[x][y])
        {
            continue;
        }
        visited[x][y] = true;
        for (int i = 0; i < 16; i++)
        {
            int newx = x + dx[i], newy = y + dy[i];
            // checking if this new location is out of bound
            if (newx < 0 || newx >= n || newy < 0 || newy >= n)
            {
                continue;
            }
            // updating the shortest distance to this new location
            if (dist[newx][newy] > dist[x][y] + 3 * t + field[newx][newy])
            {
                dist[newx][newy] = dist[x][y] + 3 * t + field[newx][newy];
                dijkstra.push(make_pair(-dist[newx][newy], make_pair(newx, newy)));
            }
        }

        int manhattan = n - x - 1 + n - y - 1;
        if (manhattan < 3)
        {
            dist[n - 1][n - 1] = min(dist[n - 1][n - 1], dist[x][y] + manhattan * t);
        }
    }

    ofstream("visitfj.out") << dist[n - 1][n - 1] << endl;
}