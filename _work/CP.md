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
using mll = vector<vll>;
using pt = complex<ld>;
const ll INF = 1000000000000000009;
const ll MOD = 998244353;
const ld EPS = 0.000000000001;
const ld PI = acos(-1);
#define all(x) (x).begin(), (x).end()
#define sz(x) (ll)(x).size()
#define debug(x) cerr << #x << " = " << x << '\n'

ll N;

void solve() {
    cin >> N;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout << fixed << setprecision(15);
    ll T = 1;
    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}
```

### Generator

```py
import random
import sys

r = random.Random(int(sys.argv[1]))

def num(lo, hi, end='\n'):
    n = r.randint(lo, hi)
    print(n, end=end)
    return n

def arr(size, lo, hi, end='\n'):
    a = [r.randint(lo, hi) for _ in range(size)]
    print(*a, end=end)
    return a

T = num(1, 1)
N, X = num(1, 2, ' '), num(0, 5)
for _ in range(N):
    M = num(1, 2)
    A = arr(M, 0, 5)
    B = arr(M, 0, 5)
```

### Environment

```sh
r(){
    f="${1%.cpp}"
    g++ -std=gnu++17 -O2 -pipe -fmax-errors=1 "$f.cpp" -o "$f" || return
    x=$(cat)
    echo ========
    echo "$x" | "./$f"
}
```

```sh
# run a.cpp (paste input, ctrl-D)
r a 
```

```sh
s(){
    f="${1%.cpp}"
    g++ -std=gnu++17 -O2 "$f.cpp" -o "$f" || return
    g++ -std=gnu++17 -O2 brute.cpp -o brute || return
    for ((seed=1; ; seed++)); do
        python3 gen.py "$seed" > fail.in
        timeout 2s "./$f" < fail.in > fail.got || {
            echo "==TLE=="
            echo "Input:"; cat fail.in
            return
        }
        ./brute < fail.in > fail.want || return
        if ! diff -q fail.want fail.got >/dev/null; then
            echo "==WA=="
            echo "Input:"; cat fail.in
            echo "Output:"; cat fail.got
            echo "Answer:"; cat fail.want
            return
        fi
        ((seed % 100 == 0)) && echo "$seed passed"
    done
}
```

```sh
# stress a.cpp (with brute.cpp, gen.py)
s a
```

---

```sh
# precompile bits/stdc++.h
sudo g++ -std=gnu++17 -O2 -pipe -x c++-header /usr/include/x86_64-linux-gnu/c++/9/bits/stdc++.h
```