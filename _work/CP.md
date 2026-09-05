---
title: 'CP'
date: 2023-01-01
permalink: /work/CP
tags:
  - note
toc: true
---

Competitive programming

### Template

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long; // __int128
using ld = long double; // __float128
using pll = array<ll,2>;
using vll = vector<ll>;
using pt = complex<ld>;
const ll INF = 1000000000000000009;
const ll MOD = 998244353;
const ld EPS = 0.000000000001;
const ld PI = acos(-1);
#define all(x) (x).begin(), (x).end()
#define sz(x) (ll)(x).size()
#define debug(x) cerr << #x << " = " << x << '\n'



void solve() {
    // cin >> N;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout << fixed << setprecision(15);
    ll T = 1;
    // cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}
```

### Environment

```sh
# new computer
sudo g++ -std=gnu++17 -O2 -pipe -x c++-header /usr/include/x86_64-linux-gnu/c++/9/bits/stdc++.h
```

```sh
# new terminal
r(){ f="${1%.cpp}"; g++ -std=gnu++17 -O2 -pipe -fmax-errors=1 "$f.cpp" -o "$f" && { x=$(cat); echo ========; echo "$x" | "./$f"; }; }
```

```sh
# paste input, ctrl-D 
r a
```
