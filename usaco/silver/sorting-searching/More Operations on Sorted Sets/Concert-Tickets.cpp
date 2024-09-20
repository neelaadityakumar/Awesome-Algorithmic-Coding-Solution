#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin >> n >> m;
    multiset<long long> ticket_prices;
    for (int i = 0; i < n; i++)
    {
        int ticket_price;
        cin >> ticket_price;
        ticket_prices.insert(ticket_price);
    }
    ticket_prices.insert(LONG_LONG_MAX);
    for (int i = 0; i < m; i++)
    {
        int customer_price;
        cin >> customer_price;
        auto it = ticket_prices.upper_bound(customer_price);
        if (it == ticket_prices.begin())
        {
            cout << -1 << "\n";
        }
        else
        {
            it--;
            cout << *it << "\n";
            ticket_prices.erase(ticket_prices.find(*it));
        }
    }
}