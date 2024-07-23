---
title: 'Algorithm 🍊⭐'
date: 2023-01-01
permalink: /note/algorithm
tags:
  - note
toc: true
---

Templates of competitive programming.

{% include toc %}

# Basic / 基本

## Brute-Force / 全探索

### Bit Exhaustive Search / ビット全探索
```cpp
vector<int> arr(N);

void search(int n) {
    for (int i=0; i<(1<<n); ++i) {
        for (int j=0; j<n; ++j) {
            if (i&(1<<j))
                "<arr[j]...>";
        }
    }
}
```

### Permutation Exhaustive Search / 順列全探索
```cpp
vector<int> arr(N);

void search(int n) {
    do {
        for (int i=0; i<n; ++i)
            "<arr[i]...>";
    } while (next_permutation(arr.begin(), arr.begin()+n));
}
```

### DFS Exhaustive Search / DFS全探索
```cpp
vector<int> arr(N);

void search(int p, int n) {
    if (p==n) {
        for (int i=0; i<n; ++i)
            "<arr[i]...>";
        return;
    }
    for ("<next value i>") {
        if ("<pruning>")
            continue;
        arr[p] = i;
        search(p+1, n);
        arr[p] = 0;
    }
}
```

### Backtracking / バックトラッキング
```cpp
vector<int> arr(N);

bool search(int p, int n) {
    if (p==n) {
        if ("<satisfied>")
            return true;
        return false;
    }
    for ("<next value i>") {
        if ("<pruning>")
            continue;
        arr[p] = i;
        if (search(p+1, n))
            return true;
        arr[p] = 0;
    }
    return false;
}
```

## Basic Method / 基本的手法

### Greedy Algorithm / 貪欲法
```cpp
void solve() {
    "<preprocess>";
    for (int i=0; i<N; ++i) {
        "<greedy>";
    }
}
```

### Binary Search / 二分探索
```cpp
vector<int> arr(N);

int search(int n, int t) {
    int l=-1, r=n;
    while (r-l>1) {
        int m = (l+r)/2;
        if (t<arr[m])
            r = m;
        else
            l = m;
    }
    return l;
}
```
```cpp
bool check(int x) {
    "<return true or false>";
}

int search(int n) {
    int l=-1, r=n;
    while (r-l>1) {
        int m = (l+r)/2;
        if (check(m))
            r = m;
        else
            l = m;
    }
    return l;
}
```

### Divide and Conquer / 分割統治法
```cpp
vector<int> arr(N);

void rec(int l, int r) {
    int m = (l+r)/2;
    if (l==r)
        "<base case>";
    rec(l, m);
    rec(m+1, r);
    "<combine>";
}
```

## Dynamic Programming / 動的計画法

### Knapsack DP / ナップサックDP
```cpp
vector<vector<int>> dp(N, vector<int>(M));

void solve(int n, int m) {
    "<base case>";
    for (int i=1; i<=n; ++i) {
        for (int j=1; j<=m; ++j) {
            dp[i][j] = "<combination of dp[<=i][<=j] >";
        }
    }
}
```

### Digit Dp / 桁DP
```cpp
int dp[N][M][2];

void solve(int n, int m) {
    "<base case>";
    for (int i=0; i<n; ++i) {
        for (int j=0; j<m; ++j) {
            "<transfer dp[i][j][0] to dp[i+1][target (0~9) ][0] >";
            "<transfer dp[i][j][1] to dp[i+1][target (0~di)][0] >";
            "<transfer dp[i][j][1] to dp[i+1][target (di)  ][1] >";
        }
    }
}
```

### Interval DP / 区間DP
```cpp
vector<vector<int>> dp(N, vector<int>(N, -1));

int rec(int l, int r) {
    if (dp[l][r]!=-1)
        return dp[l][r];
    if ("<base case>")
        return dp[l][r] = "<value>";
    int a = "<combination of rec(l+1, r-1), rec(l, i), rec(i+1, r), ...)>";
    return dp[l][r] = a;
}
```

### Bit DP / ビットDP
```cpp
vector<vector<int>> dp((1<<N), vector<int>(N, -1));

int rec(int S, int v, int n) {
    if (dp[S][v]!=-1)
        return dp[S][v];
    if ("<base case>")
        return dp[S][v] = "<value>";
    int a = "<combination of rec(S^(1<<v), i, n), ...>";
    return dp[S][v] = a;
}
```

## Data Structure / データ構造

### Basic Data Structure / 基本的データ構造
```cpp
void binary_heap() {
    priority_queue<int> q;
    q.push("<value>");
    q.pop();
    int "<value>" = q.top();
}
```
```cpp
void binary_search_tree() {
    set<int> s;
    s.insert("<value>");
    s.erase("<value>");
    set<int>::iterator "<iterator>" = s.find("<value>");
}

void binary_search_tree2() {
    map<int, int> m;
    m.insert({"<key>", "<value>"});
    m.erase("<key>");
    map<int, int>::iterator "<iterator>" = m.find("<key>");
    m["<key>"] = "<value>";
    int "<value>" = map["<key>"];
}
```
```cpp
void hash_table() {
    unordered_set<int> s;
    s.insert("<value>");
    s.erase("<value>");
    unordered_set<int>::iterator "<iterator>" = s.find("<value>");
}

void hash_table2() {
    unordered_map<int, int> m;
    m.insert({"<key>", "<value>"});
    m.erase("<key>");
    unordered_map<int, int>::iterator "<iterator>" = m.find("<key>");
    m["<key>"] = "<value>";
    int "<value>" = m["<key"];
}
```

### Disjoint Set Union / Union-Find木
```cpp
vector<int> par(N), siz(N);

void make_set(int v) {
    par[v] = v;
    siz[v] = 1;
}

int find_set(int v) {
    if (par[v] == v)
        return v;
    return par[v] = find_set(par[v]);
}

void union_set(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (a < b)
            swap(a, b);
        par[b] = a;
        siz[a] += siz[b];
    }
}
```

### Segment Tree / セグメント木
```cpp
vector<int> arr(N), tree(4*N);

void build(int v, int tl, int tr) {
    if (tl==tr) {
        tree[v] = arr[tl];
        return;
    }
    int tm = (tl+tr)/2;
    build(v*2+1, tl, tm);
    build(v*2+2, tm+1, tr);
    tree[v] = "<merge tree[v*2+1] and tree[v*2+2]>";
}

int query(int v, int tl, int tr, int l, int r) {
    if (l>r)
        return "<identity>";
    if (tl==l && tr==r)
        return tree[v];
    int tm = (tl+tr)/2;
    int q1 = query(v*2+1, tl, tm, l, min(r, tm));
    int q2 = query(v*2+2, tm+1, tr, max(l, tm+1), r);
    return "<merge q1 and q2>";
}

void update(int v, int tl, int tr, int pos, int x) {
    if (tl==tr) {
        tree[v] = x;
        return;
    }
    int tm = (tl+tr)/2;
    if (pos<=tm)
        update(v*2+1, tl, tm, pos, x);
    else
        update(v*2+2, tm+1, tr, pos, x);
    tree[v] = "<merge tree[v*2+1] and tree[v*2+2]>";
}
```
```cpp
vector<int> arr(N), tree(4*N), lazy(4*N);

void build(int v, int tl, int tr) {
    if (tl==tr) {
        tree[v] = arr[tl];
        lazy[v] = "<identity>";
        return;
    }
    int tm = (tl+tr)/2;
    build(v*2+1, tl, tm);
    build(v*2+2, tm+1, tr);
    tree[v] = "<merge tree[v*2+1] and tree[v*2+2]>";
    lazy[v] = "<identity>";
}

void push(int v, int tl, int tr) {
    int tm = (tl+tr)/2;
    tree[v*2+1] = "<update with lazy[v]>";
    tree[v*2+2] = "<update with lazy[v]>";
    lazy[v*2+1] = "<propogate lazy[v]>";
    lazy[v*2+2] = "<propogate lazy[v]>";
    lazy[v] = "<identity>";
}

int query(int v, int tl, int tr, int l, int r) {
    if (l>r)
        return "<identity>";
    if (tl==l && tr==r)
        return tree[v];
    push(v, tl, tr);
    int tm = (tl+tr)/2;
    int q1 = query(v*2+1, tl, tm, l, min(r, tm));
    int q2 = query(v*2+2, tm+1, tr, max(l, tm+1), r);
    return "<merge q1 and q2>";
}

void update(int v, int tl, int tr, int l, int r, int x) {
    if (l>r)
        return;
    if (tl==l && tr==r) {
        tree[v] = "<update with x>";
        lazy[v] = "<update with x>";
        return;
    }
    push(v, tl, tr);
    int tm = (tl+tr)/2;
    update(v*2+1, tl, tm, l, min(r, tm), x);
    update(v*2+2, tm+1, tr, max(l, tm+1), r, x);
    tree[v] = "<merge tree[v*2+1] and tree[v*2+2]>";
}
```

### Binary Indexed Tree　/ フェニック木
```cpp
vector<int> arr(N), tree(N);

void build(int n) {
    for (int i=0; i<n; ++i) {
        tree[i] = "<merge tree[i] and arr[i]>";
        int r = i|(i+1);
        if (r<n)
            tree[r] = "<merge tree[r] and tree[i]>";
    }
}

int query(int r) {
    int s = 0;
    while (r>=0) {
        s = "<merge s and tree[r]>";
        r = (r&(r+1))-1;
    }
    return s;
}

void update(int p, int x, int n) {
    while (p<n) {
        tree[p] = "<merge tree[p] and x>";
        p = p|(p+1);
    }
}
```

### Sqrt Decomposition / 平方分割
```cpp
vector<int> arr(N), buc(N);

void build(int n) {
    int s = (int)ceil(sqrt(n));
    for (int i=0; i<s; ++i) {
        for (int j=i*s; j<(i+1)*s && j<n; ++j)
            buc[i] = "<merge buc[i] and arr[j]>";
    }
}

int query(int l, int r, int n) {
    int s = (int)ceil(sqrt(n));
    int q=0, bl=l/s, br=r/s;
    if (bl==br) {
        for (int i=l; i<=r; ++i)
            q = "<merge q and arr[i]>";
        return q;
    }
    for (int i=l; i<(bl+1)*s; ++i)
        q = "<merge q and arr[i]>";
    for (int i=bl+1; i<br; ++i)
        q = "<merge q and buc[i]>";
    for (int i=br*s; i<=r; ++i)
        q = "<merge q and arr[i]>";
    return q;
}
```

# Graph / グラフ

## Graph Traversal / グラフ探索

### DFS / 深さ優先探索
```cpp
vector<vector<int>> adj(N);
vector<int> vis(N), dis(N, INF), par(N, -1);

void dfs(int v, int d, int p) {
    vis[v] = 1;
    dis[v] = d;
    par[v] = p;
    for (int u : adj[v]) {
        if (!vis[u]) {
            dfs(u, d+1, v);
        }
    }
}
```

### BFS / 幅優先探索
```cpp
vector<vector<int>> adj(N);
vector<int> vis(N), dis(N, INF), par(N, -1);

void bfs(int v) {
    queue<int> q;
    vis[v] = 1;
    dis[v] = 0;
    par[v] = -1;
    q.push(v);
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int u : adj[v]) {
            if (!vis[u]) {
                vis[u] = 1;
                dis[u] = dis[v] + 1;
                par[u] = v;
                q.push(u);
            }
        }
    }
}
```

### Topological Sort / トポロジカルソート
```cpp
vector<vector<int>> adj(N);
vector<int> vis(N), ans;

void dfs(int v) {
    vis[v] = 1;
    for (int u : adj[v]) {
        if (!vis[u])
            dfs(u);
    }
    ans.push_back(v);
}

void topological_sort(int n) {
    for (int i=0; i<n; ++i) {
        if (!vis[i])
            dfs(i);
    }
    reverse(ans.begin(), ans.end());
}
```

## Shortest Path / 最短経路

### Dijkstra's Algorithm / ダイクストラ法
```cpp
vector<vector<int>> adj(N, vector<int>(N, INF));
vector<int> vis(N), dis(N, INF), par(N, -1);

void dijkstra(int s, int n) {
    dis[s] = 0;
    for (int i=0; i<n; ++i) {
        int k = -1;
        for (int j=0; j<n; ++j) {
            if (!vis[j] && (k==-1 || dis[j]<dis[k]))
                k = j;
        }
        if (dis[k]==INF)
            return;
        vis[k] = 1;
        for (int j=0; j<n; ++j) {
            if (dis[k]+adj[k][j]<dis[j]) {
                dis[j] = dis[k] + adj[k][j];
                par[j] = k;
            }
        }
    }
}
```
```cpp
vector<vector<pii>> adj(N);
vector<int> dis(N, INF), par(N, -1);

void dijkstra(int s) {
    priority_queue<pii, vector<pii>, greater<pii>> q;
    dis[s] = 0;
    q.push({0, s});
    while (!q.empty()) {
        int v = q.top().second;
        int d_v = q.top().first;
        q.pop();
        if (d_v!=dis[v])
            continue;
        for (pii e : adj[v]) {
            int to = e.first;
            int len = e.second;
            if (dis[v]+len<dis[to]) {
                dis[to] = dis[v] + len;
                par[to] = v;
                q.push({dis[to], to});
            }
        }
    }
}

```

### Bellman–Ford Algorithm / ベルマン–フォード法
```cpp
struct edge{
    int a, b, w;
};

vector<edge> edges;
vector<int> dis(N, INF), par(N, -1);

void bellman_ford(int s, int n) {
    dis[s] = 0;
    int cnt = 0;
    for (int i=0; i<n; ++i) {
        bool any = 0;
        for (edge e : edges) {
            if (dis[e.a]!=INF && dis[e.a]+e.w<dis[e.b]) {
                dis[e.b] = dis[e.a] + e.w;
                par[e.b] = e.a;
                any = 1;
            }
        }
        if (!any)
            break;
        cnt += 1;
    }
    "<negative cycle: cnt==n>";
}
```

### Floyd–Warshall Algorithm / ワーシャル–フロイド法
```cpp
vector<vector<int>> dis(N, vector<int>(N, INF)), par(N, vector<int>(N, -1));

void floyd_warshall(int n) {
    "<each edge: dis[v][u]=w, par[v][u]=v >";
    "<each vert: dis[v][v]=0, par[v][v]=v >";
    for (int k=0; k<n; ++k) {
        for (int i=0; i<n; ++i) {
            for (int j=0; j<n; ++j) {
                if (dis[i][k]<INF && dis[k][j]<INF && dis[i][k]+dis[k][j]<dis[i][j]) {
                    dis[i][j] = dis[i][k] + dis[k][j];
                    par[i][j] = par[k][j];
                }
            }
        }
    }
    "<negative cycle: dis[i][i]<0 >";
}
```

## Minimum Spanning Tree / 最小全域木

### Prim's Algorithm / プリム法
```cpp
vector<vector<int>> adj(N, vector<int>(N, INF));
vector<int> vis(N), dis(N, INF), par(N, -1);

int prim(int s, int n) {
    int wt = 0;
    dis[s] = 0;
    for (int i=0; i<n; ++i) {
        int k = -1;
        for (int j=0; j<n; ++j) {
            if (!vis[j] && (k==-1 || dis[j]<dis[k]))
                k = j;
        }
        if (dis[k]==INF)
            return INF;
        vis[k] = 1;
        wt += dis[k];
        for (int j=0; j<n; ++j) {
            if (!vis[j] && adj[k][j]<dis[j]) {
                dis[j] = adj[k][j];
                par[j] = k;
            }
        }
    }
    return wt;
}
```
```cpp
vector<vector<pii>> adj(N);
vector<int> vis(N), dis(N, INF), par(N, -1);

int prim(int s) {
    int wt = 0;
    priority_queue<pii, vector<pii>, greater<pii>> q;
    dis[s] = 0;
    q.push({0, s});
    while (!q.empty()) {
        int v = q.top().second;
        q.pop();
        if (vis[v])
            continue;
        vis[v] = 1;
        wt += dis[v];
        for (pii e : adj[v]) {
            if (!vis[e.first] && e.second<dis[e.first]) {
                dis[e.first] = e.second;
                par[e.first] = v;
                q.push({dis[e.first], e.first});
            }
        }
    }
    return wt;
}
```

### Kruskal's Algorithm / クラスカル法
```cpp
vector<int> par(N), siz(N);

void make_set(int v) {
    par[v] = v;
    siz[v] = 1;
}

int find_set(int v) {
    if (par[v] == v)
        return v;
    return par[v] = find_set(par[v]);
}

void union_set(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (a < b)
            swap(a, b);
        par[b] = a;
        siz[a] += siz[b];
    }
}

struct edge {
    int a, b, w;
    bool operator<(edge const& other) {
        return w < other.w;
    }
};

vector<edge> edges, mst;

int kruskal() {
    int wt = 0;
    sort(edges.begin(), edges.end());
    for (edge e : edges) {
        if (find_set(e.a) != find_set(e.b)) {
            wt += e.w;
            mst.push_back(e);
            union_set(e.a, e.b);
        }
    }
    return wt;
}
```

## Connectivity / 連結性

### Connected Component / 連結成分
```cpp
vector<vector<int>> adj(N);
vector<int> vis(N), cmp(N);

void dfs(int v, int c) {
    vis[v] = 1;
    cmp[v] = c;
    for (int u : adj[v]) {
        if (!vis[u])
            dfs(u, c);
    }
}

int cc(int n) {
    int cnt = 0;
    for (int i=0; i<n; ++i) {
        if (!vis[i]) {
            dfs(i, i);
            cnt += 1;
        }
    }
    return cnt;
}
```

### Strongly Connected Component / 強連結成分
```cpp
vector<vector<int>> adj(N), adj_r(N);
vector<int> q, vis(N), cmp(N);

void dfs1(int v) {
    vis[v] = 1;
    for (int u : adj[v]) {
        if (!vis[u])
            dfs1(u);
    }
    q.push_back(v);
}

void dfs2(int v, int c) {
    vis[v] = 1;
    cmp[v] = c;
    for (int u : adj_r[v]) {
        if (!vis[u])
            dfs2(u, c);
    }
}

int scc(int n) {
    int cnt = 0;
    for (int i=0; i<n; ++i) {
        if (!vis[i])
            dfs1(i);
    }
    reverse(q.begin(), q.end());
    vis.assign(n, 0);
    for (int i : q) {
        if (!vis[i]) {
            dfs2(i, i);
            cnt += 1;
        }
    }
    return cnt;
}
```

### Bridge / 橋
```cpp
vector<vector<int>> adj(N);
vector<int> vis(N), tin(N), low(N);
int timer = 0;

void dfs(int v, int p) {
    vis[v] = 1;
    tin[v] = low[v] = timer++;
    for (int u : adj[v]) {
        if (u==p)
            continue;
        if (vis[u])
            low[v] = min(low[v], tin[u]);
        else {
            dfs(u, v);
            low[v] = min(low[v], low[u]);
            if (low[u]>tin[v]) {
                "<bridge: v-u >";
            }
        }
    }
}
```

### Articulation Point / 関節点
```cpp
vector<vector<int>> adj(N);
vector<int> vis(N), tin(N), low(N);
int timer = 0;

void dfs(int v, int p) {
    vis[v] = 1;
    tin[v] = low[v] = timer++;
    int cld = 0;
    for (int u : adj[v]) {
        if (u==p)
            continue;
        if (vis[u])
            low[v] = min(low[v], tin[u]);
        else {
            dfs(u, v);
            low[v] = min(low[v], low[u]);
            if (p!=-1 && low[u]>=tin[v]) {
                "<articulation point: v >";
            }
            cld += 1;
        }
    }
    if (p==-1 && cld>1) {
        "<articulation point: v >";
    }
}
```

## Network Flow / ネットワークフロー

### Maximum Flow / 最大流
```cpp
vector<vector<int>> adj(N), cap(N, vector<int>(N));
vector<int> vis(N, 0), par(N, -1);

int bfs(int s, int t) {
    fill(vis.begin(), vis.end(), 0);
    fill(par.begin(), par.end(), -1);
    queue<pii> q;
    q.push({s, INF});
    vis[s] = 1;
    while (!q.empty()) {
        int v = q.front().first;
        int f_v = q.front().second;
        q.pop();
        for (int u : adj[v]) {
            if (!vis[u] && cap[v][u]>0) {
                int f_u = min(f_v, cap[v][u]);
                q.push({u, f_u});
                vis[u] = 1;
                par[u] = v;
                if (u==t)
                    return f_u;
            }
        }
    }
    return 0;
}

int max_flow(int s, int t) {
    "<each edge: adj[v].pb(u) adj[u].pb(v) >";
    "<each edge: cap[v][u]=c cap[u][v]=0 >";
    int flow=0, f=0;
    while (f=bfs(s, t)) {
        flow += f;
        int cur = t;
        while (cur!=s) {
            int pre = par[cur];
            cap[pre][cur] -= f;
            cap[cur][pre] += f;
            cur = pre;
        }
    }
    return flow;
}
```

### Minimum-Cost Flow / 最小費用流
```cpp
vector<vector<pii>> adj(N);
vector<int> dis(N), par(N), pot(N);
vector<vector<int>> cap(N, vector<int>(N));

int dijkstra(int s, int t, int n) {
    fill(dis.begin(), dis.end(), INF);
    fill(par.begin(), par.end(), -1);
    priority_queue<pii, vector<pii>, greater<pii>> q;
    q.push({0, s});
    dis[s] = 0;
    while (!q.empty()) {
        int v = q.top().second;
        int d_v = q.top().first;
        q.pop();
        if (d_v!=dis[v])
            continue;
        for (pii e : adj[v]) {
            int to = e.first;
            int len = e.second;
            if (dis[v]+len+pot[v]-pot[to]<dis[to] && cap[v][to]>0) {
                dis[to] = dis[v]+len+pot[v]-pot[to];
                par[to] = v;
                q.push({dis[to], to});
            }
        }
    }
    for (int i=0; i<n; ++i)
        pot[i] += dis[i];
    return pot[t];
}

// vector<vector<int>> adj(N, vector<int>(N, INF));
// vector<int> vis(N), dis(N), par(N), pot(N);
// vector<vector<int>> cap(N, vector<int>(N));

// int dijkstra(int s, int t, int n) {
//     fill(vis.begin(), vis.end(), 0);
//     fill(dis.begin(), dis.end(), INF);
//     fill(par.begin(), par.end(), -1);
//     dis[s] = 0;
//     for (int i=0; i<n; ++i) {
//         int k = -1;
//         for (int j=0; j<n; ++j) {
//             if (!vis[j] && (k==-1 || dis[j]<dis[k]))
//                 k = j;
//         }
//         if (dis[k]==INF)
//             return INF;
//         vis[k] = 1;
//         for (int j=0; j<n; ++j) {
//             if (dis[k]+adj[k][j]+pot[k]-pot[j]<dis[j] && cap[k][j]>0) {
//                 dis[j] = dis[k]+adj[k][j]+pot[k]-pot[j];
//                 par[j] = k;
//             }
//         }
//     }
//     for (int i=0; i<n; ++i)
//         pot[i] += dis[i];
//     return pot[t];
// }

int min_cost_flow(int s, int t, int k, int n) {
    "<each edge: adj[v].pb(u,w) adj[u].pb(v,-w) >";
    "<each edge: cap[v][u]=c cap[u][v]=0 >";
    int cost=0, flow=0;
    while (flow<k) {
        int m_c = dijkstra(s, t, n);
        int m_f = k - flow;
        if (m_c==INF)
            return -1;
        int cur=t, pre=-1;
        while (cur!=s) {
            pre = par[cur];
            m_f = min(m_f, cap[pre][cur]);
            cur = pre;
        }
        cost += m_c * m_f;
        flow += m_f;
        cur = t;
        while (cur!=s) {
            pre = par[cur];
            cap[pre][cur] -= m_f;
            cap[cur][pre] += m_f;
            cur = pre;
        }
    }
    return cost;
}
```

### Bipartite Matching / 二部マッチング
```cpp
vector<vector<int>> adj(N1);
vector<int> vis(N1), mat(N2, -1);

bool dfs(int v) {
    vis[v] = 1;
    for (int u : adj[v]) {
        int w = mat[u];
        if (w==-1 || (!vis[w] && dfs(w))) {
            mat[u] = v;
            return true;
        }
    }
    return false;
}

int bipartite(int n) {
    int res = 0;
    for (int i=0; i<n; ++i) {
        fill(vis.begin(), vis.end(), 0);
        if (dfs(i))
            res += 1;
    }
    return res;
}
```

## Tree Algorithm / 木アルゴリズム

### Tree Diameter / 木の直径
```cpp
vector<vector<int>> adj(N);
vector<int> par(N);

pair<int, int> dfs(int v, int d, int p) {
    par[v] = p;
    pair<int, int> res{d, v};
    for (int u : adj[v]) {
        if (u!=p)
            res = max(res, dfs(u, d+1, v));
    }
    return res;
}

vector<int> tree_diameter() {
    vector<int> ans;
    int s = dfs(0, 0, -1).second;
    int t = dfs(s, 0, -1).second;
    while (t!=-1) {
        ans.push_back(t);
        t = par[t];
    }
    return ans;
}
```

### Tree DP / 木DP
```cpp
vector<vector<int>> adj(N);
vector<vector<int>> dp(N, vector<int>(S));

void dfs(int v, int p) {
    for (int u : adj[v]) {
        if (u==p)
            continue;
        dfs(u, v);
        dp[v][i] = "<combination of dp[u][j], ...>";
    }
}
```

### Tree Divide and Conquer / 木の分割統治法
```cpp
vector<vector<int>> adj(N);
vector<int> siz(N), cen(N);

void calsize(int v, int p) {
    siz[v] = 1;
    for (int u : adj[v]) {
        if (u==p || cen[u])
            continue;
        calsize(u, v);
        siz[v] += siz[u];
    }
}

int centroid(int v, int p, int t) {
    for (int u : adj[v]) {
        if (u==p || cen[u])
            continue;
        if (siz[u]>t/2)
            return centroid(u, v, t);
    }
    return v;
}

void rec(int v) {
    calsize(v, -1);
    int c = centroid(v, -1, siz[v]);
    cen[c] = 1;
    for (int u : adj[c]) {
        if (cen[u])
            continue;
        rec(u);
        "<combine>";
    }
}
```

### Lowest Common Ancestor / 最近共通祖先
```cpp
vector<vector<int>> adj(N), par(LOG_N, vector<int>(N, -1));
vector<int> dep(N);

void dfs(int v, int p, int d) {
    par[0][v] = p;
    dep[v] = d;
    for (int u : adj[v]) {
        if (u!=p)
            dfs(u, v, d+1);
    }
}

void init(int n) {
    dfs(0, -1, 0);
    int l_n = int(log2(n))+1;
    for (int k=1; k<l_n; ++k) {
        for (int i=0; i<n; ++i) {
            if (par[k-1][i]==-1)
                par[k][i] = -1;
            else
                par[k][i] = par[k-1][par[k-1][i]];
        }
    }
}

int lca(int a, int b, int n) {
    if (dep[a]<dep[b])
        swap(a, b);
    int l_n = int(log2(double(n)))+1;
    for (int k=0; k<l_n; ++k) {
        if (((dep[a]-dep[b])>>k) & 1)
            a = par[k][a];
    }
    if (a==b)
        return a;
    for (int k=l_n-1; k>=0; --k) {
        if (par[k][a]!=par[k][b]) {
            a = par[k][a];
            b = par[k][b];
        }
    }
    return par[0][a];
}
```
```cpp
vector<vector<int>> adj(N);
vector<int> arr, dep(N), occ(N, -1), seg(8*N);

void dfs(int v, int p, int h) {
    dep[v] = h;
    occ[v] = arr.size();
    arr.push_back(v);
    for (int u : adj[v]) {
        if (u!=p)
            dfs(u, v, h+1);
            arr.push_back(v);
    }
}

void build(int v, int tl, int tr) {
    if (tl==tr) {
        seg[v] = arr[tl];
        return;
    }
    int tm = (tl+tr)/2;
    build(v*2+1, tl, tm);
    build(v*2+2, tm+1, tr);
    int t1=seg[v*2+1], t2=seg[v*2+2];
    seg[v] = (dep[t1]<dep[t2])?t1:t2;
}

int query(int v, int tl, int tr, int l, int r) {
    if (l>tr || r<tl)
        return -1;
    if (l==tl && r==tr)
        return seg[v];
    int tm = (tl+tr)/2;
    int q1 = query(v*2+1, tl, tm, l, min(r, tm));
    int q2 = query(v*2+2, tm+1, tr, max(l, tm+1), r);
    if (q1==-1)
        return q2;
    if (q2==-1)
        return q1;
    return (dep[q1]<dep[q2])?q1:q2;
}

void init(int s) {
    dfs(s, -1, 0);
    build(0, 0, arr.size()-1);
}

int lca(int a, int b) {
    int l=occ[a], r=occ[b];
    if (l>r)
        swap(l, r);
    return query(0, 0, arr.size()-1, l, r);
}
```

# Math / 数学

## Divisor / 約数

### Euclidean Algorithm / ユークリッドの互除法
```cpp
int gcd(int a, int b) {
    if (b==0) 
        return a;
    return gcd(b, a%b);
}
```
```cpp
int extgcd(int a, int b, int& x, int& y) {
    if (b==0) {
        x = 1;
        y = 0;
        return a;
    }
    int g, x1, y1;
    g = extgcd(b, a%b, x1, y1);
    x = y1;
    y = x1 - y1*(a/b);
    return g;
}
```

### Divisor Enumeration / 約数列挙
```cpp
vector<int> divisor(int n) {
    vector<int> res;
    for (int i=1; i*i<=n; ++i) {
        if (n%i==0) {
            res.push_back(i);
            if (n/i!=i)
                res.push_back(n/i);
        }
    }
    sort(res.begin(), res.end());
    return res;
}
```

### Prime Factorization / 素因数分解
```cpp
vector<pii> factor(int n) {
    vector<pii> res;
    for (int i=2; i*i<=n; ++i) {
        if (n%i!=0)
            continue;
        int p = 0;
        while (n%i==0) {
            n /= i;
            p += 1;
        }
        res.push_back({i, p});
    }
    if (n!=1)
        res.push_back({n, 1});
    return res;
}
```

### Euler's Totient Function / オイラー関数
```cpp
int euler_phi(int n) {
    int res = n;
    for (int i=2; i*i<=n; ++i) {
        if (n%i==0) {
            res = res * (i-1) / i;
            while (n%i==0)
                n /= i;
        }
    }
    if (n!=1)
        res = res * (n-1) / n;
    return res;
}
```

## Prime / 素数

### Primality Test / 素数判定
```cpp
bool isPrime(int n) {
    for (int i=2; i*i<=n; ++i) {
        if (n%i==0)
            return false;
    }
    return true;
}
```

### Sieve of Eratosthenes / エラトステネスの篩
```cpp
vector<bool> isPrime(N, 1);

void sieve(int n) {
    for (int i=2; i*i<=n; ++i) {
        if (!isPrime[i])
            continue;
        for (int j=i*i; j<=n; j+=i)
            isPrime[j] = 0;
    }
}
```

### Segmented Sieve / 区分篩
```cpp
vector<bool> isPrime_1(N1, 1), isPrime_2(N2, 1);

void segment_sieve(int l, int r) {
    for (int i=2; i*i<=r; ++i) {
        if (isPrime_1[i]) {
            for (int j=i*i; j*j<=r; j+=i)
                isPrime_1[j] = 0;
            for (int j=max(i*i, (l+i-1)/i*i); j<=r; j+=i)
                isPrime_2[j-l] = 0;
        }
    }
}
```

## Exponentiation / べき乗

### Fast Exponentiation / 高速累乗
```cpp
int binpow(int x, int n, int mod) {
    int res = 1;
    while (n>0) {
        if (n&1)
            res = res * x % mod;
        x = x * x % mod;
        n >>= 1;
    }
    return res;
}
```

### Matric Exponentiation / 行列累乗
```cpp
typedef vector<int> vec;
typedef vector<vec> mat;

mat matmul(mat &A, mat &B, int m) {
    mat C(A.size(), vec(B[0].size()));
    for (int i=0; i<A.size(); ++i) {
        for (int j=0; j<B[0].size(); ++j) {
            for (int k=0; k<A[0].size(); ++k)
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % m;
        }
    }
    return C;
}

mat matpow(mat A, int n, int m) {
    mat B(A.size(), vec(A.size()));
    for (int i=0; i<B.size(); ++i)
        B[i][i] = 1;
    while (n>0) {
        if (n&1)
            B = matmul(B, A, m);
        A = matmul(A, A, m);
        n >>= 1;
    }
    return B;
}
```

## Mod / 剰余

### Inverse / 逆元
```cpp
int mod_inv(int a, int m) {
    int x, y;
    extgcd(a, m, x, y);
    return ((x % m) + m) % m;
}
```

### Factorial / 階乗
```cpp
vector<int> fac(M, 1);

void init(int m) {
    for (int i=1; i<m; ++i)
        fac[i] = fac[i-1] * i % m;
}

int mod_fac(int n, int m, int& e) {
    e = 0;
    if (n==0)
        return 1;
    int r = mod_fac(n/m, m, e);
    e += n/m;
    if (n/m%2==1)
        return (m-fac[n%m]) * r % m;
    else
        return fac[n%m] * r % m;
}
```

### Binary Coefficient / 二項係数
```cpp
int mod_binom(int n, int k, int m) {
    if (n<0 || k<0 || n<k)
        return 0;
    int e1, e2, e3;
    int a1=mod_fac(n, m, e1), a2=mod_fac(n-k, m, e2), a3=mod_fac(k, m, e3);
    if (e1>e2+e3)
        return 0;
    return a1 * mod_inv(a2*a3%m, m) % m;
}
```
```cpp
vector<int> fac(N, 1), inv(N, 1), finv(N, 1);

void init(int n, int m) {
    for (int i=2; i<=n; ++i) {
        fac[i] = fac[i-1] * i % m;
        inv[i] = m - inv[m%i] * (m/i) % m;
        finv[i] = finv[i-1] * inv[i] % m;
    }
}

int mod_binom(int n, int k, int m) {
    return fac[n] * (finv[n-k] * finv[k] % m) % m; 
}
```

## Linear Algebra / 線型代数

### Linear Congruence Equation / 線形合同式
```cpp
vector<int> A(N), B(N), M(N);

pair<int, int> linear_congruence(int n) {
    int x=0, m=1;
    for (int i=0; i<n; ++i) {
        int a=A[i]*m, b=B[i]-A[i]*x, d=gcd(a, M[i]);
        if (b%d!=0)
            return {0, -1};
        int y = (b/d) * mod_inv(a/d, M[i]/d) % (M[i]/d);
        x += m*y;
        m *= M[i]/d;
    }
    return {(x%m+m)%m, m};
}
```

### Gaussian Elimination / ガウスの消去法
```cpp
vector<vector<double>> A(N, vector<double>(M));
vector<double> B(N), sol(M);

int gauss(int n, int m) {
    vector<vector<double>> mat(n, vector<double>(m+1, 0));
    for (int i=0; i<n; ++i) {
        for (int j=0; j<m; ++j)
            mat[i][j] = A[i][j];
        mat[i][m] = B[i];
    }
    vector<int> piv(m, -1);
    for (int c=0, r=0; c<m && r<n; ++c) {
        int p = r;
        for (int i=r; i<n; ++i) {
            if (abs(mat[i][c])>abs(mat[p][c]))
                p = i;
        }
        if (abs(mat[p][c])<EPS)
            continue;
        swap(mat[r], mat[p]);
        piv[c] = r;
        for (int i=0; i<n; ++i) {
            if (i==r)
                continue;
            double cf = mat[i][c] / mat[r][c];
            for (int j=c; j<=m; ++j)
                mat[i][j] -= mat[r][j] * cf;
        }
        r += 1;
    }
    for (int j=0; j<m; ++j) {
        if (piv[j]!=-1)
            sol[j] = mat[piv[j]][m] / mat[piv[j]][j];
    }
    for (int i=0; i<n; ++i) {
        double sum = 0;
        for (int j=0; j<m; ++j)
            sum += mat[i][j] * sol[j];
        if (abs(sum-mat[i][m])>EPS)
            return 0;
    }
    for (int j=0; j<m; ++j) {
        if (piv[j]==-1)
            return INF;
    }
    return 1;
}
```

### Fast Fourier Transform / 高速フーリエ変換
```cpp
using cd = complex<double>;
const double PI = acos(-1);

void fft(vector<cd>& a, bool inv=0) {
    int n = a.size();
    for (int i=1, j=0; i<n; ++i) {
        int b = n>>1;
        for (; j&b; b>>=1)
            j ^= b;
        j ^= b;
        if (i<j)
            swap(a[i], a[j]);
    }
    for (int l=2; l<=n; l*=2) {
        double ag = 2*PI / l * (inv?-1:1);
        cd wl(cos(ag), sin(ag));
        for (int i=0; i<n; i+=l) {
            cd w(1);
            for (int j=0; j<l/2; ++j) {
                cd u=a[i+j], v=a[i+j+l/2]*w;
                a[i+j] = u+v;
                a[i+j+l/2] = u-v;
                w *= wl;
            }
        }
    }
    if (inv) {
        for (int i=0; i<n; ++i)
            a[i] /= n;
    }
}

vector<int> multiply(vector<int> a, vector<int> b) {
    vector<cd> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    int n = 1;
    while (n<a.size()+b.size())
        n *= 2;
    fa.resize(n);
    fb.resize(n);
    fft(fa);
    fft(fb);
    for (int i=0; i<n; ++i) 
        fa[i] *= fb[i];
    fft(fa, 1);
    vector<int> res(n);
    for (int i=0; i<n; ++i)
        res[i] = round(fa[i].real());
    return res;
}
```

# Others / その他の

## Geometry / 幾何

### Geometry Library / 幾何ライブラリ
```cpp
using Point = complex<double>;

double dot(const Point &a, const Point &b) {
    return a.real()*b.real() + a.imag()*b.imag();
}

double det(const Point &a, const Point &b) {
    return a.real()*b.imag() - a.imag()*b.real();
}

bool compare(const Point &a, const Point &b) {
    return a.real()!=b.real() ? a.real()<b.real() : a.imag()<b.imag();
}

struct Line {
    Point a, b;
    Line() = default;
    Line(Point a, Point b) : a(a), b(b) {}
};

struct Segment : Line {
    Segment() = default;
    Segment(Point a, Point b) : Line(a, b) {}
};

struct Circle {
    Point p;
    double r;
    Circle() = default;
    Circle(Point p, double r) : p(p), r(r) {}
};
```
```cpp
int ccw(Point a, Point b, Point c) {
    b -= a, c -= a;
    if (det(b, c)>EPS)
        return +1;
    if (det(b, c)<-EPS)
        return -1;
    if (dot(b, c)<-EPS)
        return +2;
    if (norm(b)<norm(c)-EPS)
        return -2;
    return 0;
}

bool intersect(Segment s, Point p) {
    return ccw(s.a, s.b, p) == 0;
}

bool intersect(Segment s, Segment t) {
    return ccw(s.a, s.b, t.a)*ccw(s.a, s.b, t.b)<=0 && ccw(t.a, t.b, s.a)*ccw(t.a, t.b, s.b)<=0;
}

bool intersect(Line l, Point p) {
    return abs(ccw(l.a, l.b, p))!=1;
}

bool intersect(Line l, Segment s) {
    return det(l.b-l.a, s.a-l.a)*det(l.b-l.a, s.b-l.a)<EPS;
}

int intersect(Line l, Line m) {
    if (intersect(l, m.a) && intersect(l, m.b))
        return 2;
    if (abs(det(l.b-l.a, m.b-m.a))>EPS)
        return 1;
    return 0;
}

Point projection(Line l, Point p) {
    double t = dot(p-l.a, l.b-l.a)/norm(l.b-l.a);
    return l.a + (l.b-l.a)*t;
}

Point reflection(Line l, Point p) {
    return p + (projection(l, p)-p)*2.0;
}

Point crosspoint(Line l, Line m) {
    double A = det(l.b-l.a, m.b-m.a);
    double B = det(l.b-l.a, l.b-m.a);
    if (A==0)
        return Point(1/EPS, 1/EPS);
    return m.a + (m.b-m.a)*B/A;
}

double distance(Point a, Point b) {
    return abs(b-a);
}

double distance(Segment s, Point p) {
    Line l(s.a, s.b);
    Point h = projection(l, p);
    if (intersect(s, h))
        return abs(p-h);
    return min(abs(s.a-p), abs(s.b-p));
}

double distance(Segment s, Segment t) {
    if (intersect(s, t))
        return 0;
    return min({distance(s, t.a), distance(s, t.b), distance(t, s.a), distance(t, s.b)});
}

double distance(Line l, Point p) {
    return abs(det(p-l.a, l.b-l.a))/abs(l.b-l.a);
}

double distance(Line l, Segment s) {
    if (intersect(l, s))
        return 0;
    return min(distance(l, s.a), distance(l, s.b));
}

double distance(Line l, Line m) {
    if (intersect(l, m))
        return 0;
    return distance(l, m.a);
}
```
```cpp
int intersect(Circle c, Line l) {
    Point h = l.a + (l.b-l.a) * dot(c.p-l.a, l.b-l.a)/norm(l.b-l.a);
    double d = abs(c.p-h);
    if (c.r<d-EPS)
        return 0;
    if (abs(c.r-d)<EPS)
        return 1;
    return 2;
}

int intersect(Circle c1, Circle c2) {
    double d = abs(c1.p-c2.p);
    if (c1.r+c2.r<d-EPS)
        return 4;
    if (abs(c1.r+c2.r-d)<EPS)
        return 3;
    if (abs(abs(c1.r-c2.r)-d)<EPS)
        return 1;
    if (abs(c1.r-c2.r)>d+EPS)
        return 0;
    return 2;
}

vector<Point> crosspoint(Circle c, Line l) {
    vector<Point> res;
    Point h = l.a + (l.b-l.a) * dot(c.p-l.a, l.b-l.a)/norm(l.b-l.a);
    int mode = intersect(c, l);
    if (mode==1) {
        res.push_back(h);
    }
    if (mode==2) {
        double b = sqrt(c.r*c.r-norm(h-c.p));
        Point e = (l.b-l.a)/abs(l.b-l.a);
        res.push_back(h-e*b);
        res.push_back(h+e*b);
    }
    return res;
}

vector<Point> crosspoint(Circle c1, Circle c2) {
    vector<Point> res;
    double d = abs(c2.p-c1.p);
    int mode = intersect(c1, c2);
    if (mode==3) {
        res.push_back(c1.p + (c2.p-c1.p)*c1.r/(c1.r+c2.r));
    }
    if (mode==1) {
        if (c2.r<c1.r-EPS)
            res.push_back(c1.p + (c2.p-c1.p)*c1.r/d);
        else 
            res.push_back(c2.p + (c1.p-c2.p)*c2.r/d);
    }
    if (mode==2) {
        double a = (c1.r*c1.r+d*d-c2.r*c2.r) / (2*d);
        double b = sqrt(c1.r*c1.r-a*a);
        Point e = (c2.p-c1.p)/abs(c2.p-c1.p);
        res.push_back(c1.p + e*a - e*Point(0, 1)*b);
        res.push_back(c1.p + e*a + e*Point(0, 1)*b);
    }
    return res;
}

vector<Line> tangent(Circle c, Point p) {
    vector<Line> res;
    double d = abs(p-c.p);
    if (abs(d-c.r)<EPS) {
        res.push_back(Line(p, p+(p-c.p)*Point(0, 1)));
    }
    if (d>c.r+EPS) {
        vector<Point> cp = crosspoint(c, Circle(p, sqrt(d*d-c.r*c.r)));
        res.push_back(Line(cp[0], p));
        res.push_back(Line(cp[1], p));
    }
    return res;
}

vector<Line> tangent(Circle c1, Circle c2) {
    vector<Line> res;
    double d = abs(c2.p-c1.p);
    Point u = (c2.p-c1.p)/abs(c2.p-c1.p);
    Point v = u*Point(0, 1);
    for (int s : {-1, 1}) {
        if (abs(d)<EPS)
            break;
        double cs = (c1.r+c2.r*s)/d;
        if (abs(cs*cs-1)<EPS) {
            Point U = (cs>0 ? u : -u);
            res.push_back(Line(c1.p+U*c1.r, c1.p+U*c1.r+v));
        }
        else if (1-cs*cs>EPS) {
            Point U = u*cs, V=v*sqrt(1-cs*cs);
            res.push_back(Line(c1.p+(U+V)*c1.r, c2.p-(U+V)*(c2.r*s)));
            res.push_back(Line(c1.p+(U-V)*c1.r, c2.p-(U-V)*(c2.r*s)));
        }
    }
    return res;
}
```
```cpp
int contain(vector<Point> g, Point p) {
    bool in = false;
    int n = g.size();
    for (int i=0; i<n; ++i) {
        Point a=g[i]-p, b=g[(i+1)%n]-p;
        if (a.imag()>b.imag())
            swap(a, b);
        if (a.imag()<EPS && b.imag()>EPS && det(a, b)>EPS)
            in = !in;
        if (abs(det(a, b))<EPS && dot(a, b)<EPS)
            return 1;
    }
    return (in ? 2 : 0);
}

double area(vector<Point> g) {
    double a = 0;
    int n = g.size();
    for (int i=0; i<n; ++i)
        a += det(g[i], g[(i+1)%n]);
    return a*0.5;
}
```

### Convex Hull / 凸包
```cpp
vector<Point> convex_hull(vector<Point> ps) {
    sort(ps.begin(), ps.end(), compare);
    int n=ps.size(), k=0;
    vector<Point> qs(2*n);
    for (int i=0; i<n; ++i) {
        while (k>1 && det(qs[k-1]-qs[k-2], ps[i]-qs[k-1])<EPS)
            k--;
        qs[k++] = ps[i];
    }
    for (int i=n-2, t=k; i>=0; --i) {
        while (k>t && det(qs[k-1]-qs[k-2], ps[i]-qs[k-1])<EPS)
            k--;
        qs[k++] = ps[i];
    }
    qs.resize(k-1);
    return qs;
}
```
```cpp
double max_distance(vector<Point> ps) {
    vector<Point> qs = convex_hull(ps);
    if (qs.size()==2)
        return abs(qs[1]-qs[0]);
    int i=0, j=0, n=qs.size();
    for (int k=0; k<n; ++k) {
        if (compare(qs[k], qs[i]))
            i = k;
        if (!compare(qs[k], qs[j]))
            j = k;
    }
    double res = 0;
    int si=i, sj=j;
    while (i!=sj || j!=si) {
        res = max(res, abs(qs[j]-qs[i]));
        if (det(qs[(i+1)%n]-qs[i], qs[(j+1)%n]-qs[j])<-EPS)
            i = (i+1)%n;
        else
            j = (j+1)%n;
    }
    return res;
}
```

### Sweep Line / 平面走査
```cpp
void solve(int n) {
    vector<pair<double, int>> v;
    for (int i=0; i<n; ++i) {
        v.push_back({"<x_left[i]>", i});
        v.push_back({"<x_right[i]>", i+n});
    }
    sort(v.begin(), v.end());
    set<pair<double, int>> s;
    for (auto p : v) {
        int i = p.second%n;
        if (p.second<n) {
            set<pair<double, int>>::iterator it = "<binary search y[i]>";
            "<construct solution>":
            s.insert({"<y[i]>", i});
        }
        else
            s.erase({"<y[i]>", i});
    }
}
```

### Plane Divide and Conquer / 平面の分割統治法
```cpp
using Point = complex<double>;

bool compare_x(const Point &a, const Point &b) {
    return a.real()<b.real();
}

bool compare_y(const Point &a, const Point &b) {
    return a.imag()<b.imag();
}

vector<Point> ps;

void rec(int l, int r) {
    if (l==r)
        "<base case>";
    int m = (l+r)/2;
    rec(l, m);
    rec(m+1, r);
    inplace_merge(ps.begin()+l, ps.begin()+m+1, ps.begin()+r+1, compare_y);
    "<combine>";
}

sort(ps.begin(), ps.end(), compare_x);
```

## String / 文字列

### Rolling Hash / ローリングハッシュ
```cpp
ll hashing(string s) {
    ll p = 257, m = 1e9+9;
    ll h = 0;
    for (char c : s)
        h = (h*p + c) % m;
    return h;
}
```
```cpp
int search(string s, string t) {
    int sl=s.size(), tl=t.size();
    ll p = 257, m = 1e9+9, pp=1, sh=0, th=0;
    for (int i=0; i<tl; ++i) {
        pp = (pp*p) % m;
        sh = (sh*p + s[i]) % m;
        th = (th*p + t[i]) % m;
    }
    for (int i=0; i+tl<=sl; ++i) {
        if (sh==th)
            return i;
        if (i+tl<sl)
            sh = (sh*p + s[i+tl] - s[i]*pp + m) % m;
    }
    return -1;
}
```

### Suffix Array / 接尾辞配列
```cpp
vector<int> suffix_array(string s) {
    s += '$';
    int n=s.size(), cls=256;
    vector<int> p(n), c(n), cnt(max(256, n)), pn(n), cn(n);
    for (int i=0; i<n; ++i) {
        p[i] = i;
        c[i] = s[i];
    }
    for (int h=1; h<=n; h*=2) {
        for (int i=0; i<n; ++i)
            p[i] = (p[i]+n-h/2)%n;
        fill(cnt.begin(), cnt.begin()+cls, 0);
        for (int i=0; i<n; ++i)
            cnt[c[p[i]]] += 1;
        for (int i=1; i<cls; ++i)
            cnt[i] += cnt[i-1];
        for (int i=n-1; i>=0; --i)
            pn[--cnt[c[p[i]]]] = p[i];
        cn[pn[0]] = 0;
        cls = 1;
        for (int i=1; i<n; ++i) {
            pair<int,int> cur = {c[pn[i]], c[(pn[i]+h/2)%n]};
            pair<int,int> pre = {c[pn[i-1]], c[(pn[i-1]+h/2)%n]};
            if (cur!=pre)
                cls += 1;
            cn[pn[i]] = cls-1;
        }
        p.swap(pn);
        c.swap(cn);
    }
    return p;
}
```
```cpp
int search(string s, string t, vector<int> sa) {
    int l=-1, r=sa.size();
    while (r-l>1) {
        int m = (l+r)/2;
        if (s.compare(sa[m], t.size(), t)>0)
            r = m;
        else
            l = m;
    }
    return s.compare(sa[l], t.size(), t)==0 ? sa[l] : -1;
}
```

## Game / ゲーム

### Nim / Nim
```cpp
vector<int> arr(N);

bool nim(int n) {
    int x = 0;
    for (int i=0; i<n; ++i)
        x ^= arr[i];
    return x > 0;
}
```

### Grundy Number / Grundy数
```cpp
vector<int> gru(X);

void build(int x) {
    for (int i=1; i<=x; ++i) {
        set<int> s;
        for ("<next state>") {
            s.insert(gru["<next state>"]);
        }
        int g = 0;
        while (s.count(g)>0)
            g += 1;
        gru[i] = g;
    }
}
```

## Technique / テクニック

### Prefix Sum / 累積和
```cpp
vector<int> arr(N), sum(N);

void build(int n) {
    for (int i=0; i<n; ++i)
        sum[i+1] = sum[i] + arr[i];
}

int query(int l, int r) {
    return sum[r+1] - sum[l];
}
```

### Two Pointers / しゃくとり法
```cpp
vector<int> arr(N);

void solve(int n) {
    int i="<>", j="<>";
    while ("<>") {
        while ("<>") {
            "<modify i>";
            "<update>":
        }
        "<modify j>";
        "<update>":
    }
}
```

### Meet in the Middle / 半分全列挙
```cpp
void solve(int n) {
    vector<int> s;
    for ("<1st half>")
        s.push_back("<>");
    sort(s.begin(), s.end());
    for ("<2nd half>")
        "<binary search>";
}
```

### Coordinate Compression / 座標圧縮
```cpp
int compress(int n, vector<int> &x1, vector<int> &x2, int w) {
    vector<int> xs;
    for (int i=0; i<n; ++i) {
        for (int d=-1; d<=1; ++d) {
            int t1=x1[i]+d, t2=x2[i]+d;
            if (0<=t1 && t1<w)
                xs.push_back(t1);
            if (0<=t2 && t2<w)
                xs.push_back(t2);
        }
    }
    sort(xs.begin(), xs.end());
    xs.erase(unique(xs.begin(), xs.end()), xs.end());
    for (int i=0; i<n; ++i) {
        x1[i] = find(xs.begin(), xs.end(), x1[i]) - xs.begin();
        x2[i] = find(xs.begin(), xs.end(), x2[i]) - xs.begin();
    }
    return xs.size();
}
```

### Binary Lifting / ダブリング
```cpp
vector<vector<int>> nex(LOG_K, vector<int>(N));

void build(int n, int k) {
    for (int i=0; i<n; ++i)
        nex[0][i] = "<next position>";
    for (int i=1; i<int(log2(k))+1; ++i) {
        for (int j=0; j<n; ++j)
            nex[i][j] = nex[i-1][nex[i-1][j]];
    }
}

int query(int p, int d) {
    for (int i=0; d>0; ++i, d>>=1) {
        if (d&1)
            p = nex[i][p];
    }
    return p;
}
```