#include <bits/stdc++.h>
using namespace std;

// Used for topological sort
vector<int> indegree = vector<int>(26);
vector<vector<int>> conn = vector<vector<int>>(26, vector<int>());
vector<int> sorted;

void topological_sort()
{
    queue<int> q;
    for (int i = 0; i < 26; i++)
    {
        if (indegree[i] == 0)
        {
            q.push(i);
        }
    }
    while (!q.empty())
    {
        int pos = q.front();
        q.pop();
        sorted.push_back(pos);
        for (auto c : conn[pos])
        {
            if ((--indegree[c]) == 0)
            {
                q.push(c);
            }
        }
    }
}

int main()
{
    int n;
    // We make sure each pair of consecutive strings are in the right order
    string cur, prev;

    /*
     * No previous string to compare the first string to,
     * so we read it directly into prev
     */
    cin >> n >> prev;
    for (int i = 1; i < n; i++)
    {
        cin >> cur;

        // Maximum length to compare
        int leng = min(prev.length(), cur.length());
        // How long the prefix has been the same for
        int samed = 0;

        while (samed < leng)
        {
            if (prev[samed] != cur[samed])
            {
                /*
                 * As soon as we see a difference, we make sure
                 * the alphabetic follows the order presented
                 */
                int ncur = cur[samed] - 'a', nprev = prev[samed] - 'a';
                indegree[ncur]++;
                conn[nprev].push_back(ncur);
                break;
            }
            samed++;
        }
        /*
         * If cur is a prefix of prev, then it is already impossible
         * for cur to be lexicographically more than prev
         */
        if ((samed == leng) && (prev.length() > cur.length()))
        {
            cout << "Impossible" << endl;
            return 0;
        }
        prev = cur;
    }

    topological_sort();

    // If topological sort not completeable, it's impossible
    if (sorted.size() < 26)
    {
        cout << "Impossible" << endl;
    }
    else
    {
        // Print out numbers converted back to characters
        for (int s : sorted)
        {
            cout << char(s + 'a');
        }
    }
}