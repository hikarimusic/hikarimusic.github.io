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

### Prime and Divisor / 素数と約数
```cpp
bool isPrime(int n) {
    for (int i=2; i*i<=n; ++i) {
        if (n%i==0)
            return false;
    }
    return true;
}
```
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

### Binary Exponentiation / べき乗
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

### Modular Arithmetic / 余りの計算
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

### Shortest Path / 最短経路
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
            if (dis[v]+len<dis[to]) {
                dis[to] = dis[v] + len;
                par[to] = v;
                q.push({dis[to], to});
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

### Minimum Spanning Tree / 最小全域木
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
    if (a == b)
        return;
    if (a < b)
        swap(a, b);
    par[b] = a;
    siz[a] += siz[b];
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

### Network Flow / ネットワークフロー
```cpp
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
    // "<each edge: adj[v].pb(u) adj[u].pb(v) >";
    // "<each edge: cap[v][u]=c cap[u][v]=0 >";
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
```cpp
struct edge {
    int a, b, w;
};

vector<edge> edges;
vector<vector<int>> cap(N, vector<int>(N));
vector<int> dis(N), par(N);

int bellman_ford(int s, int t) {
    fill(dis.begin(), dis.end(), INF);
    fill(par.begin(), par.end(), -1);
    dis[s] = 0;
    bool any = 1;
    while (any) {
        any = 0;
        for (edge e : edges) {
            if (dis[e.a]!=INF && dis[e.a]+e.w<dis[e.b] && cap[e.a][e.b]>0) {
                dis[e.b] = dis[e.a] + e.w;
                par[e.b] = e.a;
                any = 1;
            }
        }
    }
    return dis[t];
}

int min_cost_flow(int s, int t, int k) {
    "<each edge: edges.pb({v,u,w}) edges.pb({u.v.-w}) >";
    "<each edge: cap[v][u]=c cap[u][v]=0 >";
    int cost=0, flow=0;
    while (flow<k) {
        int m_c = bellman_ford(s, t);
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