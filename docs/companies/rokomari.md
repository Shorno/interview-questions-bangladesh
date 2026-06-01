# Rokomari

|                 |                          |
| :-------------- | :----------------------- |
| Founding year   | 2012                     |
| Company Website | https://www.rokomari.com |

## Introduction
[Rokomari](https://www.rokomari.com) is Bangladesh’s leading online bookstore platform, offering millions of books from local and international publishers along with gadgets, stationery, and more. With fast delivery, secure payment, and exclusive deals, Rokomari has become the go-to destination for book readers.

In this article, the questions of recruitment test for Backend Developer role at Rokomari is presented. The test was taken on 13th September, 2025 at their Motijheel Office.

## Interview Stages
- **Written test**: The total time is 2 hours.
- **On site Interview**

## Written Test Questions

### Backend Technology (40 Marks)

- Basic scenario based questions from backend technology
- Complex SQL query (15 marks)

### Problem Solving (60 Marks)


<article>

You are given a tree with n nodes and e edges. Each node has a value. Then you are given Q queries. In each query, you are given a node number, and you need to return the XOR of all nodes in the subtree rooted at that node (including the node itself).

<details><summary>Theory and explanation</summary>

The tree is **undirected** but rooted implicitly (typically at node `1` after DFS). For each query node `v`, answer = **XOR of all node values in the subtree of `v`**.

**Key insight — subtree aggregation**

If you root the tree and run one **DFS/BFS** from the root, each child subtree is disjoint. Define:

```
subXor[v] = value(v) XOR (XOR of subXor[u] for all children u of v)
```

Because XOR is **associative and commutative**, the XOR of all nodes in `v`'s subtree equals this recurrence. After one O(n) DFS, each query is **O(1) lookup** in `subXor[v]`.

**Why XOR combines this way**

For disjoint sets A and B: `XOR(A ∪ B) = XOR(A) XOR XOR(B)`. Subtrees of different children do not overlap, so fold them into parent.

**Input format note**

The problem statement says each node has a value; the sample solution XORs node **indices** (`subXor[u] = u`). In production you'd use `subXor[u] = val[u] ^ ...`. Clarify with the problem — the technique is identical.

**Complexity target**

- Preprocess: **O(n + e)** for DFS on tree.
- Queries: **O(Q)** total with array lookup.

**Alternatives (usually worse)**

- Per query DFS from `v` — O(n) each → O(nQ) too slow for n, Q up to 10⁵.

#### Further reading

- [CP-Algorithms: XOR and bitwise tricks](https://cp-algorithms.com/algebra/bit-operators.html) — properties of XOR
- [GeeksforGeeks: Subtree of a node](https://www.geeksforgeeks.org/subtree-of-a-node-in-an-n-ary-tree/) — DFS subtree definition
- [USACO Guide: Tree DP / subtrees](https://usaco.guide/CPH/) — aggregating subtree statistics
- [LeetCode 3375 (similar subtree theme)](https://leetcode.com/discuss/) — tree DFS patterns on LeetCode discuss

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function buildTree(n, edges, root = 1) {
  const adj = Array.from({ length: n + 1 }, () => []);
  for (const [u, v] of edges) {
    adj[u].push(v);
    adj[v].push(u);
  }
  return adj;
}

function subtreeXorQueries(n, edges, values, queries, root = 1) {
  const adj = buildTree(n, edges, root);
  const subXor = Array(n + 1).fill(0);

  function dfs(u, parent) {
    subXor[u] = values[u];
    for (const v of adj[u]) {
      if (v === parent) continue;
      dfs(v, u);
      subXor[u] ^= subXor[v];
    }
  }

  dfs(root, -1);
  return queries.map((node) => subXor[node]);
}

// Example: values = node index (as in exam snippet)
const n = 5;
const edges = [[1, 2], [1, 3], [3, 4], [3, 5]];
const values = [0, 1, 2, 3, 4, 5]; // 1-indexed
subtreeXorQueries(n, edges, values, [1, 3, 5]);
// node 1: 1^2^3^4^5, node 3: 3^4^5, etc.
```

#### Code walkthrough

1. Build adjacency list from undirected edges.
2. **DFS** from root; skip parent edge to avoid cycles.
3. Accumulate `subXor[u]` = own value XOR children's subtree XORs.
4. Answer each query by indexing `subXor[node]`.

#### Complexity

| | |
|-|-|
| Time | O(n + e + Q) — one DFS + constant-time queries |
| Space | O(n + e) — adjacency + subXor array |

#### Edge cases

- **Single node tree** — query returns that node's value.
- **Root query** — XOR of entire tree.
- **Leaf query** — returns leaf value only.
- **values vs indices** — replace `values[u]` with actual weights if problem provides them.

</details>

<details><summary>Solution (other languages)</summary>

```C++
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100005;
vector<int> adj[MAXN];
int subXor[MAXN];

void dfs(int u, int p) {
    subXor[u] = u;
    for (int v : adj[u]) {
        if (v == p) continue;
        dfs(v, u);
        subXor[u] ^= subXor[v];
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, e;
    cin >> n >> e;

    while(e--) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, -1);

    int Q; cin >> Q;
    while (Q--) {
        int node; cin >> node;
        cout << subXor[node] << "\n";
    }
}
```

</details>
</article>


<article>

A very large number (length between 50 to 100 digits) in string format is given. You need to check if the number is divisible by 7. Solve this for t test cases.

<details><summary>Theory and explanation</summary>

JavaScript and other languages cannot store 100-digit integers in native `number` (IEEE double loses precision around 2⁵³). The standard approach is **modular arithmetic on digits** without building the full big integer.

**Core idea**

If `R = (R_prev × 10 + d) mod 7`, processing digits left to right yields the remainder of the entire number modulo 7.

Proof sketch: if string `S = S' × 10 + d`, then `S mod 7 = ((S' mod 7) × 10 + d) mod 7`.

**Algorithm**

```
rem = 0
for each character c in num:
  rem = (rem * 10 + (c - '0')) % 7
return rem == 0
```

**Why it works for huge strings**

Only `rem` stays in `[0, 6]` — **O(1) extra space**, **O(L)** time per number for length L.

**Alternatives (less common in contests)**

- Parse into bigint (`BigInt` in JS) — works for 100 digits but slower and not always allowed.
- Divisibility tricks for 7 exist but digit DP mod is simplest and generalizable to any mod.

#### Further reading

- [CP-Algorithms: Binary exponentiation / modular arithmetic](https://cp-algorithms.com/algebra/module-arithmetic.html) — mod properties
- [GeeksforGeeks: Large number divisible by 7](https://www.geeksforgeeks.org/check-large-number-divisible-7-not/) — digit-by-digit method
- [MDN: BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt) — when native big integers are acceptable
- [Wikipedia: Modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic) — formal foundation

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function divisibleBy7(num) {
  let rem = 0;
  for (const c of num) {
    rem = (rem * 10 + (c.charCodeAt(0) - 48)) % 7;
  }
  return rem === 0;
}

function solveTests(lines) {
  const t = Number(lines[0]);
  const out = [];
  for (let i = 1; i <= t; i++) {
    out.push(divisibleBy7(lines[i].trim()) ? 'YES' : 'NO');
  }
  return out;
}

divisibleBy7('123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'); // false
divisibleBy7('7'); // true
```

#### Code walkthrough

- Initialize remainder `0`.
- For each digit, update `rem = (rem * 10 + digit) % 7` using char code for `'0'`.
- After all digits, divisibility ⇔ `rem === 0`.

#### Complexity

| | |
|-|-|
| Time | O(L) per test case — L = string length |
| Space | O(1) |

#### Edge cases

- **Leading zeros** — `"0007"` → valid, divisible.
- **Empty string** — define as 0 or invalid; 0 is divisible by 7.
- **Very large t** — total time O(sum of lengths), not O(t × maxLen) if inputs small.
- **Negative numbers** — if leading `-`, handle sign separately (not in typical BD test).

</details>

<details><summary>Solution (other languages)</summary>

```C++
#include <bits/stdc++.h>
using namespace std;

bool divisibleBy7(const string &num) {
    int rem = 0;
    for (char c : num) {
        rem = (rem * 10 + (c - '0')) % 7;
    }
    return rem == 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        string num; cin >> num;
        cout << (divisibleBy7(num) ? "YES" : "NO") << "\n";
    }
}
```

</details>
</article>


<article>

Implement Merge Sort for t test cases.

<details><summary>Theory and explanation</summary>

**Merge sort** is a divide-and-conquer comparison sort:

1. **Divide** — split array into two halves.
2. **Conquer** — recursively sort each half.
3. **Combine** — **merge** two sorted halves into one sorted array.

**Merge step**

Two pointers walk left and right sorted subarrays; repeatedly take the smaller head element. Remaining tail copied in O(k).

**Complexity**

| | |
|-|-|
| Time | **O(n log n)** — always; log n levels, O(n) merge per level |
| Space | **O(n)** auxiliary for temporary left/right arrays (or O(n) total with careful indexing) |

**Properties**

- **Stable** — equal elements keep relative order if merge takes from left when `<=`.
- **Not in-place** in typical textbook implementations (unlike heap sort).
- **External sort** favorite — sequential merge passes suit disk.

**vs quicksort**

- Merge sort guarantees O(n log n); quicksort average O(n log n) but O(n²) worst case.
- Merge sort uses extra memory; quicksort often in-place.

#### Further reading

- [Visualgo: Merge Sort](https://visualgo.net/en/sorting) — divide and merge animation
- [MDN: Array.prototype.sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort) — JS built-in (Timsort) vs manual merge sort
- [GeeksforGeeks: Merge Sort](https://www.geeksforgeeks.org/merge-sort/) — iterative and recursive variants
- [CLRS merge sort chapter (MIT OCW)](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-3-more-on-sorting/) — stability proof sketch

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function merge(arr, l, m, r) {
  const left = arr.slice(l, m + 1);
  const right = arr.slice(m + 1, r + 1);
  let i = 0, j = 0, k = l;

  while (i < left.length && j < right.length) {
    if (left[i] <= right[j]) arr[k++] = left[i++];
    else arr[k++] = right[j++];
  }
  while (i < left.length) arr[k++] = left[i++];
  while (j < right.length) arr[k++] = right[j++];
}

function mergeSort(arr, l = 0, r = arr.length - 1) {
  if (l >= r) return;
  const m = (l + r) >> 1;
  mergeSort(arr, l, m);
  mergeSort(arr, m + 1, r);
  merge(arr, l, m, r);
}

function solveMergeSortTests(testCases) {
  return testCases.map((arr) => {
    const copy = arr.slice();
    mergeSort(copy);
    return copy;
  });
}

solveMergeSortTests([[5, 2, 8, 1], [3, 3, 1]]); // [[1,2,5,8], [1,3,3]]
```

#### Code walkthrough

1. **Base case** — segment length 1 (`l >= r`).
2. **Split** at mid `m = (l + r) >> 1`.
3. **Merge** copies `[l..m]` and `[m+1..r]` to temp arrays, two-pointer merge back into `arr`.

#### Complexity

| | |
|-|-|
| Time | O(n log n) per array |
| Space | O(n) — temp arrays per merge level (O(n log n) if all levels counted; O(n) with single aux buffer optimization) |

#### Edge cases

- **Empty array** — no-op.
- **Single element** — already sorted.
- **All equal** — stable merge preserves order.
- **Large n** — watch stack depth O(log n) for recursion; use iterative bottom-up for huge arrays.

</details>

<details><summary>Solution (other languages)</summary>

```C++
#include <bits/stdc++.h>
using namespace std;

void merge(vector<int> &a, int l, int m, int r) {
    vector<int> left(a.begin() + l, a.begin() + m + 1);
    vector<int> right(a.begin() + m + 1, a.begin() + r + 1);

    int i = 0, j = 0, k = l;
    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) a[k++] = left[i++];
        else a[k++] = right[j++];
    }
    while (i < left.size()) a[k++] = left[i++];
    while (j < right.size()) a[k++] = right[j++];
}

void mergeSort(vector<int> &a, int l, int r) {
    if (l >= r) return;
    int m = (l + r) / 2;
    mergeSort(a, l, m);
    mergeSort(a, m + 1, r);
    merge(a, l, m, r);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) cin >> arr[i];
        mergeSort(arr, 0, n - 1);
        for (int x : arr) cout << x << " ";
        cout << "\n";
    }
}
```

</details>
</article>


<article>

A non-decreasing array is given. A new group is formed whenever the difference between two consecutive numbers is greater than 1 (the later number starts a new group). You are allowed to remove any elements from the array to maximize the number of groups. Return the maximum number of groups you can form. Solve this for t test cases.

[**💻 Submit Code**](https://codeforces.com/problemset/problem/2114/C)

<details><summary>Theory and explanation</summary>

**Natural grouping** on a sequence `a[0..n-1]` (non-decreasing):

- Start a group at index `0`.
- Whenever `a[i] - a[i-1] > 1`, element `a[i]` starts a **new group**.
- Within a group, consecutive values differ by at most 1.

**With deletions** you may drop elements (keeping relative order) to **maximize** the number of groups in the remaining subsequence.

**Greedy on sorted order**

After sorting (the given array is already non-decreasing, so order is preserved), scan left to right:

1. Start a new group at current index `i`, record `last = a[i]`.
2. Advance `i` while `a[i] - last <= 1` — these elements can belong to the **same** group without forcing a split (pick at most one per “chain” if maximizing groups — skip the rest).
3. When `a[i] - last > 1`, the loop ends; increment group count and repeat from new `i`.

The exam reference solution sorts then applies this chunk scan — each group consumes a **maximal segment** where values stay within 1 of the segment's first chosen element, then skips to the next segment boundary.

**Intuition for maximizing groups**

You want many **break points** where consecutive kept elements differ by **> 1**. Within a tight cluster (values differing by ≤ 1), one element suffices per group; extra elements in that cluster do not increase group count.

**Complexity**

- Sort: O(n log n) if needed; O(n) scan.
- For already sorted input: **O(n)** per test.

#### Further reading

- [Codeforces 2114C](https://codeforces.com/problemset/problem/2114/C) — original problem statement
- [GeeksforGeeks: Maximize groups (similar greedy)](https://www.geeksforgeeks.org/) — array grouping patterns
- [CP-Algorithms: Greedy algorithms](https://cp-algorithms.com/algorithms/greedy.html) — when greedy applies
- [LeetCode discussion: group consecutive with gap](https://leetcode.com/discuss/) — gap-based partitioning

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function maxGroups(arr) {
  const a = arr.slice().sort((x, y) => x - y);
  let groups = 0;
  let i = 0;
  const n = a.length;

  while (i < n) {
    groups++;
    const last = a[i];
    while (i < n && a[i] - last <= 1) i++;
  }
  return groups;
}

function solveGroupTests(testCases) {
  return testCases.map(maxGroups);
}

maxGroups([1, 2, 2, 3, 10, 11]); // e.g. groups around gaps > 1
```

#### Code walkthrough

1. **Sort** copy (safe if input not strictly non-decreasing).
2. **`groups++`** at each new segment start.
3. **Inner while** skips elements still within 1 of segment anchor `last` — they merge into one group for counting purposes.
4. Next iteration starts where gap exceeds 1.

#### Complexity

| | |
|-|-|
| Time | O(n log n) with sort; O(n) if already sorted |
| Space | O(n) for sorted copy |

#### Edge cases

- **Single element** — one group.
- **All equal** — one group (all diffs 0).
- **All gaps > 1** — n groups (keep one per element).
- **Empty array** — define as 0 groups.

</details>

<details><summary>Solution (other languages)</summary>

```C++
#include <bits/stdc++.h>
using namespace std;

int maxGroups(vector<int>& arr) {
    int n = arr.size();
    int groups = 0;
    for (int i = 0; i < n;) {
        groups++;
        int last = arr[i];
        while (i < n && arr[i] - last <= 1) i++;
    }
    return groups;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) cin >> arr[i];
        sort(arr.begin(), arr.end());
        cout << maxGroups(arr) << "\n";
    }
}
```

</details>
</article>


<article>

For a given number, find and print all of its distinct prime divisors. Solve this for t test cases.

<details><summary>Theory and explanation</summary>

**Prime factorization** — express `n` as product of primes. The problem asks for **distinct** prime divisors only (each prime once, regardless of multiplicity).

**Trial division — O(√n)**

For `i` from 2 to `√n`:

- If `i` divides `n`, `i` is a prime factor; record it and divide out all powers of `i`.
- After loop, if remaining `n > 1`, that remainder is a prime factor (e.g. large prime > √original).

**Why check only up to √n**

If `n = a × b` and `a ≤ b`, then `a ≤ √n`. Any composite factor has a prime factor ≤ √n.

**Optimizations**

- Skip even `i` after handling 2.
- Precompute primes via sieve if many queries on small `n`.
- For 64-bit `n`, trial division to √n is fine in contests.

**Distinct vs full factorization**

- `12 = 2² × 3` → distinct primes `{2, 3}`.
- Do not print `2` twice.

#### Further reading

- [CP-Algorithms: Sieve of Eratosthenes](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html) — precomputation
- [CP-Algorithms: Prime factorization](https://cp-algorithms.com/algebra/factorization.html) — trial division and Pollard rho
- [GeeksforGeeks: Print all prime factors](https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/) — walkthrough
- [Wikipedia: Integer factorization](https://en.wikipedia.org/wiki/Integer_factorization) — hardness for huge numbers

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function distinctPrimeDivisors(n) {
  const primes = [];
  if (n % 2n === 0n) {
    primes.push(2n);
    while (n % 2n === 0n) n /= 2n;
  }
  for (let i = 3n; i * i <= n; i += 2n) {
    if (n % i === 0n) {
      primes.push(i);
      while (n % i === 0n) n /= i;
    }
  }
  if (n > 1n) primes.push(n);
  return primes;
}

// Number version for contest-sized n (<= 1e12 in JS number safely with care)
function distinctPrimeDivisorsNumber(n) {
  const primes = [];
  if (n % 2 === 0) {
    primes.push(2);
    while (n % 2 === 0) n = Math.floor(n / 2);
  }
  for (let i = 3; i * i <= n; i += 2) {
    if (n % i === 0) {
      primes.push(i);
      while (n % i === 0) n = Math.floor(n / i);
    }
  }
  if (n > 1) primes.push(n);
  return primes;
}

distinctPrimeDivisorsNumber(12);   // [2, 3]
distinctPrimeDivisorsNumber(17);   // [17]
```

#### Code walkthrough

1. Pull out factor **2** separately (optional optimization).
2. Test odd `i` up to `√n`; on divide, push `i` once and strip all copies.
3. Remaining `n > 1` is prime (larger than √original quotient).

#### Complexity

| | |
|-|-|
| Time | O(√n) per test case |
| Space | O(k) — k = number of distinct prime factors (small) |

#### Edge cases

- **`n = 1`** — no prime divisors; return empty.
- **Prime `n`** — return `[n]`.
- **Perfect square** — e.g. 49 → `[7]` only once.
- **Large n** — use `BigInt` variant if n exceeds Number.MAX_SAFE_INTEGER.

</details>

<details><summary>Solution (other languages)</summary>

```C++
#include <bits/stdc++.h>
using namespace std;

vector<long long> primeDivisors(long long n) {
    vector<long long> primes;
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            primes.push_back(i);
            while (n % i == 0) n /= i;
        }
    }
    if (n > 1) primes.push_back(n);
    return primes;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        long long n; cin >> n;
        vector<long long> primes = primeDivisors(n);
        for (long long p : primes) cout << p << " ";
        cout << "\n";
    }
}
```

</details>
</article>

### Analytical (10 Marks)

<article>

There are 3 switches S1, S2, and S3 outside a server room. Inside the room, there are 3 cooling fans, and each fan is connected to exactly one switch. However, the switches are not labeled, so you don’t know which switch controls which fan. You are allowed to enter the server room only once. How can you figure out which switch controls which fan?

<details><summary>Theory and explanation</summary>

Classic **logic puzzle** — three switches, three fans, **one room entry**. You need **persistent state** beyond on/off: **heat** from a running fan.

**Strategy**

1. **Turn S1 ON** for several minutes (long enough for its fan to warm up if connected).
2. **Turn S1 OFF**, **turn S2 ON**.
3. **Enter the room once** and observe each fan:

| Fan state | Switch |
|-----------|--------|
| **Running** | S2 (currently on) |
| **Off, but warm** | S1 (was on, then off — thermal residue) |
| **Off and cold** | S3 (never turned on) |

**Why it works**

- **S2** is the only switch ON during inspection → its fan must be spinning.
- **S1** heated its fan then switched off → fan stopped but motor housing still warm.
- **S3** never energized → fan stays cold.

**Constraints to state in interview**

- Wait time must exceed fan cooldown/heating threshold (minutes, not seconds).
- Assumes fans produce detectable heat — standard puzzle assumption.
- Exactly one fan per switch (bijection).

**Generalization**

- n switches, one entry → similar tricks use heat, light bulbs, or delayed effects; information theory bound: need distinguishable states per device.

#### Further reading

- [Classic puzzle: Three switches and three bulbs](https://math.stackexchange.com/questions/130836/three-switches-three-light-bulbs-puzzle) — Math StackExchange proof
- [Brainzilla: Light switch puzzle](https://www.brainzilla.com/logic/logic-grid/three-switches/) — fan/bulb variant
- [Wikipedia: Logic puzzle](https://en.wikipedia.org/wiki/Logic_puzzle) — constraint satisfaction framing
- [MIT recreational math archives](https://math.mit.edu/~rec/) — similar one-shot inference puzzles

</details>

<details><summary>Solution (JavaScript)</summary>

State machine simulation — maps observation to switch assignment after executing the protocol.

```js
/**
 * @param {'running'|'warm'|'cold'} fanA
 * @param {'running'|'warm'|'cold'} fanB
 * @param {'running'|'warm'|'cold'} fanC
 * @returns {Record<string, string>} fan -> switch label
 */
function deduceSwitchMapping(fanA, fanB, fanC) {
  const fans = [
    { name: 'Fan1', state: fanA },
    { name: 'Fan2', state: fanB },
    { name: 'Fan3', state: fanC },
  ];

  const mapping = {};
  for (const f of fans) {
    if (f.state === 'running') mapping[f.name] = 'S2';
    else if (f.state === 'warm') mapping[f.name] = 'S1';
    else if (f.state === 'cold') mapping[f.name] = 'S3';
    else throw new Error('Invalid observation');
  }
  return mapping;
}

deduceSwitchMapping('warm', 'running', 'cold');
// { Fan1: 'S1', Fan2: 'S2', Fan3: 'S3' }
```

#### Code walkthrough

- Execute physical protocol (S1 on → wait → S1 off, S2 on → enter).
- Classify each fan: running → S2, warm → S1, cold → S3.
- Produces bijection if observations are consistent.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual); O(1) for three fans |
| Space | O(1) |

#### Edge cases

- **Two fans warm** — impossible under protocol; indicates wrong wait time or multiple fans per switch.
- **All cold** — S2 not actually on or fans broken.
- **Safety** — in real server rooms, follow facility procedures; puzzle is logical only.

</details>

</article>
