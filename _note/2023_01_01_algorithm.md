---
title: 'Algorithm'
date: 2023-01-01
permalink: /note/2023_01_01_algorithm
tags:
  - note
---

Templates for competitive programming.

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

## Graph / グラフ

### Dijkstra Algorithm / ダイクストラ法
```cpp
vector<int> d;
vector<bool> u;

void dijkstra() {
    d.assign(n, INF);
    u.assign(n, 0);
    d[0] = 0;
    for (int i=0; i<N; ++i) {
        int v = -1;
        for (int j=0; j<N; ++j) {
            if (u[j])
                continue;
            if (v==-1 || d[j]<d[v])
                v = j;
        }
        if (d[v]==INF)
            break;
        u[v] = 1;
        for (int j=0; j<N; ++j) {
            d[j] = min(d[j], d[v]+g[v][j]);
        }
    }
}
```