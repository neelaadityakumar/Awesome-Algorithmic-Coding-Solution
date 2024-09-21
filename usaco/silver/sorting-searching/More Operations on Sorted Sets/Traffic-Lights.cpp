// Keep track of the traffic lights and the distances between them. For each traffic light inserted, update the distances.

#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int x, n;
    cin >> x >> n;

    set<int> traffic_lights;
    traffic_lights.insert(0);
    traffic_lights.insert(x);

    multiset<int> distances;
    distances.insert(x);

    for (int i = 0; i < n; ++i)
    {
        int traffic_light;
        cin >> traffic_light;
        auto it = traffic_lights.upper_bound(traffic_light);
        distances.erase(distances.find(*it - *prev(it)));
        distances.insert(*it - traffic_light);
        distances.insert(traffic_light - *prev(it));
        traffic_lights.insert(traffic_light);
        (i == n - 1) ? cout << *distances.rbegin() << "\n" : cout << *distances.rbegin() << " ";
    }

    return 0;
}