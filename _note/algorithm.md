---
title: 'Algorithm'
date: 2023-01-01
permalink: /note/algorithm
tags:
  - note
toc: true
---

Templates of Algorithm

{% include toc %}

# General / 一般

## Brute-Force / 全探索

### Bit Exhaustive Search / ビット全探索
```cpp
ll arr[N];

void search(ll n) {
    for (ll s=0; s<(1LL<<n); ++s) {
        for (ll i=0; i<n; ++i) {
            if (s&(1LL<<i))
                "arr[i]...";
        }
    }
}
```

### Permutation Exhaustive Search / 順列全探索
```cpp
ll arr[N];

void search(ll n) {
    sort(arr, arr + n);
    do {
        for (ll i=0; i<n; ++i)
            "arr[i]...";
    } while (next_permutation(arr, arr+n));
}
```

### DFS Exhaustive Search / DFS全探索
```cpp
ll arr[N];

void search(ll p, ll n) {
    if (p==n) {
        for (ll i=0; i<n; ++i)
            "arr[i]...";
        return;
    }
    for ("next value i") {
        if ("pruning")
            continue;
        arr[p] = i;
        search(p+1, n);
        arr[p] = 0;
    }
}
```
```cpp
ll arr[N];

bool search(ll p, ll n) {
    if (p==n) {
        if ("satisfied")
            return true;
        return false;
    }
    for ("next value i") {
        if ("pruning")
            continue;
        arr[p] = i;
        if (search(p+1, n))
            return true;
        arr[p] = 0;
    }
    return false;
}
```

## Greedy Algorithm / 貪欲法

### Greedy Algorithm / 貪欲法
```cpp
void solve() {
    "preprocess";
    for (ll i=0; i<N; ++i) {
        "optimize";
    }
}
```

## Dynamic Programming / 動的計画法

### Knapsack DP / ナップサックDP
```cpp
ll arr[N];
ll dp[N][M];

void solve(ll n, ll m) {
    "base (dp[i][0])";
    for (ll i=1; i<=n; ++i) {
        for (ll j=1; j<=m; ++j) {
            "update dp[i][j] with dp[i-1][f(arr[i-1])]";
        }
    }
}
```

### Digit Dp / 桁DP
```cpp
ll arr[N];
ll dp[N][M][2];

void solve(ll n, ll m) {
    "base (dp[0][0][1])";
    for (ll i=0; i<n; ++i) {
        for (ll j=0; j<=m; ++j) {
            "transfer dp[i][j][0] to dp[i+1][f(0~9)       ][0]";
            "transfer dp[i][j][1] to dp[i+1][f(0~arr[i]-1)][0]";
            "transfer dp[i][j][1] to dp[i+1][f(arr[i])    ][1]";
        }
    }
}
```

### llerval DP / 区間DP
```cpp
ll arr[N];
ll dp[N][N]; // fill -1

"base (dp[i][i], dp[i][i+1])";

ll rec(ll l, ll r) {
    if (dp[l][r]!=-1)
        return dp[l][r];
    "update dp[l][r] with rec(l, i), rec(i+1, r), rec(l+1, r-1)";
    return dp[l][r];
}
```

### Bit DP / ビットDP
```cpp
ll arr[N];
ll dp[2^N][N]; // fill -1

"base (dp[1LL<<i][i], dp[s][0])";

ll rec(ll s, ll v) {
    if (dp[s][v]!=-1)
        return dp[s][v];
    "update dp[s][v] with rec(s^(1LL<<v), i)";
    return dp[s][v];
}
```

## Binary Search / 二分探索

### Binary Search / 二分探索
```cpp
ll arr[M];
bool check(ll x);

ll search(ll n, ll t) {
    ll l=-1, r=n;
    while (r-l>1) {
        ll m = l + (r-l)/2;
        if (t<arr[m]) // if (check(m))
            r = m;
        else
            l = m;
    }
    return r; // arr[l] <= t < arr[r]
}
```
```cpp
ll a[N];
vector<ll> v; // deque
set<ll> s; // map

void search(ll n, ll t) {
    sort(a, a+n);
    ll lb = lower_bound(a, a+n, t) - a; // first >= t
    ll ub = upper_bound(a, a+n, t) - a; // first > t
}

void search(ll t) {
    sort(v.begin(), v.end());
    ll lb = lower_bound(v.begin(), v.end(), t) - v.begin(); // first >= t
    ll ub = upper_bound(v.begin(), v.end(), t) - v.begin(); // first > t
}

void search(ll t) {
    auto li = s.lower_bound(t); // first >= t
    auto ui = s.upper_bound(t); // first > t
}
```

### Ternary Search / 三分探索
```cpp
ll arr[N];

ll search(ll n) {
    ll l=-1, r=n;
    while (r-l>2) {
        ll m1 = l + (r-l)/3;
        ll m2 = r - (r-l)/3;
        if (arr[m1]<arr[m2])
            l = m1;
        else
            r = m2;
    }
    return l+1; // peak
}
```

## Data Structure / データ構造

### Standard Library / 標準ライブラリ
```cpp
void binary_heap() {
    priority_queue<ll> q;
    // priority_queue<ll, vector<ll>, greater<ll>> q;
    q.push("value");
    q.pop();
    ll "value" = q.top();
}
```
```cpp
void binary_search_tree() {
    set<ll> s;
    s.insert("value");
    s.erase("value");
    auto "iterator" = s.find("value");
}

void binary_search_tree() {
    map<ll, ll> m;
    m["key"] = "value";
    ll "value" = map["key"];
    auto "iterator" = m.find("key");
}
```
```cpp
void hash_table() {
    unordered_set<ll> s;
    s.insert("value");
    s.erase("value");
    auto "iterator" = s.find("value");
}

void hash_table() {
    unordered_map<ll, ll> m;
    m["key"] = "value";
    ll "value" = m["key"];
    auto "iterator" = m.find("key");
}
```

### Disjoll Set Union / Union-Find木
```cpp
ll par[N], siz[N];

void make_set(ll n) {
    for (ll i=0; i<n; ++i) {
        par[i] = i;
        siz[i] = 1;
    }
}

ll find_set(ll v) {
    if (par[v] == v)
        return v;
    return par[v] = find_set(par[v]);
}

void union_set(ll a, ll b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (siz[a] < siz[b])
            swap(a, b);
        par[b] = a;
        siz[a] += siz[b];
    }
}
```

### Prefix Sum / 累積和
```cpp
ll arr[N], pre[N];

void build(ll n) {
    // for (l~r: k) {
    //     pre[l] += k;
    //     pre[r+1] -= k;
    // }
    for (ll i=1; i<=n; ++i) {
        pre[i] = pre[i-1] + arr[i];
        // pre[i] += pre[i-1];
    }
}

ll query(ll l, ll r) {
    return pre[r]-pre[l-1];
    // return pre[p];
}
```
```cpp
ll arr[H][W], pre[H][W];

void build(ll h, ll w) {
    // for ("x1~x2, y1~y2: k") {
    //     pre[x1][y1] += k;
    //     pre[x2+1][y1] -= k;
    //     pre[x1][y2+1] -= k;
    //     pre[x2+1][y2+1] += k;
    // }
    for (ll i=1; i<=h; ++i) {
        for (ll j=1; j<=w; ++j) {
            pre[i][j] = pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1] + arr[i][j];
            // pre[i][j] += pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1];
        }
    }
}

ll query(ll x1, ll y1, ll x2, ll y2) {
    return pre[x2][y2]-pre[x1-1][y2]-pre[x2][y1-1]+pre[x1-1][y1-1];
    // return pre[x][y];
}
```

### Fenwick Tree　/ フェニック木
```cpp
ll arr[N], tree[N];

void build(ll n) {
    for (ll i = 1; i <= n; ++i) {
        tree[i] += arr[i];
        ll r = i + (i&-i);
        if (r <= n)
            tree[r] += tree[i];
    }
}

void update(ll p, ll x, ll n) {
    while (p <= n) {
        tree[p] += x;
        p += (p&-p);
    }
}

ll query(ll l, ll r) {
    ll s = 0;
    while (r > 0) {
        s += tree[r];
        r -= (r&-r);
    }
    l -= 1;
    while (l > 0) {
        s -= tree[l];
        l -= (l&-l);
    }
    return s;
}

ll bound(ll t, ll n) {
    ll p = 0;
    ll s = 1;
    while (s<<1 <= n)
        s <<= 1;
    for (; s>0; s>>=1) {
        if (p+s<=n && tree[p+s]<t) { // or <=t
            p += s;
            t -= tree[p];
        }
    }
    return p+1; // first [1,r] >= t or >t
}
```

### Segment Tree / セグメント木
```cpp
ll arr[N], tree[4*N];

ll merge(ll a, ll b) {
    return "merge a and b";
}

void build(ll v, ll tl, ll tr) {
    if (tl==tr) {
        tree[v] = arr[tl];
        return;
    }
    ll tm = (tl+tr)/2;
    build(v*2+1, tl, tm);
    build(v*2+2, tm+1, tr);
    tree[v] = merge(tree[v*2+1], tree[v*2+2]);
}

void update(ll v, ll tl, ll tr, ll p, ll x) {
    if (tl==tr) {
        tree[v] += x; // = for set
        return;
    }
    ll tm = (tl+tr)/2;
    if (p<=tm)
        update(v*2+1, tl, tm, p, x);
    else
        update(v*2+2, tm+1, tr, p, x);
    tree[v] = merge(tree[v*2+1], tree[v*2+2]);
}

ll query(ll v, ll tl, ll tr, ll l, ll r) {
    if (tl==l && tr==r)
        return tree[v];
    ll tm = (tl+tr)/2;
    if (r<=tm)
        return query(v*2+1, tl, tm, l, r);
    if (l>tm)
        return query(v*2+2, tm+1, tr, l, r);
    ll q1 = query(v*2+1, tl, tm, l, tm);
    ll q2 = query(v*2+2, tm+1, tr, tm+1, r);
    return merge(q1, q2);
}
```
```cpp
ll arr[N], tree[4*N], lazy[4*N];

ll merge(ll a, ll b) {
    return "merge a and b";
}

void push(ll v, ll tl, ll tr) {
    // if (lazy[v]==INF) return; for set
    ll tm = (tl+tr)/2;
    tree[v*2+1] += "lazy[v] or lazy[v]*(tm-tl+1)"; // = for set
    tree[v*2+2] += "lazy[v] or lazy[v]*(tr-tm)  "; // = for set
    lazy[v*2+1] += lazy[v]; // = for set
    lazy[v*2+2] += lazy[v]; // = for set
    lazy[v] = 0; // INF for set;
}

void build(ll v, ll tl, ll tr) {
    if (tl==tr) {
        tree[v] = arr[tl];
        return;
    }
    ll tm = (tl+tr)/2;
    build(v*2+1, tl, tm);
    build(v*2+2, tm+1, tr);
    tree[v] = merge(tree[v*2+1], tree[v*2+2]);
}

void update(ll v, ll tl, ll tr, ll l, ll r, ll x) {
    if (tl==l && tr==r) {
        tree[v] += "x or x*(tr-tl+1)"; // = for set
        lazy[v] += x; // = for set
        return;
    }
    push(v, tl, tr);
    ll tm = (tl+tr)/2;
    if (r<=tm)
        update(v*2+1, tl, tm, l, r, x);
    else if (l>tm)
        update(v*2+2, tm+1, tr, l, r, x);
    else {
        update(v*2+1, tl, tm, l, tm, x);
        update(v*2+2, tm+1, tr, tm+1, r, x);
    }
    tree[v] = merge(tree[v*2+1], tree[v*2+2]);
}

ll query(ll v, ll tl, ll tr, ll l, ll r) {
    if (tl==l && tr==r)
        return tree[v];
    push(v, tl, tr);
    ll tm = (tl+tr)/2;
    if (r<=tm)
        return query(v*2+1, tl, tm, l, r);
    if (l>tm)
        return query(v*2+2, tm+1, tr, l, r);
    ll q1 = query(v*2+1, tl, tm, l, tm);
    ll q2 = query(v*2+2, tm+1, tr, tm+1, r);
    return merge(q1, q2);
}
```

# Graph / グラフ

## Graph Traversal / グラフ探索

### Depth First Search / 深さ優先探索
```cpp
vector<ll> adj[N];
ll vis[N], dis[N], par[N];
// fill dis INF, fill par -1

void dfs(ll v, ll d, ll p) {
    vis[v] = 1;
    dis[v] = d;
    par[v] = p;
    for (ll u : adj[v]) {
        // if (u!=p && vis[u])
        //     "cycle from u (undirected)";
        if (!vis[u]) { // tree: if (u!=p)
            dfs(u, d+1, v);
        }
    }
}
```
```cpp
vector<ll> adj[N];
ll col[N], tmi[N], tmo[N];
ll tmr;

void dfs(ll v) {
    col[v] = 1;
    tmi[v] = tmr++;
    for (ll u : adj[v]) {
        // if (col[u]==1)
        //     "cycle from u (directed)";
        if (col[u]==0) {
            dfs(u);
        }
    }
    col[v] = 2;
    tmo[v] = tmr++;
}
```

### Breadth First Search / 幅優先探索
```cpp
vector<ll> adj[N];
ll vis[N], dis[N], par[N];
// fill dis INF, fill par -1

void bfs(ll s) {
    queue<ll> q;
    vis[s] = 1;
    dis[s] = 0;
    par[s] = -1;
    q.push(s);
    while (!q.empty()) {
        ll v = q.front();
        q.pop();
        for (ll u : adj[v]) {
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
```cpp
vector<pll> adj[N];
ll vis[N], dis[N], par[N];
// fill dis INF, fill par -1

void bfs(ll s) {
    deque<ll> q;
    dis[s] = 0;
    par[s] = -1;
    q.push_front(s);
    while (!q.empty()) {
        ll v = q.front();
        q.pop_front();
        if (vis[v])
            continue;
        vis[v] = 1;
        for (pll e : adj[v]) {
            ll u = e.first;
            ll w = e.second;
            if (dis[v]+w<dis[u]) {
                dis[u] = dis[v] + w;
                par[u] = v;
                if (w==1)
                    q.push_back(u);
                else
                    q.push_front(u);
            }
        }
    }
}
```

### Topological Sort / トポロジカルソート
```cpp
vector<ll> adj[N];
vector<ll> vis(N), arr;

void dfs(ll v) {
    vis[v] = 1;
    for (ll u : adj[v]) {
        if (!vis[u])
            dfs(u);
    }
    arr.push_back(v);
}

void topological_sort(ll n) {
    for (ll i=1; i<=n; ++i) {
        if (!vis[i])
            dfs(i);
    }
    reverse(arr.begin(), arr.end());
}
```
```cpp
vector<ll> adj[N];
vector<ll> idg(N), arr;

void topological_sort(ll n) {
    for (ll i=1; i<=n; ++i) {
        for (ll j : adj[i])
            idg[j] += 1;
    }
    queue<ll> q;
    for (ll i=1; i<=n; ++i) {
        if (idg[i]==0)
            q.push(i);
    }
    while (!q.empty()) {
        ll v = q.front();
        q.pop();
        arr.push_back(v);
        for (ll u : adj[v]) {
            idg[u] -= 1;
            if (idg[u]==0)
                q.push(u);
        }
    }
    // if (arr.size()<n)
    //     "cycle (directed)";
}
```

## Connectivity / 連結性

### Connected Component / 連結成分
```cpp
vector<ll> adj[N];
ll vis[N], com[N];

void dfs(ll v, ll c) {
    vis[v] = 1;
    com[v] = c;
    for (ll u : adj[v]) {
        if (!vis[u])
            dfs(u, c);
    }
}

void solve(ll n) {
    for (ll i=1; i<=n; ++i) {
        if (!vis[i])
            dfs(i, i);
    }
}
```

### Strongly Connected Component / 強連結成分
```cpp
vector<ll> adj[N], adj_r[N];
vector<ll> arr, vis(N), com(N);

void dfs1(ll v) {
    vis[v] = 1;
    for (ll u : adj[v]) {
        if (!vis[u])
            dfs1(u);
    }
    arr.push_back(v);
}

void dfs2(ll v, ll c) {
    vis[v] = 1;
    com[v] = c;
    for (ll u : adj_r[v]) {
        if (!vis[u])
            dfs2(u, c);
    }
}

void solve(ll n) {
    for (ll i=1; i<=n; ++i) {
        if (!vis[i])
            dfs1(i);
    }
    reverse(arr.begin(), arr.end());
    fill(vis.begin(), vis.end(), 0);
    for (ll v : arr) {
        if (!vis[v]) {
            dfs2(v, v);
        }
    }
}
```

### Bridge / 橋
```cpp
vector<ll> adj[N];
ll vis[N], tin[N], low[N];
ll tmr;

void dfs(ll v, ll p) {
    vis[v] = 1;
    tin[v] = low[v] = tmr++;
    for (ll u : adj[v]) {
        if (u==p)
            continue;
        if (vis[u])
            low[v] = min(low[v], tin[u]);
        else {
            dfs(u, v);
            low[v] = min(low[v], low[u]);
            if (low[u]>tin[v]) {
                "bridge: v-u ";
            }
        }
    }
}
```

### Articulation Point / 関節点
```cpp
vector<ll> adj[N];
ll vis[N], tin[N], low[N];
ll tmr;

void dfs(ll v, ll p) {
    vis[v] = 1;
    tin[v] = low[v] = tmr++;
    ll chd = 0;
    for (ll u : adj[v]) {
        if (u==p)
            continue;
        if (vis[u])
            low[v] = min(low[v], tin[u]);
        else {
            dfs(u, v);
            low[v] = min(low[v], low[u]);
            if (p!=-1 && low[u]>=tin[v]) {
                "articulation point: v";
            }
            chd += 1;
        }
    }
    if (p==-1 && chd>1) {
        "articulation point: v";
    }
}
```

## Shortest Path / 最短経路

### Dijkstra's Algorithm / ダイクストラ法
```cpp
vector<pll> adj[N];
ll vis[N], dis[N], par[N];
// fill dis INF, fill par -1

void dijkstra(ll s) {
    priority_queue<pll, vector<pll>, greater<pll>> q;
    dis[s] = 0;
    par[s] = -1;
    q.push({0, s});
    while (!q.empty()) {
        ll v = q.top().second;
        q.pop();
        if (vis[v])
            continue;
        vis[v] = 1;
        for (pll e : adj[v]) {
            ll u = e.first;
            ll w = e.second;
            if (dis[v]+w<dis[u]) {
                dis[u] = dis[v]+w;
                par[u] = v;
                q.push({dis[v]+w, u});
            }
        }
    }
}
```
```cpp
ll adj[N][N];
ll vis[N], dis[N], par[N];
// fill dis INF, fill par -1

void dijkstra(ll s, ll n) {
    dis[s] = 0;
    par[s] = -1;
    for (ll i=0; i<n; ++i) {
        ll v = -1;
        for (ll j=1; j<=n; ++j) {
            if (!vis[j] && (v==-1 || dis[j]<dis[v]))
                v = j;
        }
        if (dis[v]==INF)
            break;
        vis[v] = 1;
        for (ll u=1; u<=n; ++u) {
            if (adj[v][u]<INF && dis[v]+adj[v][u]<dis[u]) {
                dis[u] = dis[v]+adj[v][u];
                par[u] = v;
            }
        }
    }
}
```

### Bellman–Ford Algorithm / ベルマン–フォード法
```cpp
struct edge{
    ll a, b, w;
};

vector<edge> edges;
ll dis[N], par[N];
// fill dis INF, fill par -1

void bellman_ford(ll s, ll n) {
    dis[s] = 0;
    par[s] = -1;
    ll x = -1;
    for (ll i=0; i<n; ++i) {
        x = -1;
        for (edge e : edges) {
            if (dis[e.a]<INF && dis[e.a]+e.w<dis[e.b]) {
                dis[e.b] = dis[e.a] + e.w;
                par[e.b] = e.a;
                x = e.b;
            }
        }
        if (x==-1)
            break;
    }
    // if (x!=-1) {
    //     for (ll i=0; i<n; ++i)
    //         x = par[x];
    //     "negative cycle from x";
    // }
}
```

### Floyd–Warshall Algorithm / ワーシャル–フロイド法
```cpp
ll dis[N][N], par[N][N];
// fill dis INF, fill par -1

void floyd_warshall(ll n) {
    "for edge: dis[v][u]=w, par[v][u]=v";
    "for vert: dis[v][v]=0, par[v][v]=v";
    for (ll k=1; k<=n; ++k) {
        for (ll i=1; i<=n; ++i) {
            for (ll j=1; j<=n; ++j) {
                if (dis[i][k]<INF && dis[k][j]<INF && dis[i][k]+dis[k][j]<dis[i][j]) {
                    dis[i][j] = dis[i][k] + dis[k][j];
                    par[i][j] = par[k][j];
                }
            }
        }
    }
    // for (ll i=0; i<n; ++i)
    //     if (dis[i][i]<0) 
    //         "negative cycle from i";
}
```

## Minimum Spanning Tree / 最小全域木

### Prim's Algorithm / プリム法
```cpp
vector<pll> adj[N];
ll vis[N], dis[N], par[N];
// fill dis INF, fill par -1

ll prim(ll s, ll n) {
    ll wt = 0;
    ll cnt = 0;
    priority_queue<pll, vector<pll>, greater<pll>> q;
    dis[s] = 0;
    par[s] = -1;
    q.push({0, s});
    while (!q.empty()) {
        ll v = q.top().second;
        q.pop();
        if (vis[v])
            continue;
        vis[v] = 1;
        cnt += 1;
        wt += dis[v];
        for (pll e : adj[v]) {
            ll u = e.first;
            ll w = e.second;
            if (!vis[u] && w<dis[u]) {
                dis[u] = w;
                par[u] = v;
                q.push({dis[u], u});
            }
        }
    }
    if (cnt<n)
        return INF;
    return wt;
}
```
```cpp
ll adj[N][N];
ll vis[N], dis[N], par[N];
// fill dis INF, fill par -1

ll prim(ll s, ll n) {
    ll wt = 0;
    dis[s] = 0;
    par[s] = -1;
    for (ll i=0; i<n; ++i) {
        ll v = -1;
        for (ll j=1; j<=n; ++j) {
            if (!vis[j] && (v==-1 || dis[j]<dis[v]))
                v = j;
        }
        if (dis[v]==INF)
            return INF;
        vis[v] = 1;
        wt += dis[v];
        for (ll j=1; j<=n; ++j) {
            if (!vis[j] && adj[v][j]<dis[j]) {
                dis[j] = adj[v][j];
                par[j] = v;
            }
        }
    }
    return wt;
}
```

### Kruskal's Algorithm / クラスカル法
```cpp
struct edge {
    ll a, b, w;
    bool operator<(edge const& other) const {
        return w < other.w;
    }
};

vector<edge> edges;
ll par[N], siz[N];

void make_set(ll n) {
    for (ll i=1; i<=n; ++i) {
        par[i] = i;
        siz[i] = 1;
    }
}

ll find_set(ll v) {
    if (par[v] == v)
        return v;
    return par[v] = find_set(par[v]);
}

void union_set(ll a, ll b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (siz[a] < siz[b])
            swap(a, b);
        par[b] = a;
        siz[a] += siz[b];
    }
}

ll kruskal(ll n) {
    ll wt = 0;
    ll cnt = 0;
    make_set(n);
    sort(edges.begin(), edges.end());
    for (edge e : edges) {
        if (find_set(e.a) != find_set(e.b)) {
            wt += e.w;
            cnt += 1;
            union_set(e.a, e.b);
        }
    }
    if (cnt<n-1)
        return INF;
    return wt;
}
```


## Network Flow / ネットワークフロー

### Maximum Flow / 最大流
```cpp
struct edge{
    ll v, u, c;
};

vector<ll> adj[N];
vector<edge> edges;
vector<ll> lev(N), ptr(N);

void add_edge(ll v, ll u, ll c) {
    ll m = edges.size();
    adj[v].push_back(m);
    adj[u].push_back(m+1);
    edges.push_back({v, u, c});
    edges.push_back({u, v, 0}); // undirected: {u, v, c}
}

bool bfs(ll s, ll t) {
    fill(lev.begin(), lev.end(), -1);
    lev[s] = 0;
    queue<ll> q;
    q.push(s);
    while (!q.empty()) {
        ll v = q.front();
        q.pop();
        for (ll id : adj[v]) {
            edge e = edges[id];
            if (e.c>0 && lev[e.u]==-1) {
                lev[e.u] = lev[e.v] + 1;
                q.push(e.u);
            }
        }
    }
    return lev[t]!=-1;
}

ll dfs(ll v, ll t, ll p) {
    if (v==t)
        return p;
    for (ll& cid=ptr[v]; cid<(ll)adj[v].size(); ++cid) {
        ll id = adj[v][cid];
        edge e = edges[id];
        if (e.c>0 && lev[e.u]==lev[e.v]+1) {
            ll tr = dfs(e.u, t, min(p, e.c));
            if (tr>0) {
                edges[id].c -= tr;
                edges[id^1].c += tr;
                return tr;
            }
        }
    }
    return 0;
}

ll dinic(ll s, ll t) {
    ll f = 0;
    while (bfs(s, t)) {
        fill(ptr.begin(), ptr.end(), 0);
        while (ll p = dfs(s, t, INF)) {
            f += p;
        }
    }
    return f; // also minimum cut
}
```

### Minimum-Cost Flow / 最小費用流
```cpp
struct edge {
    ll v, u, c, w;
};

vector<ll> adj[N];
vector<edge> edges;
vector<ll> dis(N), par_e(N), inq(N);

void add_edge(ll v, ll u, ll c, ll w) {
    ll m = edges.size();
    adj[v].push_back(m);
    adj[u].push_back(m+1);
    edges.push_back({v, u, c, w});
    edges.push_back({u, v, 0, -w});
}

bool spfa(ll s, ll t) {
    fill(dis.begin(), dis.end(), INF);
    fill(inq.begin(), inq.end(), 0);
    queue<ll> q;
    dis[s] = 0;
    q.push(s);
    inq[s] = 1;
    while (!q.empty()) {
        ll v = q.front();
        q.pop();
        inq[v] = 0;
        for (ll id : adj[v]) {
            edge e = edges[id];
            if (e.c>0 && dis[e.v]<INF && dis[e.v]+e.w<dis[e.u]) {
                dis[e.u] = dis[e.v] + e.w;
                par_e[e.u] = id;
                if (!inq[e.u]) {
                    q.push(e.u);
                    inq[e.u] = 1;
                }
            }
        }
    }
    return dis[t]<INF;
}

pll solve(ll s, ll t, ll k) {
    ll f = 0;
    ll w = 0;
    while (f<k) {
        if (!spfa(s, t))
            break;
        ll p = k-f;
        ll cur = t;
        while (cur!=s) {
            ll id = par_e[cur];
            p = min(p, edges[id].c);
            cur = edges[id].v;
        }
        cur = t;
        while (cur!=s) {
            ll id = par_e[cur];
            edges[id].c -= p;
            edges[id^1].c += p;
            w += p * edges[id].w;
            cur = edges[id].v;
        }
        f += p;
    }
    return {f, w}; // max_flow <=k, then min_cost
}
```

### Bipartite Matching / 二部マッチング
```cpp
vector<ll> adj[N];
vector<ll> vis(N), mat(M);

bool dfs(ll v) {
    if (vis[v])
        return false;
    vis[v] = 1;
    for (ll u : adj[v]) {
        ll w = mat[u];
        if (w==-1 || dfs(w)) {
            mat[u] = v;
            return true;
        }
    }
    return false;
}

ll solve(ll n) {
    ll f = 0;
    fill(mat.begin(), mat.end(), -1);
    for (ll i=1; i<=n; ++i) {
        fill(vis.begin(), vis.end(), 0);
        if (dfs(i))
            f += 1;
    }
    return f;
}
```

## Tree Algorithm / 木アルゴリズム

### Tree Diameter / 木の直径
```cpp
vector<ll> adj[N];
vector<ll> par(N);

pll dfs(ll v, ll d, ll p) {
    par[v] = p;
    pair<ll, ll> res{d, v};
    for (ll u : adj[v]) {
        if (u!=p)
            res = max(res, dfs(u, d+1, v));
    }
    return res;
}

ll solve() {
    ll s = dfs(1, 0, -1).second;
    ll d = dfs(s, 0, -1).first;
    // ll t = dfs(s, 0, -1).second;
    // while (t!=-1) {
    //     arr.push_back(t);
    //     t = par[t];
    // }
    return d;
}
```

### Tree DP / 木DP
```cpp
vector<ll> adj[N];
ll dp[N][S];

void dfs(ll v, ll p) {
    "base (dp[v][s])";
    for (ll u : adj[v]) {
        if (u==p)
            continue;
        dfs(u, v);
        "update dp[v][i] with dp[u][j]";
    }
}
```
```cpp
vector<ll> adj[N];
ll siz[N], dp[N][S];

void dfs(ll v, ll p) {
    siz[v] = 1;
    "base (dp[v][s])";
    for (ll u : adj[v]) {
        if (u==p)
            continue;
        dfs(u, v);
        vector<ll> tp(S);
        for (ll i=0; i<siz[v]; ++i) {
            for (ll j=0; j<siz[u]; ++j) {
                "update tp[s] with dp[v][i] & dp[u][j]";
            }
        }
        siz[v] += siz[u];
        for (ll s=0; s<siz[v]; ++s)
            dp[v][s] = tp[s];
    }
}
```

### Euler Tour / オイラーツアー

```cpp
vector<ll> arr;
ll tmi[N], tmo[N], tmr;

void dfs(ll v, ll p) {
    tmi[v] = tmr++;
    arr.push_back(v);
    for (ll u : adj[v]) {
        if (u!=p) {
            dfs(u, v);
        }
    }
    tmo[v] = tmr;
}
```
```cpp
vector<ll> arr;
ll occ[N], dep[N];

void dfs(ll v, ll p, ll d) {
    occ[v] = (ll)arr.size();
    dep[v] = d;
    arr.push_back(v);
    for (ll u : adj[v]) {
        if (u!=p) {
            dfs(u, v, d+1);
            arr.push_back(v);
        }
    }
}
```

### Lowest Common Ancestor / 最近共通祖先
```cpp
vector<ll> adj[N];
ll dep[N], par[N][LogN];

void dfs(ll v, ll d, ll p) {
    dep[v] = d;
    par[v][0] = p;
    for (ll u : adj[v]) {
        if (u!=p)
            dfs(u, d+1, v);
    }
}

void build(ll n, ll l_n) {
    dfs(1, 0, 0);
    for (ll s=1; s<l_n; ++s) {
        for (ll i=1; i<=n; ++i)
            par[i][s] = par[par[i][s-1]][s-1];
    }
}

ll lca(ll a, ll b, ll l_n) {
    if (dep[a]<dep[b])
        swap(a, b);
    for (ll s=l_n-1; s>=0; --s) {
        if ((dep[a]-dep[b])&(1LL<<s))
            a = par[a][s];
    }
    if (a==b)
        return a;
    for (ll k=l_n-1; k>=0; --k) {
        if (par[a][k]!=par[b][k]) {
            a = par[a][k];
            b = par[b][k];
        }
    }
    return par[a][0];
}
```
```cpp
vector<ll> adj[N], arr;
ll dep[N], occ[N];
ll lg[2*N], st[2*N][LogN+1];

void dfs(ll v, ll d, ll p) {
    occ[v] = arr.size();
    dep[v] = d;
    arr.push_back(v);
    for (ll u : adj[v]) {
        if (u!=p) {
            dfs(u, d+1, v);
            arr.push_back(v);
        }
    }
}

void build(ll s) {
    dfs(s, 0, 0);
    ll m = arr.size();
    lg[1] = 0;
    for (ll i=2; i<=m; ++i)
        lg[i] = lg[i/2]+1;
    for (ll i=0; i<m; ++i)
        st[i][0] = arr[i];
    for (ll j=1; j<=lg[m]; ++j) {
        for (ll i=0; i+(1LL<<j)<=m; ++i) {
            ll v1 = st[i][j-1];
            ll v2 = st[i+(1LL<<(j-1))][j-1];
            st[i][j] = (dep[v1]<dep[v2])?v1:v2;
        }
    }
}

ll lca(ll a, ll b) {
    ll l=occ[a], r=occ[b];
    if (l>r)
        swap(l, r);
    ll k = lg[r-l+1];
    ll v1 = st[l][k];
    ll v2 = st[r-(1LL<<k)+1][k];
    return (dep[v1]<dep[v2])?v1:v2;
}
```

### Centroid Decomposition / 重心分解
```cpp
vector<ll> adj[N];
ll siz[N], cen[N];

void calsize(ll v, ll p) {
    siz[v] = 1;
    for (ll u : adj[v]) {
        if (u==p || cen[u])
            continue;
        calsize(u, v);
        siz[v] += siz[u];
    }
}

ll centroid(ll v, ll p, ll t) {
    for (ll u : adj[v]) {
        if (u==p || cen[u])
            continue;
        if (siz[u]>t/2)
            return centroid(u, v, t);
    }
    return v;
}

void build(ll v) {
    calsize(v, -1);
    ll c = centroid(v, -1, siz[v]);
    cen[c] = 1;
    for (ll u : adj[c]) {
        if (cen[u])
            continue;
        build(u);
    }
}
```


# Math / 数学

## Modular Arithmetic / 合同算術

### Mod Library / Modライブラリ
```cpp
ll madd(ll a, ll b) {
    a = (a % MOD + MOD) % MOD;
    b = (b % MOD + MOD) % MOD;
    return (a + b) % MOD;
}

ll msub(ll a, ll b) {
    a = (a % MOD + MOD) % MOD;
    b = (b % MOD + MOD) % MOD;
    return (a - b + MOD) % MOD;
}

ll mmul(ll a, ll b) {
    a = (a % MOD + MOD) % MOD;
    b = (b % MOD + MOD) % MOD;
    return (a * b) % MOD;
}

ll mpow(ll a, ll n) {
    ll res = 1;
    while (n>0) {
        if (n&1)
            res = mmul(res, a);
        a = mmul(a, a);
        n >>= 1;
    }
    return res;
}

ll minv(ll a) {
    return mpow(a, MOD-2);
}

ll mdiv(ll a, ll b) {
    return mmul(a, minv(b));
}
```

### Binary Exponentiation / 繰り返し二乗法
```cpp
ll binpow(ll x, ll n, ll m) {
    ll res = 1;
    while (n>0) {
        if (n&1)
            res = res * x % m;
        x = x * x % m;
        n >>= 1;
    }
    return res;
}
```

### Modular Inverse / モジュラ逆数
```cpp
ll inv(ll a, ll m) { // m is prime
    return binpow(a, m-2, m);
}
```
```cpp
ll inv(ll a, ll m) { // a m coprime
    ll x, y;
    extgcd(a, m, x, y);
    return ((x % m) + m) % m;
}
```

### Binomial Coefficient / 二項係数
```cpp
ll fac[N], inv[N], finv[N];

void init(ll n, ll m) {
    fac[0] = inv[0] = finv[0] = 1;
    fac[1] = inv[1] = finv[1] = 1;
    for (ll i=2; i<=n; ++i) {
        fac[i] = fac[i-1] * i % m;
        inv[i] = m - inv[m%i] * (m/i) % m;
        finv[i] = finv[i-1] * inv[i] % m;
    }
}

ll binom(ll n, ll k, ll m) {
    if (k<0 || k>n)
        return 0;
    return fac[n] * (finv[n-k] * finv[k] % m) % m; 
}
```
```cpp
ll binom(ll n, ll k, ll m) {
    if (k<0 || k>n)
        return 0;
    k = min(k, n-k);
    ll a = 1;
    ll b = 1;
    for (ll i=1; i<=k; ++i) {
        a = a * (n-i+1) % m;
        b = b * i % m;
    }
    return a * binpow(b, m-2, m) % m;
}
```


## Divisor & Prime / 約数と素数

### Euclidean Algorithm / ユークリッドの互除法
```cpp
ll gcd(ll a, ll b) {
    if (b==0) 
        return a;
    return gcd(b, a%b);
}

ll lcm(ll a, ll b) {
    return a / gcd(a, b) * b;
}
```
```cpp
ll extgcd(ll a, ll b, ll& x, ll& y) {
    if (b==0) {
        x = 1;
        y = 0;
        return a;
    }
    ll g, x1, y1;
    g = extgcd(b, a%b, x1, y1);
    x = y1;
    y = x1 - y1*(a/b);
    return g;
}
```

### Divisor Enumeration / 約数列挙
```cpp
vector<ll> divisor(ll n) {
    vector<ll> res;
    for (ll i=1; i*i<=n; ++i) {
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
```cpp
bool prime(ll n) {
    if (n<2)
        return false;
    for (ll i=2; i*i<=n; ++i) {
        if (n%i==0)
            return false;
    }
    return true;
}
```

### Prime Factorization / 素因数分解
```cpp
vector<pll> factor(ll n) {
    vector<pll> res;
    for (ll i=2; i*i<=n; ++i) {
        if (n%i==0) {
            ll p = 0;
            while (n%i==0) {
                n /= i;
                p += 1;
            }
            res.push_back({i, p});
        }
    }
    if (n!=1)
        res.push_back({n, 1});
    return res;
}
```
```cpp
ll phi(ll n) {
    ll res = n;
    for (ll i=2; i*i<=n; ++i) {
        if (n%i==0) {
            while (n%i==0)
                n /= i;
            res -= res / i;
        }
    }
    if (n!=1)
        res -= res / n;
    return res;
}
```


### Sieve of Eratosthenes / エラトステネスの篩
```cpp
bool prime[N];

void sieve(ll n) {
    prime[0] = prime[1] = false;
    for (ll i=2; i<=n; ++i)
        prime[i] = true;
    for (ll i=2; i*i<=n; ++i) {
        if (!prime[i])
            continue;
        for (ll j=i*i; j<=n; j+=i)
            prime[j] = false;
    }
}
```
```cpp
vector<ll> lp(N), pr;

void sieve(ll n) {
    for (ll i=2; i<=n; ++i) {
        if (lp[i]==0) {
            lp[i] = i;
            pr.push_back(i);
        }
        for (ll j=0; j<(ll)pr.size() && pr[j]*i<=n; ++j) {
            lp[i*pr[j]] = pr[j];
            if (pr[j]==lp[i])
                break;
        }
    }
}

// is prime: lp[i]==i
// factorize: while (x>1) x/=lp[x]
```


## Linear Algebra / 線型代数

### Matrix Exponentiation / 行列累乗
```cpp
typedef vector<ll> vec;
typedef vector<vec> mat;

mat matmul(mat &A, mat &B, ll m) {
    mat C(A.size(), vec(B[0].size()));
    for (ll i=0; i<A.size(); ++i) {
        for (ll j=0; j<B[0].size(); ++j) {
            for (ll k=0; k<A[0].size(); ++k)
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % m;
        }
    }
    return C;
}

mat matpow(mat X, ll n, ll m) {
    mat R(X.size(), vec(X.size()));
    for (ll i=0; i<X.size(); ++i)
        R[i][i] = 1;
    while (n>0) {
        if (n&1)
            R = matmul(R, X, m);
        X = matmul(X, X, m);
        n >>= 1;
    }
    return R;
}
```

### Linear Congruence Equation / 線形合同式
```cpp
vector<ll> A(N), B(N), M(N);

pair<ll, ll> linear_congruence(ll n) {
    ll x=0, m=1;
    for (ll i=0; i<n; ++i) {
        ll a=A[i]*m, b=B[i]-A[i]*x, d=gcd(a, M[i]);
        if (b%d!=0)
            return {0, -1};
        ll y = (b/d) * mod_inv(a/d, M[i]/d) % (M[i]/d);
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

ll gauss(ll n, ll m) {
    vector<vector<double>> mat(n, vector<double>(m+1, 0));
    for (ll i=0; i<n; ++i) {
        for (ll j=0; j<m; ++j)
            mat[i][j] = A[i][j];
        mat[i][m] = B[i];
    }
    vector<ll> piv(m, -1);
    for (ll c=0, r=0; c<m && r<n; ++c) {
        ll p = r;
        for (ll i=r; i<n; ++i) {
            if (abs(mat[i][c])>abs(mat[p][c]))
                p = i;
        }
        if (abs(mat[p][c])<EPS)
            continue;
        swap(mat[r], mat[p]);
        piv[c] = r;
        for (ll i=0; i<n; ++i) {
            if (i==r)
                continue;
            double cf = mat[i][c] / mat[r][c];
            for (ll j=c; j<=m; ++j)
                mat[i][j] -= mat[r][j] * cf;
        }
        r += 1;
    }
    for (ll j=0; j<m; ++j) {
        if (piv[j]!=-1)
            sol[j] = mat[piv[j]][m] / mat[piv[j]][j];
    }
    for (ll i=0; i<n; ++i) {
        double sum = 0;
        for (ll j=0; j<m; ++j)
            sum += mat[i][j] * sol[j];
        if (abs(sum-mat[i][m])>EPS)
            return 0;
    }
    for (ll j=0; j<m; ++j) {
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
    ll n = a.size();
    for (ll i=1, j=0; i<n; ++i) {
        ll b = n>>1;
        for (; j&b; b>>=1)
            j ^= b;
        j ^= b;
        if (i<j)
            swap(a[i], a[j]);
    }
    for (ll l=2; l<=n; l*=2) {
        double ag = 2*PI / l * (inv?-1:1);
        cd wl(cos(ag), sin(ag));
        for (ll i=0; i<n; i+=l) {
            cd w(1);
            for (ll j=0; j<l/2; ++j) {
                cd u=a[i+j], v=a[i+j+l/2]*w;
                a[i+j] = u+v;
                a[i+j+l/2] = u-v;
                w *= wl;
            }
        }
    }
    if (inv) {
        for (ll i=0; i<n; ++i)
            a[i] /= n;
    }
}

vector<ll> multiply(vector<ll> a, vector<ll> b) {
    vector<cd> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    ll n = 1;
    while (n<a.size()+b.size())
        n *= 2;
    fa.resize(n);
    fb.resize(n);
    fft(fa);
    fft(fb);
    for (ll i=0; i<n; ++i) 
        fa[i] *= fb[i];
    fft(fa, 1);
    vector<ll> res(n);
    for (ll i=0; i<n; ++i)
        res[i] = round(fa[i].real());
    return res;
}
```

## Geometry / 幾何学

### Geometry Library / 幾何ライブラリ
```cpp
using Poll = complex<double>;

double dot(const Poll &a, const Poll &b) {
    return a.real()*b.real() + a.imag()*b.imag();
}

double det(const Poll &a, const Poll &b) {
    return a.real()*b.imag() - a.imag()*b.real();
}

bool compare(const Poll &a, const Poll &b) {
    return a.real()!=b.real() ? a.real()<b.real() : a.imag()<b.imag();
}

struct Line {
    Poll a, b;
    Line() = default;
    Line(Poll a, Poll b) : a(a), b(b) {}
};

struct Segment : Line {
    Segment() = default;
    Segment(Poll a, Poll b) : Line(a, b) {}
};

struct Circle {
    Poll p;
    double r;
    Circle() = default;
    Circle(Poll p, double r) : p(p), r(r) {}
};
```
```cpp
ll ccw(Poll a, Poll b, Poll c) {
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

bool llersect(Segment s, Poll p) {
    return ccw(s.a, s.b, p) == 0;
}

bool llersect(Segment s, Segment t) {
    return ccw(s.a, s.b, t.a)*ccw(s.a, s.b, t.b)<=0 && ccw(t.a, t.b, s.a)*ccw(t.a, t.b, s.b)<=0;
}

bool llersect(Line l, Poll p) {
    return abs(ccw(l.a, l.b, p))!=1;
}

bool llersect(Line l, Segment s) {
    return det(l.b-l.a, s.a-l.a)*det(l.b-l.a, s.b-l.a)<EPS;
}

ll llersect(Line l, Line m) {
    if (llersect(l, m.a) && llersect(l, m.b))
        return 2;
    if (abs(det(l.b-l.a, m.b-m.a))>EPS)
        return 1;
    return 0;
}

Poll projection(Line l, Poll p) {
    double t = dot(p-l.a, l.b-l.a)/norm(l.b-l.a);
    return l.a + (l.b-l.a)*t;
}

Poll reflection(Line l, Poll p) {
    return p + (projection(l, p)-p)*2.0;
}

Poll crosspoll(Line l, Line m) {
    double A = det(l.b-l.a, m.b-m.a);
    double B = det(l.b-l.a, l.b-m.a);
    if (A==0)
        return Poll(1/EPS, 1/EPS);
    return m.a + (m.b-m.a)*B/A;
}

double distance(Poll a, Poll b) {
    return abs(b-a);
}

double distance(Segment s, Poll p) {
    Line l(s.a, s.b);
    Poll h = projection(l, p);
    if (llersect(s, h))
        return abs(p-h);
    return min(abs(s.a-p), abs(s.b-p));
}

double distance(Segment s, Segment t) {
    if (llersect(s, t))
        return 0;
    return min({distance(s, t.a), distance(s, t.b), distance(t, s.a), distance(t, s.b)});
}

double distance(Line l, Poll p) {
    return abs(det(p-l.a, l.b-l.a))/abs(l.b-l.a);
}

double distance(Line l, Segment s) {
    if (llersect(l, s))
        return 0;
    return min(distance(l, s.a), distance(l, s.b));
}

double distance(Line l, Line m) {
    if (llersect(l, m))
        return 0;
    return distance(l, m.a);
}
```
```cpp
ll llersect(Circle c, Line l) {
    Poll h = l.a + (l.b-l.a) * dot(c.p-l.a, l.b-l.a)/norm(l.b-l.a);
    double d = abs(c.p-h);
    if (c.r<d-EPS)
        return 0;
    if (abs(c.r-d)<EPS)
        return 1;
    return 2;
}

ll llersect(Circle c1, Circle c2) {
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

vector<Poll> crosspoll(Circle c, Line l) {
    vector<Poll> res;
    Poll h = l.a + (l.b-l.a) * dot(c.p-l.a, l.b-l.a)/norm(l.b-l.a);
    ll mode = llersect(c, l);
    if (mode==1) {
        res.push_back(h);
    }
    if (mode==2) {
        double b = sqrt(c.r*c.r-norm(h-c.p));
        Poll e = (l.b-l.a)/abs(l.b-l.a);
        res.push_back(h-e*b);
        res.push_back(h+e*b);
    }
    return res;
}

vector<Poll> crosspoll(Circle c1, Circle c2) {
    vector<Poll> res;
    double d = abs(c2.p-c1.p);
    ll mode = llersect(c1, c2);
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
        Poll e = (c2.p-c1.p)/abs(c2.p-c1.p);
        res.push_back(c1.p + e*a - e*Poll(0, 1)*b);
        res.push_back(c1.p + e*a + e*Poll(0, 1)*b);
    }
    return res;
}

vector<Line> tangent(Circle c, Poll p) {
    vector<Line> res;
    double d = abs(p-c.p);
    if (abs(d-c.r)<EPS) {
        res.push_back(Line(p, p+(p-c.p)*Poll(0, 1)));
    }
    if (d>c.r+EPS) {
        vector<Poll> cp = crosspoll(c, Circle(p, sqrt(d*d-c.r*c.r)));
        res.push_back(Line(cp[0], p));
        res.push_back(Line(cp[1], p));
    }
    return res;
}

vector<Line> tangent(Circle c1, Circle c2) {
    vector<Line> res;
    double d = abs(c2.p-c1.p);
    Poll u = (c2.p-c1.p)/abs(c2.p-c1.p);
    Poll v = u*Poll(0, 1);
    for (ll s : {-1, 1}) {
        if (abs(d)<EPS)
            break;
        double cs = (c1.r+c2.r*s)/d;
        if (abs(cs*cs-1)<EPS) {
            Poll U = (cs>0 ? u : -u);
            res.push_back(Line(c1.p+U*c1.r, c1.p+U*c1.r+v));
        }
        else if (1-cs*cs>EPS) {
            Poll U = u*cs, V=v*sqrt(1-cs*cs);
            res.push_back(Line(c1.p+(U+V)*c1.r, c2.p-(U+V)*(c2.r*s)));
            res.push_back(Line(c1.p+(U-V)*c1.r, c2.p-(U-V)*(c2.r*s)));
        }
    }
    return res;
}
```
```cpp
ll contain(vector<Poll> g, Poll p) {
    bool in = false;
    ll n = g.size();
    for (ll i=0; i<n; ++i) {
        Poll a=g[i]-p, b=g[(i+1)%n]-p;
        if (a.imag()>b.imag())
            swap(a, b);
        if (a.imag()<EPS && b.imag()>EPS && det(a, b)>EPS)
            in = !in;
        if (abs(det(a, b))<EPS && dot(a, b)<EPS)
            return 1;
    }
    return (in ? 2 : 0);
}

double area(vector<Poll> g) {
    double a = 0;
    ll n = g.size();
    for (ll i=0; i<n; ++i)
        a += det(g[i], g[(i+1)%n]);
    return a*0.5;
}
```

### Convex Hull / 凸包
```cpp
vector<Poll> convex_hull(vector<Poll> ps) {
    sort(ps.begin(), ps.end(), compare);
    ll n=ps.size(), k=0;
    vector<Poll> qs(2*n);
    for (ll i=0; i<n; ++i) {
        while (k>1 && det(qs[k-1]-qs[k-2], ps[i]-qs[k-1])<EPS)
            k--;
        qs[k++] = ps[i];
    }
    for (ll i=n-2, t=k; i>=0; --i) {
        while (k>t && det(qs[k-1]-qs[k-2], ps[i]-qs[k-1])<EPS)
            k--;
        qs[k++] = ps[i];
    }
    qs.resize(k-1);
    return qs;
}
```
```cpp
double max_distance(vector<Poll> ps) {
    vector<Poll> qs = convex_hull(ps);
    if (qs.size()==2)
        return abs(qs[1]-qs[0]);
    ll i=0, j=0, n=qs.size();
    for (ll k=0; k<n; ++k) {
        if (compare(qs[k], qs[i]))
            i = k;
        if (!compare(qs[k], qs[j]))
            j = k;
    }
    double res = 0;
    ll si=i, sj=j;
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
void solve(ll n) {
    vector<pair<double, ll>> v;
    for (ll i=0; i<n; ++i) {
        v.push_back({"<x_left[i]>", i});
        v.push_back({"<x_right[i]>", i+n});
    }
    sort(v.begin(), v.end());
    set<pair<double, ll>> s;
    for (auto p : v) {
        ll i = p.second%n;
        if (p.second<n) {
            set<pair<double, ll>>::iterator it = "<binary search y[i]>";
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
using Poll = complex<double>;

bool compare_x(const Poll &a, const Poll &b) {
    return a.real()<b.real();
}

bool compare_y(const Poll &a, const Poll &b) {
    return a.imag()<b.imag();
}

vector<Poll> ps;

void rec(ll l, ll r) {
    if (l==r)
        "<base case>";
    ll m = (l+r)/2;
    rec(l, m);
    rec(m+1, r);
    inplace_merge(ps.begin()+l, ps.begin()+m+1, ps.begin()+r+1, compare_y);
    "<combine>";
}

sort(ps.begin(), ps.end(), compare_x);
```


# Others / その他の

## Technique / テクニック

### Two Pointers / しゃくとり法
```cpp
ll arr[N];

ll solve(ll n, ll t) {
    ll ans = 0;
    ll s = 0;
    for (ll l=0, r=0; r<n; ++r) {
        s += arr[r];
        for (;l<=r && s>t; ++l) {
            s -= arr[l];
        }
        "[l, r] with s<=t";
    }
    return ans;
}
```

### Coordinate Compression / 座標圧縮
```cpp
vector<ll> xs;
unordered_map<ll, ll> id;

void solve() {
    for ("segment [l, r)") {
        xs.push_back(l);
        xs.push_back(r);
    }
    sort(xs.begin(), xs.end());
    xs.erase(unique(xs.begin(), xs.end()), xs.end());
    for (ll i=0; i<(ll)xs.size(); ++i)
        id[xs[i]] = i;
    for (ll i=0; i+1<(ll)xs.size(); ++i) {
        "compressed [xs[i], xs[i+1])";
    }
}
```

### Binary Lifting / ダブリング
```cpp
ll nxt[N][LogD];

void build(ll n, ll l_d) {
    for (ll i=0; i<n; ++i)
        nxt[i][0] = "next position";
    for (ll s=1; s<l_d; ++s) {
        for (ll i=0; i<n; ++i) {
            nxt[i][s] = nxt[nxt[i][s-1]][s-1];
        }
    }
}

ll query(ll p, ll d, ll l_d) {
    for (ll s=0; s<l_d; ++s) {
        if (d&(1LL<<s))
            p = nxt[p][s];
    }
    return p;
}
```

### Meet in the Middle / 半分全列挙
```cpp
void solve(ll n) {
    ll n1 = n/2, n2 = n-n/2;
    map<ll,ll> m1, m2; // set, vector
    for (ll s=0; s<(1LL<<n1); ++s) {
        for (ll i=0; i<n1; ++i) {
            if (s&(1LL<<i))
                "select i";
        }
        "insert to m1";
    }
    for (ll s=0; s<(1LL<<n2); ++s) {
        for (ll i=0; i<n2; ++i) {
            if (s&(1LL<<i))
                "select n/2+i";
        }
        "insert to m2";
    }
    for ("iterate m1") {
        if ("match m2") {
            "update ans";
        }
    }
}
```

### Sparse Table / スパーステーブル
```cpp
ll arr[N];
ll lg[N], st[N][LogN];

void build(ll n) {
    lg[1] = 0;
    for (ll i=2; i<=n; ++i)
        lg[i] = lg[i/2]+1;
    for (ll i=0; i<n; ++i)
        st[i][0] = arr[i];
    for (ll j=1; j<=lg[n]; ++j) {
        for (ll i=0; i+(1LL<<j)<=n; ++i) {
            st[i][j] = min(st[i][j-1], st[i+(1LL<<(j-1))][j-1]);
        }
    }
}

ll query(ll l, ll r) {
    ll k = lg[r-l+1];
    return min(st[l][k], st[r-(1LL<<k)+1][k]);
}
```

### Sqrt Decomposition / 平方分割
```cpp
struct query {
    ll l, r, id;
};

ll arr[N], ans[Q];
vector<query> qs;

void solve(ll n) {
    ll bs = sqrt(n)+1;
    sort(qs.begin(), qs.end(), [&](query a, query b) {
        if (a.l/bs != b.l/bs)
            return a.l/bs < b.l/bs;
        if ((a.l/bs) & 1)
            return a.r > b.r;
        return a.r < b.r;
    });
    ll l=0, r=-1, cur=0;
    for (auto q : qs) {
        while (r < q.r) {
            r += 1;
            "extend r";
        }
        while (l > q.l) {
            l -= 1;
            "extend l";
        }
        while (r > q.r) {
            "remove r";
            r -= 1;
        }
        while (l < q.l) {
            "remove l";
            l += 1;
        }
        ans[q.id] = cur;
    }
}
```


## String / 文字列

### KMP Algorithm / KMP法

```cpp
ll pi[M];

void build(string t) {
    ll l = 0;
    for (ll i=1; i<t.size(); ++i) {
        while (l>0 && t[l]!=t[i])
            l = pi[l-1];
        if (t[l]==t[i])
            l += 1;
        pi[i] = l;
    }
}

void search(string s, string t) {
    ll j = 0;
    for (ll i=0; i<s.size(); ++i) {
        while (j>0 && s[i]!=t[j])
            j = pi[j-1];
        if (s[i]==t[j])
            j += 1;
        if (j==t.size()) {
            "match from i+1-j";
            j = pi[j-1];
        }
    }
}
```

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
ll search(string s, string t) {
    ll sl=s.size(), tl=t.size();
    ll p = 257, m = 1e9+9, pp=1, sh=0, th=0;
    for (ll i=0; i<tl; ++i) {
        pp = (pp*p) % m;
        sh = (sh*p + s[i]) % m;
        th = (th*p + t[i]) % m;
    }
    for (ll i=0; i+tl<=sl; ++i) {
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
vector<ll> suffix_array(string s) {
    s += '$';
    ll n=s.size(), cls=256;
    vector<ll> p(n), c(n), cnt(max(256, n)), pn(n), cn(n);
    for (ll i=0; i<n; ++i) {
        p[i] = i;
        c[i] = s[i];
    }
    for (ll h=1; h<=n; h*=2) {
        for (ll i=0; i<n; ++i)
            p[i] = (p[i]+n-h/2)%n;
        fill(cnt.begin(), cnt.begin()+cls, 0);
        for (ll i=0; i<n; ++i)
            cnt[c[p[i]]] += 1;
        for (ll i=1; i<cls; ++i)
            cnt[i] += cnt[i-1];
        for (ll i=n-1; i>=0; --i)
            pn[--cnt[c[p[i]]]] = p[i];
        cn[pn[0]] = 0;
        cls = 1;
        for (ll i=1; i<n; ++i) {
            pair<ll,ll> cur = {c[pn[i]], c[(pn[i]+h/2)%n]};
            pair<ll,ll> pre = {c[pn[i-1]], c[(pn[i-1]+h/2)%n]};
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
ll search(string s, string t, vector<ll> sa) {
    ll l=-1, r=sa.size();
    while (r-l>1) {
        ll m = (l+r)/2;
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
vector<ll> arr(N);

bool nim(ll n) {
    ll x = 0;
    for (ll i=0; i<n; ++i)
        x ^= arr[i];
    return x > 0;
}
```

### Grundy Number / Grundy数
```cpp
vector<ll> gru(X);

void build(ll x) {
    for (ll i=1; i<=x; ++i) {
        set<ll> s;
        for ("<next state>") {
            s.insert(gru["<next state>"]);
        }
        ll g = 0;
        while (s.count(g)>0)
            g += 1;
        gru[i] = g;
    }
}
```
