---
description: IQVIA interview questions, IQVIA interview stages, IQVIA interview details, IQVIA interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/iqvia
---
# IQVIA

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-| :- |
| Founding year | |
| Company Website | https://www.iqvia.com/ |
| Career Website | https://jobs.iqvia.com/en/search-jobs |
| Technologies Used| .Net, Python, Javascript, Angular |

## Introduction
[IQVIA](https://www.iqvia.com/) is an American Fortune 500 and S&P 500 multinational company serving the combined industries of health information technology and clinical research. They hire professionals from Bangladesh as remote.
## Interview Stages
The preliminary test of IQVIA consists of 3 stage

- **Aptitude:** Understanding, Vocabulary, Reasoning, Maths
- **Automata:** Easy level coding test
- **Automata Pro:** Medium level coding test

Then if selected there will be a technical interview. 

## Questions

<article>

Given a string of lowercase characters. Find the count of characters which only occured once in the string.

[**💻 Submit Code**](https://supecoder.dev/questions/Count%20of%20Characters%20Occurring%20Exactly%20Once?questionId=66ae165b9e71a163cdd21527)

<details><summary>Theory and explanation</summary>

Count characters that appear **exactly once** in the string.

**Approaches**

1. **Frequency array / hash map** — scan once to count each char, scan again (or iterate map) to count entries with frequency `1`. **O(n) time, O(1) space** for lowercase English (26 buckets) or **O(k)** for alphabet size `k`.
2. **Sort then scan** — sort the string, walk runs of equal characters; a run of length `1` contributes one to the answer. **O(n log n)** from sorting.

**Interview talking points**

- Clarify alphabet size (lowercase only → fixed 26).
- Sorting avoids extra hash structure but costs log factor.
- For Unicode or large alphabets, prefer a map.

#### Further reading

- [LeetCode: First Unique Character](https://leetcode.com/problems/first-unique-character-in-a-string/) — related frequency problem
- [MDN: Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) — counting in JavaScript
- [GeeksforGeeks: Count characters frequency](https://www.geeksforgeeks.org/count-number-of-times-each-character-appears-in-a-string/) — hash vs sort

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function countCharsOnce(s) {
  const freq = new Map();
  for (const ch of s) freq.set(ch, (freq.get(ch) || 0) + 1);
  let ans = 0;
  for (const count of freq.values()) if (count === 1) ans++;
  return ans;
}

// Sort-based variant
function countCharsOnceSorted(s) {
  const arr = [...s].sort();
  let ans = 0;
  let i = 0;
  while (i < arr.length) {
    let j = i;
    while (j < arr.length && arr[j] === arr[i]) j++;
    if (j - i === 1) ans++;
    i = j;
  }
  return ans;
}
```

#### Code walkthrough

1. **Hash map** — first pass builds frequencies; second pass counts keys with value `1`.
2. **Sorted** — group equal adjacent chars; increment when group length is `1`.

#### Complexity

| Approach | Time | Space |
|----------|------|-------|
| Hash map | O(n) | O(1) for 26 lowercase letters |
| Sort | O(n log n) | O(n) if copying for sort |

#### Edge cases

- **Empty string** — return `0`.
- **All duplicates** — return `0`.
- **Single character** — return `1`.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
int solve(string s) {
    sort(s.begin(),s.end());
    int unik = 0;
    int cnt = 1;
    for(int i=1;i<s.size();i++){
        if( s[i] != s[i-1] ){
            unik += (cnt == 1);
            cnt = 0;
        }
        cnt++;
    }
    unik += (cnt == 1);
    return unik;
}
```

</details>
</article>

<article>

Given n,Find all primes less than equal n.

<details><summary>Theory and explanation</summary>

Return all **primes ≤ n**.

**Approaches**

1. **Trial division** — for each `i` from 2 to `n`, test divisibility up to `i-1`. Simple but **O(n²)** or **O(n √n)** with early stop at √i.
2. **Sieve of Eratosthenes** — boolean array `notPrime`; for each prime `i`, mark multiples starting at `i²`. **O(n log log n)** time, **O(n)** space — standard for `n` up to millions.

**Interview talking points**

- Always mention sieve for competitive constraints.
- `1` is not prime; start from `2`.
- For very large `n`, segmented sieve or bitset optimizations may apply.

#### Further reading

- [CP-Algorithms: Sieve of Eratosthenes](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html) — implementation details
- [GeeksforGeeks: Sieve](https://www.geeksforgeeks.org/sieve-of-eratosthenes/) — walkthrough
- [LeetCode: Count Primes](https://leetcode.com/problems/count-primes/) — related counting variant

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function sievePrimes(n) {
  if (n < 2) return [];
  const notPrime = Array(n + 1).fill(false);
  const primes = [];
  for (let i = 2; i <= n; i++) {
    if (notPrime[i]) continue;
    primes.push(i);
    for (let j = i * i; j <= n; j += i) notPrime[j] = true;
  }
  return primes;
}

function trialPrimes(n) {
  const primes = [];
  for (let i = 2; i <= n; i++) {
    let ok = true;
    for (let d = 2; d * d <= i; d++) {
      if (i % d === 0) { ok = false; break; }
    }
    if (ok) primes.push(i);
  }
  return primes;
}
```

#### Code walkthrough

1. **Sieve** — outer loop finds next unmarked `i` (prime); inner marks multiples.
2. Start marking at `i * i` because smaller multiples already marked by smaller primes.
3. **Trial** — only test divisors up to √i.

#### Complexity

| Approach | Time | Space |
|----------|------|-------|
| Sieve | O(n log log n) | O(n) |
| Trial (√ check) | O(n √n) | O(1) extra |

#### Edge cases

- **n < 2** — empty list.
- **n = 2** — `[2]`.

</details>

<details><summary>Solution (other languages)</summary>

::: code-group
```cpp [O(n^2)]
vector<int> solve(int n) {
    vector<int> primes;
    for(int i=2;i<=n;i++){
        bool isPrime = true;
        for(int j=2;j<i;j++) {
            if( i%j == 0 ) isPrime = false;
        }
        if( isPrime ) primes.push_back(i);
    }
    return primes;
}
```
```cpp [O(n logn)]
vector<int> solve(int n) {
    bool notPrime[n+1] = {0};
    vector<int> primes;
    for(int i=2;i<=n;i++){
        if( notPrime[i] == true ) continue;
        primes.push_back(i);
        for(int j=i*i;j<=n;j+=i) notPrime[j] = true;
    }
    return primes;
}
```
:::

</details>
</article>

<article>

Given coordinates x,y and radius r of two circle. Find the area of intersection between them. Print area in double with 6 digit precision.

<details><summary>Theory and explanation</summary>

Compute **intersection area** of two circles `(x1,y1,r1)` and `(x2,y2,r2)`.

**Geometry cases** (distance `d` between centers)

| Condition | Intersection |
|-----------|--------------|
| `d ≥ r1 + r2` | No overlap → area 0 |
| `d ≤ |r1 − r2|` | One circle inside other → area of smaller circle |
| Otherwise | Lens-shaped overlap — sum of two circular segments |

For partial overlap, use **central angles** `α`, `β` from the law of cosines, then segment areas:

`segment = (θ/2) · r² − (1/2) · r² · sin(θ)`

**Interview talking points**

- Use `long double` / precise π for floating output.
- Handle concentric and tangent circles as boundary cases.
- IQVIA automata problems often expect geometry formulas, not Monte Carlo.

#### Further reading

- [GeeksforGeeks: Area of intersection of two circles](https://www.geeksforgeeks.org/area-of-intersection-of-two-circles/) — formula reference
- [Wolfram MathWorld: Circle-circle intersection](https://mathworld.wolfram.com/Circle-CircleIntersection.html) — derivation
- [CP-Algorithms: Geometry basics](https://cp-algorithms.com/geometry/basic-geometry.html) — distance and angles

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function circleIntersectionArea(x1, y1, r1, x2, y2, r2) {
  const d = Math.hypot(x2 - x1, y2 - y1);
  if (d >= r1 + r2) return 0;
  if (d <= Math.abs(r1 - r2)) {
    const r = Math.min(r1, r2);
    return Math.PI * r * r;
  }
  const alpha = Math.acos((r1 * r1 + d * d - r2 * r2) / (2 * r1 * d)) * 2;
  const beta = Math.acos((r2 * r2 + d * d - r1 * r1) / (2 * r2 * d)) * 2;
  const seg = (theta, r) => 0.5 * r * r * (theta - Math.sin(theta));
  return seg(alpha, r1) + seg(beta, r2);
}
```

#### Code walkthrough

1. Compute center distance `d`.
2. Branch on separation, containment, or partial overlap.
3. Partial case: angles via `acos`, segment areas via standard lens formula.

#### Complexity

| | |
|-|-|
| Time | O(1) |
| Space | O(1) |

#### Edge cases

- **Identical circles** — full circle area `π r²`.
- **Tangent externally** (`d = r1 + r2`) — area 0.
- **Zero radius** — treat as point; usually area 0.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
// src: https://www.geeksforgeeks.org/area-of-intersection-of-two-circles/

#include <bits/stdc++.h>
using namespace std;
#define ld long double
// Function to return area of intersection
long long int
intersectionArea(long double X1, long double Y1,
                    long double R1, long double X2,
                    long double Y2, long double R2){
	long double Pi = 3.14;
	long double d, alpha, beta, a1, a2;
	long long int ans;

	// Calculate the euclidean distance
	// between the two points
	d = sqrt((X2 - X1) * (X2 - X1) + (Y2 - Y1) * (Y2 - Y1));

	if (d > R1 + R2)
		ans = 0;
	else if (d <= (R1 - R2) && R1 >= R2)
		ans = floor(Pi * R2 * R2);
	else if (d <= (R2 - R1) && R2 >= R1)
		ans = floor(Pi * R1 * R1);
	else {
		alpha = acos((R1 * R1 + d * d - R2 * R2) / (2 * R1 * d))* 2;
		beta = acos((R2 * R2 + d * d - R1 * R1) / (2 * R2 * d))* 2;
		a1 = 0.5 * beta * R2 * R2 - 0.5 * R2 * R2 * sin(beta);
		a2 = 0.5 * alpha * R1 * R1 - 0.5 * R1 * R1 * sin(alpha);
		ans = floor(a1 + a2);
	}

	return ans;
}

```

</details>
</article>

<article>

Given a list of ranges. Find the length covered by at least one of the range. <br>
input: [[1,3],[2,5],[6,7]] <br>
output: 5 <br>
explanation: range [1,5],[6,7] are covered by at least one range

<details><summary>Theory and explanation</summary>

Given intervals `[start, end]`, compute **total length** of the union (merge overlapping intervals).

**Algorithm**

1. Sort intervals by start (then end).
2. Track current merged segment `[st, en]`.
3. If next interval starts after `en`, add `en - st` to answer and start new segment.
4. Else extend `en = max(en, next.end)`.
5. Add final segment length.

This is the classic **merge intervals** problem on a number line.

**Interview talking points**

- Clarify inclusive vs exclusive endpoints — sample uses inclusive length `end - start` on merged spans (adjust if half-open).
- Same pattern as meeting rooms, skyline coverage.

#### Further reading

- [LeetCode 56: Merge Intervals](https://leetcode.com/problems/merge-intervals/) — canonical form
- [LeetCode 435: Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) — related greedy
- [GeeksforGeeks: Merge intervals](https://www.geeksforgeeks.org/merging-intervals/) — walkthrough

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function coveredLength(ranges) {
  if (!ranges.length) return 0;
  ranges.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  let st = ranges[0][0];
  let en = ranges[0][1];
  let covered = 0;
  for (let i = 1; i < ranges.length; i++) {
    const [s, e] = ranges[i];
    if (s > en) {
      covered += en - st;
      st = s;
      en = e;
    } else {
      en = Math.max(en, e);
    }
  }
  covered += en - st;
  return covered;
}
```

#### Code walkthrough

1. Sort by start time.
2. On gap (`s > en`), flush previous merged interval length.
3. Overlap extends `en` only.

#### Complexity

| | |
|-|-|
| Time | O(n log n) for sort |
| Space | O(1) extra |

#### Edge cases

- **Single interval** — its length.
- **Nested intervals** — outer envelope only.
- **Touching intervals** `[1,2],[2,3]` — clarify if touching counts as overlap.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
int solve(vector<pair<int,int>> ranges) {
    sort(ranges.begin(),ranges.end());
    int covered = 0;
    int st = ranges[0].first;
    int en = ranges[0].second;
    for(int i=1;i<ranges.size();i++){
        if( ranges[i].first > en ) {
            covered += en - st;
            st = ranges[i].first;
            en = ranges[i].second;
        }
        en = max(en,ranges[i].second);
    }
    covered += en - st;
    return covered;
}
```

</details>
</article>

<article>

Sort array elements by their frequency and in case of tie, keep the order they arrive in the original array.

<details><summary>Theory and explanation</summary>

**Stable frequency sort**: elements with higher frequency come first; among equal frequency, preserve **original order** (stable sort by frequency descending).

**Algorithm**

1. Count frequencies with a map while recording **first occurrence index** for tie-breaking.
2. Sort unique values by `(−freq, firstIndex)` or use bucket sort by frequency from `n` down to `1` (stable if you push in first-seen order).

**Why stable matters**

- `[1,2,2,3,3,3]` → `[3,3,3,2,2,1]` — two `2`s stay in relative order.

**Interview talking points**

- Bucket sort by frequency achieves **O(n)** when frequencies bounded by `n`.
- JavaScript `sort` is stable in modern engines — `(a,b) => freq(b)-freq(a)` with index tie-break works.

#### Further reading

- [LeetCode 1636: Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/) — inverse ordering
- [LeetCode 451: Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) — same idea on strings
- [MDN: Array.prototype.sort stability](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort) — stable sort note

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function sortByFrequencyStable(arr) {
  const freq = new Map();
  const firstIdx = new Map();
  arr.forEach((v, i) => {
    freq.set(v, (freq.get(v) || 0) + 1);
    if (!firstIdx.has(v)) firstIdx.set(v, i);
  });
  return [...arr]
    .filter((v, i, a) => a.indexOf(v) === i) // unique in first-seen order
    .sort((a, b) => {
      const df = freq.get(b) - freq.get(a);
      return df !== 0 ? df : firstIdx.get(a) - firstIdx.get(b);
    })
    .flatMap(v => Array(freq.get(v)).fill(v));
}

// Bucket O(n) variant
function sortByFrequencyBucket(arr) {
  const freq = new Map();
  arr.forEach(v => freq.set(v, (freq.get(v) || 0) + 1));
  const buckets = Array(arr.length + 1).fill(null).map(() => []);
  const order = [];
  for (const v of arr) if (!order.includes(v)) order.push(v);
  for (const v of order) buckets[freq.get(v)].push(v);
  const out = [];
  for (let f = buckets.length - 1; f >= 0; f--)
    for (const v of buckets[f]) for (let k = 0; k < f; k++) out.push(v);
  return out;
}
```

#### Code walkthrough

1. Build frequency and first-index maps in one pass.
2. Sort unique keys by descending freq, ascending first index.
3. Expand each value `freq` times — stable reconstruction.

#### Complexity

| Approach | Time | Space |
|----------|------|-------|
| Sort keys | O(n log n) | O(n) |
| Bucket | O(n) | O(n) |

#### Edge cases

- **All unique** — original order preserved.
- **Single element** — unchanged.
- **Equal frequency throughout** — stable original order.

</details>
</article>

<article>

Given the connection between cities, Count the number of disjoint clusters of cities.

<details><summary>Theory and explanation</summary>

Count **connected components** in an undirected graph of cities.

**Approaches**

1. **DFS / BFS** — iterate all nodes; each unvisited node starts a new component; flood-fill neighbors. **O(V + E)**.
2. **Union-Find (Disjoint Set Union)** — for each edge, `union(u,v)`; answer = number of distinct roots after all unions. **O(E α(V))** — good for dynamic or edge-list input.

**Interview talking points**

- Clarify if graph is guaranteed connected — if yes, answer is 1.
- Isolated city with no edges is its own component.
- Same problem as "Number of Provinces" / "Connected components".

#### Further reading

- [LeetCode 547: Number of Provinces](https://leetcode.com/problems/number-of-provinces/) — adjacency matrix variant
- [LeetCode 323: Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) — edge list
- [CP-Algorithms: DSU](https://cp-algorithms.com/data_structures/disjoint_set_union.html) — union-find

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function countComponents(n, edges) {
  const adj = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) {
    adj[u].push(v);
    adj[v].push(u);
  }
  const seen = new Array(n).fill(false);
  let components = 0;
  function dfs(u) {
    seen[u] = true;
    for (const v of adj[u]) if (!seen[v]) dfs(v);
  }
  for (let i = 0; i < n; i++) {
    if (!seen[i]) { components++; dfs(i); }
  }
  return components;
}

class DSU {
  constructor(n) {
    this.p = Array.from({ length: n }, (_, i) => i);
    this.count = n;
  }
  find(x) {
    if (this.p[x] !== x) this.p[x] = this.find(this.p[x]);
    return this.p[x];
  }
  union(a, b) {
    a = this.find(a); b = this.find(b);
    if (a === b) return;
    this.p[a] = b;
    this.count--;
  }
}
function countComponentsDSU(n, edges) {
  const dsu = new DSU(n);
  for (const [u, v] of edges) dsu.union(u, v);
  return dsu.count;
}
```

#### Code walkthrough

1. **DFS** — each outer-loop launch on unvisited node increments component count.
2. **DSU** — start with `n` components; each successful union decrements count.

#### Complexity

| | Time | Space |
|-|------|-------|
| DFS/BFS | O(V + E) | O(V + E) |
| DSU | O(E α(V)) | O(V) |

#### Edge cases

- **No edges** — `n` isolated components.
- **Complete graph** — 1 component.

</details>
</article>

<article>

Given a string of characters S and a specific character C. Find the number of occurance of C in S.

<details><summary>Theory and explanation</summary>

Simple **character frequency count**: iterate the string and increment when `s[i] === C`.

**Alternatives**

- Built-in: `s.split(C).length - 1` (careful with empty matches) or filter/count in functional style.
- For many queries on same string, preprocess prefix counts or frequency map.

**Interview talking points**

- Case sensitivity — clarify uppercase vs lowercase.
- Time is always **O(n)** single pass; space **O(1)**.

#### Further reading

- [MDN: String.prototype.match](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match) — regex counting
- [LeetCode 383: Ransom Note](https://leetcode.com/problems/ransom-note/) — frequency maps

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function countChar(s, c) {
  let cnt = 0;
  for (const ch of s) if (ch === c) cnt++;
  return cnt;
}

// Functional
const countCharFn = (s, c) => [...s].filter(ch => ch === c).length;
```

#### Code walkthrough

- Linear scan; compare each character to `C`.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases

- **C not present** — return 0.
- **Empty string** — return 0.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
int solve(string s, char c) {
    int cnt = 0;
    for(auto cc:s) cnt += (cc==c);
    return cnt;
}
```

</details>
</article>

<article>

Given a range [l,r]. Find all primes between this range. 

<details><summary>Theory and explanation</summary>

**Primes in [l, r]** when `r` can be large but interval width `(r − l)` is moderate → use **segmented sieve**.

**Steps**

1. Sieve primes up to `√r` with classic Eratosthenes.
2. Mark composites in `[l, r]` using those base primes.
3. Collect unmarked numbers ≥ 2 in range.

For small ranges, trial division per number is acceptable.

**Interview talking points**

- Naive sieve of size `r` fails when `r` is 10⁹ but width is 10⁶.
- Handle `l = 1` (1 is not prime).

#### Further reading

- [CP-Algorithms: Segmented sieve](https://cp-algorithms.com/algebra/primality_sieve.html) — range queries
- [GeeksforGeeks: Segmented sieve](https://www.geeksforgeeks.org/segmented-sieve/) — implementation
- [LeetCode: Count Primes](https://leetcode.com/problems/count-primes/) — prefix sieve

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function primesUpTo(n) {
  const isComp = Array(n + 1).fill(false);
  const small = [];
  for (let i = 2; i <= n; i++) {
    if (!isComp[i]) {
      small.push(i);
      for (let j = i * i; j <= n; j += i) isComp[j] = true;
    }
  }
  return small;
}

function primesInRange(l, r) {
  if (r < 2) return [];
  const limit = Math.floor(Math.sqrt(r));
  const base = primesUpTo(limit);
  const size = r - l + 1;
  const seg = Array(size).fill(false);
  for (const p of base) {
    let start = Math.max(p * p, Math.ceil(l / p) * p);
    for (let j = start; j <= r; j += p) seg[j - l] = true;
  }
  const out = [];
  for (let i = Math.max(l, 2); i <= r; i++) if (!seg[i - l]) out.push(i);
  return out;
}
```

#### Code walkthrough

1. Generate small primes to √r.
2. Mark multiples in offset array indexed by `i - l`.
3. Collect indices where mark is false.

#### Complexity

| | |
|-|-|
| Time | O((r−l) log log r + √r log log √r) |
| Space | O(√r + (r−l)) |

#### Edge cases

- **l = r = 2** — `[2]`.
- **Range includes 1** — skip 1.

</details>
</article>

<article>

Given two binary string A,B. Find the minimum number of bit flips to change string A to string B.

<details><summary>Theory and explanation</summary>

Minimum **bit flips** = count positions where `A[i] !== B[i]` (Hamming distance).

If lengths differ, clarify padding or return impossible.

**Interview talking points**

- XOR trick: `(parseInt(a,2) ^ parseInt(b,2)).toString(2)` popcount — watch BigInt for long strings.
- Per-bit scan is O(n) and safest for arbitrary length strings.

#### Further reading

- [LeetCode 2220: Minimum Bit Flips](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/) — numeric variant
- [GeeksforGeeks: Minimum bit flips](https://www.geeksforgeeks.org/minimum-number-of-bit-flips-to-convert-a-into-b/) — XOR approach
- [MDN: BigInt bitwise XOR](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_XOR) — large binaries

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function minBitFlips(a, b) {
  if (a.length !== b.length) throw new Error('length mismatch');
  let flips = 0;
  for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) flips++;
  return flips;
}

function minBitFlipsXor(a, b) {
  let flips = 0;
  for (let i = 0; i < a.length; i++) flips += (a.charCodeAt(i) ^ b.charCodeAt(i)) & 1 ? 1 : 0;
  return flips;
}
```

#### Code walkthrough

- Compare each bit position; increment when bits differ.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases

- **Identical strings** — 0 flips.
- **Different lengths** — define behavior (error or pad).

</details>
</article>

<article>

2 shops sell apples in lots. their price is given. You cannot buy any loose apples. find minimum cost of buying exactly n apples.

<details><summary>Theory and explanation</summary>

Classic **coin change / unbounded knapsack** variant: shop 1 sells packs of size `a` at price `p1`, shop 2 sells packs of size `b` at price `p2`. Buy exactly `n` apples using any nonnegative combination of pack counts.

**Approach**

- Iterate number of packs from shop 1: `i = 0 … ⌊n/a⌋`; remainder `rem = n - i·a` must be divisible by `b`; cost = `i·p1 + (rem/b)·p2`.
- Or BFS on `(apples mod gcd(a,b))` if optimizing — for small `n`, brute force suffices.

**Interview talking points**

- If `gcd(a,b)` does not divide `n`, impossible → return −1.
- Compare **per-apple unit cost** for greedy intuition but greedy fails in general — try all valid combos.

#### Further reading

- [LeetCode 322: Coin Change](https://leetcode.com/problems/coin-change/) — minimum coins
- [GeeksforGeeks: Linear Diophantine](https://www.geeksforgeeks.org/linear-diophantine-equations/) — feasibility
- [CP-Algorithms: Extended Euclidean](https://cp-algorithms.com/algebra/extended-euclid-algorithm.html) — existence of solution

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function minAppleCost(n, a, p1, b, p2) {
  let best = Infinity;
  for (let x = 0; x * a <= n; x++) {
    const rem = n - x * a;
    if (rem % b !== 0) continue;
    const y = rem / b;
    best = Math.min(best, x * p1 + y * p2);
  }
  return best === Infinity ? -1 : best;
}
```

#### Code walkthrough

1. Try every count `x` of type-a packs.
2. Remaining apples must be fillable by type-b packs exactly.
3. Track minimum total price.

#### Complexity

| | |
|-|-|
| Time | O(n / a) ≤ O(n) |
| Space | O(1) |

#### Edge cases

- **Impossible n** — gcd(a,b) ∤ n → −1.
- **Cheaper bulk shop** — may require more packs than minimum count.

</details>
</article>

<article>

Given an integer array. Sort the array in nondecreasing order using frequency count of elements in the array. 

<details><summary>Theory and explanation</summary>

Sort by **ascending frequency** (nondecreasing frequency order). Ties typically preserve first appearance or sort by value — clarify with interviewer; IQVIA wording matches LeetCode 1636 style (increasing frequency, tie by value).

**Algorithm**

1. Count frequencies.
2. Sort values by `(freq asc, value asc)`.
3. Expand each value by its frequency.

#### Further reading

- [LeetCode 1636: Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/) — exact match
- [LeetCode 451: Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) — descending variant

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function sortArrayByFreqNonDecreasing(arr) {
  const freq = new Map();
  for (const v of arr) freq.set(v, (freq.get(v) || 0) + 1);
  const keys = [...freq.keys()].sort((a, b) => {
    const df = freq.get(a) - freq.get(b);
    return df !== 0 ? df : a - b;
  });
  return keys.flatMap(k => Array(freq.get(k)).fill(k));
}
```

#### Code walkthrough

1. Frequency map in one pass.
2. Sort unique keys by ascending frequency, then value.
3. Flatten repeated values.

#### Complexity

| | |
|-|-|
| Time | O(n log n) |
| Space | O(n) |

#### Edge cases

- **All same element** — unchanged multiset.
- **All unique** — sorted by value if tie-break by value.

</details>
</article>

<article>

Given an array of thresholds. For each threshold print the first negative number.

<details><summary>Theory and explanation</summary>

For each **threshold** `t`, find the **first negative** element in the array (left to right) that satisfies a condition — typically first element `< t` or first negative number in prefix. IQVIA variants often mean: given thresholds array `T`, for each `t ∈ T`, print first `arr[i] < 0` where `arr[i] < t` or simply first negative in array independent of `t`.

**Common interpretation**: for each threshold value, scan array left-to-right for first element `< threshold`.

**Optimization**: preprocess — not helpful if each query scans O(n); if many queries on fixed array, sort thresholds with offline queries or segment tree.

**Interview talking points**

- Ask: "First negative" means `< 0` or `< threshold`?"
- State O(n · q) brute force; mention prefix precompute if definition is first index where `arr[i] < 0`.

#### Further reading

- [LeetCode 1351: Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/) — negative search
- [GeeksforGeeks: First negative element](https://www.geeksforgeeks.org/find-first-negative-number-in-array/) — linear scan

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// For each threshold t, first arr[i] < t (or < 0 if t unused)
function firstBelowThreshold(arr, thresholds) {
  return thresholds.map(t => {
    for (const x of arr) {
      if (x < t) return x;
    }
    return null; // none
  });
}

// First negative in array (same answer for every threshold)
function firstNegative(arr) {
  for (const x of arr) if (x < 0) return x;
  return null;
}
```

#### Code walkthrough

- Per threshold linear scan until condition met.
- Clarify problem variant in interview before coding.

#### Complexity

| | |
|-|-|
| Time | O(q · n) for q thresholds |
| Space | O(1) extra |

#### Edge cases

- **No matching element** — print sentinel or "NA".
- **All positive** — no output per query.

</details>
</article>

<article>

What happens when you type google.com and press enter in your search bar

<details><summary>Theory and explanation</summary>

Classic **systems / networking** question tracing the full request path.

**High-level stages**

1. **URL parsing** — browser identifies protocol (HTTPS), host (`google.com`), path.
2. **DNS resolution** — cache check (browser → OS → resolver); recursive query (root → TLD → authoritative) → IP address.
3. **TCP connection** — SYN/SYN-ACK/ACK to server IP:443; possibly **TLS handshake** (ClientHello, cert, key exchange).
4. **HTTP request** — encrypted GET / with headers (Host, User-Agent, cookies).
5. **Server processing** — load balancers, application servers, possibly CDN edge.
6. **HTTP response** — status, headers, HTML body.
7. **Browser rendering** — HTML parse → DOM; CSS → CSSOM; JS download/execute; layout, paint, composite; subresource fetches.

**Interview talking points**

- Mention **caching** at every layer (DNS, CDN, browser cache).
- **HTTPS** adds TLS before HTTP.
- Optional depth: HSTS, HTTP/2 multiplexing, QUIC/HTTP/3.

#### Further reading

- [What Happens When (alex/github)](https://github.com/alex/what-happens-when) — exhaustive community answer
- [MDN: How the Web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works) — approachable overview
- [Cloudflare: How DNS works](https://www.cloudflare.com/learning/dns/what-is-dns/) — DNS primer
- [TLS 1.3 RFC 8446](https://datatracker.ietf.org/doc/html/rfc8446) — handshake details

</details>

<details><summary>Solution (JavaScript)</summary>

N/A — conceptual systems question. Use the theory tab as your interview script; no code required unless asked to sketch DNS cache API:

```js
// Illustrative: browser would not implement DNS this way — for discussion only
async function resolveHost(hostname) {
  // 1. cache lookup  2. DoH / system resolver  3. return A/AAAA records
  return fetch(`https://cloudflare-dns.com/dns-query?name=${hostname}&type=A`);
}
```

#### Complexity

N/A (conceptual)

#### Edge cases

- **Offline / captive portal** — error page instead of Google.
- **Typo domain** — NXDOMAIN or typo-squat.
- **Cached 301** — may skip some steps.

</details>
</article>

<article>

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

[**💻 Submit Code**](https://leetcode.com/problems/valid-parentheses/)

<details><summary>Theory and explanation</summary>

**Valid parentheses** — every closing bracket matches the most recent unmatched opener in LIFO order → use a **stack**.

**Algorithm**

1. Push opening brackets.
2. On closing: if stack empty or top mismatch → false.
3. End: stack must be empty.

**Pair map**: `')' → '('`, `'}' → '{'`, `']' → '['`.

#### Further reading

- [LeetCode 20: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) — problem
- [GeeksforGeeks: Stack](https://www.geeksforgeeks.org/stack-data-structure/) — LIFO structure
- [CP-Algorithms: Stack](https://cp-algorithms.com/data_structures/stack_queue.html) — implementation

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function isValid(s) {
  const pairs = { ')': '(', '}': '{', ']': '[' };
  const stack = [];
  for (const ch of s) {
    if (ch === '(' || ch === '{' || ch === '[') stack.push(ch);
    else if (stack.pop() !== pairs[ch]) return false;
  }
  return stack.length === 0;
}
```

#### Code walkthrough

1. Openers push onto stack.
2. Closers pop and compare to expected opener.
3. Empty stack at wrong time → invalid.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(n) worst-case stack |

#### Edge cases

- **Empty string** — valid.
- **Single opener** — invalid.
- **Wrong nesting** `([)]` — invalid.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
bool isValid(string s) {
    stack<char> st;
    for(auto c:s){
        if( c == '(' or c == '[' or c == '{' ) {
            st.push(c);
            continue;
        }
        if( !st.size() ) return false;
        if( c == ')' ) {
            if(  st.top() != '(' ) return false;
        }else if(  c == '}' ) {
            if( st.top() != '{' ) return false;
        } else if( c == ']' ) {
            if( st.top() != '[' ) return false;
        }
        st.pop();
    }
    return st.size() == 0;
}
```

</details>
</article>

<article>

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police

[**💻 Submit Code**](https://leetcode.com/problems/house-robber/)

<details><summary>Theory and explanation</summary>

**House Robber** — classic 1D DP: at each house, either rob it (plus best up to i−2) or skip (best up to i−1).

**Recurrence**

`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`

**Space optimization**: track `prev` and `curr` instead of full array.

**Interview talking points**

- Cannot rob adjacent → greedy fails (counterexample `[2,1,2]`).
- Extension: circular street (LeetCode 213), tree (337).

#### Further reading

- [LeetCode 198: House Robber](https://leetcode.com/problems/house-robber/) — base problem
- [LeetCode 213: House Robber II](https://leetcode.com/problems/house-robber-ii/) — circular
- [GeeksforGeeks: Maximum sum with no two adjacent](https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/) — same recurrence

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function rob(nums) {
  let prev2 = 0, prev1 = 0;
  for (const x of nums) {
    const cur = Math.max(prev1, prev2 + x);
    prev2 = prev1;
    prev1 = cur;
  }
  return prev1;
}
```

#### Code walkthrough

1. `prev2` = max loot excluding previous house; `prev1` = max including up to previous.
2. Each step chooses rob current + prev2 or skip (prev1).

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases

- **Empty** — 0.
- **Single house** — that house's value.
- **All zeros** — 0.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
int rob(vector<int>& nums) {
    int n = nums.size();
    int dp[n+1][2];
    memset(dp, 0, sizeof(dp));
    for(int i=1;i<=n;i++){
        // we dont rob the ith house
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]);
        // we rob the ith house
        dp[i][1] = dp[i-1][0] + nums[i-1];
    }
    return max(dp[n][0],dp[n][1]);
}
```

</details>
</article>

<article>

Input given is an int array, which may or may not contain positive, negative or zero values. Write a program to find out the two numbers which gives the highest product. 

<details><summary>Theory and explanation</summary>

**Maximum product of two numbers** in an array:

- If all non-positive, answer is product of two **largest** (least negative) values.
- Otherwise answer is max of:
  - two largest positives, OR
  - two smallest negatives (product positive and large).

**Algorithm**: track two smallest and two largest in one pass, or sort and compare top2 and bottom2.

**Three-number product** variant is different — clarify pair vs triplet.

#### Further reading

- [GeeksforGeeks: Pair with maximum product](https://www.geeksforgeeks.org/return-a-pair-with-maximum-product-in-array-of-integers/) — original reference
- [LeetCode 628: Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/) — three-element variant

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function maxProductPair(nums) {
  if (nums.length < 2) return null;
  let min1 = Infinity, min2 = Infinity;
  let max1 = -Infinity, max2 = -Infinity;
  for (const x of nums) {
    if (x <= min1) { min2 = min1; min1 = x; }
    else if (x < min2) min2 = x;
    if (x >= max1) { max2 = max1; max1 = x; }
    else if (x > max2) max2 = x;
  }
  return Math.max(max1 * max2, min1 * min2);
}
```

#### Code walkthrough

1. Track two minima and two maxima in single pass.
2. Compare product of top two vs bottom two negatives.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases

- **Two elements** — their product.
- **Zeros** — may dominate if all non-positive.

</details>
</article>

<article>

Given an array having 0 to n-1 unsorted. Return a new array having their indices 

<details><summary>Theory and explanation</summary>

Given values `0 … n−1` in unsorted order, return **index array** where `result[v] = index of v in original array` (inverse permutation).

**Algorithm**

- Create `ans` of size `n`.
- For each index `i`, set `ans[arr[i]] = i`.

Also called **finding permutation inverse** or **pos array**.

#### Further reading

- [GeeksforGeeks: Find index of element](https://www.geeksforgeeks.org/searching-array/) — linear search baseline
- [LeetCode 448: Find All Numbers Disappeared](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) — index marking tricks

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function valueToIndex(arr) {
  const n = arr.length;
  const pos = Array(n);
  arr.forEach((v, i) => { pos[v] = i; });
  return pos;
}

// If output means "rank" order: sort indices by arr[i]
function sortIndicesByValue(arr) {
  return arr.map((_, i) => i).sort((a, b) => arr[a] - arr[b]);
}
```

#### Code walkthrough

- Direct inverse: value at each position maps back to its index.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(n) |

#### Edge cases

- **Not a permutation** — validate values in `0..n-1` unique.

</details>
</article>

<article>

Given two strings, find the number of times the second string occurs in the first string, whether continuous or discontinuous. 

<details><summary>Theory and explanation</summary>

Count **subsequences** (not necessarily contiguous) of `text` equal to `pattern` — classic **DP** / recursive matching.

**Recurrence**

`dp[i][j]` = ways to match `pattern[0..j)` in `text[0..i)`.

If `text[i-1] === pattern[j-1]`: `dp[i][j] = dp[i-1][j-1] + dp[i-1][j]` (use char or skip).

Else: `dp[i][j] = dp[i-1][j]`.

Answer: `dp[n][m]`.

**Interview talking points**

- Distinct from substring count (contiguous) — KMP for contiguous.
- Related to LeetCode **Distinct Subsequences**.

#### Further reading

- [GeeksforGeeks: Count subsequences](https://www.geeksforgeeks.org/find-number-times-string-occurs-given-string/) — original link
- [LeetCode 115: Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) — same problem
- [CP-Algorithms: DP on strings](https://cp-algorithms.com/sequences/longest_increasing_subsequence.html) — DP patterns

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function countSubseq(text, pattern) {
  const n = text.length, m = pattern.length;
  const dp = Array.from({ length: n + 1 }, () => Array(m + 1).fill(0));
  for (let i = 0; i <= n; i++) dp[i][0] = 1;
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= m; j++) {
      dp[i][j] = dp[i - 1][j];
      if (text[i - 1] === pattern[j - 1])
        dp[i][j] += dp[i - 1][j - 1];
    }
  }
  return dp[n][m];
}
```

#### Code walkthrough

1. Empty pattern matched in one way everywhere.
2. Match char: add ways with previous char matched.
3. Always carry ways that skip current text char.

#### Complexity

| | |
|-|-|
| Time | O(n · m) |
| Space | O(n · m) — can roll to O(m) |

#### Edge cases

- **Empty pattern** — 1 way.
- **pattern longer than text** — 0.

</details>
</article>

<article>

Given an array of positive integers. We need to make the given array a ‘Palindrome’. The only allowed operation is”merging” (of two adjacent elements). Merging two adjacent elements means replacing them with their sum. The task is to find the array of maximum length with the minimum number of merge operations required to make the given array a ‘Palindrome’. 

<details><summary>Theory and explanation</summary>

**Minimum adjacent merges to palindrome** — compare from both ends; if `arr[l] !== arr[r]`, merge smaller side inward (greedy on sums):

- If `arr[l] < arr[r]`: merge `arr[l]` with `arr[l+1]`, increment ops.
- Else merge from right.

When equal, shrink both pointers.

Goal: minimum merges so merged sequence reads palindrome — related to **minimum insertions to form palindrome** on multiset of merge sums.

#### Further reading

- [GeeksforGeeks: Minimum merges for palindrome array](https://www.geeksforgeeks.org/find-minimum-number-of-merge-operations-to-make-an-array-palindrome/) — original reference
- [LeetCode 131: Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) — palindrome structure
- [LeetCode 516: Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) — related DP

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function minMergesToPalindrome(arr) {
  const a = [...arr];
  let l = 0, r = a.length - 1, ops = 0;
  while (l < r) {
    if (a[l] === a[r]) { l++; r--; continue; }
    if (a[l] < a[r]) {
      a[l + 1] += a[l];
      l++;
    } else {
      a[r - 1] += a[r];
      r--;
    }
    ops++;
  }
  return ops;
}
```

#### Code walkthrough

1. Two pointers at ends of working array.
2. Equal values — move inward without merge.
3. Unequal — merge smaller endpoint with neighbor; count operation.

#### Complexity

| | |
|-|-|
| Time | O(n) merges each may shift — worst O(n²) with array copies; deque improves |
| Space | O(n) |

#### Edge cases

- **Already palindrome** — 0 merges.
- **Single element** — 0.

</details>
</article>


<article>
    Given a lowercase string <i>s</i>, find the length <i>L</i> of the
    longest prefix <i>p</i> such that the entire string is exactly
    <i>p</i> repeated <i>k</i> times for some integer <i>k ≥ 2</i>.
    If no such prefix exists, return <i>-1</i>. <br>
	For string: "ababab", L = 2; for "aaaaaa", L = 3; for "abcd", L = -1.

<details><summary>Theory and explanation</summary>

Find longest prefix `p` such that `s = p^k` for **k ≥ 2** (string equals `k` repeats of prefix).

**Approaches**

1. **Brute force** — try prefix lengths `L` from `⌊n/2⌋` down to `1`; check if `n % L === 0` and each block equals `s[0..L)`. **O(n²)** worst case.
2. **KMP LPS** — let `len = lps[n-1]`; period `d = n - len`; if `n % d === 0` and `d < n`, answer relates to smallest period; adjust for **longest** prefix with k≥2 per problem's return format (may return `L` not `d`).

For `"ababab"`, smallest period length 2, `k=3`; longest valid prefix length for k≥2 is 2.

**Interview talking points**

- Distinguish **longest** vs **shortest** period.
- KMP failure function encodes border structure.

#### Further reading

- [CP-Algorithms: Prefix function (KMP)](https://cp-algorithms.com/string/prefix-function.html) — LPS array
- [LeetCode 459: Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) — period detection
- [GeeksforGeeks: String periodicity](https://www.geeksforgeeks.org/find-if-a-string-is-a-repeated-pattern/) — KMP approach

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function longestRepeatedPrefix(s) {
  const n = s.length;
  for (let L = Math.floor(n / 2); L >= 1; L--) {
    if (n % L !== 0) continue;
    const k = n / L;
    if (k < 2) continue;
    let ok = true;
    for (let i = L; i < n; i++) {
      if (s[i] !== s[i % L]) { ok = false; break; }
    }
    if (ok) return L;
  }
  return -1;
}

function buildLps(s) {
  const lps = Array(s.length).fill(0);
  for (let i = 1, len = 0; i < s.length; ) {
    if (s[i] === s[len]) lps[i++] = ++len;
    else if (len) len = lps[len - 1];
    else lps[i++] = 0;
  }
  return lps;
}

function longestRepeatedPrefixKmp(s) {
  const n = s.length;
  const lps = buildLps(s);
  const d = n - lps[n - 1];
  if (d !== n && n % d === 0) {
    const k = n / d;
    if (k >= 2) return d; // smallest period = longest prefix for repetition
  }
  return -1;
}
```

#### Code walkthrough

1. **BF** — try L from half length downward; verify k copies.
2. **KMP** — smallest period `d`; valid if `n % d === 0` and k≥2.

#### Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute force | O(n²) | O(1) |
| KMP | O(n) | O(n) |

#### Edge cases

- **No repeat** — `-1`.
- **All same char** `"aaaaaa"` — L = 3 (k=2) or smallest period 1 depending on definition; problem says L=3.

</details>

<details><summary>Solution (other languages)</summary>

**Brute force — O(n²)**

```
n = |s|.
For L from n/2 down to 1:
    If (n mod L ≠ 0) skip L.
    Check if s[0..L-1] is repeated n/L times.
    If yes, return L.
return -1
```

**KMP — O(n)**

```cpp
// Use KMP LPS array.
int n = s.length();
computeLsa(s);
int d = n - lsa[n - 1];
if (n % d != 0 || d == n) return -1;
else {
    int ans = floor(n / (2 * d)) * d;
    if(n % ans != 0) return -1;
    else return ans;
}
```

</details>
</article>

