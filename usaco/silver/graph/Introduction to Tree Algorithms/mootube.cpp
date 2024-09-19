#include <bits/stdc++.h>
using namespace std;

vector<vector<pair<int, int>>> neighbors;
vector<bool> visited;
int threshold;
int num_reachable;

/** searches all vertices that can be reached through the current video v */
void search_videos(int v)
{
    visited[v] = true;
    for (const pair<int, int> &n : neighbors[v])
    {
        /*
         * only visit nonvisited videos whose relevance
         * is greater than the current threshold
         */
        if (!visited[n.first] && n.second >= threshold)
        {
            num_reachable++;
            search_videos(n.first);
        }
    }
}

int main()
{
    freopen("mootube.in", "r", stdin);
    int video_num;
    int query_num;
    cin >> video_num >> query_num;

    neighbors = vector<vector<pair<int, int>>>(video_num);
    for (int e = 0; e < video_num - 1; e++)
    {
        int a, b;
        int relevance;
        cin >> a >> b >> relevance;
        a--;
        b--;
        neighbors[a].push_back({b, relevance});
        neighbors[b].push_back({a, relevance});
    }

    freopen("mootube.out", "w", stdout);
    for (int q = 0; q < query_num; q++)
    {
        int start;
        cin >> threshold >> start;
        start--;

        // reset our global variables for the current query
        num_reachable = 0;
        visited = vector<bool>(video_num);
        search_videos(start);

        cout << num_reachable << '\n';
    }
}