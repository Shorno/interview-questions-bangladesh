---
description: ShellBeeHaken interview questions, ShellBeeHaken interview stages, ShellBeeHaken interview details, ShellBeeHaken interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/shellbeehaken
---
# ShellBeeHaken Limited

|                   |                                   |
| :---------------- | :-------------------------------- |
| Founding year     | 2020                              |
| Company Website   | https://shellbeehaken.com/        |
| Career Website    | https://shellbeehaken.com/join-us |
| Technologies Used |                                   |

## Introduction
ShellBeeHaken is a dev shop that specializes in customized software solutions development. As a product-based company, we have a unique customer-centric task management philosophy. We take pride in working with individuals who share similar ideologies with us. Within a short time, we were able to produce software for world-famous brands like Toyota, Fujitsu, Nagase, N-village, CCC, etc. Now we are working on a couple of SaaS-based exciting startup products. We have a perpetual startup spirit that differentiates us from others.

## Interview Stages:

ShellBeeHaken interviews generally involve multiple rounds for Associate Software Engineer
1. **Written Test**:	In-person at ShellBeeHaken office
2. **On-site Interview**:   2 technical rounds, 1 behavioral round
3. **Offer**:	Salary negotiations and offer

## Topics:

- Programming Fundamentals
- Data Structures and Algorithms
- Object Oriented Programming
- Object Oriented Design
- Database
- Software Engineering

## Questions
Questions from the written exam took place on 12 September 2025 

<article>

Given a string of lowercase letters, you have to find the longest mirror substring from it. The string `radar` or `racecar` is not mirror but `bid` or `dib` is. For simplicity lets say `b=d,i=i,o=o,w=w,v=v,x=x,p=q` in the mirrored substring.

<details><summary>Theory and explanation</summary>

A **mirror substring** is **not** a palindrome. In a palindrome, `s[i] === s[j]` when `i` and `j` are symmetric. Here, symmetric positions must hold **mirror partners** under a fixed map:

| char | mirrors to |
|------|------------|
| b | d |
| d | b |
| p | q |
| q | p |
| i, o, w, v, x | themselves |

For substring `s` of length `m`, for every index `i` in `0 … m-1`:

`mirror(s[i]) === s[m - 1 - i]`

**Examples**

- `bid` → positions `(b,d)`, `(i,i)`, `(d,b)` ✓
- `radar` → `r` has no mirror partner in the rules ✗
- `racecar` → `r`, `c`, `e` are not in the mirror alphabet ✗

**Algorithm (center expansion)**

Same skeleton as “longest palindromic substring,” but compare **mirror partners** instead of equality. For each center (odd length at `i`, even length between `i` and `i+1`), expand outward while the mirror rule holds. Track the longest valid window.

**Interview talking points**

- Clarify the mirror map up front; write a `mirror(c)` helper.
- Brute force all `O(n³)` substrings is acceptable for small `n`; expansion is `O(n²)`.
- Mention that only characters in the map can appear in a mirror substring of length &gt; 1.

#### Further reading

- [GeeksforGeeks: Longest Palindromic Substring](https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/) — same expansion technique, different compare
- [LeetCode: Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) — practice center expansion
- [CP-Algorithms: Manacher's algorithm](https://cp-algorithms.com/string/manacher.html) — linear-time variant for palindromes (optional optimization)
- [MDN: String slice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice) — substring extraction in JS

</details>

<details><summary>Solution (JavaScript)</summary>

```js
const MIRROR = {
  b: 'd', d: 'b', p: 'q', q: 'p',
  i: 'i', o: 'o', w: 'w', v: 'v', x: 'x',
};

function mirror(ch) {
  return MIRROR[ch] ?? null;
}

function expand(s, left, right) {
  while (left >= 0 && right < s.length) {
    const a = s[left];
    const b = s[right];
    if (!mirror(a) || mirror(a) !== b) break;
    left--;
    right++;
  }
  return s.slice(left + 1, right);
}

function longestMirrorSubstring(s) {
  let best = '';
  for (let i = 0; i < s.length; i++) {
    const odd = expand(s, i, i);
    const even = expand(s, i, i + 1);
    for (const cand of [odd, even]) {
      if (cand.length > best.length) best = cand;
    }
  }
  return best;
}
```

#### Code walkthrough

- **`mirror(ch)`** — returns the partner character or `null` if `ch` is outside the mirror alphabet.
- **`expand`** — moves `left`/`right` outward while mirror symmetry holds, then returns the substring inside the final bounds.
- **Two centers per index** — odd-length substrings center on one character; even-length center between `i` and `i+1`.
- **`longestMirrorSubstring`** — keeps the longest candidate over all centers.

#### Complexity

| | |
|-|-|
| Time | O(n²) — each center expansion is O(n), `n` centers |
| Space | O(1) extra beyond the output string |

#### Edge cases

- **Empty string** — return `''`.
- **Single mirrorable char** — e.g. `"i"` is valid length 1.
- **No mirror pair in string** — longest may be a single self-mirror char (`i`, `o`, …).
- **Characters outside map** — break expansion; they cannot belong to a mirror substring longer than 1 unless alone.

</details>

</article>

<article>

There is an array of numbers `n`. You have to merge any two neighboring elements to make the length of the array `n-1` in such way that, the minimum of the maximum of each consecutive pair gets removed. If the array is `{ 2, 5, 3, 7, 9 }`, the result can be `{ 7, 3, 7, 9 }` or `{ 2, 8, 7, 9 }`

<details><summary>Theory and explanation</summary>

You perform **exactly one merge**: pick adjacent indices `i` and `i+1`, replace them with their **sum** `arr[i] + arr[i+1]`, and remove the two original cells.

Among all adjacent pairs, compute `max(arr[i], arr[i+1])`. The pair you merge must have the **smallest** such value — that is the “minimum of the maximum of each consecutive pair” that gets **removed** from consideration when you collapse the pair.

For `{2, 5, 3, 7, 9}`:

| adjacent pair | max |
|---------------|-----|
| (2, 5) | 5 |
| (5, 3) | 5 |
| (3, 7) | 7 |
| (7, 9) | 9 |

Minimum max is **5** → merge `(2,5)` → `{7,3,7,9}` **or** merge `(5,3)` → `{2,8,7,9}`.

**Interview talking points**

- Scan adjacent pairs once; track minimum `max` and all indices achieving it.
- If multiple pairs tie (here both max = 5), either valid merge is accepted.
- Do not confuse with “merge until one element remains” — only one step is required.

#### Further reading

- [GeeksforGeeks: Minimum adjacent pair sum](https://www.geeksforgeeks.org/minimum-sum-of-adjacent-elements/) — adjacent pair reasoning
- [LeetCode discussion: Array merge greedy](https://leetcode.com/discuss/) — similar local-choice patterns
- [MDN: Array splice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice) — in-place merge in JS

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function mergeNeighborsOnce(arr) {
  if (arr.length < 2) return [...arr];

  let minPairMax = Infinity;
  const candidates = [];

  for (let i = 0; i < arr.length - 1; i++) {
    const pairMax = Math.max(arr[i], arr[i + 1]);
    if (pairMax < minPairMax) {
      minPairMax = pairMax;
      candidates.length = 0;
      candidates.push(i);
    } else if (pairMax === minPairMax) {
      candidates.push(i);
    }
  }

  // Example uses first optimal merge; any index in candidates is valid.
  const i = candidates[0];
  const result = [...arr];
  const merged = result[i] + result[i + 1];
  result.splice(i, 2, merged);
  return result;
}
```

#### Code walkthrough

- **Scan pairs** — compute `max(left, right)` for each consecutive pair.
- **Track minimum** — store every starting index `i` that achieves the global minimum pair-max.
- **Merge** — replace `arr[i]` and `arr[i+1]` with their sum via `splice`.

#### Complexity

| | |
|-|-|
| Time | O(n) — one pass over adjacent pairs |
| Space | O(n) — copy of the array for the result |

#### Edge cases

- **Length 0 or 1** — return unchanged (no merge possible).
- **Tie on min pair-max** — multiple correct outputs; return any or list all for tests.
- **Negative numbers** — `max` and sum still work; clarify with interviewer if needed.

</details>

</article>

<article>

Write the shortest path of the scenario graph. (The scenario included undirected graph with cycles)

<details><summary>Theory and explanation</summary>

For an **undirected graph with cycles**, an unweighted **shortest path** between two nodes is found with **BFS** (breadth-first search). BFS explores layer by layer from the source; the first time you reach the target, you have the minimum number of edges.

**Steps**

1. Build an adjacency list (each undirected edge appears in both directions).
2. BFS queue stores `(node, distance)` or parent pointers for path reconstruction.
3. Mark visited nodes to avoid infinite loops on cycles.
4. When the target is dequeued, reconstruct the path via `parent[]` or stop if only distance is required.

**Why not DFS?** DFS does not guarantee shortest edge-count path in general graphs.

**Dijkstra** is only needed when edges have **non-negative weights**; for unit-weight edges, BFS is optimal.

**Interview talking points**

- State “undirected + unweighted → BFS.”
- Cycles are handled by the `visited` set.
- Mention disconnected graphs: return no path or `-1`.

#### Further reading

- [CP-Algorithms: BFS](https://cp-algorithms.com/graph/breadth-first-search.html) — shortest paths in unweighted graphs
- [GeeksforGeeks: Shortest path in undirected graph](https://www.geeksforgeeks.org/shortest-path-in-an-unweighted-graph/) — BFS walkthrough
- [VisuAlgo: BFS](https://visualgo.net/en/bfs) — interactive visualization
- [LeetCode: Word Ladder](https://leetcode.com/problems/word-ladder/) — BFS on implicit graphs

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function shortestPathUndirected(n, edges, start, goal) {
  const adj = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) {
    adj[u].push(v);
    adj[v].push(u);
  }

  if (start === goal) return [start];

  const visited = new Set([start]);
  const parent = new Map([[start, null]]);
  const queue = [start];

  while (queue.length) {
    const node = queue.shift();
    for (const nei of adj[node]) {
      if (visited.has(nei)) continue;
      visited.add(nei);
      parent.set(nei, node);
      if (nei === goal) {
        const path = [];
        for (let cur = goal; cur != null; cur = parent.get(cur)) path.push(cur);
        return path.reverse();
      }
      queue.push(nei);
    }
  }

  return []; // disconnected
}
```

#### Code walkthrough

- **Adjacency list** — undirected edges added both ways.
- **BFS** — `queue` processes nodes in increasing distance from `start`.
- **`parent` map** — records first predecessor for path reconstruction.
- **Early exit** — when `goal` is first visited, rebuild path from `goal` back to `start`.

#### Complexity

| | |
|-|-|
| Time | O(V + E) |
| Space | O(V) for queue, visited, and parent |

#### Edge cases

- **Start equals goal** — path `[start]`.
- **Disconnected** — return `[]` or `null` per problem spec.
- **Multiple shortest paths** — BFS returns one valid shortest path; any is usually acceptable.

</details>

</article>

<article>

Create a data structure `uniqueQueue` where you can get the kth last element of the queue by using `get(k)` method and push `n` if it is not in the queue using `push(n)` method.

Example: 
```python
push(11)
push(22)
push(33)
get(1) # returns 33
push(22)
get(2) # returns 22
```

<details><summary>Theory and explanation</summary>

Requirements:

- **`push(n)`** — append `n` only if it is **not already** in the queue (duplicates ignored).
- **`get(k)`** — return the **k-th element from the back** (`k = 1` is the most recently pushed element still in the queue).

From the example, front-to-back order is `11 → 22 → 33`. `get(1) = 33`, `get(2) = 22`. After `push(22)` (duplicate), order unchanged.

**Implementation**

- `queue` — array (or linked list) preserving FIFO order among unique values.
- `Set` — O(1) membership for duplicate checks.
- `get(k)` — index `queue.length - k` (validate `1 ≤ k ≤ size`).

**Interview talking points**

- Duplicate `push` is a no-op, not a move-to-back (unless interviewer says otherwise — confirm).
- `get(k)` is O(1) with array indexing; `push` is O(1) amortized with `Set`.
- Contrast with standard `Queue` (no uniqueness, no random access from rear).

#### Further reading

- [LeetCode: Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) — queue API design
- [MDN: Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) — O(1) membership
- [GeeksforGeeks: Queue using Stacks](https://www.geeksforgeeks.org/queue-using-stacks/) — classic queue variants

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class UniqueQueue {
  constructor() {
    this.queue = [];
    this.seen = new Set();
  }

  push(n) {
    if (this.seen.has(n)) return false;
    this.seen.add(n);
    this.queue.push(n);
    return true;
  }

  get(k) {
    if (k < 1 || k > this.queue.length) {
      throw new RangeError('k out of range');
    }
    return this.queue[this.queue.length - k];
  }

  size() {
    return this.queue.length;
  }
}
```

#### Code walkthrough

- **`seen`** — blocks duplicate inserts before they reach `queue`.
- **`push`** — returns `false` on duplicate so callers can distinguish no-op.
- **`get(k)`** — `k=1` maps to last index `length - 1` (most recent unique element).

#### Complexity

| | |
|-|-|
| `push` | O(1) average time, O(1) extra space per element |
| `get` | O(1) time |
| Space | O(n) for `n` unique stored values |

#### Edge cases

- **`get` with invalid k** — throw or return `undefined`; document choice.
- **`push` duplicate** — no structural change.
- **Large k** — same bounds check as empty queue.

</details>

</article>

<article>

You are designing a ride sharing app where you can take multiple passenger in specific destination. Given a set of trip data as tuples `{ pickup_time, drop_time, passenger_count }`. You have to return the number of total trips taken maximizing the passenger count.

Example Input: `[(0,30,5),(5,10,2),(15,20,2)]` 

Exmaple Output: `1`

<details><summary>Theory and explanation</summary>

Each tuple `(start, end, passengers)` is a trip interval. Trips that **overlap in time** cannot both be taken on one vehicle (only one active route at a time).

**Goal (per sample output `1`)** — among all **non-overlapping** subsets of trips, pick a subset with **maximum total passengers**; return the **count of trips** in that optimal subset. For the sample, the best single trip is `(0,30,5)` with 5 passengers; two non-overlapping small trips sum to 4, so optimum is **one trip** → output `1`.

This is **weighted interval scheduling**:

1. Sort trips by **end time**.
2. `dp[i]` = max passengers using trips among the first `i` sorted trips.
3. For trip `i`, either skip it or take it plus `dp[p(i)]` where `p(i)` is the last trip that ends before `i` starts (binary search).

**Interview talking points**

- Clarify overlap: `[5,10)` overlaps `[0,30)` but `[5,10)` and `[15,20)` do not.
- Greedy by earliest finish works for **count** of intervals, not for **weighted** passengers — use DP.
- If they ask for the schedule itself, backtrack from `dp`.

#### Further reading

- [GeeksforGeeks: Weighted Job Scheduling](https://www.geeksforgeeks.org/weighted-job-scheduling-log-n-time/) — same DP pattern
- [LeetCode: Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) — weighted intervals
- [CP-Algorithms: Scheduling jobs](https://cp-algorithms.com/algebra/scheduling.html) — theory and DP
- [MIT 6.006: Weighted interval scheduling](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — lecture notes

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function maxPassengerTripCount(trips) {
  if (!trips.length) return 0;

  const sorted = [...trips].sort((a, b) => a[1] - b[1]);
  const n = sorted.length;
  const ends = sorted.map((t) => t[1]);

  function lastNonOverlapping(i) {
    const start = sorted[i][0];
    let lo = 0;
    let hi = i - 1;
    let ans = -1;
    while (lo <= hi) {
      const mid = (lo + hi) >> 1;
      if (ends[mid] <= start) {
        ans = mid;
        lo = mid + 1;
      } else {
        hi = mid - 1;
      }
    }
    return ans;
  }

  const dp = Array(n).fill(0);
  const takeCount = Array(n).fill(0);

  for (let i = 0; i < n; i++) {
    const [, , w] = sorted[i];
    const j = lastNonOverlapping(i);
    const with = w + (j >= 0 ? dp[j] : 0);
    const without = i > 0 ? dp[i - 1] : 0;

    if (with >= without) {
      dp[i] = with;
      takeCount[i] = 1 + (j >= 0 ? takeCount[j] : 0);
    } else {
      dp[i] = without;
      takeCount[i] = i > 0 ? takeCount[i - 1] : 0;
    }
  }

  return takeCount[n - 1];
}
```

#### Code walkthrough

- **Sort by end time** — enables “last compatible trip” binary search.
- **`lastNonOverlapping(i)`** — largest index `j < i` with `end[j] ≤ start[i]`.
- **`dp[i]`** — best total passengers using trips `0..i`.
- **`takeCount[i]`** — number of trips in that optimal solution (for the required output).

#### Complexity

| | |
|-|-|
| Time | O(n log n) — sort + `n` binary searches |
| Space | O(n) |

#### Edge cases

- **Empty input** — return `0`.
- **All overlapping** — answer is one trip with max `passengers`.
- **All disjoint** — can sum all trips; count equals `n`.
- **Tie weights** — any optimal subset count is fine if multiple exist.

</details>

</article>

<article>

A SQL query was given to perform with a subquery and a JOIN operation.

<details><summary>Theory and explanation</summary>

Written tests often show a **schema** (e.g. `employees`, `departments`, `orders`) and ask for rows that need **JOIN** plus a **subquery** (filter, aggregate, or derived table).

**Typical patterns**

1. **JOIN + scalar subquery** — e.g. employees earning more than their department average:
   - Inner query: `AVG(salary) GROUP BY dept_id`
   - Outer: join employee to dept aggregate and filter `salary > avg_salary`

2. **JOIN + `IN` / `EXISTS` subquery** — e.g. customers who placed orders in the last 30 days:
   - `WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id AND o.order_date >= …)`

3. **Derived table (subquery in FROM)** — compute aggregates first, then join:
   - `SELECT * FROM t JOIN (SELECT id, COUNT(*) cnt FROM … GROUP BY id) s ON …`

**Interview talking points**

- Draw table relationships before writing SQL.
- Prefer `EXISTS` over `IN` for large correlated sets when appropriate.
- Name columns explicitly; avoid `SELECT *` in production-style answers.
- Mention indexes on join keys (`dept_id`, `customer_id`).

#### Further reading

- [SQLBolt: Subqueries](https://sqlbolt.com/lesson/select_queries_subqueries) — nested SELECT practice
- [W3Schools SQL JOIN](https://www.w3schools.com/sql/sql_join.asp) — join types reference
- [PostgreSQL: Subquery expressions](https://www.postgresql.org/docs/current/functions-subquery.html) — `EXISTS`, `IN`, derived tables
- [Use The Index, Luke: Joins](https://use-the-index-luke.com/sql/join) — performance mindset

</details>

<details><summary>Solution (JavaScript)</summary>

SQL is not executed in JavaScript for this question; use a **template** you adapt to the schema on the exam paper:

```sql
-- Pattern: employees earning above department average (JOIN + subquery)
SELECT e.employee_id, e.name, e.salary, d.dept_name
FROM employees e
JOIN departments d ON d.dept_id = e.dept_id
JOIN (
  SELECT dept_id, AVG(salary) AS avg_salary
  FROM employees
  GROUP BY dept_id
) dept_avg ON dept_avg.dept_id = e.dept_id
WHERE e.salary > dept_avg.avg_salary;
```

```sql
-- Pattern: EXISTS instead of IN
SELECT c.customer_id, c.name
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.customer_id
    AND o.order_date >= CURRENT_DATE - INTERVAL '30 days'
);
```

#### Code walkthrough

- **Derived table `dept_avg`** — aggregates once per department; outer query compares row-level salary.
- **`JOIN departments`** — adds denormalized labels the question may require.
- **`EXISTS`** — stops at first matching order; often clearer than `IN (SELECT …)` for correlation.

#### Complexity

| | |
|-|-|
| Time | Depends on DB engine, indexes, and row counts (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases

- **NULL salaries** — `AVG` ignores NULLs; clarify `WHERE salary IS NOT NULL`.
- **Employees with no department** — use `LEFT JOIN` if orphans must appear.
- **Duplicate rows from JOIN** — use `DISTINCT` or fix join keys.

</details>

</article>

<article>

Draw a class diagram of a course management system

<details><summary>Theory and explanation</summary>

A **course management system** (CMS) tracks users, courses, enrollments, assignments, and grades. Interviewers want a clear **UML class diagram**: entities, associations, multiplicity, and key methods.

**Core classes**

| Class | Responsibility |
|-------|----------------|
| `User` | Base for `Student`, `Instructor` (inheritance) |
| `Course` | `code`, `title`, `credits`, `instructor` |
| `Enrollment` | Links `Student` ↔ `Course`, status, grade |
| `Assignment` | Belongs to `Course`; due date, max points |
| `Submission` | `Student` work for one `Assignment` |

**Relationships**

- `Instructor` **1 — * ** `Course` (teaches)
- `Student` **\* — * ** `Course` through `Enrollment`
- `Course` **1 — * ** `Assignment`
- `Assignment` **1 — * ** `Submission`
- `Student` **1 — * ** `Submission`

**Methods (examples)**

- `Course.addStudent(student)`
- `Enrollment.drop()`
- `Assignment.publish()`
- `Submission.grade(score)`

**Interview talking points**

- Use **composition** for parts that cannot exist alone (`Submission` → `Assignment`).
- Show **multiplicity** on associations (`1`, `0..*`, `1..*`).
- Optional: `Department`, `Semester`, `DiscussionForum` if time allows.

#### Further reading

- [UML Class Diagrams — IBM](https://www.ibm.com/topics/uml-class-diagrams) — notation reference
- [Lucidchart: Class diagram tutorial](https://www.lucidchart.com/pages/uml-class-diagram) — drawing guide
- [Martin Fowler: UML Distilled](https://martinfowler.com/books/uml.html) — lightweight modeling
- [Coursera: OOP design for LMS](https://www.coursera.org/articles/object-oriented-programming) — entity brainstorming

</details>

<details><summary>Solution (JavaScript)</summary>

Diagrams are usually on paper; this **textual UML sketch** is what you replicate visually:

```
┌─────────────┐       ┌──────────────┐
│   User      │       │   Course     │
├─────────────┤       ├──────────────┤
│ id, email   │       │ code, title  │
└──────┬──────┘       │ credits      │
       △              └──────┬───────┘
       │                     │ 1
  ┌────┴────┐                │
  │         │                │ *
Student  Instructor          │
       │ 1                  │
       │ *    ┌───────────────┴────────────┐
       └──────│      Enrollment            │
              ├────────────────────────────┤
              │ status, enrolledAt, grade  │
              └────────────────────────────┘

Course 1 ── * Assignment 1 ── * Submission * ── 1 Student
```

#### Code walkthrough

- **Inheritance** — `Student` and `Instructor` specialize `User` for role-specific behavior.
- **`Enrollment` association class** — resolves many-to-many between students and courses.
- **`Submission`** — ties a student to one assignment; supports grading workflow.

#### Complexity

| | |
|-|-|
| Time | N/A (design / modeling) |
| Space | N/A (conceptual) |

#### Edge cases

- **Audit / admin role** — optional `Admin` actor with permissions.
- **Waitlisted enrollment** — `status` enum: `ACTIVE`, `WAITLIST`, `DROPPED`.
- **Team assignments** — may need `Group` entity if interviewer extends scope.

</details>

</article>

<article>

If you are given to design a authentication service. Which design pattern you will use? 

<details><summary>Theory and explanation</summary>

The original short answer is **Strategy pattern** — and that is a strong choice.

**Why Strategy fits authentication**

- Multiple **authentication mechanisms** (password, OAuth2, SAML, magic link, API key, MFA step-up) share one interface, e.g. `authenticate(credentials): AuthResult`.
- The service selects a **strategy** at runtime based on tenant, client type, or route — without `if/else` chains in controllers.
- New providers are added by implementing `AuthStrategy` and registering in a factory or DI container — **Open/Closed Principle**.

**Supporting patterns**

| Pattern | Use |
|---------|-----|
| **Factory / Abstract Factory** | Build the right strategy from config |
| **Chain of Responsibility** | MFA checks, rate limits, account lockout |
| **Decorator** | Logging, metrics, token refresh around core auth |
| **Singleton** (careful) | Shared token verifier / JWKS cache |

**Interview talking points**

- Separate **authentication** (who you are) from **authorization** (what you may do).
- Store secrets hashed (bcrypt/argon2); never log raw passwords.
- JWT vs server sessions: mention rotation, revocation, and `HttpOnly` cookies for web.

#### Further reading

- [Refactoring Guru: Strategy](https://refactoring.guru/design-patterns/strategy) — pattern structure
- [OWASP: Authentication cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) — security practices
- [Auth0: OAuth 2.0 overview](https://auth0.com/docs/authenticate/protocols/oauth) — modern delegated auth
- [Martin Fowler: Patterns of Enterprise Application Architecture](https://martinfowler.com/eaaCatalog/) — enterprise auth context

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class AuthStrategy {
  async authenticate(_credentials) {
    throw new Error('Not implemented');
  }
}

class PasswordStrategy extends AuthStrategy {
  async authenticate({ email, password, userRepo, hashVerify }) {
    const user = await userRepo.findByEmail(email);
    if (!user || !(await hashVerify(password, user.passwordHash))) {
      return { ok: false, reason: 'INVALID_CREDENTIALS' };
    }
    return { ok: true, userId: user.id };
  }
}

class OAuthStrategy extends AuthStrategy {
  async authenticate({ code, oauthClient }) {
    const profile = await oauthClient.exchangeCode(code);
    return { ok: true, userId: profile.sub };
  }
}

class AuthenticationService {
  constructor(strategies) {
    this.strategies = strategies; // { password: PasswordStrategy, oauth: OAuthStrategy }
  }

  async login(method, credentials) {
    const strategy = this.strategies[method];
    if (!strategy) throw new Error('Unknown auth method');
    return strategy.authenticate(credentials);
  }
}
```

#### Code walkthrough

- **`AuthStrategy`** — common interface for all login mechanisms.
- **Concrete strategies** — encapsulate password vs OAuth flows.
- **`AuthenticationService`** — delegates to the strategy chosen by `method` (route header, tenant config, etc.).

#### Complexity

| | |
|-|-|
| Time | N/A (design); runtime depends on strategy (DB hash, HTTP to IdP) |
| Space | N/A (conceptual) |

#### Edge cases

- **Unknown `method`** — fail fast with clear error.
- **MFA required** — chain a second strategy after primary success.
- **Account enumeration** — use generic error messages on password failure.

</details>

</article>

<article>

You are given a chat system to design. Polling, streaming or sockets which will you use? Why?

<details><summary>Theory and explanation</summary>

| Approach | How it works | Pros | Cons |
|----------|----------------|------|------|
| **Short polling** | Client repeatedly `GET /messages?since=id` | Simple, works everywhere | High latency, wasted requests, server load |
| **Long polling** | Server holds request until new message or timeout | Near real-time, HTTP-friendly | Many open connections, timeout handling |
| **SSE (streaming)** | One-way HTTP stream `text/event-stream` | Efficient server→client push | One-way only; some proxies buffer |
| **WebSockets** | Full-duplex persistent connection | Best for chat: typing, read receipts, low latency | Stateful servers, load balancer sticky sessions |

**Recommendation for chat**

- **WebSockets** (or **Socket.IO** with fallback) for interactive chat: bidirectional, low overhead after connect.
- **SSE** if you only need server→client notifications and want simpler infra.
- **Polling** only for MVP, legacy clients, or very low message volume.

**Supporting architecture**

- Message broker (Redis Pub/Sub, NATS) between API nodes.
- Store messages in DB; deliver via connection map `userId → socketId`.
- Heartbeats and reconnect with missed-message sync (`since` cursor).

#### Further reading

- [MDN: WebSockets API](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) — browser API
- [MDN: Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) — one-way streaming
- [Socket.IO documentation](https://socket.io/docs/v4/) — fallbacks and rooms
- [System Design Primer: Real-time chat](https://github.com/donnemartin/system-design-primer) — scaling patterns

</details>

<details><summary>Solution (JavaScript)</summary>

Minimal **WebSocket** server sketch (Node `ws`) showing why sockets beat polling for chat:

```js
import { WebSocketServer } from 'ws';

const wss = new WebSocketServer({ port: 8080 });
const rooms = new Map(); // roomId -> Set<ws>

function broadcast(roomId, payload) {
  const clients = rooms.get(roomId);
  if (!clients) return;
  const data = JSON.stringify(payload);
  for (const client of clients) {
    if (client.readyState === 1) client.send(data);
  }
}

wss.on('connection', (ws) => {
  ws.on('message', (raw) => {
    const msg = JSON.parse(raw);
    if (msg.type === 'join') {
      if (!rooms.has(msg.roomId)) rooms.set(msg.roomId, new Set());
      rooms.get(msg.roomId).add(ws);
    }
    if (msg.type === 'chat') {
      broadcast(msg.roomId, { type: 'chat', text: msg.text, user: msg.user });
    }
  });
});
```

#### Code walkthrough

- **Persistent connection** — no repeated HTTP headers per message.
- **Rooms** — isolate channels; maps to chat threads or groups.
- **`broadcast`** — pushes to all members in O(room size).

#### Complexity

| | |
|-|-|
| Time | O(1) amortized per message send per connection; broadcast O(k) for k clients in room |
| Space | O(active connections) |

#### Edge cases

- **Reconnect** — client sends `since=lastMessageId` over REST or on `join` to backfill.
- **Offline users** — persist then push via FCM/APNs; sockets only for online delivery.
- **Load balancers** — need sticky sessions or shared pub/sub between nodes.

</details>

</article>

<article>

- Describe idempotent and non-idempotent request in REST.
- How does a DNS resolver work ?

<details><summary>Theory and explanation</summary>

### Idempotent vs non-idempotent REST requests

An operation is **idempotent** if performing it **once or many times** has the **same effect** on server state (safe retries).

| HTTP method | Idempotent? | Notes |
|-------------|-------------|-------|
| GET, HEAD, OPTIONS | Yes | Read-only; should not change state |
| PUT, DELETE | Yes | Repeating DELETE on same resource is still “deleted” |
| POST | **No** (usually) | Creates resources, charges cards — repeats may duplicate |
| PATCH | Often **no** | Depends on semantics (increment vs set) |

**Examples**

- **Idempotent**: `PUT /users/1` with full body — same final user state.
- **Non-idempotent**: `POST /orders` — retry without protection may create two orders → use **Idempotency-Key** header.

### How a DNS resolver works

When you resolve `www.example.com`:

1. **Stub resolver** (OS/browser) checks **cache** (OS cache, browser cache).
2. If miss, query goes to **recursive resolver** (ISP or `8.8.8.8`).
3. Recursive resolver walks the hierarchy:
   - **Root** nameservers → TLD (`.com`)
   - **TLD** → authoritative NS for `example.com`
   - **Authoritative** → A/AAAA record for `www`
4. Answer is cached with **TTL**; returned to the application.
5. Browser opens **TCP** to the IP (often then **TLS** SNI uses the hostname).

**Interview talking points**

- DNS is distributed, cached, and TTL-bound — not instant propagation after changes.
- Mention **CNAME**, **DNSSEC** (optional), and difference between recursive vs authoritative.

#### Further reading

- [RFC 7231: HTTP methods and idempotency](https://datatracker.ietf.org/doc/html/rfc7231#section-4.2.2) — normative HTTP semantics
- [Stripe: Idempotent requests](https://stripe.com/docs/api/idempotent_requests) — real-world retry pattern
- [Cloudflare: What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/) — resolver overview
- [MDN: HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) — method safety table

</details>

<details><summary>Solution (JavaScript)</summary>

**Idempotency key middleware (POST safety)**

```js
const processedKeys = new Map(); // use Redis in production

function idempotencyMiddleware(handler) {
  return async (req, res) => {
    const key = req.headers['idempotency-key'];
    if (!key) return handler(req, res);

    if (processedKeys.has(key)) {
      return res.status(200).json(processedKeys.get(key));
    }

    const result = await handler(req, res);
    processedKeys.set(key, result);
    return result;
  };
}
```

**DNS resolution flow (pseudo-steps for explanation)**

```js
async function resolveHostname(hostname) {
  // 1. Check local cache (conceptual)
  // 2. Ask recursive resolver (system resolver / DoH)
  // 3. Recursive queries root → TLD → authoritative
  // 4. Return A/AAAA records; cache by TTL
  const dns = await import('node:dns/promises');
  return dns.lookup(hostname); // stub → OS → recursive chain
}
```

#### Code walkthrough

- **Idempotency-Key** — store first successful response; duplicates return the same body without re-running side effects.
- **`dns.lookup`** — illustrates stub resolver entry point; actual recursion happens on the configured resolver.

#### Complexity

| | |
|-|-|
| Time | Idempotency map: O(1); DNS: typically milliseconds, cached O(1) locally |
| Space | Idempotency store grows with keys until TTL/eviction |

#### Edge cases

- **POST that is intentionally idempotent** — document exception (e.g. “set flag to true”).
- **DNS TTL expired** — re-query; stale cache causes wrong IP briefly.
- **NXDOMAIN** — hostname does not exist; handle errors in client.

</details>

</article>
