#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;

int roadhelper(unordered_map<int, vector<int>>& graph, int root) {
    vector<int> childs = graph[root];
    int size = childs.size();
    if (size == 0) {
        return 0;
    }
    int ans = 0;
    for (int son : childs) {
        ans = max(ans, roadhelper(graph, son));
    }
    return ans + 1;
}

int main() {
    int N;
    cin >> N;
    unordered_map<int, vector<int>> graph;
    int x, y;
    for (int i = 0; i < N-1; i++) {
        cin >> x >> y;
        graph[x].push_back(y);
    }
    int ans = roadhelper(graph, 1);
    ans = 2 * (N-1) - ans;
    cout << ans << endl;
    return 0;
}