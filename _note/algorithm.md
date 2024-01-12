---
title: 'Algorithm (工事中)'
date: 2023-01-02
permalink: /note/algorithm
tags:
  - note
toc: true
---

Templates of competitive programming.

{% include toc %}

## Search / 探索

### Exhaustive Search / 全探索
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
```cpp
vector<int> arr(N);

void search(int n) {
    do {
        for (int i=0; i<n; ++i)
            "<arr[i]...>";
    } while (next_permutation(arr.begin(), arr.begin()+n));
}
```
```cpp
vector<int> arr(N);

void search(int p, int n) {
    if (p==n) {
        for (int i=0; i<n; ++i)
            "<arr[i]...>";
        return;
    }
    for ("<next value i>") {
        arr[p] = i;
        search(p+1, n);
        arr[p] = 0;
    }
}
```
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

## Optimization / 最適化

### Dynamic Programming / 動的計画法
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

### Greedy Algorithm / 貪欲法
```cpp
void solve() {
    "<preprocess>";
    for (int i=0; i<N; ++i) {
        "<greedy>";
    }
}
```

## Data Structure / データ構造

### Disjoint Set Union / Union-Find 木
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

### Modular Arithmetic / 余りの計算
```cpp
int mod_inv(int a, int m) {
    int x, y;
    extgcd(a, m, x, y);
    return ((x % m) + m) % m;
}
```
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

### Linear Algebra / 線型代数
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
    int l_n = int(log2(double(n)))+1;
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