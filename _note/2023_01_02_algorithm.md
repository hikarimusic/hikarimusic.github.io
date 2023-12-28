---
title: 'Algorithm (工事中)'
date: 2023-01-02
permalink: /note/2023_01_02_algorithm
tags:
  - note
toc: true
---

Templates of competitive programming.

{% include toc %}

## Search / 探索

### Exhaustive Search / 全探索
```cpp
vector<int> arr;

void dfs("<position>") {
    if ("<complete>") {
        "<check>";
        return;
    }
    for ("<next step>") {
        "<construct state>";
        dfs("<next position>");
        "<recover state>";
    }
}
```
```cpp
vector<int> sol;

bool dfs("<position>") {
    if ("<complete>")
        return true;
    for ("<next step>") {
        if ("<pruning condition>")
            continue;
        "<construct solution>";
        if (dfs("<next position>"))
            return true;
        "<recover solution>";
    }
    return false;
}
```
```cpp
void search() {
    for (int S=0; S<(1<<N); ++S) {
        "< S&(1<<i), ...>";
    }
}
```
```cpp
vector<int> arr;

void search() {
    do {
        "< arr[i], ...>";
    } while (next_permutation(arr.begin(), arr.end()));
}
```


### Binary Search / 二分探索
```cpp
void search() {
    int l=-1, r=N;
    while (r-l>1) {
        int m = (l+r)/2;
        int a = "<value at m>";
        if (t < a)
            r = m;
        else
            l = m;
    }
}
```

## Optimization / 最適化

### Dynamic Programming / 動的計画法
```cpp
vector<vector<int>> dp;

void solve() {
    "<base case>";
    for (int i=1; i<=N; ++i) {
        for (int j=1; j<=M; ++j) {
            dp[i][j] = "<function of dp[i-1][j-1], dp[i-1][j], ...>";
        }
    }
}
```
```cpp
vector<vector<int>> dp;

int rec(int S, int v) {
    if ("<memorized>")
        return dp[S][v];
    if ("<base case>")
        return dp[S][v] = "<value>";
    dp[S][v] = "<function of rec(S^(1<<_), v'), ...>":
    return dp[S][v];
}
```
```cpp
vector<vector<int>> dp;

int rec(int l, int r) {
    if ("<memorized>")
        return dp[l][r];
    if ("<base case>")
        return dp[l][r] = "<value>";
    dp[l][r] = "<function of rec(l, i), rec(i+1, r), ...>";
}
```

### Greedy Algorithm / 貪欲法
```cpp
void solve() {
    "<sort>";
    for (int i=0; i<N; ++i) {
        "<construct solution>";
    }
}
```

## Data Structure / データ構造

### Disjoint Set Union / Union-Find 木
```cpp
vector<int> p, s;

void make_set(int v) {
    p[v] = v;
    s[v] = 1;
}

int find_set(int v) {
    if (p[v]==v)
        return v;
    return p[v] = find_set(p[v]);
}

void union_set(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a==b)
        return;
    if (a < b)
        swap(a, b);
    p[b] = a;
    s[a] += s[b];
}
```

### Segment Tree / セグメント木
```cpp
vector<int> a, t;

void build(int v, int tl, int tr) {
    if (tl==tr) {
        t[v] = a[tl];
        return;
    }
    int tm = (tl+tr)/2;
    build(v*2+1, tl, tm);
    build(v*2+2, tm+1, tr);
    t[v] = "<merge t[v*2+1] and t[v*2+2]>";
}

void update(int v, int tl, int tr, int id, int nv) {
    if (tl==tr) {
        t[v] = nv;
        return;
    }
    int tm = (tl+tr)/2;
    if (id<=tm)
        update(v*2+1, tl, tm, id, nv);
    else
        update(v*2+2, tm+1, tr, id, nv);
    t[v] = "<merge t[v*2+1] and t[v*2+2]>";
}

int query(int v, int tl, int tr, int l, int r) {
    if (l>r)
        return "<identity>";
    if (tl==l && tr==r)
        return t[v];
    int tm = (tl+tr)/2;
    int q1 = query(v*2+1, tl, tm, l, min(r, tm));
    int q2 = query(v*2+2, tm+1, tr, max(l, tm+1), r);
    return "<merge q1 and q2>";
}
```

## Mathematics / 数学

### Euclidean Algorithm / ユークリッドの互除法
```cpp
int gcd(int a, int b) {
    if (b==0) 
        return a;
    return gcd(b, a%b);
}
```
```cpp
int gcd(int a, int b, int& x, int& y) {
    if (b==0) {
        x = 1;
        y = 0;
        return a;
    }
    int g, x1, y1;
    g = gcd(b, a%b, x1, y1);
    x = y1;
    y = x1 - y1*(a/b);
    return g;
}
```

### Primality Test / 素数判定
```cpp
bool isPrime(int n) {
    for (int d=2; d*d<=n; ++d) {
        if (n%d==0)
            return false;
    }
    return true;
}
```
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

### Binary Exponentiation / べき乗
```cpp
int binpow(int x, int n) {
    int r = 1;
    while (n>0) {
        if (n&1)
            r *= x;
        x *= x;
        n >>= 1;
    }
    return r;
}
```

### Modular Inverse / 逆元
```cpp
int modinv(int x, int m) {
    int a=x, b=m, u=1, v=0;
    while (b>0) {
        int t = a/b;
        a -= t*b; swap(a, b);
        u -= t*v; swap(u, v);
    }
    int r = (u%m + m) % m;
    return r;
}
```
```cpp
vector<int> fac(N, 1), inv(N, 1), finv(N, 1);

void build(int n, int m) {
    for (int i=2; i<=n; ++i) {
        fac[i] = fac[i-1] * i % m;
        inv[i] = m - inv[m%i] * (m/i) % m;
        finv[i] = finv[i-1] * inv[i] % m;
    }
}

int binom(int n, int k, int m) {
    return fac[n] * (finv[n-k] * finv[k] % m) % m; 
}
```

## Graph / グラフ

### Graph Traversal / グラフ探索
```cpp
vector<vector<int>> adj(N);
vector<bool> vis(N);

void dfs(int v) {
    vis[v] = true;
    "<visit v>";
    for (int u : adj[v]) {
        if (!vis[u])
            dfs(u);
    }
}
```
```cpp
vector<vector<int>> adj(N);
vector<bool> vis(N);

void bfs(int v) {
    queue<int> q;
    q.push(v);
    vis[v] = true;
    while (!q.empty()) {
        v = q.front();
        q.pop();
        "<visit v>";
        for (int u : adj[v]) {
            if (!vis[u]) {
                q.push(u);
                vis[u] = true;
            }
        }
    }
}
```

### Shortest Path / 最短経路
```cpp
vector<vector<int>> adj(N, vector<int>(N, INF));
vector<int> u(N), d(N, INF), p(N, -1);

void dijkstra(int s, int n) {
    d[s] = 0;
    for (int i=0; i<n; ++i) {
        int k = -1;
        for (int j=0; j<n; ++j) {
            if (!u[j] && (k==-1 || d[j]<d[k]))
                k = j;
        }
        if (d[k]==INF)
            return;
        u[k] = 1;
        for (int j=0; j<n; ++j) {
            if (d[k]+adj[k][j]<d[j]) {
                d[j] = d[k] + adj[k][j];
                p[j] = k;
            }
        }
    }
}
```
```cpp
vector<vector<pii>> adj(N);
vector<int> d(N, INF), p(N, -1);

void dijkstra(int s) {
    priority_queue<pii, vector<pii>, greater<pii>> q;
    q.push({0, s});
    d[s] = 0;
    while (!q.empty()) {
        int v = q.top().second;
        int d_v = q.top().first;
        q.pop();
        if (d_v!=d[v])
            continue;
        for (pii e : adj[v]) {
            int to = e.first;
            int len = e.second;
            if (d[v]+len<d[to]) {
                d[to] = d[v] + len;
                p[to] = v;
                q.push({d[to], to});
            }
        }
    }
}
```
```cpp
struct edge{
    int a, b, w;
};

vector<edge> edges;
vector<int> d(N, INF), p(N, -1);

void bellman_ford(int s, int n) {
    d[s] = 0;
    int cnt = 0;
    for (int i=0; i<n; ++i) {
        bool any = 0;
        for (edge e : edges) {
            if (d[e.a]!=INF && d[e.a]+e.w<d[e.b]) {
                d[e.b] = d[e.a] + e.w;
                p[e.b] = e.a;
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
```cpp
vector<vector<int>> d(N, vector<int>(N, INF)), p(N, vector<int>(N, -1));

void floyd_warshall(int n) {
    "<each edge: d[v][u]=w, p[v][u]=v >";
    "<each vert: d[v][v]=0, p[v][v]=v >";
    for (int k=0; k<n; ++k) {
        for (int i=0; i<n; ++i) {
            for (int j=0; j<n; ++j) {
                if (d[i][k]<INF && d[k][j]<INF && d[i][k]+d[k][j]<d[i][j]) {
                    d[i][j] = d[i][k] + d[k][j];
                    p[i][j] = p[k][j];
                }
            }
        }
    }
    "<negative cycle: d[i][i]<0 >";
}
```

### Minimum Spanning Tree / 最小全域木
```cpp
vector<vector<int>> adj(N, vector<int>(N, INF));
vector<int> u(N), d(N, INF), p(N, -1);

int prim(int s, int n) {
    int wt = 0;
    d[s] = 0;
    for (int i=0; i<n; ++i) {
        int k = -1;
        for (int j=0; j<n; ++j) {
            if (!u[j] && (k==-1 || d[j]<d[k]))
                k = j;
        }
        if (d[k]==INF)
            return INF;
        u[k] = 1;
        wt += d[k];
        for (int j=0; j<n; ++j) {
            if (!u[j] && adj[k][j]<d[j]) {
                d[j] = adj[k][j];
                p[j] = k;
            }
        }
    }
    return wt;
}
```
```cpp
vector<vector<pii>> adj(N);
vector<int> u(N), d(N, INF), p(N, -1);

int prim(int s) {
    int wt = 0;
    priority_queue<pii, vector<pii>, greater<pii>> q;
    d[s] = 0;
    q.push({0, s});
    while (!q.empty()) {
        int v = q.top().second;
        q.pop();
        if (u[v])
            continue;
        u[v] = 1;
        wt += d[v];
        for (pii e : adj[v]) {
            if (!u[e.first] && e.second<d[e.first]) {
                d[e.first] = e.second;
                p[e.first] = v;
                q.push({d[e.first], e.first});
            }
        }
    }
    return wt;
}
```
```cpp
vector<int> p(N), s(N);

void make_set(int v) {
    p[v] = v;
    s[v] = 1;
}

int find_set(int v) {
    if (p[v]==v)
        return v;
    return p[v] = find_set(p[v]);
}

void union_set(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a==b)
        return;
    if (a<b)
        swap(a, b);
    p[b] = a;
    s[a] += s[b];
}

struct edge{
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
        if (find_set(e.a)!=find_set(e.b)) {
            wt += e.w;
            mst.push_back(e);
            union_set(e.a, e.b);
        }
    }
    return wt;
}
```