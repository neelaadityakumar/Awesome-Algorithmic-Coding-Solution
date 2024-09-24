#include <iostream>
#include <vector>
#include <algorithm>
// Add other headers as needed
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
// BeginCodeSnip{DSU}
class DisjointSets
{
private:
    vector<int> parents;
    vector<int> sizes;

public:
    int component = 0;
    int max_component = 0;
    DisjointSets(int size) : parents(size), sizes(size, 1)
    {
        for (int i = 0; i < size; i++)
        {
            parents[i] = i;
        }

        component = size;
    }

    /** @return the "representative" node in x's component */
    int find(int x) { return parents[x] == x ? x : (parents[x] = find(parents[x])); }

    /** @return whether the merge changed connectivity */
    bool unite(int x, int y)
    {
        int x_root = find(x);
        int y_root = find(y);
        if (x_root == y_root)
        {
            return false;
        }

        if (sizes[x_root] < sizes[y_root])
        {
            swap(x_root, y_root);
        }
        sizes[x_root] += sizes[y_root];
        max_component = max(max_component, sizes[x_root]);
        parents[y_root] = x_root;
        component--;
        return true;
    }

    /** @return whether x and y are in the same connected component */
    bool connected(int x, int y) { return find(x) == find(y); }
};
// EndCodeSnip

int main()
{

    setIO("/Users/aditya.kumar/Desktop/code/_test/test");

    int node_num, query_num;
    cin >> node_num >> query_num;

    DisjointSets dsu(node_num);
    for (int i = 0; i < query_num; i++)
    {
        int u, v;
        cin >> u >> v;

        dsu.unite(u - 1, v - 1);
        cout << dsu.component << " " << dsu.max_component << endl;
    }
}