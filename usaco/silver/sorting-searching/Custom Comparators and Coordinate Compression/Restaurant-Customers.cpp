#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<pair<int, int>> entries(n);

    // Input all entries
    for (int i = 0; i < n; ++i)
    {
        cin >> entries[i].first >> entries[i].second;
    }

    // Use a map to track changes in the timeline
    map<int, int> timeline;

    // Mark the start and end points
    for (const auto &entry : entries)
    {
        timeline[entry.first] += 1;      // Increment at start
        timeline[entry.second + 1] -= 1; // Decrement at end + 1
    }

    int curr = 0;
    int ans = 0;

    // Traverse the map to calculate the maximum overlap
    for (const auto &[key, value] : timeline)
    {
        curr += value;
        ans = max(ans, curr);
    }

    cout << ans << endl;

    return 0;
}
