---
description: AppifyLab interview questions, AppifyLab interview stages, AppifyLab coding contest, AppifyLab interview details
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/appifylab
---
# AppifyLab Ltd

|                   |                                            |
| :---------------- | :----------------------------------------- |
| Company Website   | https://www.appifylab.com/                 |
| Career Website    | https://www.appifylab.com/career           |
| Technologies Used | React, Flutter, Vue, Laravel, Nuxt, NodeJS |

## Introduction
Appify lab has a LMS(Learning Management System) product name [EzyCourse](https://ezycourse.com/)

## Interview Stages

### Initial Online Contest
**Platform:** vJudge  
**Details:** Participated in an online coding contest.  
**Selection:** Out of numerous participants, around 40-50 were selected for the onsite contest.  

### Onsite Contest
**Selection:** Out of numerous participants, around 10-15 were selected for the final interview.  
**Details:** The onsite contest was held in Sylhet.   

### Final Interview
The final interview is mainly a discussion about the company and the candidate's interest in joining. Employment terms like probabtion periond, internship time, possibility of permanent position, and location were discussed.

## First Round Questions

The given questions are the summarized version of the original questions. The original questions are available in the  [Online Round Problem Set](https://github.com/TamimEhsan/interview-questions-bangladesh/tree/master/docs/resource/appify/Online_Round.pdf).

<article>

Given multiple test cases, each containing a 3-letter string (uppercase/lowercase letters), you have to check whether the string equals "YES", case-insensitively. Output "YES" if it matches, else "NO".

<details><summary>Theory and explanation</summary>

Straightforward **string normalization** problem — compare input to `"yes"` after lowercasing all characters.

**Steps per test case**

1. Read 3-character string.
2. Convert each char to lowercase (`tolower` / `toLowerCase`).
3. Compare to `"yes"` — output `YES` or `NO`.

**Complexity**

O(1) per test — fixed length 3.

**Contest tips**

- Handle `t` up to large bounds — still O(t).
- No special Unicode — ASCII letters only.

#### Further reading

- [C++ cctype tolower](https://en.cppreference.com/w/cpp/string/byte/tolower) — character case conversion
- [MDN: String.prototype.toLowerCase()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase) — JS equivalent
- [Codeforces A problems pattern](https://codeforces.com/problemset?order=BY_SOLVED_ASC) — warm-up implementation style

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function solveYesNo(lines) {
  const results = [];
  for (let i = 1; i <= Number(lines[0]); i++) {
    const st = lines[i].trim().toLowerCase();
    results.push(st === 'yes' ? 'YES' : 'NO');
  }
  return results;
}

// solveYesNo(['2', 'YES', 'no']); // ['YES', 'NO']
```

#### Code walkthrough

1. First line is test count `t`.
2. Lowercase entire string — 3 chars fixed.
3. Strict equality with `'yes'`.

#### Complexity

| | |
|-|-|
| Time | O(t) |
| Space | O(1) per case |

#### Edge cases

- **Mixed case** — `YeS` → YES.
- **Wrong length** — problem guarantees 3 letters; still fail compare if not `yes`.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
# include<bits/stdc++.h>
using namespace std;

int main() {
    int t; cin >> t; // number of test cases

    while (t--) {
        string st; cin >> st;  // read input string

        // convert input string into lowercase
        for (auto &c: st) {
            c = tolower(c);
        }

        // if input string equals yes, the result is YES, otherwise NO
        (st == "yes") ? cout << "YES\n" : cout << "NO\n";
    }

    return 0;
}
```

</details>
</article>

<article>

Given
- Number of students, games, and connection events
- For each student, the game they like
- A sequence of connections between pairs of students over time

For each game, determine the earliest time when all students who like that game become connected (either directly or indirectly). Output `-1` if they never get connected.

<details><summary>Theory and explanation</summary>

Model as **Union-Find (Disjoint Set Union)** per game with **timestamped merges**.

**Setup**

- Group students by favorite game `g`.
- Process connection events `(u, v, time)` in chronological order.
- After each union, check if DSU component size for `u` equals total students liking game `g(u)` (or track counts per root per game).

**Better approach**

- For each game, list its student IDs.
- Process all edges globally in time order; maintain DSU.
- After processing event at time `t`, for each game check if all its students share one root — first `t` where true is answer.

**Optimization**

- Only games with ≥2 students matter.
- Track `connectedCount[game]` when merging two components containing students of same game.

**Answer**

- Earliest time all students of game `g` in one component, else `-1`.

#### Further reading

- [CP-Algorithms: Disjoint Set Union](https://cp-algorithms.com/data_structures/disjoint_set_union.html) — union by rank, path compression
- [USACO Guide: DSU](https://usaco.guide/CPH/) — connectivity over time
- [GeeksforGeeks: Union-Find](https://www.geeksforgeeks.org/union-find/) — implementation

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class DSU {
  constructor(n) {
    this.p = Array.from({ length: n }, (_, i) => i);
    this.sz = Array(n).fill(1);
  }
  find(x) {
    if (this.p[x] !== x) this.p[x] = this.find(this.p[x]);
    return this.p[x];
  }
  union(a, b) {
    a = this.find(a); b = this.find(b);
    if (a === b) return false;
    if (this.sz[a] < this.sz[b]) [a, b] = [b, a];
    this.p[b] = a;
    this.sz[a] += this.sz[b];
    return true;
  }
}

function earliestGameConnection(n, gameOfStudent, events) {
  const studentsByGame = new Map();
  for (let i = 0; i < n; i++) {
    const g = gameOfStudent[i];
    if (!studentsByGame.has(g)) studentsByGame.set(g, []);
    studentsByGame.get(g).push(i);
  }

  const ans = new Map();
  const dsu = new DSU(n);

  for (const [u, v, t] of events) {
    dsu.union(u, v);
    for (const [game, ids] of studentsByGame) {
      if (ans.has(game) || ids.length < 2) continue;
      const root = dsu.find(ids[0]);
      if (ids.every((id) => dsu.find(id) === root)) {
        ans.set(game, t);
      }
    }
  }

  return [...studentsByGame.keys()].map((g) => ans.get(g) ?? -1);
}
```

#### Code walkthrough

1. Bucket students by liked game.
2. Process timed edges; union in DSU.
3. After each event, test each unsettled game for full connectivity.
4. Record first timestamp or `-1`.

#### Complexity

| | |
|-|-|
| Time | O(E × G × S) naive; optimize with per-game counters to O(E × α(n)) |
| Space | O(n + G) |

#### Edge cases

- **Single student likes game** — connected at time 0 (or `-1` per statement; clarify).
- **No events** — `-1` if >1 student.
- **Duplicate edges** — union no-op.

</details>
</article>

<article>

Given:
- Number of questions
- For each question: initial score, per-minute penalty, minimum score
- For each question: submission time and number of submissions (positive if solved, non-positive if unsolved)

Calculate the total score based on a formula involving penalties and number of attempts. If a question is unsolved, its score is 0.

<details><summary>Theory and explanation</summary>

Classic **ICPC / contest scoring** variant.

**Per question (if solved)**

```
score = max(minScore, initialScore - penalty × minutes - attemptPenalty × (attempts - 1))
```

Exact formula varies — read PDF constants. General pattern:

- **Unsolved** (`submissions <= 0` or no AC) → **0 points**.
- **Solved** → start from `initialScore`, subtract time penalty × minutes from start, subtract wrong submission penalty × wrong tries, floor at `minimumScore`.

**Implementation**

Loop questions, branch on solved flag, accumulate total.

**Interview talking points**

- Clarify whether minutes are from contest start or problem open time.
- Integer vs floating penalties.

#### Further reading

- [ICPC scoring rules](https://icpc.global/regionals/rules) — penalty conventions
- [Codeforces contest FAQ](https://codeforces.com/help) — penalty timing
- [Kattis ICPC scoring](https://open.kattis.com/help) — reference implementation style

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function contestScore(questions) {
  let total = 0;
  for (const q of questions) {
    const { initial, penalty, minScore, timeMin, attempts } = q;
    if (attempts <= 0) continue; // unsolved
    const wrong = Math.max(0, attempts - 1);
    const earned = Math.max(minScore, initial - penalty * timeMin - wrong * penalty);
    total += earned;
  }
  return total;
}

// Example shape
contestScore([
  { initial: 100, penalty: 5, minScore: 20, timeMin: 30, attempts: 2 },
  { initial: 80, penalty: 4, minScore: 0, timeMin: 10, attempts: -1 },
]);
```

#### Code walkthrough

1. Skip unsolved (`attempts <= 0`).
2. Count wrong attempts as `attempts - 1`.
3. Apply penalty formula, clamp to `minScore`.
4. Sum across questions.

#### Complexity

| | |
|-|-|
| Time | O(Q) questions |
| Space | O(1) |

#### Edge cases

- **First-submit AC** — wrong count 0.
- **Score below minimum** — clamp applies.
- **Negative time** — validate input.

</details>
</article>

<article>

Given a list of unique 9-digit phone numbers. For each phone number, find the shortest digit substring that uniquely identifies it (i.e., no other number contains it as a substring).

<details><summary>Theory and explanation</summary>

**Shortest unique substring** among a set of strings (phone numbers fixed length 9).

**Approach 1 — all prefixes by length**

For each number, try substrings of length `L = 1..9` until exactly one number contains that substring (as substring of full number).

**Approach 2 — trie / hash map of substring counts**

- Generate all substrings of all numbers (O(9² × N) = O(81N)).
- Count occurrences globally.
- For each number, pick shortest substring with count === 1.

**Optimization**

Process increasing length; stop at first unique — guarantees minimal length.

**Related**

- Phone autocomplete / contact search in mobile apps (AppifyLab product context).

#### Further reading

- [GeeksforGeeks: Shortest unique substring](https://www.geeksforgeeks.org/) — substring enumeration
- [Trie data structure](https://cp-algorithms.com/string/trie.html) — prefix indexing
- [LeetCode 3076: Shortest Uncommon Substring](https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/) — similar flavor

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function shortestUniqueIds(numbers) {
  const counts = new Map();

  for (const num of numbers) {
    const seen = new Set();
    for (let i = 0; i < num.length; i++) {
      for (let j = i + 1; j <= num.length; j++) {
        const sub = num.slice(i, j);
        if (seen.has(sub)) continue;
        seen.add(sub);
        counts.set(sub, (counts.get(sub) || 0) + 1);
      }
    }
  }

  return numbers.map((num) => {
    for (let len = 1; len <= num.length; len++) {
      for (let i = 0; i + len <= num.length; i++) {
        const sub = num.slice(i, i + len);
        if (counts.get(sub) === 1) return sub;
      }
    }
    return num; // fallback: whole number is unique in set
  });
}
```

#### Code walkthrough

1. Count every substring across all numbers (dedupe per number per substring).
2. For each number, scan lengths 1→9, left-to-right.
3. First substring with global count 1 is minimal by construction.

#### Complexity

| | |
|-|-|
| Time | O(N × L²) with L=9 constant → O(N) |
| Space | O(N × L²) substring map |

#### Edge cases

- **No proper substring unique** — return full number.
- **Leading zeros in substring** — still valid digit string.
- **Two numbers differ only in length** — not here (all length 9).

</details>
</article>

<article>

Given:
- Number of dishes, adults, and kids
- For each dish: happiness value if eaten by an adult or by a kid

Assign one dish to each person (adult or kid) to maximize the total happiness. An adult eats the entire dish; a kid partially eats it.

<details><summary>Theory and explanation</summary>

**Assignment problem** — each dish to exactly one person; each person gets one dish.

If **adults and kids count equals dishes** and one-to-one assignment:

- Build bipartite-style cost matrix: for each dish `d` and person slot, happiness depends on role.
- Since each dish used once and each person once → **maximum weight matching** on complete bipartite graph.

**Simpler contest variant**

Often `dishes = adults + kids` and each dish assigned to unique person — try all permutations if small, or:

- Sort dishes by `(adultHappy - kidHappy)` greedy if problem structure allows swapping.

**General solution**

`maxHappiness = max over assignments` — Hungarian algorithm O(n³) or DP with bitmask if n ≤ 20.

**Kid "partial eat"**

May mean kid gets `kidHappy[d]` while adult gets `adultHappy[d]` — use appropriate table entry per assignee type.

#### Further reading

- [CP-Algorithms: Assignment problem](https://cp-algorithms.com/graph/hungarian-algorithm.html) — Hungarian algorithm
- [Kuhn-Munkres visualization](https://visualgo.net/en/matching) — bipartite matching
- [GeeksforGeeks: Assignment problem](https://www.geeksforgeeks.org/assignment-problem-using-hungarian-algorithm/) — implementation

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function maxHappiness(adultHappy, kidHappy, adults, kids) {
  const n = adultHappy.length;
  const people = [
    ...Array(adults).fill('adult'),
    ...Array(kids).fill('kid'),
  ];
  if (people.length !== n) throw new Error('Expected dishes == people');

  let best = -Infinity;
  const used = Array(n).fill(false);
  const assign = [];

  function dfs(i, sum) {
    if (i === people.length) {
      best = Math.max(best, sum);
      return;
    }
    for (let d = 0; d < n; d++) {
      if (used[d]) continue;
      used[d] = true;
      const gain = people[i] === 'adult' ? adultHappy[d] : kidHappy[d];
      dfs(i + 1, sum + gain);
      used[d] = false;
    }
  }

  dfs(0, 0);
  return best;
}
```

#### Code walkthrough

1. Build role list (adults then kids — order may matter if problem specifies matching slots).
2. Backtracking assigns distinct dishes to people.
3. Track maximum total happiness.

#### Complexity

| | |
|-|-|
| Time | O(n!) — fine for n ≤ 10 contest bounds |
| Space | O(n) recursion |

#### Edge cases

- **More dishes than people** — problem usually balanced; else add dummy zero-happiness.
- **Same happiness values** — any optimal assignment valid.
- **Large n** — switch to Hungarian algorithm.

</details>
</article>

<article>

Given:
- A list of item costs
- A limit on the total increase Sabbir can apply to the item costs

Sabbir increases item costs (total increment ≤ limit) to minimize the final score difference in a turn-based game where players pick items alternately and optimally.

<details><summary>Theory and explanation</summary>

**Game theory + optimization** — both players play optimally on alternating picks (often sorted order matters).

Typical model:

- Items have values/costs; two players alternately pick one remaining item; Sabbir wants to **minimize difference** (or first player maximize sum difference) after optimal play.
- Sabbir can **add** up to `L` total to costs before game — increasing an item may change pick order.

**Approach sketch**

1. Without boosts, optimal play on line often solved by **sorting** + DP: `dp[i][turn]` max/min difference from index `i`.
2. With boost budget `L`, try distributing increments (discretized) to items — search or DP over `(mask, remainingLimit)`.

**Minimax recurrence (two piles variant)**

Sort costs descending; players always pick ends — classic **optimal strategy on sorted multiset** reduces to picking max remaining each turn for greedy variant.

Read original PDF for exact scoring — implement minimax with memo on state `(idx, limitLeft, player)`.

#### Further reading

- [CP-Algorithms: Game theory](https://cp-algorithms.com/game_theory/games_on_graphs.html) — impartial/partisan games
- [GeeksforGeeks: Minimax](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/) — optimal play
- [LeetCode 464: Can I Win](https://leetcode.com/problems/can-i-win/) — bounded game DP

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function minimaxDiff(costs, limitBoost) {
  const n = costs.length;
  const memo = new Map();

  function solve(idx, limit, turn) {
    if (idx >= n) return 0;
    const key = `${idx},${limit},${turn}`;
    if (memo.has(key)) return memo.get(key);

    let best = turn === 0 ? -Infinity : Infinity;
  // try picking each remaining item idx..n-1 (simplified)
    for (let pick = idx; pick < n; pick++) {
      const swap = (arr, i, j) => ([arr[i], arr[j]] = [arr[j], arr[i]]);
      const arr = costs.slice();
      // local search: optional boost on picked item
      for (let add = 0; add <= limit; add++) {
        const val = arr[pick] + add;
        const diff = (turn === 0 ? val : -val) + solve(pick + 1, limit - add, 1 - turn);
        best = turn === 0 ? Math.max(best, diff) : Math.min(best, diff);
      }
    }
    memo.set(key, best);
    return best;
  }

  return solve(0, limitBoost, 0);
}
```

#### Code walkthrough

1. State: next index, remaining boost budget, player turn (0/1).
2. Try picking each item with optional cost increase within budget.
3. Minimax accumulates signed value difference.

#### Complexity

| | |
|-|-|
| Time | Exponential in n — tighten with problem constraints |
| Space | Memo states |

#### Edge cases

- **limit = 0** — pure optimal pick game.
- **Single item** — difference equals its (possibly boosted) cost.
- **Large limit** — cap useful boost per item at max needed to flip pick order.

</details>
</article>

<article>

Given:
- A circular string of length `N×K` representing N fragments of length `K`
- A list of G candidate fragments (all distinct)

Determine if the circular string can be split into a sequence of N valid fragments (from the candidate list) in some rotation. If possible, output any such valid sequence.

<details><summary>Theory and explanation</summary>

**Circular string parsing** — length `N×K`, unknown rotation.

**Steps**

1. Extract all `N` substrings of length `K` from circular string starting at offsets `0..N×K-1` (wrap around).
2. At rotation `r`, fragments are `S[r], S[r+K], …` (mod length) — must match multiset of candidates.
3. Check if each fragment ∈ candidate set; use hash set for O(1) lookup.
4. Verify exactly `N` fragments partition the circle without overlap at chosen rotation.

**Rotation try**

For each start offset `0..K-1` (unique rotations of fragment boundaries), slice N consecutive blocks of length K around circle.

**Hashing**

Store candidate fragments in `Set`; compare counts if duplicates allowed in circle but candidates distinct.

#### Further reading

- [Rolling hash / string hashing](https://cp-algorithms.com/string/string-hashing.html) — fast fragment compare
- [GeeksforGeeks: Circular string](https://www.geeksforgeeks.org/find-occurrences-of-a-substring-in-a-string/) — wrap indexing
- [String matching on circle](https://en.wikipedia.org/wiki/Circular_string) — definition

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function fragmentAt(circle, start, k) {
  let s = '';
  for (let i = 0; i < k; i++) s += circle[(start + i) % circle.length];
  return s;
}

function canSplitCircular(circle, n, k, candidates) {
  const dict = new Set(candidates);
  const len = n * k;

  for (let rot = 0; rot < k; rot++) {
    const seq = [];
    let ok = true;
    for (let i = 0; i < n; i++) {
      const frag = fragmentAt(circle, rot + i * k, k);
      if (!dict.has(frag)) { ok = false; break; }
      seq.push(frag);
    }
    if (ok) return seq;
  }
  return null;
}
```

#### Code walkthrough

1. Try each of `K` rotational alignments of fragment boundaries.
2. Cut `N` fragments of length `K` around circle.
3. All must be in candidate set — return sequence or continue.

#### Complexity

| | |
|-|-|
| Time | O(K × N × K) = O(N × K²) |
| Space | O(N × K) output |

#### Edge cases

- **No valid rotation** — return null / NO.
- **Multiple solutions** — output any.
- **len mismatch** — validate `circle.length === n*k`.

</details>
</article>

<article>

Given multiple test cases, each with two numbers: total artifacts `n` and a position `k`. Artifacts are arranged in a special sequence: first all odd-numbered ones, then multiples of odd numbers (2×odd, 3×odd, etc.) in order, skipping duplicates. Find which artifact appears at position k.

<details><summary>Theory and explanation</summary>

**Sequence generation** — enumerate numbers in order:

1. All odd numbers: 1, 3, 5, 7, …
2. Then for multiplier `m = 2, 3, 4, …`: append `m × odd` for each odd, skipping values already placed.

Equivalent to **sorted unique** numbers of form `odd × m` with priority by `(m, odd)` lex order, or simulate with visited set until `k`-th element.

**Simulation**

```text
seen = set()
for m in 1, 2, 3, ...:
  for odd in 1, 3, 5, ... while odd*m <= n:
    if odd*m not seen: append; stop when count == k
```

**Binary search on answer**

If monotonic mapping from value to rank exists up to `n`, binary search artifact number with rank function — faster for large `k`.

#### Further reading

- [OEIS sequences](https://oeis.org/) — lookup similar ordering patterns
- [Sieve-like generation](https://cp-algorithms.com/algebra/all-submasks.html) — duplicate skipping with sets
- [Codeforces math construction problems](https://codeforces.com/tag/math) — pattern finding

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function artifactAtK(n, k) {
  const seen = new Set();
  let count = 0;

  for (let m = 1; ; m++) {
    for (let odd = 1; odd <= n; odd += 2) {
      const v = odd * m;
      if (v > n || seen.has(v)) continue;
      seen.add(v);
      count++;
      if (count === k) return v;
    }
    if (seen.size === n) break;
  }
  return -1;
}
```

#### Code walkthrough

1. Outer loop multiplier `m` (1 = odds only, then 2×odds, 3×odds, …).
2. Inner loop odd numbers; compute `v = odd * m`.
3. Skip duplicates/`v > n`; count until index `k`.

#### Complexity

| | |
|-|-|
| Time | O(k log k) typical simulation |
| Space | O(k) seen set |

#### Edge cases

- **k > total artifacts ≤ n** — invalid input.
- **k = 1** — first odd = 1.
- **Large n** — prefer binary search rank function.

</details>
</article>

<article>

Given grid dimensions `n × m`. Determine if it is possible to assign pigment values to rows and columns such that every cell in the grid (combining row and column pigment modulo nm) has a unique value. If possible, output the row and column pigments.

<details><summary>Theory and explanation</summary>

Cell value often defined as **`f(row, col) = (rowPigment[r] + colPigment[c]) mod (n×m)`** or **`r * m + c` style encoding** — read PDF for exact combine rule; common contest form:

**Unique via linear combination**

Assign:

- `rowPigment[i] = i * m` (or `i * K`)
- `colPigment[j] = j`

Then `cell(i,j) = rowPigment[i] + colPigment[j]` yields unique pairs if range large enough (0..nm-1).

**Existence condition**

Need **injection** from `(i,j)` pairs to computed values — typically possible when modulus ≥ `n×m` and coefficients coprime to modulus structure.

**Construction**

```text
row[i] = i
col[j] = j * n
value(i,j) = (row[i] + col[j]) mod (n*m)
```

All `n×m` pairs `(i,j)` map to distinct residues if formula is `(i * m + j)`.

#### Further reading

- [Pigeonhole principle](https://brilliant.org/wiki/pigeonhole-principle/) — uniqueness requires enough codomain size
- [Grid labeling problems](https://math.stackexchange.com/) — modular arithmetic constructions
- [Chinese remainder / pairing arguments](https://cp-algorithms.com/algebra/chinese-remainder-theorem.html) — related modular uniqueness

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function assignPigments(n, m) {
  const nm = n * m;
  const row = Array.from({ length: n }, (_, i) => i * m);
  const col = Array.from({ length: m }, (_, j) => j);

  const seen = new Set();
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      const v = (row[i] + col[j]) % nm;
      if (seen.has(v)) return null;
      seen.add(v);
    }
  }
  return { row, col };
}
```

#### Code walkthrough

1. Set row pigment spaced by `m`, column by `1`.
2. Cell value = sum mod `nm`.
3. Verify all unique — if so, output pigments.

#### Complexity

| | |
|-|-|
| Time | O(n × m) |
| Space | O(n × m) verification set |

#### Edge cases

- **1×1 grid** — single cell value 0.
- **Formula differs in PDF** — adjust construction accordingly.
- **Impossible case** — return NO when pigeonhole violated.

</details>
</article>

## Second Round Questions

The given questions are the summarized version of the original questions. The original questions are available in the [Final Round Problem Set](https://github.com/TamimEhsan/interview-questions-bangladesh/tree/master/docs/resource/appify/Final_Onsite.pdf).

<article>
 
Given a sequence of integers, convert each number to binary using parity (even → 1, odd → 0), concatenate to form a binary string, and print it with leading zeros removed.

<details><summary>Theory and explanation</summary>

Map each integer to one **bit**:

- Even → `'1'`
- Odd → `'0'`

Concatenate bits in input order → binary string. **Strip leading zeros**; if all zeros, print `0` or empty per spec.

**Leading zero removal**

Find first `'1'` index; substring from there. If none, answer is `"0"`.

Matches sample loop finding last leading zero before first one in some formulations — equivalent to trim left zeros.

#### Further reading

- [MDN: parseInt binary](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt) — parse binary strings
- [Bit parity](https://en.wikipedia.org/wiki/Parity_bit) — even/odd classification
- [CodeChef/CF implementation challenges](https://codeforces.com/) — I/O formatting

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function parityBinaryString(arr) {
  let bits = arr.map((x) => (x % 2 === 0 ? '1' : '0')).join('');
  bits = bits.replace(/^0+/, '');
  return bits === '' ? '0' : bits;
}

function solveCase(arr) {
  return parityBinaryString(arr);
}
```

#### Code walkthrough

1. Map parity to characters.
2. Join and remove leading `'0'` chars.
3. Empty → `'0'`.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(n) string |

#### Edge cases

- **All even** — all `'1'` bits — no leading zero issue.
- **All odd** — all `'0'` → output `0` after trim.
- **Negative numbers** — `% 2` in JS preserves sign; clarify problem domain.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n; cin >> n;    // size of the array

    // read input array
    vector<int> arr(n);
    for (auto &x : arr) cin >> x;

    // convert even -> 1, odd -> 0
    for (int i = 0; i < n; i++) {
        arr[i] = (arr[i] % 2 == 0) ? 1 : 0;
    }

    // find position of the last leading zero (if any)
    int initial_zero = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] == 0) {
            initial_zero = i;
        } else {
            break;
        }
    }

    // Build answer string from remaining elements
    string ans;
    for (int i = initial_zero + 1; i < n; i++) {
        ans += char(arr[i] + '0');
    }

    cout << ans << "\n";
}

int32_t main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t; 
    cin >> t;  // number of test cases

    for (int i = 1; i <= t; i++) {
        cout << "Case " << i << ": ";
        solve();
    }

    return 0;
}
```

</details>
</article>

<article>
 
Given dimensions of two rectangles, one inside another, where the outer rectangle is `(A×B)` and inner rectangle is `(C×D)`, with `C ≤ A` and `D ≤ B`.

Compute the area between the two rectangles modulo `1,000,000,007`.

[**💻 Submit Code**](https://toph.co/p/the-attack-titan)

<details><summary>Theory and explanation</summary>

**Shaded area** = outer area − inner area = `A×B - C×D`.

**Modulo arithmetic**

Use `(a - b + mod) % mod` to avoid negative results.

**Overflow**

Use 64-bit (`long long`) before mod when values up to 10⁹.

#### Further reading

- [TOPH: The Attack Titan](https://toph.co/p/the-attack-titan) — original problem
- [CP-Algorithms: Modular arithmetic](https://cp-algorithms.com/algebra/module-arithmetic.html) — safe subtract/multiply
- [GeeksforGeeks: Modular arithmetic](https://www.geeksforgeeks.org/modular-arithmetic/) — basics

</details>

<details><summary>Solution (JavaScript)</summary>

```js
const MOD = 1_000_000_007n;

function mul(a, b) {
  return (BigInt(a) * BigInt(b)) % MOD;
}

function ringArea(A, B, C, D) {
  const outer = mul(A, B);
  const inner = mul(C, D);
  return Number((outer - inner + MOD) % MOD);
}

ringArea(1000000000, 1000000000, 999999999, 999999999);
```

#### Code walkthrough

1. Multiply with BigInt mod at each step.
2. Subtract inner from outer with `+ MOD` guard.
3. Return Number if safe for output.

#### Complexity

| | |
|-|-|
| Time | O(1) |
| Space | O(1) |

#### Edge cases

- **Inner equals outer** — area 0.
- **Inner zero area** — full outer area mod M.
- **Large inputs** — BigInt prevents overflow.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
#include<bits/stdc++.h>
using namespace std;

const int mod = 1e9 + 7;

long long multiplication(long long a, long long b,long long m){
    a %= m;
	b %= m;
	return (a * b) % m;
}


void solve(){
    long long a, b, c, d; cin >> a >> b >> c >> d;

    long long x = multiplication(a, b, mod);
    long long y = multiplication(c, d, mod);

    long long result = (x - y + mod) % mod;
    cout << result << "\n";
}
 
int32_t main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t = 1;
    cin >> t;
    for(int i = 1; i <= t; i++){
        solve();
    }
    
    return 0;
}
```

</details>

</article>

<article>
 
Given `N` baskets arranged in a circle with given apples in each and a number `K` indicating how many apples one will eat. 

Simulate the person moving right and eating apples if present, and output the number of apples left in each basket after exactly K apples are eaten.

<details><summary>Theory and explanation</summary>

**Circular simulation** — classic **Josephus / candy distribution** variant.

**Rules (typical)**

- Start at basket 0 (or 1 — check PDF).
- Move clockwise; if current basket has apples > 0, eat one (`--`), count toward `K`.
- Stop when exactly `K` apples eaten.

**Implementation**

While `eaten < K`:

- If `baskets[i] > 0`: decrement, `eaten++`.
- `i = (i + 1) % N`.

**Optimization**

If sum of apples >> K, direct simulation OK. If K huge, skip empty rounds with next-non-empty pointer.

#### Further reading

- [Josephus problem](https://cp-algorithms.com/others/josephus_problem.html) — circular elimination
- [Simulation techniques](https://usaco.guide/CPH/) — competitive programming
- [Modular indexing on circles](https://en.wikipedia.org/wiki/Modular_arithmetic) — wrap with `% N`

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function eatApples(baskets, k) {
  const n = baskets.length;
  const arr = baskets.slice();
  let idx = 0;
  let eaten = 0;

  while (eaten < k) {
    if (arr[idx] > 0) {
      arr[idx]--;
      eaten++;
    }
    idx = (idx + 1) % n;
  }
  return arr;
}

eatApples([3, 1, 0, 2], 5);
```

#### Code walkthrough

1. Copy baskets to avoid mutating input.
2. Walk circle; decrement when apple available.
3. Stop after `k` eats; return final counts.

#### Complexity

| | |
|-|-|
| Time | O(k × n) worst; O(k) with skip optimization |
| Space | O(n) |

#### Edge cases

- **k > total apples** — loop until all gone or clarify spec.
- **All empty initially** — infinite loop unless guarded.
- **Single basket** — eat until k or empty.

</details>
</article>

<article>

Given a string `s` of length `n`. Pick an integer `k` `(1 ≤ k ≤ n)` and perform a transformation: reverse each substring of length `k` sliding through the string, and find the lexicographically smallest resulting string. Output that string and the smallest such k.

[**💻 Submit Code**](https://codeforces.com/problemset/problem/1316/B)

<details><summary>Theory and explanation</summary>

[Codeforces 1316B — String Modification](https://codeforces.com/problemset/problem/1316/B)

**Operation for fixed k**

For `i = 0 .. n-k`: reverse substring `s[i .. i+k-1]` **in place sequentially** — each reversal mutates current string before next slide.

**Goal**

Choose `k` minimizing final string lexicographically; output minimal `k` too if tie-break smallest k.

**Approach**

- Try all `k` from 1 to `n`.
- Simulate reversals O(n²) each → O(n³) total (n ≤ 5000 may need optimization — use efficient simulation or known CF solution).
- Track best string and k.

**Lex order**

Compare strings character by character; shorter k may win tie on string equality.

#### Further reading

- [Codeforces 1316B editorial](https://codeforces.com/problemset/problem/1316/B) — official discussion
- [GeeksforGeeks: Lexicographic order](https://www.geeksforgeeks.org/lexicographic-order/) — string comparison
- [Substring reversal simulation](https://cp-algorithms.com/string/manacher.html) — related string techniques

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function transform(s, k) {
  const arr = s.split('');
  for (let i = 0; i + k <= arr.length; i++) {
    let l = i, r = i + k - 1;
    while (l < r) {
      [arr[l], arr[r]] = [arr[r], arr[l]];
      l++; r--;
    }
  }
  return arr.join('');
}

function bestModification(s) {
  let bestK = 1;
  let best = transform(s, 1);
  for (let k = 2; k <= s.length; k++) {
    const cur = transform(s, k);
    if (cur < best || (cur === best && k < bestK)) {
      best = cur;
      bestK = k;
    }
  }
  return { k: bestK, string: best };
}
```

#### Code walkthrough

1. **`transform`** — apply sliding window reversals in order.
2. Brute all `k`; keep lexicographically smallest result.
3. Tie on string → smaller `k`.

#### Complexity

| | |
|-|-|
| Time | O(n³) — n values of k, each O(n²) simulation |
| Space | O(n) |

#### Edge cases

- **n = 1** — only k=1, string unchanged.
- **k = n** — one reversal of whole string at i=0 only.
- **Equal strings** — pick minimum k.

</details>
</article>

<article>
 
Given a simple directed graph with `N` vertices and `M` edges. Count how many vertices can be starting points for infinite walks (i.e., they lie on or can reach a cycle).

[**💻 Submit Code**](https://atcoder.jp/contests/abc245/tasks/abc245_f)

<details><summary>Theory and explanation</summary>

[AtCoder ABC245 F — Logistic Center](https://atcoder.jp/contests/abc245/tasks/abc245_f)

**Vertices allowing infinite walk**

From start `v`, infinite directed walk exists iff you can **reach a directed cycle** and stay on cycle forever.

Equivalently: `v` can reach some node on a **cycle** (including itself on cycle).

**Algorithm**

1. Find all nodes on cycles — nodes in **strongly connected components (SCC)** with size > 1, or self-loop size-1 SCC.
2. Mark nodes that can reach any cycle node — **reverse graph DFS/BFS** from cycle nodes.

**Steps**

- Kosaraju/Tarjan for SCCs.
- Identify `onCycle` nodes.
- Reverse edges; multi-source BFS from `onCycle` → all reachable can start infinite walk.

**Answer** = count of nodes reaching a cycle.

#### Further reading

- [AtCoder ABC245 F](https://atcoder.jp/contests/abc245/tasks/abc245_f) — problem statement
- [CP-Algorithms: Finding cycles](https://cp-algorithms.com/graph/finding-cycle.html) — cycle detection
- [CP-Algorithms: Strongly connected components](https://cp-algorithms.com/graph/strongly-connected-components.html) — Kosaraju/Tarjan

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function countInfiniteWalkStarts(n, edges) {
  const adj = Array.from({ length: n }, () => []);
  const radj = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) {
    adj[u].push(v);
    radj[v].push(u);
  }

  const state = Array(n).fill(0);
  const onCycle = Array(n).fill(false);

  function dfs(v) {
    state[v] = 1;
    for (const to of adj[v]) {
      if (state[to] === 0) dfs(to);
      else if (state[to] === 1) onCycle[v] = onCycle[to] = true;
    }
    state[v] = 2;
  }

  for (let i = 0; i < n; i++) if (!state[i]) dfs(i);

  const can = Array(n).fill(false);
  const q = [];
  for (let i = 0; i < n; i++) if (onCycle[i]) { can[i] = true; q.push(i); }
  while (q.length) {
    const u = q.shift();
    for (const p of radj[u]) {
      if (!can[p]) { can[p] = true; q.push(p); }
    }
  }
  return can.filter(Boolean).length;
}
```

#### Code walkthrough

1. DFS coloring detects back-edges → nodes on cycles.
2. Reverse graph BFS from cycle nodes marks all predecessors.
3. Count marked nodes.

#### Complexity

| | |
|-|-|
| Time | O(N + M) |
| Space | O(N + M) |

#### Edge cases

- **Self-loop** — vertex on cycle immediately.
- **DAG** — answer 0.
- **Whole graph one cycle** — all n vertices.

</details>
</article>

<article>

Given a book with `N` pages (numbered `1` to `N`) and a secret digit (0–9), and you randomly pick a page. 
Compute the probability that the page number you picked contains the secret digit, expressed as an irreducible fraction `P/Q`.

[**💻 Submit Code**](https://www.codechef.com/problems/ANUBGC)

<details><summary>Theory and explanation</summary>

[CodeChef ANUBGC — Anubis and Good Numbers](https://www.codechef.com/problems/ANUBGC)

**Uniform probability** over pages `1..N`.

**Count favorable pages**

Pages whose decimal representation contains digit `d`.

For each length / range, count numbers with digit `d` using **digit DP** or inclusion-exclusion, or brute for N ≤ 10⁶.

**Irreducible fraction**

`P/Q = favorable / N`, then `g = gcd(P, Q)`, divide both.

**Digit DP state**

`(pos, tight, started, hasDigit)` count numbers ≤ N with digit present.

#### Further reading

- [CodeChef ANUBGC](https://www.codechef.com/problems/ANUBGC) — statement
- [CP-Algorithms: Digit DP](https://cp-algorithms.com/dynamic_programming/digit-dp.html) — counting with digit constraints
- [GeeksforGeeks: GCD](https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/) — reduce fraction

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function gcd(a, b) {
  while (b) [a, b] = [b, a % b];
  return a;
}

function containsDigit(num, d) {
  return String(num).includes(String(d));
}

function probabilityContainsDigit(n, digit) {
  let favorable = 0;
  for (let p = 1; p <= n; p++) {
    if (containsDigit(p, digit)) favorable++;
  }
  const g = gcd(favorable, n);
  return { p: favorable / g, q: n / g };
}

// probabilityContainsDigit(100, 7); // pages with 7: 19/100 → reduce
```

#### Code walkthrough

1. Brute count pages 1..N containing digit (upgrade to digit DP for large N).
2. Probability = favorable / N.
3. Reduce with GCD.

#### Complexity

| | |
|-|-|
| Time | O(N log N) brute; O(log N) with digit DP |
| Space | O(1) brute |

#### Edge cases

- **digit 0** — pages like 10, 20 count; leading zero not in page numbers.
- **N = 0** — undefined; problem N ≥ 1.
- **favorable = 0** — output `0/1`.

</details>
</article>

<article>
 
Given Grid size `n×m` and manhattan distances from a hidden cell `(a, b)` to `(1, 1)` and `(1, m)`. Find the coordinates `(a, b)` of the hidden cell using the given distances

[**💻 Submit Code**](https://codeforces.com/problemset/problem/1934/C)

<details><summary>Theory and explanation</summary>

[Codeforces 1934C — Turtle and Good Pairs](https://codeforces.com/problemset/problem/1934/C) — verify problem ID matches PDF (grid hidden cell with Manhattan distances to corners).

**Manhattan distance**

`d1 = |a - 1| + |b - 1| = (a - 1) + (b - 1)` if `(a,b)` in 1-indexed lower quadrant from corners.

Given:

- `d1 = dist to (1,1) = (a-1) + (b-1)`
- `d2 = dist to (1,m) = (a-1) + (m-b)`

**Solve**

Add: `d1 + d2 = 2(a-1) + (m-1)` → `a = (d1 + d2 - m + 1) / 2 + 1` (adjust indexing).

Subtract: `d2 - d1 = m - 2b` → `b = (m - (d2 - d1)) / 2`.

Validate `(a,b)` in `[1,n]×[1,m]`.

#### Further reading

- [Codeforces 1934C](https://codeforces.com/problemset/problem/1934/C) — grid puzzle
- [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry) — L1 metric
- [GeeksforGeeks: Manhattan distance](https://www.geeksforgeeks.org/manhattan-distance/) — formula

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function findHiddenCell(n, m, d11, d1m) {
  // d11 = |a-1| + |b-1|, d1m = |a-1| + |m-b|
  const a = Math.floor((d11 + d1m - m) / 2) + 1;
  const b = Math.floor((d11 - d1m + m) / 2);
  if (a < 1 || a > n || b < 1 || b > m) return null;
  return { a, b };
}

findHiddenCell(5, 5, 4, 6); // example — verify with problem constraints
```

#### Code walkthrough

1. Solve linear equations from two Manhattan distances to top corners.
2. Floor/integer division handles parity constraints.
3. Validate bounds in grid.

#### Complexity

| | |
|-|-|
| Time | O(1) |
| Space | O(1) |

#### Edge cases

- **No valid cell** — inconsistent distances → null.
- **Multiple corners** — distances must be consistent with single `(a,b)`.
- **1-indexed vs 0-indexed** — adjust formulas to match statement.

</details>
</article>

## Contributors
- Interview applicant [Peal Hassan](https://www.linkedin.com/in/pealhassan/)  
- Collected and organized by [Mustaq Mujahid Mim](https://www.linkedin.com/in/mmmim/)
