---
description: Priyo sys interview questions, Priyo sys interview stages, Priyo sys interview details, Priyo sys interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/priyo
---
# Priyo sys

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-| :- |
| Founding year | |
| Company Website | https://www.priyo.com/ |
| Career Website |  |
| Technologies Used|  |

## Introduction
[Priyo](https://www.priyo.com/) is a finance based tech company operating in US market. They operate from Bangladesh. 
## Interview Stages
Priyo takes 2 interview. 
1. **Coding Round:** The coding round is half hour long. The problem given is typically harder than usual. Upon completion, follow ups can be asked
2. **Technical Round:** The technical round is also half hour. 
3. **CEO Round:** It is kind of a behavioural round. But the questions can be coding or technical.

## Coding Round Questions
<article>

Given an array of positive integers and a integer p. Find the length of the minimum subarray upon deleting which the sum of remaining element will be divisible by p;

Follow up 1: find the number of subarray (need not be minimum) deleting which will result the sum to be divisible by p

Follow up 2: For each index find the number of times it is included in any subarray upon deleting which the remaining sum will be divisible by p

<details><summary>Theory and explanation</summary>

Let **S** = total sum of the array. After deleting subarray `[l..r]`, remaining sum = **S − sum(l..r)**. We need:

```
(S - sum(l..r)) ≡ 0 (mod p)  ⟺  sum(l..r) ≡ S (mod p)
```

Let **target = S mod p**. Find subarrays whose sum modulo **p** equals **target**.

**Prefix sums modulo p**

Define `pref[0] = 0`, `pref[i+1] = (pref[i] + arr[i]) % p`.  
Subarray sum `arr[l..r]` ≡ `(pref[r+1] - pref[l]) mod p`.

Need `(pref[r+1] - pref[l]) % p == target`, i.e.:

```
pref[l] ≡ (pref[r+1] - target) mod p
```

**Minimum length (main problem)**

For each right endpoint `r+1`, look up the **earliest** index `l` with matching `pref[l]`. Length = `(r+1) - l`. Track minimum.

- If **target === 0** and no non-empty subarray needed, answer can be **0** (delete nothing).
- Use hash map `firstSeen[mod] = earliest index`.

**Follow up 1 — count subarrays**

For each `r+1`, add `count[pref[r+1] - target]` to answer (number of valid `l` values). Increment frequency of `pref[r+1]` after processing.

**Follow up 2 — per-index inclusion count**

Index `k` (0-based) lies in deletion subarray `[l..r]` iff `l ≤ k ≤ r`. Count valid `(l,r)` pairs containing `k` where subarray sum ≡ target (mod p).

Fix `k`. Split into:
- `l ≤ k` — choose `l`, derive required `pref[r+1]`.
- `r ≥ k` — choose `r`, derive required `pref[l]`.

Use prefix frequency maps on left/right of `k`, or enumerate one side O(n) per index → O(n²) total (acceptable for interview discussion; O(n) per index with careful counting is possible).

**Complexity**

- Main + follow up 1: **O(n)** time, **O(p)** or **O(n)** map space.
- Follow up 2: **O(n²)** naive; optimized variants O(n log n) or O(n) with advanced techniques.

#### Further reading

- [LeetCode 1546 / similar mod subarray problems](https://leetcode.com/discuss/general-discussion/560043/subarray-sum-equals-k-and-modular-variants) — prefix + hash pattern
- [CP-Algorithms: Modular arithmetic](https://cp-algorithms.com/algebra/module-arithmetic.html) — congruence manipulation
- [GeeksforGeeks: Subarray sum divisible by k](https://www.geeksforgeeks.org/longest-subarray-with-sum-divisible-by-k/) — related mod prefix technique
- [Prefix sum hash map pattern (NeetCode)](https://neetcode.io/) — subarray sum equals K template

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function minSubarrayLenDivisibleRemainder(arr, p) {
  const n = arr.length;
  let total = 0;
  for (const x of arr) total = (total + x) % p;
  const target = total;

  if (target === 0) return 0;

  const first = new Map([[0, 0]]);
  let pref = 0;
  let minLen = Infinity;

  for (let i = 1; i <= n; i++) {
    pref = (pref + arr[i - 1]) % p;
    const need = (pref - target + p) % p;
    if (first.has(need)) minLen = Math.min(minLen, i - first.get(need));
    if (!first.has(pref)) first.set(pref, i);
  }
  return minLen === Infinity ? -1 : minLen;
}

function countValidDeletionSubarrays(arr, p) {
  const n = arr.length;
  let total = 0;
  for (const x of arr) total = (total + x) % p;
  const target = total;

  const freq = new Map([[0, 1]]);
  let pref = 0;
  let count = 0;

  for (let i = 0; i < n; i++) {
    pref = (pref + arr[i]) % p;
    const need = (pref - target + p) % p;
    count += freq.get(need) || 0;
    freq.set(pref, (freq.get(pref) || 0) + 1);
  }
  if (target === 0) count += 1; // empty deletion
  return count;
}

function indexInclusionCounts(arr, p) {
  const n = arr.length;
  let total = 0;
  for (const x of arr) total = (total + x) % p;
  const target = total;
  const counts = Array(n).fill(0);

  for (let l = 0; l < n; l++) {
    let sum = 0;
    for (let r = l; r < n; r++) {
      sum = (sum + arr[r]) % p;
      if (sum === target) {
        for (let k = l; k <= r; k++) counts[k]++;
      }
    }
  }
  return counts;
}

minSubarrayLenDivisibleRemainder([3, 1, 4, 2], 6);
countValidDeletionSubarrays([3, 1, 4, 2], 6);
```

#### Code walkthrough

- Compute **target = total % p** — required subarray sum mod p.
- **`first` map** stores earliest prefix index for each remainder → minimum length.
- **Count variant** uses frequency of prior prefixes instead of earliest index.
- **Follow up 2** naive triple loop marks every index inside valid `[l,r]`; optimize in interview discussion with prefix counts split at `k`.

#### Complexity

| | Main | Count | Per-index (naive) |
|-|-|-|-|
| Time | O(n) | O(n) | O(n³) naive inner; O(n²) with two loops |
| Space | O(min(n,p)) | O(min(n,p)) | O(n) output |

#### Edge cases

- **No valid subarray** — return -1 or Infinity per spec.
- **target === 0** — empty deletion valid; length 0.
- **p === 1** — everything divisible; answer 0.
- **Single element** — check if deleting it makes remainder ≡ 0 mod p.

</details>

</article>

<article>

You are given an array people and an integer limit, where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. 
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

<details><summary>Theory and explanation</summary>

Classic **greedy two-pointer** problem ([LeetCode 881 — Boats to Save People](https://leetcode.com/problems/boats-to-save-people/)).

**Observations**

- Sort `people` ascending.
- Pair **lightest** (`lo`) with **heaviest** (`hi`) when possible — saves boats.
- If `people[lo] + people[hi] <= limit`, both fit in one boat → `lo++`, `hi--`, boats++.
- Else heaviest alone exceeds pairing with lightest → heaviest goes solo → `hi--`, boats++.

**Why greedy works**

Heavy people are the bottleneck. Giving them the lightest available partner never hurts optimality (exchange argument): if heaviest pairs with someone heavier than lightest, lightest still needs a boat eventually and wastes less capacity when paired with heavy.

**Complexity**

- Sort: O(n log n).
- Two pointers: O(n).

#### Further reading

- [LeetCode 881: Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) — official statement
- [Greedy proof discussion (LeetCode)](https://leetcode.com/problems/boats-to-save-people/solutions/) — community proofs
- [CP-Algorithms: Greedy](https://cp-algorithms.com/algorithms/greedy.html) — exchange arguments
- [Visual proof — two pointers pattern](https://leetcode.com/discuss/general-discussion/581884/two-pointer-technique) — template

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function numRescueBoats(people, limit) {
  people.sort((a, b) => a - b);
  let lo = 0;
  let hi = people.length - 1;
  let boats = 0;

  while (lo <= hi) {
    if (people[lo] + people[hi] <= limit) lo++;
    hi--;
    boats++;
  }
  return boats;
}

numRescueBoats([1, 2], 3);           // 1
numRescueBoats([3, 2, 2, 1], 3);     // 3
numRescueBoats([3, 5, 3, 4], 5);     // 4
```

#### Code walkthrough

1. **Sort** ascending.
2. While `lo <= hi`, attempt to pair lightest with heaviest.
3. If sum ≤ limit, advance `lo` (both aboard); always decrement `hi` (heaviest handled).
4. Each iteration uses one boat.

#### Complexity

| | |
|-|-|
| Time | O(n log n) — dominated by sort |
| Space | O(1) extra if sorting in place |

#### Edge cases

- **One person** — one boat.
- **All equal at limit** — each person alone if weight = limit and can't pair.
- **Lightest + heaviest > limit** — heaviest goes alone (`hi--` only).

</details>

</article>

<article>

Given an array of n colored balls. And some boxes. Each box has some capacity and each box must contain balls of same color. What is the maximum number of balls that the boxes can carry?
Constraint: max capacity of box - min capacity of box <= 1

<details><summary>Theory and explanation</summary>

**Problem model**

- `balls` — array of length `n` where `balls[i]` is a **color id** (or count per color if given as frequency map).
- `boxes` — array of **capacities**; each box holds **one color only**.
- **Constraint**: `max(box) - min(box) ≤ 1` → every capacity is `C` or `C+1` for some integer `C`.

**Goal**: maximize total balls placed — assign colors to boxes respecting capacity and single-color rule.

**Greedy strategy**

1. **Count** balls per color → frequency array `freq`.
2. **Sort** `freq` descending (use most common colors first).
3. **Sort** box capacities descending (fill largest boxes first).
4. For each box in sorted order, take the color with largest remaining count; place `min(remaining[color], capacity)` balls; decrease remaining.

**Why sort both sides**

Matching largest demand (color count) to largest supply (box capacity) is a standard greedy for maximum bipartite matching when boxes differ by at most 1 — capacities are nearly uniform so heavy colors should not be starved by small boxes early.

**Variant clarification**

If input is **ball counts per color** already aggregated, skip step 1. If boxes outnumber colors, excess boxes stay empty.

#### Further reading

- [Greedy assignment — matching intuition](https://cp-algorithms.com/algorithms/greedy.html) — scheduling resources
- [LeetCode 1648 (similar capacity theme)](https://leetcode.com/discuss/) — frequency + capacity problems
- [Bin packing overview](https://en.wikipedia.org/wiki/Bin_packing_problem) — NP-hard general case; this constraint simplifies
- [Hash map frequency counting (MDN)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) — color counts in JS

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function maxBallsPacked(balls, boxCapacities) {
  const freq = new Map();
  for (const color of balls) {
    freq.set(color, (freq.get(color) || 0) + 1);
  }

  const colorCounts = [...freq.values()].sort((a, b) => b - a);
  const boxes = boxCapacities.slice().sort((a, b) => b - a);

  let total = 0;
  let ci = 0;

  for (const cap of boxes) {
    if (ci >= colorCounts.length) break;
    const placed = Math.min(colorCounts[ci], cap);
    total += placed;
    colorCounts[ci] -= placed;
    if (colorCounts[ci] === 0) ci++;
  }
  return total;
}

maxBallsPacked(
  ['r', 'r', 'r', 'g', 'g', 'b'],
  [3, 3, 2] // capacities differ by at most 1
); // 6 if enough box space for all colors optimally
```

#### Code walkthrough

1. **`freq`** — tally balls per color.
2. Sort color remainders **descending**, box caps **descending**.
3. Each box: fill from current dominant color up to capacity; advance color when exhausted.

#### Complexity

| | |
|-|-|
| Time | O(n + m log m + k log k) — n balls, m boxes, k distinct colors |
| Space | O(k) for frequency map |

#### Edge cases

- **More boxes than colors** — extra boxes unused.
- **Capacity 0** — skip or place nothing.
- **All one color** — first boxes absorb until balls or boxes exhausted.
- **Constraint validation** — if max−min > 1, greedy may need different strategy; problem guarantees ≤ 1.

</details>

</article>

<article>

Given an array of n integers.Find max subarray sum with at most one delete.

<details><summary>Theory and explanation</summary>

Find maximum sum of a **contiguous subarray** after deleting **at most one** element (delete 0 or 1 element from the chosen segment, or delete one element globally — typical interpretation: remove **one** element from the array, then take max subarray sum on what remains).

**Standard interpretation (LeetCode-style)**

Allow **one skip** while computing max subarray sum (generalized Kadane):

- **`kadaneNoDelete`** — normal max subarray ending here.
- Track **`kadaneOneDelete`** — best sum ending here having used one deletion.
- Transition: extend previous states or start fresh.

**Alternative DP (prefix/suffix split)**

- `left[i]` — max subarray sum ending at or before `i` (no delete).
- `right[i]` — max subarray sum starting at or after `i`.
- Answer = max over split `left[i-1] + right[i+1]` (delete element `i`) and `kadane(all)` (delete none).

**Complexity**: O(n) time, O(n) space (or O(1) with rolling Kadane variant).

#### Further reading

- [LeetCode 1186: Maximum Subarray Sum with One Deletion](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/) — canonical problem
- [Kadane's algorithm (CP-Algorithms)](https://cp-algorithms.com/sequences/kadane-algorithm.html) — base case
- [GeeksforGeeks: Max subarray one deletion](https://www.geeksforgeeks.org/maximum-sum-subarray-removing-one-element/) — prefix/suffix method
- [Dynamic programming on arrays](https://usaco.guide/CPH/) — state machine view

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function maximumSumWithOneDeletion(arr) {
  let noDel = arr[0];
  let oneDel = 0;
  let best = arr[0];

  for (let i = 1; i < arr.length; i++) {
    oneDel = Math.max(noDel, oneDel + arr[i]); // delete current or earlier
    noDel = Math.max(arr[i], noDel + arr[i]);
    best = Math.max(best, noDel, oneDel);
  }
  return best;
}

// Prefix / suffix variant (clearer for interviews)
function maximumSumWithOneDeletionSplit(arr) {
  const n = arr.length;
  const left = Array(n).fill(0);
  const right = Array(n).fill(0);

  left[0] = arr[0];
  for (let i = 1; i < n; i++) {
    left[i] = Math.max(arr[i], left[i - 1] + arr[i]);
  }
  right[n - 1] = arr[n - 1];
  for (let i = n - 2; i >= 0; i--) {
    right[i] = Math.max(arr[i], right[i + 1] + arr[i]);
  }

  let best = left[n - 1];
  for (let i = 1; i < n - 1; i++) {
    best = Math.max(best, left[i - 1] + right[i + 1]);
  }
  return best;
}

maximumSumWithOneDeletion([1, -2, 0, 3]); // 4
maximumSumWithOneDeletion([-1, -1, -1]);  // -1
```

#### Code walkthrough

- **`noDel`** — Kadane best ending at `i` without deletion used.
- **`oneDel`** — best ending at `i` after exactly one deletion somewhere in segment.
- **Split method** — delete `i` by joining best left subarray before `i` with best right after `i`.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(1) Kadane variant; O(n) split variant |

#### Edge cases

- **All negative** — best single element (one deletion may not help).
- **Length 1** — return sole element.
- **Deleting outside subarray** — equivalent to one skip inside max subarray path.

</details>

</article>

<article>

Given an array of n integers. Find the number of subarrays where the maximum element is between x and y

<details><summary>Theory and explanation</summary>

Count subarrays where **x ≤ max(subarray) ≤ y**.

**Inclusion–exclusion on “max ≤ M”**

Let **F(M)** = number of subarrays whose maximum **≤ M**.

Subarrays with max **≤ M** are formed within segments between elements **> M**; a segment of length `L` contributes `L(L+1)/2` subarrays.

Then:

```
answer = F(y) - F(x - 1)
```

**Why this works**

- `F(y)` counts subarrays with all elements ≤ y (max ≤ y).
- Subtract those with max ≤ x−1 (equivalently all elements ≤ x−1).
- Remaining subarrays have max ≥ x and ≤ y.

**Algorithm**

```
function countAtMost(arr, M):
  total = 0, len = 0
  for v in arr:
    if v > M: len = 0
    else: len++; total += len
  return total
```

**Complexity**: O(n) per query on M; O(n) overall for one (x, y) pair.

#### Further reading

- [LeetCode 795: Number of Subarrays with Bounded Maximum](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/) — same technique
- [AtCoder / CF subarray counting tricks](https://cp-algorithms.com/sequences/rmq-computation.html) — monotonic stack variants
- [GeeksforGeeks: Count subarrays with max in range](https://www.geeksforgeeks.org/) — two-pointer related
- [Prefix counting subarrays formula](https://math.stackexchange.com/) — L(L+1)/2 in segments

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function countSubarraysWithMaxAtMost(arr, M) {
  let total = 0;
  let len = 0;
  for (const v of arr) {
    if (v > M) len = 0;
    else {
      len++;
      total += len;
    }
  }
  return total;
}

function countSubarraysMaxInRange(arr, x, y) {
  return countSubarraysWithMaxAtMost(arr, y) - countSubarraysWithMaxAtMost(arr, x - 1);
}

countSubarraysMaxInRange([1, 2, 3, 4], 2, 3); // subarrays whose max is 2 or 3
countSubarraysWithMaxAtMost([2, 2, 2], 2);      // 6
```

#### Code walkthrough

- **`countSubarraysWithMaxAtMost`** — extend run length while elements ≤ M; each new ending position adds `len` subarrays ending at this index.
- **Range count** — subtract counts for max ≤ x−1 from max ≤ y.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases

- **x > y** — return 0.
- **All elements > y** — return 0.
- **x ≤ min(arr) and y ≥ max(arr)** — all n(n+1)/2 subarrays if max in range.
- **Negative x** — adjust if problem allows negative values.

</details>

</article>

## Technical Round Questions
<article>

Suppose you want to update value of a field in a database. Generally, a read operation is done to fetch the value. Based on the retrieved value some logic is applies and the result is updated in the field. Example, subtract from balance if the balance is more than some threshold. Another client in the meantime can update the field too thus resulting unexpected behaviour. How can this be solved?

<details><summary>Theory and explanation</summary>

This is the classic **read-modify-write race** (lost update). Two transactions interleave:

```
A: read balance = 100
B: read balance = 100
A: write balance = 100 - 30 = 70
B: write balance = 100 - 20 = 80   // overwrites A; lost 30 deduction
```

**Solutions (increasing robustness)**

1. **Atomic single-statement update (preferred)**

   ```sql
   UPDATE accounts
   SET balance = balance - 30
   WHERE id = ? AND balance > threshold;
   ```

   Database executes atomically; no separate read in app code.

2. **Optimistic concurrency control (OCC)**

   Add `version` column; read `(balance, version)`; update only if version unchanged:

   ```sql
   UPDATE accounts SET balance = ?, version = version + 1
   WHERE id = ? AND version = ?;
   ```

   Retry on 0 rows affected.

3. **Pessimistic locking**

   `SELECT balance FROM accounts WHERE id = ? FOR UPDATE` in a transaction — blocks other writers until commit.

4. **Serializable isolation** — DB guarantees no anomalies; may cost throughput.

5. **Stored procedure / DB-side logic** — same atomicity as (1), logic centralized.

6. **Application distributed lock** (Redis Redlock) — last resort for multi-service; easy to get wrong.

**Priyo finance context**

Money movement demands **atomic debit/credit**, idempotency keys, and audit logs. Never implement balance changes with read-then-write in application code without versioning or locking.

#### Further reading

- [PostgreSQL: Transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — anomaly definitions
- [MySQL: InnoDB locking reads](https://dev.mysql.com/doc/refman/8.0/en/innodb-locking-reads.html) — `FOR UPDATE`
- [Martin Kleppmann: Designing Data-Intensive Applications](https://dataintensive.net/) — concurrency chapter
- [AWS: Idempotency keys for payments](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) — fintech pattern

</details>

<details><summary>Solution (JavaScript)</summary>

Illustrative **optimistic retry** in Node with parameterized SQL (pseudo-ORM):

```js
async function deductBalance(db, accountId, amount, threshold) {
  for (let attempt = 0; attempt < 5; attempt++) {
    const row = await db.query(
      'SELECT balance, version FROM accounts WHERE id = $1',
      [accountId]
    );
    if (!row || row.balance <= threshold) return { ok: false, reason: 'threshold' };

    const newBalance = row.balance - amount;
    const result = await db.query(
      `UPDATE accounts
       SET balance = $1, version = version + 1
       WHERE id = $2 AND version = $3 AND balance > $4`,
      [newBalance, accountId, row.version, threshold]
    );
    if (result.rowCount === 1) return { ok: true, balance: newBalance };
    // version conflict — retry
  }
  throw new Error('Concurrent update; retry exhausted');
}

// Best: one atomic statement — no read in app
async function deductBalanceAtomic(db, accountId, amount, threshold) {
  const result = await db.query(
    `UPDATE accounts
     SET balance = balance - $1
     WHERE id = $2 AND balance > $3
     RETURNING balance`,
    [amount, accountId, threshold]
  );
  return result.rows[0] ?? null;
}
```

#### Code walkthrough

- **Optimistic path** — read version, compute new balance, conditional update; retry on conflict.
- **Atomic path** — single `UPDATE` with `balance - amount` in SQL — no lost update.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual); O(1) DB round-trips per attempt |
| Space | N/A (conceptual) |

#### Edge cases

- **Retry storms** — cap retries; exponential backoff.
- **Double spend** — combine with idempotency key on transaction id.
- **Read replica lag** — do not read balance from stale replica before write.

</details>

<details><summary>Solution (other languages)</summary>

There can be multiple approach to solve this problem.  

1. Complete the whole scenario in one query. 
1. Use stored procedure
1. Use locks. Add an extra column for the purpose of locking. Before fetching a data for update, set the said lock to 1. If it is already 1 then don't proceed.

</details>
</article>

<article>

How authentication is done in microservice based applications?

<details><summary>Theory and explanation</summary>

Microservices split auth into **identity issuance** (who you are) and **per-service authorization** (what you may do). Common patterns:

**1. Centralized identity provider (IdP)**

- **OAuth 2.0 / OpenID Connect (OIDC)** — user logs in at Auth0, Keycloak, Cognito, or corporate IdP; receives **access token** (API) and **ID token** (profile).
- **JWT** — signed claims (`sub`, `exp`, `roles`); services verify signature with IdP public key (**JWKS**).

**2. Token validation at the edge**

- **API Gateway** validates JWT once; forwards trusted headers (`X-User-Id`, scopes) to internal services.
- Internal network may use **mTLS** so only gateway calls services.

**3. Service-to-service auth**

- **Client credentials** flow for machine clients.
- **Short-lived tokens** exchanged from long-lived secrets.
- **SPIFFE/SPIRE** workload identity in Kubernetes.

**4. Session vs stateless**

- **Stateless JWT** — scalable; revocation hard (short TTL + refresh tokens).
- **Session store** (Redis) — central revoke; extra hop.

**5. Authorization layers**

- **RBAC** — roles → permissions.
- **ABAC** — policy on attributes (tenant, resource owner).
- **OPA / policy engine** — centralized policy decisions.

**Priyo / fintech notes**

- MFA, device binding, audit trail.
- Never pass raw passwords between services.
- **Zero trust** — validate every call, even internal.

#### Further reading

- [OAuth 2.0 RFC 6749](https://dataclass.net/rfc/6749/) — flows and tokens
- [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html) — ID token standard
- [Microservices.io: Access token pattern](https://microservices.io/patterns/security/access-token.html) — architecture pattern
- [Auth0: Zero trust architecture](https://auth0.com/docs/secure/zero-trust) — modern microservice auth
- [NIST SP 800-207 Zero Trust](https://csrc.nist.gov/publications/detail/sp/800-207/final) — framework reference

</details>

<details><summary>Solution (JavaScript)</summary>

Gateway middleware verifying JWT and attaching user context (Node + `jose` style):

```js
import { createRemoteJWKSet, jwtVerify } from 'jose';

const JWKS = createRemoteJWKSet(new URL('https://idp.priyo.com/.well-known/jwks.json'));

async function authMiddleware(req, res, next) {
  const header = req.headers.authorization || '';
  const token = header.startsWith('Bearer ') ? header.slice(7) : null;
  if (!token) return res.status(401).json({ error: 'missing_token' });

  try {
    const { payload } = await jwtVerify(token, JWKS, {
      issuer: 'https://idp.priyo.com',
      audience: 'priyo-api',
    });
    req.user = { id: payload.sub, roles: payload.roles || [] };
    next();
  } catch {
    return res.status(401).json({ error: 'invalid_token' });
  }
}

function requireRole(role) {
  return (req, res, next) => {
    if (!req.user?.roles?.includes(role)) {
      return res.status(403).json({ error: 'forbidden' });
    }
    next();
  };
}

// Service-to-service: client credentials (outline)
async function getServiceToken(clientId, clientSecret) {
  const body = new URLSearchParams({
    grant_type: 'client_credentials',
    client_id: clientId,
    client_secret: clientSecret,
    audience: 'priyo-internal',
  });
  const res = await fetch('https://idp.priyo.com/oauth/token', {
    method: 'POST',
    body,
  });
  const json = await res.json();
  return json.access_token;
}
```

#### Code walkthrough

- **`jwtVerify`** — validates signature, expiry, issuer, audience against IdP JWKS.
- **`req.user`** — downstream microservices trust gateway or re-verify token.
- **`requireRole`** — RBAC at route level.
- **Client credentials** — machine-to-machine without user context.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual); JWT verify O(1) crypto per request |
| Space | N/A (conceptual); JWKS cached at gateway |

#### Edge cases

- **Expired token** — 401; client refreshes with refresh token.
- **Revoked user** — short TTL + token introspection endpoint or session blacklist.
- **Clock skew** — allow small `leeway` in JWT verify.
- **Token in URL** — avoid; use Authorization header only.

</details>

</article>

