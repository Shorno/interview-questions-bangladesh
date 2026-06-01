---
description: Wedevs interview questions, Wedevs interview stages, Wedevs interview details, Wedevs interview questions and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/wedevs
---
# weDevs

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-| :- |
| Founding year | 2008  |
| Company Website | https://wedevs.com/ |
| Career Website | https://wedevs.com/career/ |
| Technologies Used| WordPress, PHP |

## Introduction
[WeDevs](https://wedevs.com/) is an international software company. weDevs is the parent company of Dokan Multivendor, WP User Frontend, WP Project Manager, WP ERP, weMail, FlyWP, and six more exclusive WordPress products. At weDevs, they are dedicated to pushing the boundaries of what is possible with WordPress and SaaS solutions.

## Interview Stages
weDevs' fresher recruitment is currently based on competitive programming. They post job circulars on their career page and LinkedIn page. The circulars often ask for a good national rank or a Codeforces rating of 1600+ (you can apply if you are slightly below this).

Their interview process consists of three stages. The first two stages vary from person to person. For some, the first stage is a basic verbal session focusing on fundamental computer science concepts, while for others, it is a coding round. The final stage is called the HR round. To receive an offer, you must pass all three stages.

## Questions

<article>

Discuss BFS and DFS: which one is faster, and what are their use cases?

<details><summary>Theory and explanation</summary>

**BFS (Breadth-First Search)** and **DFS (Depth-First Search)** are graph/tree traversals differing in **order of exploration** and **data structure**.

| | BFS | DFS |
|-|-----|-----|
| Structure | **Queue** (FIFO) | **Stack** or recursion |
| Order | Level by level from source | Deep branch first, then backtrack |
| Shortest path (unweighted) | **Yes** — first arrival is fewest edges | No guarantee |
| Memory | O(width) — can be large in wide graphs | O(height) — often lower for deep narrow graphs |

**Which is “faster”?**

Neither is universally faster — both are **O(V + E)** for adjacency-list graphs. Constant factors differ:

- **BFS** — queue operations; visits each edge once.
- **DFS** — stack/recursion; also O(V + E) but deeper recursion may hit stack limits.

Choose by **problem requirements**, not raw speed.

**BFS use cases**

- **Shortest path** in unweighted graphs (maze, social network degrees).
- **Level-order** tree traversal (print by depth).
- **Multi-source BFS** (fire spread, 0-1 BFS variants).
- **Bipartite check** (color layers).

**DFS use cases**

- **Cycle detection** (directed/undirected).
- **Topological sort** (dependency order).
- **Connected components / flood fill** (grid islands).
- **Backtracking** (paths, permutations with pruning).
- **Tree DP** (post-order aggregation).

**weDevs / WordPress angle**

- Plugin dependency graphs → topological sort (DFS).
- Category trees → either traversal for menus; BFS for breadth-limited expansion.

#### Further reading

- [Visualgo: BFS](https://visualgo.net/en/bfs) — queue animation
- [Visualgo: DFS](https://visualgo.net/en/dfs) — stack/recursion animation
- [CP-Algorithms: Breadth-first search](https://cp-algorithms.com/graph/breadth-first-search.html) — shortest path proof
- [CP-Algorithms: Depth-first search](https://cp-algorithms.com/graph/depth-first-search.html) — timers and applications
- [GeeksforGeeks: BFS vs DFS](https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/) — comparison table

</details>

<details><summary>Solution (JavaScript)</summary>

Same graph — BFS returns shortest-hop distance; DFS collects a depth-first path.

```js
function buildAdj(n, edges) {
  const adj = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) {
    adj[u].push(v);
    adj[v].push(u);
  }
  return adj;
}

function bfsShortestDistance(adj, start, target) {
  const n = adj.length;
  const dist = Array(n).fill(-1);
  const q = [start];
  dist[start] = 0;
  while (q.length) {
    const u = q.shift();
    if (u === target) return dist[u];
    for (const v of adj[u]) {
      if (dist[v] === -1) {
        dist[v] = dist[u] + 1;
        q.push(v);
      }
    }
  }
  return -1;
}

function dfsPath(adj, start, target) {
  const path = [];
  const visited = new Set();
  function dfs(u) {
    visited.add(u);
    path.push(u);
    if (u === target) return true;
    for (const v of adj[u]) {
      if (!visited.has(v) && dfs(v)) return true;
    }
    path.pop();
    return false;
  }
  dfs(start);
  return path;
}

const adj = buildAdj(6, [[0,1],[0,2],[1,3],[2,4],[4,5]]);
bfsShortestDistance(adj, 0, 5); // 3
dfsPath(adj, 0, 5);             // e.g. [0,2,4,5] — not necessarily shortest
```

#### Code walkthrough

- **BFS** — first time reaching `target` gives minimum edge count in unweighted graph.
- **DFS** — explores one branch deeply; `path` backtracks on failure.

#### Complexity

| | BFS | DFS |
|-|-|-|
| Time | O(V + E) | O(V + E) |
| Space | O(V) queue | O(V) stack/recursion |

#### Edge cases

- **Disconnected graph** — BFS returns -1 if target unreachable.
- **Self-loop / multi-edge** — mark visited to avoid infinite loops.
- **Large graphs** — DFS recursion depth; prefer iterative stack.

</details>

</article>

<article>

Explain the principles of OOP.

<details><summary>Theory and explanation</summary>

**Object-Oriented Programming (OOP)** models software as **objects** combining **state (fields)** and **behavior (methods)**, communicating via message passing (method calls).

**Four pillars**

1. **Encapsulation** — hide internal state; expose controlled API via public methods. Prevents invalid states (e.g. negative bank balance). In PHP/WordPress: private plugin internals, public hooks/filters.

2. **Abstraction** — show essential behavior, hide complexity. Interfaces and abstract classes define contracts without implementation detail (e.g. `PaymentGateway` interface with `charge()`).

3. **Inheritance** — reuse and extend base class behavior. Subclass overrides or extends parent (`class PremiumPlugin extends BasePlugin`). Favor **composition over inheritance** when behavior stacks get fragile.

4. **Polymorphism** — same interface, different implementations. Runtime dispatch: `processPayment(gateway)` works for Stripe or PayPal subclasses. Duck typing in JS; interfaces + extends in PHP 8+.

**SOLID (often expected in senior interviews)**

- **S** — Single responsibility
- **O** — Open/closed (extend without modify)
- **L** — Liskov substitution
- **I** — Interface segregation
- **D** — Dependency inversion

**weDevs context**

WordPress plugins use OOP heavily (singleton services, dependency injection containers in modern WP). Dokan multivendor domains (vendor, product, order) map naturally to classes with encapsulated business rules.

#### Further reading

- [MDN: Object-oriented programming](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_programming) — JS perspective
- [PHP: Object-Oriented Programming](https://www.php.net/manual/en/language.oop5.php) — weDevs stack
- [Refactoring Guru: OOP basics](https://refactoring.guru/design-patterns/what-is-pattern) — pillars explained with examples
- [Uncle Bob: SOLID principles](https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html) — relevance in modern code
- [WordPress: Plugin architecture (handbook)](https://developer.wordpress.org/plugins/) — hooks vs OOP services

</details>

<details><summary>Solution (JavaScript)</summary>

Minimal illustration of all four pillars in JS (ES6 classes).

```js
// Abstraction + Encapsulation
class BankAccount {
  #balance = 0; // private field

  deposit(amount) {
    if (amount <= 0) throw new Error('Invalid amount');
    this.#balance += amount;
  }

  getBalance() {
    return this.#balance;
  }
}

// Inheritance + Polymorphism
class SavingsAccount extends BankAccount {
  constructor(interestRate) {
    super();
    this.interestRate = interestRate;
  }

  applyInterest() {
    this.deposit(this.getBalance() * this.interestRate);
  }
}

class CheckingAccount extends BankAccount {
  withdraw(amount) {
    if (amount > this.getBalance()) throw new Error('Insufficient funds');
    this.deposit(-amount);
  }
}

function printBalance(account) {
  // Polymorphic — works for any BankAccount subclass
  console.log(account.getBalance());
}

const accounts = [new SavingsAccount(0.05), new CheckingAccount()];
accounts[0].deposit(100);
accounts[0].applyInterest();
printBalance(accounts[0]); // 105
```

#### Code walkthrough

- **`#balance`** — encapsulation; only methods mutate state safely.
- **`BankAccount`** — abstract contract for balances; subclasses specialize behavior.
- **`printBalance`** — polymorphism via shared interface (`getBalance`).

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases

- **Deep inheritance trees** — fragile base class problem; prefer composition.
- **JS private fields** — `#` syntax; older code used closures or WeakMaps.
- **PHP vs JS** — weDevs interviews may expect PHP examples with `visibility` keywords.

</details>

</article>

<article>

How many types of relationships exist in databases?

<details><summary>Theory and explanation</summary>

In **relational databases**, tables relate through **keys**. The classic **ER model** defines three cardinalities:

| Relationship | Meaning | Example |
|--------------|---------|---------|
| **One-to-One (1:1)** | Each row in A maps to at most one row in B and vice versa | User ↔ UserProfile |
| **One-to-Many (1:N)** | One row in A relates to many in B; each B row relates to one A | Department → Employees |
| **Many-to-Many (M:N)** | Rows on both sides can relate to multiple on the other | Students ↔ Courses |

**Implementation**

- **1:1** — foreign key on either table with **UNIQUE** constraint (or share primary key).
- **1:N** — foreign key on the **“many”** side (`employee.department_id`).
- **M:N** — **junction / join table** with composite key or surrogate PK (`enrollment(student_id, course_id)`).

**Extended relationship concepts (worth mentioning)**

- **Self-referencing** — employee `manager_id` → employee (1:N on same table).
- **Optional vs mandatory** — nullable FK (optional membership).
- **Identifying vs non-identifying** — weak entity depends on parent PK vs independent FK.

**NoSQL note**

Document stores embed (1:N denormalized) or reference by ID; graph DBs make relationships first-class edges.

**weDevs / WordPress**

`wp_posts` ↔ `wp_postmeta` is 1:N; `wp_users` ↔ roles via capabilities is M:N through junction-like tables.

#### Further reading

- [W3Schools SQL: Relationships](https://www.w3schools.com/sql/sql_foreignkey.asp) — FK basics
- [Microsoft: Database relationship types](https://learn.microsoft.com/en-us/office/troubleshoot/access/define-database-relationship-types) — 1:1, 1:N, M:N diagrams
- [Vertabelo: ER diagram relationships](https://vertabelo.com/blog/crow-s-foot-notation/) — crow's foot notation
- [MySQL: Foreign keys](https://dev.mysql.com/doc/refman/8.0/en/create-table-foreign-keys.html) — referential integrity
- [Database Design (Stanford DB course notes)](https://web.stanford.edu/class/cs145/) — ER modeling

</details>

<details><summary>Solution (JavaScript)</summary>

Schema sketch as JS objects — maps ER concepts to how ORMs represent relationships.

```js
// One-to-One: user.id <-> profile.user_id (unique)
const user = { id: 1, email: 'dev@wedevs.com' };
const profile = { user_id: 1, bio: 'WordPress builder' };

// One-to-Many: department.id -> employees.department_id
const department = { id: 10, name: 'Engineering' };
const employees = [
  { id: 101, department_id: 10, name: 'Alice' },
  { id: 102, department_id: 10, name: 'Bob' },
];

// Many-to-Many: junction table enrollments
const students = [{ id: 1 }, { id: 2 }];
const courses = [{ id: 'WP101' }, { id: 'PHP201' }];
const enrollments = [
  { student_id: 1, course_id: 'WP101' },
  { student_id: 1, course_id: 'PHP201' },
  { student_id: 2, course_id: 'WP101' },
];

function coursesForStudent(studentId) {
  const courseIds = enrollments
    .filter((e) => e.student_id === studentId)
    .map((e) => e.course_id);
  return courses.filter((c) => courseIds.includes(c.id));
}

coursesForStudent(1); // both courses
```

#### Code walkthrough

- **1:1** — `profile.user_id` unique FK to `user.id`.
- **1:N** — many `employees` share one `department_id`.
- **M:N** — `enrollments` resolves student–course pairs; query filters junction.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual); junction lookup O(E) in naive JS |
| Space | N/A (conceptual) |

#### Edge cases

- **Nullable FK** — optional relationship (employee without department).
- **Cascade delete** — deleting department may nullify or delete employees (DB policy).
- **M:N with payload** — junction may carry `enrolled_at` grade, etc.

</details>

</article>

<article>

What is binary search? How does it work?

<details><summary>Theory and explanation</summary>

**Binary search** finds a target in a **sorted** array by repeatedly halving the search interval.

**Invariant**

If `target` exists, it lies in index range `[lo, hi]`.

**Steps**

1. Set `lo = 0`, `hi = n - 1`.
2. While `lo <= hi`:
   - `mid = lo + floor((hi - lo) / 2)` — avoids overflow in other languages.
   - If `a[mid] === target`, return `mid`.
   - If `a[mid] < target`, search right: `lo = mid + 1`.
   - Else search left: `hi = mid - 1`.
3. Return “not found” (or insertion point variant).

**Complexity**

- **Time**: O(log n) — halve each iteration.
- **Space**: O(1) iterative; O(log n) recursive stack.

**Requirements**

- **Sorted** (or monotonic predicate) data.
- **Random access** — arrays; linked lists cannot binary search efficiently.

**Variants**

- **Lower bound** — first index where `a[i] >= target`.
- **Upper bound** — first where `a[i] > target`.
- **Binary search on answer** — minimize maximum / maximize minimum when monotonic feasibility check exists (common in CP — relevant to weDevs coding round).

#### Further reading

- [Visualgo: Binary Search](https://visualgo.net/en/binarysearch) — interactive trace
- [CP-Algorithms: Binary search](https://cp-algorithms.com/num_methods/binary_search.html) — on answer technique
- [MDN: binary search concept (guide)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort) — sort prerequisite
- [LeetCode 704: Binary Search](https://leetcode.com/problems/binary-search/) — canonical implementation
- [TopCoder: Binary search tutorial](https://www.topcoder.com/thrive/articles/Binary%20Search) — off-by-one pitfalls

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function binarySearch(arr, target) {
  let lo = 0;
  let hi = arr.length - 1;
  while (lo <= hi) {
    const mid = lo + ((hi - lo) >> 1);
    if (arr[mid] === target) return mid;
    if (arr[mid] < target) lo = mid + 1;
    else hi = mid - 1;
  }
  return -1;
}

// Lower bound: first index with arr[i] >= target
function lowerBound(arr, target) {
  let lo = 0;
  let hi = arr.length;
  while (lo < hi) {
    const mid = lo + ((hi - lo) >> 1);
    if (arr[mid] < target) lo = mid + 1;
    else hi = mid;
  }
  return lo;
}

binarySearch([1, 3, 5, 7, 9], 7);     // 3
binarySearch([1, 3, 5, 7, 9], 4);     // -1
lowerBound([1, 2, 2, 2, 5], 2);       // 1
```

#### Code walkthrough

- **`lo <= hi`** — closed interval; exits when interval empty.
- **Mid bias** — `lo + ((hi-lo)>>1)` prevents overflow in C++/Java; good habit in JS too.
- **`lowerBound`** — half-open `[lo, hi)` variant common in CP libraries.

#### Complexity

| | |
|-|-|
| Time | O(log n) |
| Space | O(1) |

#### Edge cases

- **Empty array** — return -1 / 0 for lower bound.
- **Duplicates** — standard search returns any match; use lower/upper bound for range.
- **Unsorted input** — must sort first O(n log n) or answer is wrong.

</details>

</article>

<article>

Questions may be asked about the projects you have mentioned.

<details><summary>Theory and explanation</summary>

Project deep-dives verify that **resume claims match understanding**. weDevs interviewers often probe WordPress plugins, SaaS architecture, or competitive programming side projects.

**How to prepare**

1. **Elevator pitch (30 s)** — problem, your role, stack, measurable outcome (users, performance, rank).
2. **Architecture diagram verbally** — client → API → DB → cache → third parties.
3. **Hardest technical decision** — trade-offs you considered (why Redis vs file cache, why custom table vs post meta).
4. **Failure / bug story** — what broke, how you debugged, what you changed (tests, monitoring).
5. **Ownership boundaries** — what you built vs team; honest scope avoids follow-up traps.

**Common follow-up topics**

- Authentication and authorization model.
- Database schema and indexing choices.
- Scaling bottlenecks and what you'd do at 10× traffic.
- Testing strategy (unit, integration, E2E).
- Deployment and CI/CD.

**STAR format for behavioral edges**

- **Situation**, **Task**, **Action**, **Result** — keeps answers structured under time pressure.

**Red flags to avoid**

- Cannot explain code you claim to have written.
- No metrics or concrete outcomes.
- Blaming teammates without reflecting on your part.

#### Further reading

- [Cracking the Coding Interview: project section tips](https://www.crackingthecodinginterview.com/) — explaining projects clearly
- [Star method (MIT CAPD)](https://capd.mit.edu/resources/the-star-method-for-behavioral-interviews/) — behavioral structure
- [WordPress Plugin Handbook](https://developer.wordpress.org/plugins/) — if projects are WP-based
- [GitHub: README best practices](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) — documenting projects recruiters read

</details>

<details><summary>Solution (JavaScript)</summary>

Use a **project brief object** as an interview crib sheet — not code to run in production, but a structured template.

```js
const projectBrief = {
  name: 'Dokan Vendor Analytics Widget',
  pitch:
    'WordPress plugin module showing sales charts for marketplace vendors using cached REST aggregates.',
  stack: ['PHP 8', 'WordPress REST API', 'React', 'MySQL', 'Redis'],
  architecture: [
    'Vendor browser → WP REST `/dokan/v1/stats`',
    'Endpoint checks Redis cache keyed by vendor_id + date range',
    'On miss: SQL aggregate on wp_dokan_orders, store 5 min TTL',
  ],
  hardestDecision:
    'Chose transient cache over real-time SQL to cut dashboard load from 800 ms to 40 ms p95.',
  metrics: { p95Ms: 40, dailyActiveVendors: 1200 },
  debuggingStory:
    'Timezone boundary bug double-counted orders; fixed by normalizing to UTC in query.',
};

function answerFollowUp(topic) {
  const map = {
    auth: 'Cookie nonce + `current_user_can("dokan_view_reports")` capability check.',
    scale: 'Shard cache keys; read replica for reporting queries at 10× vendors.',
    tests: 'PHPUnit for REST permissions; Jest for chart empty states.',
  };
  return map[topic] ?? ' Tie back to concrete files and commits in the repo.';
}

answerFollowUp('auth');
```

#### Code walkthrough

- **`projectBrief`** — rehearse each field aloud before the interview.
- **`answerFollowUp`** — maps predictable questions to prepared, specific answers.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases

- **Group projects** — clarify your contribution without underselling teamwork.
- **Stale projects** — refresh memory from repo/README before interview.
- **Non-technical interviewer (HR)** — emphasize impact and learning, less low-level detail.

</details>

</article>

<article>

The coding round is conducted on vjudge and contains Codeforces problems. The complexity is around 1000-1600 ELO rating.

<details><summary>Theory and explanation</summary>

weDevs fresher **coding rounds on vJudge** typically mirror **Codeforces Div. 2 A–C** difficulty: rating band **1000–1600** (Newbie to Pupil/Expert threshold).

**What 1000–1600 usually demands**

| Rating band | Typical skills |
|-------------|----------------|
| **800–1000** | Implementation, loops, arrays, strings, basic math |
| **1000–1200** | Sorting, greedy, simple data structures (stack, map) |
| **1200–1400** | Binary search, two pointers, BFS/DFS basics, prefix sums |
| **1400–1600** | DP intro, combinatorics, bitmask, tree DFS, number theory mod |

**vJudge specifics**

- Contest problems cloned from Codeforces / other judges.
- **IO format** and **time limits** match original — practice reading specs carefully.
- **C++** dominates CP; Java/Python allowed on some contests — confirm rules.

**Preparation plan**

1. Solve **Codeforces Div. 2** A and B consistently under 30 min combined.
2. Upsolve C until 1600 stable.
3. Drill **C++ STL**: `vector`, `map`, `set`, `priority_queue`, `sort`, fast IO.
4. Track weak tags (DP, graphs, binary search on answer) on [Codeforces profile](https://codeforces.com/).

**During the round**

- Read all problems first; pick easiest score first.
- Write brute force for partial credit if stuck.
- Test edge cases: n=1, all equal, max constraints.

#### Further reading

- [Codeforces rating distribution](https://codeforces.com/ratings) — context for 1600 bar
- [USACO Guide: General CP](https://usaco.guide/CPH/) — structured topic list
- [CSES Problem Set](https://cses.fi/problemset/) — skill-building by category
- [vJudge FAQ](https://vjudge.net/faq) — how virtual contests work
- [Codeforces Edu: Binary search / Two pointers](https://codeforces.com/edu/courses) — step-by-step lessons

</details>

<details><summary>Solution (JavaScript)</summary>

Rating-band checklist generator — use during practice to track readiness (not exam code).

```js
const TOPICS_BY_RATING = [
  { max: 1000, topics: ['implementation', 'arrays', 'strings'] },
  { max: 1200, topics: ['sorting', 'greedy', 'maps'] },
  { max: 1400, topics: ['binary search', 'two pointers', 'bfs dfs'] },
  { max: 1600, topics: ['dp 1d', 'prefix sums', 'basic trees', 'mod arithmetic'] },
];

function readinessCheck(solvedTags) {
  const need = new Set();
  for (const band of TOPICS_BY_RATING) {
    for (const t of band.topics) need.add(t);
  }
  const missing = [...need].filter((t) => !solvedTags.includes(t));
  return { readyFor1600: missing.length === 0, missing };
}

readinessCheck(['implementation', 'sorting', 'bfs dfs', 'dp 1d']);
// lists gaps like binary search, mod arithmetic, etc.
```

#### Code walkthrough

- **`TOPICS_BY_RATING`** — maps weDevs ELO band to expected Codeforces tags.
- **`readinessCheck`** — highlights weak tags to drill before vJudge contest.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases

- **Strong math, weak implementation** — balance with timed A/B practice.
- **JavaScript on vJudge** — rare for CP; confirm language; C++ usually faster for IO.
- **Rating inflation** — upsolve harder than your current rating for margin.

</details>

</article>

