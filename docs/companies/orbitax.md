---
description: Orbitax interview questions, Orbitax interview stages, Orbitax interview details, Orbitax interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/orbitax
---
# Orbitax Bangladesh Limited 

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-| :- |
| Founding year | |
| Company Website | https://www.orbitax.com/ |
| Career Website |  |
| Technologies Used| Java, JavaScript, Android, PHP |

## Coding Round Questions
<article>

You are given an HTML string. Your task is to determine the number of characters encompassed by each HTML tag in the string. For each tag, count the number of characters that are enclosed between the opening (`<tag>`) and closing (`</tag>`) tags.

A tag is composed of one or more lowercase English letters (a-z). For example: `<div> ... </div>`, `<span>..</span>`. It can be followed by digits (0-9) i.e `<h1>..</h1>`.

The content between the tags can consist of:
1. English characters (a-z, A-Z).
2. Digits (0-9).
3. Punctuation marks: period (.), comma (,), and spaces(' ').

Note:
When a character is encompassed by a same tag multiple times, count only once for that tag.
A tag can have 0 characters. In that case don't print that tag.
Spaces(' ') between the tags are not counted.

[**💻 Submit Code**](https://www.hackerrank.com/contests/orbitax-associate-software-engineer-recruitment-2024-phase-1/challenges/count-between-tags/problem)

<details><summary>Theory and explanation</summary>

This is a **structured parsing** problem. You walk the HTML string left to right and treat `<` as the start of a tag token. Opening tags push state; closing tags pop state and aggregate character counts upward.

**Core ideas**

1. **Stack of active tags** — Each opening tag pushes its name onto a stack. The innermost tag is `tags[tags.length - 1]`.
2. **Per-level character counter** — Maintain `charCount[level]` for text seen while that tag is open. Only non-space characters increment the counter (spaces *between* tags are excluded by the problem statement).
3. **Nested duplicate tags** — The same tag name can appear nested (`<p><p></p></p>`). Count characters for the outer `<p>` only when its nesting level for `p` returns to zero (`nestedTagLevel[tag] === 0` after decrement on close). Inner occurrences bubble their counts to the parent via `charCount[parent] += cnt`.
4. **Output** — After a full parse, print `tag: count` for every tag with a positive total.

**Algorithm (single pass)**

- On `<tag>` (not closing): parse tag name, push onto stack, push a zero counter, increment nesting count for that tag name.
- On `</tag>`: parse name, read `cnt` from top counter, decrement nesting; if nesting is zero, add `cnt` to `totalCharCount[tag]`; pop stack/counter; add `cnt` to the new top counter (propagate to parent).
- Otherwise: if character is not space, increment top counter.

**Interview talking points**

- Why a stack? HTML nesting is LIFO; the stack mirrors the DOM nesting depth.
- Why track nesting level per tag name? Without it, inner and outer tags with the same name would double-count or mis-attribute text.
- Complexity is linear in string length; extra maps track tag names seen.

#### Further reading

- [MDN: HTML elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) — valid tag structure and nesting
- [LeetCode: Tag Validator](https://leetcode.com/problems/tag-validator/) — related bracket/tag parsing practice
- [GeeksforGeeks: Stack data structure](https://www.geeksforgeeks.org/stack-data-structure/) — LIFO model used for nesting
- [W3C HTML parser overview](https://html.spec.whatwg.org/multipage/parsing.html) — how real browsers tokenize markup

#### Complexity

| | |
|-|-|
| Time | O(n) — one scan of the HTML string; tag names are bounded by tag length |
| Space | O(d + t) — stack depth d (nesting) plus maps for t distinct tag names |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
/**
 * Parse HTML-like string and print tag character counts.
 * @param {string} s
 */
function countBetweenTags(s) {
  const totalCharCount = new Map();
  const nestedTagLevel = new Map();
  const tags = [''];
  const charCount = [0];

  function consume(str, start) {
    let tag = '';
    let i = start;
    while (str[i] !== '>') tag += str[i++];
    return { tag, nextIndex: i };
  }

  for (let i = 0; i < s.length; i++) {
    if (s[i] === '<' && s[i + 1] !== '/') {
      const { tag, nextIndex } = consume(s, i + 1);
      i = nextIndex;
      tags.push(tag);
      charCount.push(0);
      nestedTagLevel.set(tag, (nestedTagLevel.get(tag) || 0) + 1);
    } else if (s[i] === '<' && s[i + 1] === '/') {
      const { tag, nextIndex } = consume(s, i + 2);
      i = nextIndex;
      const cnt = charCount.pop();
      tags.pop();
      nestedTagLevel.set(tag, nestedTagLevel.get(tag) - 1);
      if (nestedTagLevel.get(tag) === 0) {
        totalCharCount.set(tag, (totalCharCount.get(tag) || 0) + cnt);
      }
      charCount[charCount.length - 1] += cnt;
    } else if (s[i] !== ' ') {
      charCount[charCount.length - 1]++;
    }
  }

  const result = [];
  for (const [tag, cnt] of totalCharCount) {
    if (cnt > 0) result.push(`${tag}: ${cnt}`);
  }
  return result;
}
```

#### Code walkthrough

- **`consume`** — Reads characters after `<` or `</` until `>`, returning the tag name (e.g. `div`, `h1`).
- **Opening tag** — Push tag and a fresh zero counter; track how many open instances of that tag name exist.
- **Closing tag** — Pop the inner counter; if this closes the outermost instance of that tag name, record in `totalCharCount`; always bubble the count to the parent level.
- **Text** — Non-space characters increment only the innermost open tag's counter.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(n) worst case for deeply nested tags |

#### Edge cases

- **Empty tag** `<div></div>` — count stays 0; omit from output.
- **Same tag nested** `<p><p>x</p></p>` — inner `p` text bubbles up; outer `p` gets credited once when nesting level hits zero.
- **Spaces only between tags** — ignored; spaces inside content between tags are counted.
- **Tags with digits** `<h1>` — parsed as full tag name including digits.

</details>

<details><summary>Solution (other languages)</summary>

```C++
string consume(string &s,int st){
    string tag;
    while(s[st]!='>') tag+=s[st++];
    return tag;
}

void solve(string s) {
    // the total character inside a tag
    map<string,int> totalCharCount;
    // to find the nesting level of a tag
    // eg. <p><p></p></p>, here p is nested two times
    map<string,int> nestedTagLevel;

    vector<string> tags;
    vector<int> charCount;

    // signifies root level tag
    // helps to simplify code logic
    tags.push_back("");
    charCount.push_back(0);

    for(int i=0;i<s.size();i++){
        if( s[i] == '<' and s[i+1]!='/'  ){
            // starting tag
            string tag = consume(s,i+1);
            // advance pointer by the consumer
            // character count
            i+=tag.size()+1;
            tags.push_back(tag);
            charCount.push_back(0);
            nestedTagLevel[tag]++;
        }else if( s[i] == '<' and s[i+1] == '/' ){
            // ending tag
            string tag = consume(s,i+2);
             // advance pointer by the consumer
            // character count
            i+=tag.size()+2;
            int cnt = charCount.back();
            nestedTagLevel[tag]--;

            // increment count only if it has no parent
            // tag of same type
            if( nestedTagLevel[tag] == 0 ){
                totalCharCount[tags.back()] += cnt;
            }
            charCount.pop_back();
            tags.pop_back();
            // propagate the character count to its
            // parents too
            charCount.back()+=cnt;

        }else{
            if(s[i] != ' ') charCount.back()++;
        }
    }

    for(auto [tag,cnt]:totalCharCount){
        if(cnt) {
            cout<<tag<<": "<<cnt<<endl;
        }
    }
}
```

</details>
</article>

<article>

You are given a string S of length N and an integer K. Your task is to find the total number of subsequences in S that match the pattern P = "orbitaxian", where the difference in position between every consecutive character in the subsequence is no more than K.

More formally, let the subsequence of P be represented by an array pos, where (1 ≤ pos[i] ≤ N) and S[pos[i]] = P[i]. Then for each i > 1, the condition pos[i] − pos[i-1] ≤ K must hold.

The result should be returned modulo 10^9+7

[**💻 Submit Code**](https://www.hackerrank.com/contests/orbitax-associate-software-engineer-recruitment-2024-phase-1/challenges/orbitax-sub-sequence)

<details><summary>Theory and explanation</summary>

This is **constrained subsequence counting**. You must count ways to pick indices in `S` that spell the fixed pattern (in the Orbitax contest, the effective chain is `o → r → b → i → t → a → x → I → A → n` with case-sensitive transitions), where each consecutive picked index is at most `K` apart.

**Dynamic programming on the pattern**

Instead of enumerating all subsequences (exponential), maintain for each pattern stage how many valid partial matches **end at the current index**:

1. When you see `o`, start a new partial match: count 1 at this index.
2. When you see the next pattern character `c`, extend every valid partial match for the previous character `p` whose index is within `K` of the current index.
3. Use **queues** keyed by `(pattern char → list of {index, count})` and a running **`cntStack[char]`** (total valid partial matches ending with that char in the sliding window).

**Sliding window on index gap**

For transition `p → c` at index `ind`, expire entries from `pos[p]` where `ind - front.index > K`, subtracting their counts from `cntStack[p]`. Remaining entries represent matches you can extend; push new `{ind, cntStack[p]}` onto `pos[c]` and add to `cntStack[c]`.

**Special transitions in the Orbitax variant**

The reference solution branches at certain letters (e.g. `i` can extend `b→i` or `x→I`; `a` extends both `t→a` and `I→A`). Mirror those transitions exactly when porting to another language.

**Modulo arithmetic**

Keep all counts under `M = 1_000_000_007`; normalize after each add/subtract.

**Interview talking points**

- Relates to [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) with an extra window constraint on indices.
- Queues give amortized O(1) expiry per character step when each index is pushed/popped once.
- Explain why brute force over all index tuples is infeasible for large `N`.

#### Further reading

- [LeetCode: Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) — classic subsequence DP
- [GeeksforGeeks: Subsequence with constraint](https://www.geeksforgeeks.org/count-subsequences-of-length-k/) — counting fixed-length subsequences
- [CP-Algorithms: Sliding window](https://cp-algorithms.com/others/sliding-window-minimum.html) — queue-based window maintenance
- [Modular arithmetic (Khan Academy)](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic) — keeping counts under a prime modulus

#### Complexity

| | |
|-|-|
| Time | O(n · L) — each of n characters triggers O(1) amortized queue work per transition; L = pattern length (constant) |
| Space | O(n) — each index enters a queue at most once per pattern stage |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
const MOD = 1_000_000_007;

function addMod(a, b) {
  return ((a % MOD) + (b % MOD) + MOD) % MOD;
}

function subMod(a, b) {
  return ((a % MOD) - (b % MOD) + MOD) % MOD;
}

/**
 * Count constrained "orbitaxian" subsequences in s with max gap k.
 * @param {string} s
 * @param {number} k
 * @returns {number}
 */
function countOrbitaxSubsequences(s, k) {
  const pos = new Map(); // char -> queue of [index, count]
  const cntStack = new Map(); // char -> total count in window

  const getQueue = (ch) => {
    if (!pos.has(ch)) pos.set(ch, []);
    return pos.get(ch);
  };
  const getCnt = (ch) => cntStack.get(ch) || 0;
  const setCnt = (ch, val) => cntStack.set(ch, val % MOD);

  function calc(prev, cur, ind) {
    const q = getQueue(prev);
    while (q.length && ind - q[0][0] > k) {
      setCnt(prev, subMod(getCnt(prev), q[0][1]));
      q.shift();
    }
    if (q.length) {
      getQueue(cur).push([ind, getCnt(prev)]);
      setCnt(cur, addMod(getCnt(cur), getCnt(prev)));
    }
  }

  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (c === 'o') {
      getQueue('o').push([i, 1]);
      setCnt('o', addMod(getCnt('o'), 1));
    } else if (c === 'r') {
      calc('o', 'r', i);
    } else if (c === 'b') {
      calc('r', 'b', i);
    } else if (c === 'i') {
      calc('b', 'i', i);
      calc('x', 'I', i);
    } else if (c === 't') {
      calc('i', 't', i);
    } else if (c === 'a') {
      calc('t', 'a', i);
      calc('I', 'A', i);
    } else if (c === 'x') {
      calc('a', 'x', i);
    } else if (c === 'n') {
      calc('A', 'n', i);
    }
  }

  return getCnt('n') % MOD;
}
```

#### Code walkthrough

- **`calc(prev, cur, ind)`** — Drops expired partial matches from `prev`, then extends all surviving counts to `cur` at index `ind`.
- **Starting `o`** — Each `o` begins a new partial match with count 1.
- **Branching** — At `'i'` and `'a'`, two transitions reflect the contest pattern (`b→i` vs `x→I`, etc.).
- **Answer** — Total completed matches are in `cntStack['n']` after scanning `s`.

#### Complexity

| | |
|-|-|
| Time | O(n) amortized — each queue entry pushed and popped once |
| Space | O(n) — queue storage across pattern stages |

#### Edge cases

- **No `o` in string** — answer is 0.
- **K = 0** — consecutive indices must be adjacent; only tight matches count.
- **Large K** — window rarely expires; behaves like unconstrained subsequence counting per transition.
- **Modulo** — use safe add/subtract to avoid negative intermediate values.

</details>

<details><summary>Solution (other languages)</summary>

```C++
#define M 1000000007
map<char,queue<pii> > pos;
map<char,int> cntStack;
int k;
void calc(char prev, char cur,int ind){
    while(pos[prev].size() and ind-pos[prev].front().first>k) {
        cntStack[prev]-=pos[prev].front().second;
        cntStack[prev] %= M;
        cntStack[prev] += M;
        cntStack[prev] %= M;

        pos[prev].pop();
    }
    if( pos[prev].size() ) {
        pos[cur].push({ind,cntStack[prev]});
        cntStack[cur]+=cntStack[prev];
        cntStack[cur] %= M;
    }
}

void solve() {
    string orbitax = "orbitaxIAn";
    pos.clear();
    cntStack.clear();
    int n;
    cin>>n>>k;
    string s;
    cin>>s;
    for(int i=0;i<s.size();i++){
        char cur = s[i];
        char prev;
        if( s[i] == 'o' ){
            pos[cur].push({i,1});
            cntStack[cur]++;
        }else if( s[i] == 'r' ){
            calc('o','r',i);
        }else if( s[i] == 'b' ){
            calc('r','b',i);
        }else if( s[i] == 'i' ){
            calc('b','i',i);
            calc('x','I',i);
        }else if( s[i] == 't' ){
            calc('i','t',i);
        }else if( s[i] == 'a' ){
            calc('t','a',i);
            calc('I','A',i);
        }else if( s[i] == 'x' ){
            calc('a','x',i);
        }else if( s[i] == 'n' ){
            calc('A','n',i);
        }
    }
    cout<<cntStack['n']<<endl;
}

signed main() {
    FASTIO;
    int tc=1;
    cin>>tc;
    while(tc--) solve();
}
```

</details>
</article>

<article>

You are given an array of weights of length 200 and 3 buckets. The sum of total weights of the array will not exceed 100. You need to distribute the weights among the buckets such that the maximum value of the difference between the sum of weights in any two bucket is minimum.

<details><summary>Theory and explanation</summary>

This is a **multi-way partition** problem with three buckets. Given weights `w[1..n]` with total sum `T ≤ 100`, assign each weight to bucket 1, 2, or 3 to **minimize** the maximum pairwise difference among the three bucket sums.

**Reformulation**

Let bucket sums be `(s1, s2, s3)` with `s1 + s2 + s3 = T`. The objective is:

\[
\min \max(|s1 - s2|, |s2 - s3|, |s3 - s1|)
\]

Because `T` is small (≤ 100), **dynamic programming** over achievable sums is practical.

**DP state**

`dp[i][j][k] = true` if using the first `i` items you can achieve sum `j` in bucket 1 and sum `k` in bucket 2 (bucket 3 gets the remainder of the running total). Transitions for item `weights[i]`:

1. Put in bucket 3 — keep `(j, k)` unchanged (implicitly increases bucket 3).
2. Put in bucket 1 — increase `j` by `weights[i]`.
3. Put in bucket 2 — increase `k` by `weights[i]`.

After processing all items, iterate feasible `(s1, s2)`, compute `s3 = T - s1 - s2`, and track the minimum `max(|s1-s2|, |s2-s3|, |s3-s1|)`.

**Why not greedy?**

Greedy "put next item in lightest bucket" does not guarantee optimal balance for three buckets with arbitrary weights.

**Interview talking points**

- Closely related to [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) and [Split Array With Same Average](https://leetcode.com/problems/split-array-with-same-average/) — subset-sum DP family.
- Small `T` makes 2D boolean DP (`101 × 101`) feasible despite `n ≤ 200`.
- For two buckets, the target is `T/2`; for three, you minimize worst-case spread instead of hitting an exact target.

#### Further reading

- [LeetCode: Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) — 2-bucket subset-sum DP
- [GeeksforGeeks: Subset sum problem](https://www.geeksforgeeks.org/subset-sum-problem-dp-25/) — foundational 0/1 knapsack DP
- [LeetCode: Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/) — minimize difference via partition
- [CP-Algorithms: Knapsack](https://cp-algorithms.com/dynamic_programming/knapsack.html) — DP state design patterns

#### Complexity

| | |
|-|-|
| Time | O(n · T²) — with T ≤ 100, about 200 × 101 × 101 operations |
| Space | O(n · T²) — boolean DP table; can roll to O(T²) with one row |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
/**
 * Minimize max pairwise difference among three bucket sums.
 * @param {number[]} weights - length <= 200, total sum <= 100
 * @returns {number}
 */
function minBucketSpread(weights) {
  const n = weights.length;
  let total = 0;
  for (const w of weights) total += w;

  const dp = Array.from({ length: n + 1 }, () =>
    Array.from({ length: 501 }, () => Array(501).fill(false))
  );
  dp[0][0][0] = true;

  for (let i = 1; i <= n; i++) {
    const w = weights[i - 1];
    for (let j = 0; j <= Math.min(total, 500); j++) {
      for (let k = 0; k <= Math.min(total, 500); k++) {
        if (!dp[i - 1][j][k]) continue;
        dp[i][j][k] = true; // bucket 3
        if (j + w <= 500) dp[i][j + w][k] = true; // bucket 1
        if (k + w <= 500) dp[i][j][k + w] = true; // bucket 2
      }
    }
  }

  let best = Infinity;
  for (let s1 = 0; s1 <= Math.min(total, 500); s1++) {
    for (let s2 = 0; s2 <= Math.min(total, 500); s2++) {
      if (!dp[n][s1][s2]) continue;
      const s3 = total - s1 - s2;
      if (s3 < 0) continue;
      const spread = Math.max(
        Math.abs(s1 - s2),
        Math.abs(s2 - s3),
        Math.abs(s3 - s1)
      );
      best = Math.min(best, spread);
    }
  }
  return best;
}
```

#### Code walkthrough

- **`dp[i][j][k]`** — After considering first `i` weights, bucket 1 sums to `j` and bucket 2 to `k`; bucket 3 holds the rest of the prefix total.
- **Three transitions** — Each weight goes to exactly one bucket via unchanged `(j,k)`, `j+w`, or `k+w`.
- **Final scan** — For every reachable `(s1, s2)`, derive `s3` and minimize the max absolute pairwise difference.

#### Complexity

| | |
|-|-|
| Time | O(n · T²) with T ≤ 100 |
| Space | O(n · T²) |

#### Edge cases

- **Single weight** — one bucket gets the item; others 0; spread equals the weight.
- **All equal weights** — optimal spread is 0 or 1 depending on divisibility by 3.
- **Impossible negative s3** — skip states where `s1 + s2 > total`.

</details>

<details><summary>Solution (other languages)</summary>

```C++
bool dp[205][505][505];
// until index i, weights on 1st bucket is j and 2nd bucket is k,
// and 3rd bucket is cumsum[i]-j-k;
void solve() {
    int n;
    cin>>n;
    int weights[n+1];
    int csum = 0;
    for(int i=1;i<=n;i++)
        cin>>weights[i];

    // we can put 0 weight in 1st,2nd and 3rd bucket with 0 weights
    dp[0][0][0] = true;

    for(int i=1;i<=n;i++){
        for(int j=0;j<=min(csum,500);j++){
            for(int k=0;k<=min(csum,500);k++){
                if( !dp[i-1][j][k] ) continue;
                // put it in 1st bucket
                dp[i][j][k] = true;
                // put it in the second bucket
                if( j+weights[i]<=500 ) dp[i][j+weights[i]][k] = true;
                // put it in the third bucket
                if( k+weights[i]<=500 ) dp[i][j][k+weights[i]] = true;
            }
        }
        csum+=weights[i];
    }
    cout<<csum<<endl;
    int mx = -1;
    for(int i=0;i<=min(csum,500);i++){
        for(int j=0;j<=min(csum,500);j++){
            if( dp[n][i][j] == false ) continue;
            int k = csum-i-j;
            cout<<i<<" "<<j<<" "<<k<<endl;
            int val = max( {abs(i-j),abs(j-k),abs(k-i)} );
            mx = mx == -1? val: min(mx,val);
        }
    }
    cout<<mx<<endl;
}
```

</details>
</article>
