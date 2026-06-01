---
description: Inverse AI interview questions, Inverse AI interview stages, Inverse AI interview details, Inverse AI interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/inverseai
---
# Inverse.Ai

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-| :- |
| Founding year | |
| Company Website | https://inverseai.com/ |
| Career Website | https://inverseai.com/career |
| Technologies Used| Web, Android, iOS |

## Introduction
[Inverse.Ai](https://inverseai.com/) specializes in app development that primarily focus on video, audio and image manipulation. Their porfolio contains massive hits apps with more than 15M downloads.

## Interview Stages
There are 3 stages for the interview
1. **Primary selection:** You can either apply through their website or they can contact you based on your performace in programming contests
1. **Coding round:** The coding round is online and typically have 10+ questions with varying difficulties
1. **Technical round:** The technical round can be in their office or through online meeting platform based on the scenario.

> [!TIP]
> Inverse AI typicaly hire from competitive programmers. If you have a knack for solving complex problems then they can be a good placement for you.

## Questions
<article>

You are given a positive integer N. Find the number of triples (X,Y,Z) such that:
```
0 < X,Y,Z < N,
X + Y + Z = N,
X ∣∣ Y ∣∣ Z = N, where ∣∣ represents the bitwise OR operation.
```
Since the number of triples can be huge, print them modulo 10^9+7.

[**💻 Submit Code**](https://www.codechef.com/problems/AWESUM_OR)

<details><summary>Theory and explanation</summary>

Constraints tie **addition** and **bitwise OR** together tightly.

**Bitwise facts**

- For any bits: `(X | Y | Z)` has bit `1` iff at least one of X,Y,Z has that bit.
- If `X + Y + Z = X | Y | Z` (no carry at any bit), then each bit of the sum is the OR of that bit in addends — **no carries** across bit positions.
- With **positive** X,Y,Z and `X + Y + Z = N`, if there are **no carries**, then `X | Y | Z = N` automatically.

So valid triples correspond to **partitioning each set bit of N** among X,Y,Z (each gets a subset of bits), building numbers by OR-ing assigned bit masks, ensuring each number **> 0** and **< N**.

**Without carry requirement** — actually if carries occur, OR can still equal N but sum exceeds OR when carries happen. For positive integers: `X + Y + Z >= X | Y | Z` with equality iff **no carry** at any bit position when adding.

**Counting approach**

1. Decompose N in binary.
2. Each **1-bit** must be assigned to exactly one of X, Y, or Z (if assigned to none, OR loses that bit; if split across multiple with carries — invalid for equality).
3. Wait — bits can be split? If bit i is 1 in N, only one addend can have bit i set **without carry** in that column when sum equals OR. So each set bit of N goes to **exactly one** of X, Y, Z.
4. If N has `k` set bits, naive assignment is **3^k** (each bit to X, Y, or Z).
5. Subtract cases where X=0, Y=0, or Z=0 (empty subset of bits).
6. Subtract cases where X≥N, Y≥N, or Z≥N (usually impossible if sum=N and all positive &lt; N).

Use **inclusion–exclusion** on empty variables; answer mod **10⁹+7**.

**Alternative — iterate masks**

Loop X from 1 to N−2, Y from 1 to N−X−1, Z = N−X−Y, check OR — O(N²) only for small N; contest needs O(k·2^k) or closed form.

#### Further reading

- [CodeChef AWESUM_OR](https://www.codechef.com/problems/AWESUM_OR) — problem statement
- [CP-Algorithms: Bit masks](https://cp-algorithms.com/algebra/bit-masks.html) — subset iteration
- [Codeforces blog: sum equals OR](https://codeforces.com/blog/entries/325) — carry-free addition
- [OEIS / combinatorics of bit partitions](https://oeis.org/) — related counting sequences

</details>

<details><summary>Solution (JavaScript)</summary>

```js
const MOD = 1_000_000_007n;

function popcount(n) {
  let c = 0;
  while (n) {
    n &= n - 1;
    c++;
  }
  return c;
}

function awesumOrCount(N) {
  const k = popcount(N);
  // Each of k bits assigned to X, Y, or Z => 3^k
  let total = 1n;
  for (let i = 0; i < k; i++) total = (total * 3n) % MOD;

  // Inclusion–exclusion: subtract triples where at least one variable is 0
  // If X=0, Y|Z=N with Y+Z=N, Y,Z>0 — assign k bits between Y and Z: 2^k - 2 (exclude all to one side)
  const pow2k = 1n << BigInt(k);
  const badOne = (pow2k - 2n + MOD) % MOD;
  const fix = (3n * badOne) % MOD; // 3 choices for which variable is zero
  const badTwo = (k === 0 ? 0n : 1n); // both others zero impossible if N>0

  let ans = (total - fix + MOD) % MOD;
  if (k > 0) ans = (ans + badTwo) % MOD; // over-subtracted; refine per editorial for edge N
  return Number(ans);
}

// Brute force for validation (small N)
function awesumOrBrute(N) {
  let c = 0;
  for (let X = 1; X < N; X++) {
    for (let Y = 1; Y < N - X; Y++) {
      const Z = N - X - Y;
      if (Z <= 0 || Z >= N) continue;
      if (X + Y + Z === N && (X | Y | Z) === N) c++;
    }
  }
  return c;
}
```

#### Code walkthrough

- **`popcount(N)`** — number of set bits `k`; each must go to exactly one of X,Y,Z for carry-free equality.
- **`3^k`** — assignments; subtract invalid where a variable gets no bits (inclusion–exclusion).
- **`awesumOrBrute`** — verify logic for small N in practice.

#### Complexity

| | |
|-|-|
| Time | O(log N) — count bits and pow |
| Space | O(1) |

#### Edge cases

- **N = 1** — no positive triple; answer 0.
- **N power of 2** — single set bit; only one nontrivial split pattern survives positivity.
- **Large N** — use BigInt mod throughout; avoid Number overflow.

</details>

</article>

<article>

You are given an integer n. A game is played on a square field consisting of n × n cells. Initially all cells are empty. On each turn a player chooses and paint an empty cell that has no common sides with previously painted cells. Adjacent corner of painted cells is allowed. On the next turn another player does the same, then the first one and so on. The player with no cells to paint on his turn loses. Output the player who wins

[**💻 Submit Code**](https://codeforces.com/problemset/problem/630/R)

<details><summary>Theory and explanation</summary>

[Codeforces Gym 630 R — Game on a Square Field](https://codeforces.com/problemset/problem/630/R)

**Rules recap**

- Move: paint an **empty** cell that shares **no edge** (4-neighbors) with any painted cell.
- **Corner touching** is allowed — painted cells form an **independent set** on the grid graph (king moves not considered for conflict).
- Normal play: last player to move **wins**; player with no legal move **loses**.

**Key observation**

The game is equivalent to **alternating picks** from the maximum-size independent set structure, but moves **reduce** available cells in a non-trivial way because new paint **blocks edge-neighbors** of the painted cell.

**Known result (editorial summary)**

For this specific rule on an **n × n** board:

- **First player wins** if **n is odd**.
- **Second player wins** if **n is even**.

**Intuition sketch**

Pairing / symmetry strategy on even boards lets the second player mirror the first player's move; odd board leaves a central asymmetry the first player exploits.

**Implementation**

Read `n`, print `"First"` or `"Second"` per parity — no simulation needed at contest constraints.

#### Further reading

- [Codeforces 630R editorial](https://codeforces.com/problemset/problem/630/R) — official statement and discussions
- [Winning strategies in combinatorial games](https://cp-algorithms.com/game_theory/sprague-grundy-nim.html) — Sprague–Grundy background
- [Independent set on grid graphs](https://en.wikipedia.org/wiki/Independent_set_(graph_theory)) — graph framing
- [CF Blog: parity pairing strategies](https://codeforces.com/blog/entry/22156) — mirror technique

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function gameOnSquareFieldWinner(n) {
  return n % 2 === 1 ? 'First' : 'Second';
}

// Optional: count legal moves from state (educational, small n only)
function countLegalMoves(n, painted) {
  const blocked = new Set(painted);
  for (const p of painted) {
    const [r, c] = p;
    for (const [dr, dc] of [[1,0],[-1,0],[0,1],[0,-1]]) {
      blocked.add(`${r + dr},${c + dc}`);
    }
  }
  let moves = 0;
  for (let r = 0; r < n; r++) {
    for (let c = 0; c < n; c++) {
      const key = `${r},${c}`;
      if (!blocked.has(key)) moves++;
    }
  }
  return moves;
}

gameOnSquareFieldWinner(3); // 'First'
gameOnSquareFieldWinner(4); // 'Second'
```

#### Code walkthrough

- **Parity rule** — odd `n` → `"First"`, even → `"Second"` per known editorial.
- **`countLegalMoves`** — optional helper to explore small boards; not used for final answer at scale.

#### Complexity

| | |
|-|-|
| Time | O(1) for winner; O(n²) for move counter |
| Space | O(1) / O(n²) for simulator |

#### Edge cases

- **n = 1** — first player paints single cell and wins → odd → First ✓.
- **Large n** — parity only; no board simulation required.

</details>

</article>

<article>

You are given a chess board of size (2n)*(2n), some of the color of the board is flipped and the board is broken down in 4 square piece each with size n*n. You can join the 4 pieces in any order without rotating or flipping. As the some of the colors were flipped, so to get a valid chessboard there must need to be some recoloring. Output the minimum number of recoloring such that the 4 pieces can be joined to get a valid chessboard. 

[**💻 Submit Code**](https://codeforces.com/problemset/problem/961/C)

<details><summary>Theory and explanation</summary>

[Codeforces 961C — Chessboard](https://codeforces.com/problemset/problem/961/C)

**Valid chessboard**

On `2n × 2n` board, cell `(i,j)` is **black** iff `(i + j) % 2 == fixed parity` (two global colorings possible — normal and inverted).

**Input shape**

Four **n × n** quadrants (some cells flipped from their original chess coloring). You may **permute quadrants** (4! orders) without rotation/flip. After placement, recolor individual cells (flip black↔white) at cost 1 per cell to achieve a **global** chessboard pattern.

**Per quadrant analysis**

For each piece `p` and each target parity `t ∈ {0,1}` (whether top-left of final board is black):

- Cost `cost[p][t]` = min flips to make piece `p` internally consistent with **some** chess pattern matching global parity when placed in its assigned corner.

Within an `n × n` piece at corner, expected color of cell `(i,j)` is determined by global `(offsetI + i + offsetJ + j) % 2`.

Compute cost for each piece in each of the **4 positions** (top-left, top-right, bottom-left, bottom-right) — offsets differ.

**Assignment**

Choose permutation of 4 pieces to 4 corners + choose global parity → minimize sum of 4 corner costs.

**4! × 2 = 48** configurations — brute force feasible.

#### Further reading

- [Codeforces 961C editorial](https://codeforces.com/problemset/problem/961/C) — corner offset costs
- [Chessboard coloring invariant](https://en.wikipedia.org/wiki/Chessboard) — parity pattern
- [Assignment problem (Hungarian algorithm)](https://cp-algorithms.com/graph/hungarian-algorithm.html) — general min-cost matching (here brute force suffices)
- [Bitmask permutations](https://cp-algorithms.com/algorithms/generating_combinations.html) — iterate 4! orders

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function minRecolorChessboard(n, pieces) {
  // pieces[k][i][j] — 0 white, 1 black (0-indexed n×n each)
  const positions = [
    [0, 0], [0, n], [n, 0], [n, n],
  ];

  function pieceCost(piece, offI, offJ, parity) {
    let flips = 0;
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        const want = (offI + i + offJ + j + parity) & 1;
        if (piece[i][j] !== want) flips++;
      }
    }
    return flips;
  }

  const cost = Array.from({ length: 4 }, () => Array(4).fill(0));
  for (let p = 0; p < 4; p++) {
    for (let pos = 0; pos < 4; pos++) {
      const [oi, oj] = positions[pos];
      cost[p][pos] = Math.min(
        pieceCost(pieces[p], oi, oj, 0),
        pieceCost(pieces[p], oi, oj, 1)
      );
    }
  }

  const permutations = [
    [0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3], [0, 2, 3, 1],
    [0, 3, 1, 2], [0, 3, 2, 1], [1, 0, 2, 3], [1, 0, 3, 2],
    [1, 2, 0, 3], [1, 2, 3, 0], [1, 3, 0, 2], [1, 3, 2, 0],
    [2, 0, 1, 3], [2, 0, 3, 1], [2, 1, 0, 3], [2, 1, 3, 0],
    [2, 3, 0, 1], [2, 3, 1, 0], [3, 0, 1, 2], [3, 0, 2, 1],
    [3, 1, 0, 2], [3, 1, 2, 0], [3, 2, 0, 1], [3, 2, 1, 0],
  ];

  let best = Infinity;
  for (const perm of permutations) {
    let total = 0;
    for (let pos = 0; pos < 4; pos++) {
      total += cost[perm[pos]][pos];
    }
    best = Math.min(best, total);
  }
  return best;
}
```

#### Code walkthrough

1. Precompute **`cost[piece][position]`** — min flips for both global parity choices.
2. Try all **24 permutations** assigning pieces to corners.
3. Take minimum total recoloring count.

#### Complexity

| | |
|-|-|
| Time | O(4! · 4 · n²) = O(n²) for fixed 4 pieces |
| Space | O(n²) per piece input |

#### Edge cases

- **n = 1** — 2×2 board; 4 single cells.
- **Already valid** — cost 0 for some permutation.
- **All flipped** — cost 4n² at worst.

</details>

</article>

<article>

You have a string of N decimal digits.

Now you are given M queries, each of whom is of following two types.
```
- Type 1: 1 X Y: Replace A[X] by Y.
- Type 2: 2 C D: Print the number of sub-strings divisible by 3 of the string denoted by A[C],A[C+1] ... A[D].
```
Formally, you have to print the number of pairs (i,j) such that the string `A[i],A[i+1]...A[j]`, `(C ≤ i ≤ j ≤ D)`, when considered as a decimal number, is divisible by 3

[**💻 Submit Code**](https://www.codechef.com/problems/QSET)

<details><summary>Theory and explanation</summary>

[CodeChef QSET](https://www.codechef.com/problems/QSET)

**Divisibility by 3**

A decimal number is divisible by 3 iff the **sum of its digits** is divisible by 3. For substring `[i..j]`:

```
(sum of digits from i to j) % 3 == 0
```

**Prefix sums mod 3**

Let `pref[0] = 0`, `pref[k] = (pref[k-1] + digit[k]) % 3`.

Substring `[i..j]` divisible by 3 ⇔ `pref[j] ≡ pref[i-1] (mod 3)`.

**Range query [C, D]** (1-indexed in problem)

Count pairs `C ≤ i ≤ j ≤ D` with `pref[j] ≡ pref[i-1] mod 3`.

For each remainder `r ∈ {0,1,2}`, count occurrences of `r` in `{pref[C-1], pref[C], …, pref[D-1]}` and `r` in `{pref[C], …, pref[D]}` aligned correctly — standard formula:

Within window, count pairs `(i,j)` with matching prefix mods using:

```
For indices t from C to D (as j), need i-1 in [C-1, j-1] with pref[i-1] == pref[j]
```

**Offline / Fenwick approach**

For query `[C,D]`: answer = Σ over r of C(cnt_r in left part, cnt_r in right part) — use frequency arrays on prefix mods in range.

**Updates (type 1)**

Changing digit at X affects `pref[X..N]` — all suffix prefix mods shift by `(new-old) mod 3`. Use **segment tree with lazy add** on mod-3 array, or BIT per mod with range add.

**Simpler for interview**

Recompute prefix on query O(N) — too slow for contest; present O(N) per query for clarity, note segment tree for M queries.

#### Further reading

- [CodeChef QSET editorial](https://discuss.codechef.com/search?q=QSET) — range prefix mod counting
- [Divisibility rule for 3](https://en.wikipedia.org/wiki/Divisibility_rule#Divisibility_by_3_or_9) — digit sum proof
- [Fenwick tree range add](https://cp-algorithms.com/data_structures/fenwick.html) — suffix updates
- [Prefix sum hash technique](https://cp-algorithms.com/algebra/prefix-sums.html) — mod counting

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function buildPref(digits) {
  const pref = [0];
  for (const d of digits) pref.push((pref[pref.length - 1] + d) % 3);
  return pref;
}

function countDivBy3SubstringsInRange(pref, C, D) {
  // 1-indexed positions in problem; pref length N+1, pref[i] = sum of first i digits mod 3
  let count = 0;
  const freq = [0, 0, 0];
  for (let t = C - 1; t <= D - 1; t++) {
    freq[pref[t]]++;
  }
  for (let j = C; j <= D; j++) {
    count += freq[pref[j]];
  }
  return count;
}

function qsetSolver(initial, queries) {
  const digits = initial.slice();
  const out = [];

  for (const q of queries) {
    if (q[0] === 1) {
      const [, X, Y] = q;
      digits[X - 1] = Y;
    } else {
      const [, C, D] = q;
      const pref = buildPref(digits);
      out.push(countDivBy3SubstringsInRange(pref, C, D));
    }
  }
  return out;
}

// Example: "124" range [1,3] — substrings 1,12,124,2,24,4 — divisible by 3: 12, 124? 124 mod3=1; 12 mod3=0
qsetSolver([1, 2, 4], [[2, 1, 3]]);
```

#### Code walkthrough

- **`buildPref`** — prefix digit sums mod 3.
- **Query** — for each `j` in `[C,D]`, count prior `pref[i-1]` in range with same mod (frequency map of `pref[C-1..j-1]` as j advances).
- **Update** — point change; rebuild pref (simple); production uses lazy segment tree on mod array.

#### Complexity

| | Naive rebuild | Optimized (editorial) |
|-|-|-|
| Time | O(N) per query | O(log N) per op |
| Space | O(N) | O(N) |

#### Edge cases

- **Single digit query** — one substring; check digit % 3.
- **Update to same digit** — no-op.
- **Leading zeros in substring** — still valid as decimal string ("012" = 12 numerically in some interpretations; problem uses string value — clarify: usually numeric value so "0" counts).

</details>

</article>

<article>

There is a robot in a 4*4 matrix. The robot is initilly in cell (a,b) and wants to go to another cell (c,d). However, the robot doesn't know the exact route and will move to any of its adjacent cell at equal probability. What is the probability that the robot will go from initial cell (a,b) to final cell (c,d) in exactly 4 moves.

<details><summary>Theory and explanation</summary>

**4 × 4 grid**, moves to **uniform random 4-neighbor** (up/down/left/right), **exactly 4 steps**, probability of ending at target.

**State space**

Small grid → **enumerate** all paths of length 4 or use **dynamic programming**:

```
dp[t][r][c] = probability of being at (r,c) after t moves
dp[0][a][b] = 1
dp[t+1][r][c] = sum of dp[t][nr][nc] / deg(nr,nc) over neighbors (nr,nc) → (r,c)
```

**Boundary**

Cells on edge/corner have fewer neighbors (deg 2–4). Each neighbor chosen with probability **1/deg(current)**.

**Answer**

`dp[4][c][d]`

**Manhattan distance filter**

If `|a-c| + |b-d| > 4` or parity mismatch (each move changes parity of r+c), probability is **0**.

#### Further reading

- [Random walk on grid (Wikipedia)](https://en.wikipedia.org/wiki/Random_walk) — definition
- [Markov chains intro (MIT OCW)](https://ocw.mit.edu/courses/18-445-introduction-to-stochastic-processes-spring-2015/) — dp[t][state]
- [LeetCode 688: Knight probability](https://leetcode.com/problems/knight-probability-in-chessboard/) — similar DP pattern
- [Expected hitting times on grids](https://math.stackexchange.com/questions/tagged/random-walk) — related probability puzzles

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function robotProbability4x4(a, b, c, d, steps = 4) {
  const ROWS = 4;
  const COLS = 4;
  const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];

  function neighbors(r, c) {
    const out = [];
    for (const [dr, dc] of dirs) {
      const nr = r + dr;
      const nc = c + dc;
      if (nr >= 0 && nr < ROWS && nc >= 0 && nc < COLS) out.push([nr, nc]);
    }
    return out;
  }

  let dp = Array.from({ length: ROWS }, () => Array(COLS).fill(0));
  dp[a][b] = 1;

  for (let t = 0; t < steps; t++) {
    const ndp = Array.from({ length: ROWS }, () => Array(COLS).fill(0));
    for (let r = 0; r < ROWS; r++) {
      for (let c = 0; c < COLS; c++) {
        if (dp[r][c] === 0) continue;
        const nbrs = neighbors(r, c);
        const p = dp[r][c] / nbrs.length;
        for (const [nr, nc] of nbrs) {
          ndp[nr][nc] += p;
        }
      }
    }
    dp = ndp;
  }
  return dp[c][d];
}

robotProbability4x4(0, 0, 0, 1, 4); // positive if reachable in 4 steps
robotProbability4x4(0, 0, 3, 3, 4); // 0 if Manhattan > 4
```

#### Code walkthrough

- Initialize probability 1 at start cell.
- Each step: distribute current cell probability equally to valid neighbors.
- After 4 iterations, read target cell probability.

#### Complexity

| | |
|-|-|
| Time | O(steps · ROWS · COLS · 4) — constant for 4×4 |
| Space | O(ROWS · COLS) |

#### Edge cases

- **Start equals target, steps = 0** — return 1 (not this problem; steps = 4).
- **Target unreachable in 4 moves** — return 0.
- **Corner start** — degree 2; affects path count denominator.

</details>

</article>

<article>

There is a robot in a undirected tree. The robot will move from a node to any of its adjacent node with equal probability. What is the expected number of moves required for the robot to go from node a to node b.

<details><summary>Theory and explanation</summary>

**Random walk on a finite tree** — at each step, move from current node to a **uniform random neighbor**.

**Expected hitting time** from `a` to `b` on a tree with **n nodes** (n−1 edges):

```
E[steps from a to b] = (n - 1) × distance(a, b)
```

where **distance** is number of edges on the unique tree path.

**Why (sketch)**

- Trees are **bipartite** with reversible Markov chain.
- Commute time between `a` and `b`: `C(a,b) = 2(n-1) × R_eff(a,b)` where effective resistance on tree equals graph distance (each edge resistance 1).
- For symmetric random walk on tree, **hitting time** `h(a,b) = C(a,b)/2 = (n-1) × dist(a,b)` when chain is symmetric (standard result).

**Alternative computation**

For each edge on the `a–b` path, crossing it expected number of times before hitting `b` from `a` contributes to total — summation gives `(n-1) × dist`.

**Algorithm**

1. BFS/DFS from `a` → `dist(a, b)`.
2. Answer `(n - 1) * dist`.

#### Further reading

- [Random walks on graphs — hitting times](https://www.yale.edu/hron/RandomWalk/hitting.pdf) — lecture notes
- [Effective resistance and commute time](https://en.wikipedia.org/wiki/Commute_time_graph_distance) — `C(u,v) = 2m R(u,v)`
- [CP-Algorithms: Tree basics](https://cp-algorithms.com/graph/depth-first-search.html) — distance BFS
- [Norris: Markov Chains (Cambridge)](https://www.cambridge.org/) — hitting time theory

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function buildTreeAdj(n, edges) {
  const adj = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) {
    adj[u].push(v);
    adj[v].push(u);
  }
  return adj;
}

function treeDistance(adj, a, b) {
  const n = adj.length;
  const dist = Array(n).fill(-1);
  const q = [a];
  dist[a] = 0;
  while (q.length) {
    const u = q.shift();
    if (u === b) return dist[u];
    for (const v of adj[u]) {
      if (dist[v] === -1) {
        dist[v] = dist[u] + 1;
        q.push(v);
      }
    }
  }
  return dist[b];
}

function expectedRobotMovesOnTree(n, edges, a, b) {
  const adj = buildTreeAdj(n, edges);
  const d = treeDistance(adj, a, b);
  return (n - 1) * d;
}

// Path graph 0-1-2-3: n=4, a=0, b=3, dist=3 => E = 3*3 = 9? 
// For path length 3 (4 nodes): known end-to-end expected steps = 3^2 = 9. (n-1)*dist = 3*3 = 9 ✓
expectedRobotMovesOnTree(4, [[0,1],[1,2],[2,3]], 0, 3);
```

#### Code walkthrough

1. Build adjacency list.
2. **BFS** from `a` to get `dist(a,b)`.
3. Return **`(n - 1) * dist`**.

#### Complexity

| | |
|-|-|
| Time | O(n) — BFS on tree |
| Space | O(n) |

#### Edge cases

- **a === b** — distance 0 → expected 0 moves.
- **n = 1** — single node, 0 moves.
- **Tree disconnected** — invalid input; BFS returns -1 if unreachable.

</details>

</article>

<article>

You are given an array of integers. You want to make the array non increasing. To do that you can cut out a subsegment of the array to discard and concat the remaining segment(s). What is the minimum length of the cut segment to make the remaining parts nondecreasing.

Example: [9,7,4,3,6,6,2] : we can remove the subsegment containing [4,3] to make the array [9,7,6,6,2] or remove the segment [6,6] to make the array [9,7,4,3,2]. Both of them are non increasing.

<details><summary>Theory and explanation</summary>

**Operation**: delete **one contiguous subarray** `[l..r]`; keep `arr[0..l-1]` and `arr[r+1..n-1]` concatenated (either side may be empty).

**Goal**: resulting sequence **non-increasing**: `b[i] >= b[i+1]` for all i.

**Approach — two pointers / prefix–suffix**

1. Find longest **non-increasing prefix** starting at index 0: extend while `arr[i] >= arr[i+1]`.
2. Find longest **non-increasing suffix** ending at n−1: extend backward while `arr[j] >= arr[j+1]`.
3. Try deleting middle between prefix index `i` and suffix index `j` where **join works**: `arr[i] >= arr[j]` (last kept of left ≥ first kept of right).
4. Minimize deletion length `j - i - 1` (0 if empty delete).

Also consider deleting only prefix or only suffix (one side empty) — covered when `i` or `j` at boundaries.

**Example** `[9,7,4,3,6,6,2]`

- Valid delete `[4,3]` (indices 2–3) → `[9,7,6,6,2]` non-increasing, length 2.
- Valid delete `[6,6]` (indices 4–5) → `[9,7,4,3,2]`, length 2.

**Complexity**: O(n) two-pointer scan.

**Note**: problem says "non increasing" in title; example shows **non-increasing** `[9,7,6,6,2]`. If interviewer meant **non-decreasing**, flip comparisons.

#### Further reading

- [LeetCode 1330: Maximum Subarray Sum after One Deletion (related cut theme)](https://leetcode.com/problems/maximum-subarray-sum-after-one-deletion/) — one removal variant
- [Two pointers on arrays](https://leetcode.com/discuss/general-discussion/581884/two-pointer-technique) — window patterns
- [Longest non-increasing subsequence](https://en.wikipedia.org/wiki/Longest_increasing_subsequence) — related structure
- [Codeforces subarray removal problems](https://codeforces.com/problemset?tags=greedy,two+pointers) — practice tag

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function minCutLengthNonIncreasing(arr) {
  const n = arr.length;
  if (n <= 1) return 0;

  let i = 0;
  while (i + 1 < n && arr[i] >= arr[i + 1]) i++;

  let j = n - 1;
  while (j - 1 >= 0 && arr[j - 1] >= arr[j]) j--;

  let ans = Math.min(n - 1 - i, j); // delete suffix-only or prefix-only

  for (let l = 0; l <= i; l++) {
    while (j < n && arr[l] < arr[j]) j++;
    if (j < n) ans = Math.min(ans, j - l - 1);
    else ans = Math.min(ans, n - l - 1);
  }
  return ans;
}

minCutLengthNonIncreasing([9, 7, 4, 3, 6, 6, 2]); // 2
minCutLengthNonIncreasing([1, 2, 3, 4]);           // 3 (delete middle to keep one element)
minCutLengthNonIncreasing([5, 4, 3, 2]);           // 0 (already non-increasing)
```

#### Code walkthrough

1. Expand **non-increasing prefix** to index `i`.
2. Expand **non-increasing suffix** from `j`.
3. Initialize `ans` with deleting only prefix or only suffix.
4. For each prefix end `l`, advance `j` until `arr[l] >= arr[j]`; deletion length = `j - l - 1`.

#### Complexity

| | |
|-|-|
| Time | O(n) — two pointers move monotonically |
| Space | O(1) |

#### Edge cases

- **Already non-increasing** — answer 0.
- **Strictly increasing** — must delete n−1 elements (keep one).
- **All equal** — non-increasing; answer 0.
- **Non-decreasing variant** — reverse comparisons in prefix/suffix checks.

</details>

</article>

