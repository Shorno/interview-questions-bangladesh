#!/usr/bin/env python3
"""Enrich exabyting.md and bs23.md to CONTRIBUTING enriched-answer format."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXABYTING = ROOT / "docs/companies/exabyting.md"
BS23 = ROOT / "docs/companies/bs23.md"

FURTHER_CS = """#### Further reading
- [GeeksforGeeks](https://www.geeksforgeeks.org/) — algorithms and CS fundamentals
- [MDN Web Docs](https://developer.mozilla.org/) — JavaScript and web platform
"""

def normalize(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())[:120]


def has_theory(block: str) -> bool:
    return "Theory and explanation" in block


def extract_question(block: str) -> str:
    m = re.match(r"\s*(.*?)(?=\n<details>|\n\*\*|\n```|\Z)", block, re.S)
    return (m.group(1) if m else block).strip()


def further_reading_links(question: str) -> str:
    q = question.lower()
    links = []
    if "sql" in q or "join" in q or "acid" in q or "index" in q or "rdbms" in q:
        links.append("- [PostgreSQL: Indexes](https://www.postgresql.org/docs/current/indexes.html) — B-tree index internals")
    if "javascript" in q or "react" in q or "closure" in q or "hoist" in q or "event loop" in q:
        links.append("- [MDN: JavaScript guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) — language reference")
    if "tcp" in q or "udp" in q or "http" in q or "https" in q or "jwt" in q or "cookie" in q:
        links.append("- [Cloudflare Learning Center](https://www.cloudflare.com/learning/) — networking concepts")
    if "tree" in q or "bst" in q or "graph" in q or "sort" in q or "array" in q or "linked" in q:
        links.append("- [VisuAlgo](https://visualgo.net/en) — interactive data structure visualizations")
    if "oop" in q or "polymorphism" in q or "inheritance" in q or "diamond" in q:
        links.append("- [Oracle Java Tutorials: OOP](https://docs.oracle.com/javase/tutorial/java/concepts/) — class design")
    if not links:
        links = [
            "- [GeeksforGeeks](https://www.geeksforgeeks.org/) — interview CS topics",
            "- [MDN Web Docs](https://developer.mozilla.org/) — web and JS reference",
        ]
    return "#### Further reading\n" + "\n".join(links) + "\n"


def complexity_table(time: str, space: str, note: str = "") -> str:
    n = f"\n{note}\n" if note else "\n"
    return f"""#### Complexity{n}
| | |
|-|-|
| Time | {time} |
| Space | {space} |
"""


def js_footer(walkthrough: str, time: str, space: str, edges: str) -> str:
    return f"""
#### Code walkthrough
{walkthrough}

{complexity_table(time, space)}

#### Edge cases
{edges}
"""


def rename_show_answer(block: str) -> str:
    block = block.replace("<details><summary>Show Answer</summary>", "<details><summary>Theory and explanation</summary>")
    block = block.replace("<details><summery>Show Answer</summery>", "<details><summary>Theory and explanation</summary>")
    block = block.replace("<details><summary>Show Details</summary>", "<details><summary>Theory and explanation</summary>")
    return block


def split_cpp_from_details(details_body: str):
    m = re.search(r"```cpp\n(.*?)```", details_body, re.S)
    if not m:
        return details_body, None
    cpp = m.group(0)
    rest = details_body.replace(cpp, "").strip()
    return rest, cpp


def dedupe_paragraphs(body: str) -> str:
    paras = re.split(r"\n\n+", body.strip())
    out: list[str] = []
    prev_key: str | None = None
    for p in paras:
        p = p.strip()
        if not p:
            continue
        key = re.sub(r"\s+", " ", p).lower()
        if prev_key is not None and key == prev_key:
            continue
        out.append(p)
        prev_key = key
    return "\n\n".join(out)


def wrap_theory_body(body: str, question: str) -> str:
    body = body.strip()
    if "#### Further reading" not in body:
        body += "\n\n" + further_reading_links(question)
    return dedupe_paragraphs(body)


def add_js_section(js_code: str, walkthrough: str, time: str, space: str, edges: str) -> str:
    return f"""
<details><summary>Solution (JavaScript)</summary>

```js
{js_code.strip()}
```

{js_footer(walkthrough, time, space, edges)}
</details>
"""


def add_cpp_section(cpp_block: str) -> str:
    return f"""
<details><summary>Solution (C++)</summary>

{cpp_block.strip()}

#### Code walkthrough

See theory section; original onsite/phone-round C++ solution preserved above.

#### Complexity

| | |
|-|-|
| Time | Depends on problem — see JavaScript tab for typical bounds |
| Space | Depends on problem |

</details>
"""


# --- Topic-specific JS solutions (keyed by substring in question) ---
JS_SOLUTIONS = [
    ("decimal number to binary", "function decimalToBinary(n) {\n  if (n === 0) return '0';\n  let bits = '';\n  while (n > 0) {\n    bits = (n % 2) + bits;\n    n = Math.floor(n / 2);\n  }\n  return bits;\n}", "Repeatedly take `n % 2` and prepend; divide by 2 until zero.", "O(log n)", "O(log n)", "Handle `n === 0`; negative integers need a separate convention if required."),
    ("reverse the digits", "function reverseInteger(x) {\n  let rev = 0;\n  while (x !== 0) {\n    const pop = x % 10;\n    x = (x / 10) | 0;\n    if (rev > 2147483647 / 10 || (rev === 2147483647 / 10 && pop > 7)) return 0;\n    if (rev < -2147483648 / 10 || (rev === -2147483648 / 10 && pop < -8)) return 0;\n    rev = rev * 10 + pop;\n  }\n  return rev;\n}", "Pop digit from `x`, push onto `rev`; check 32-bit overflow before multiply.", "O(log n)", "O(1)", "Overflow returns 0 per LeetCode; trailing zeros in input."),
    ("armstrong", "function isArmstrong(n) {\n  const s = String(n);\n  const p = s.length;\n  let sum = 0;\n  for (const ch of s) sum += Number(ch) ** p;\n  return sum === n;\n}", "Sum each digit raised to power of digit count; compare to `n`.", "O(log n)", "O(1)", "Single-digit numbers; leading zeros not in integer form."),
    ("removing", "function removeExtraSpaces(s) {\n  return s.trim().split(/\\s+/).join(' ');\n}", "Trim ends, split on whitespace runs, join with single space.", "O(n)", "O(n)", "Empty string → ''; only spaces → ''."),
    ("divisible by 3", "function starCoder(n) {\n  for (let i = 1; i <= n; i++) {\n    let out = '';\n    if (i % 3 === 0) out += 'Star';\n    if (i % 5 === 0) out += 'Coder';\n    console.log(out || i);\n  }\n}", "Build string for FizzBuzz-style rules; print number if no rule matched.", "O(n)", "O(1)", "`n` large — use loop not recursion."),
    ("rotate the array", "function rotate(nums, k) {\n  const n = nums.length;\n  k %= n;\n  reverse(nums, 0, n - 1);\n  reverse(nums, 0, k - 1);\n  reverse(nums, k, n - 1);\n}\nfunction reverse(a, l, r) {\n  while (l < r) [a[l++], a[r--]] = [a[r], a[l]];\n}", "Three reverses: whole array, first k, remainder — in-place O(1) extra space.", "O(n)", "O(1)", "`k > n` use modulo; `n === 0` edge case."),
    ("factorial", "function factorial(n) {\n  if (n < 0) return null;\n  let f = 1;\n  for (let i = 2; i <= n; i++) f *= i;\n  return f;\n}", "Iterative product avoids stack overflow of naive recursion.", "O(n)", "O(1)", "Large `n` overflows Number — use BigInt in interviews if asked."),
    ("longest consecutive", "function longestConsecutive(nums) {\n  const set = new Set(nums);\n  let best = 0;\n  for (const x of set) {\n    if (set.has(x - 1)) continue;\n    let len = 1;\n    while (set.has(x + len)) len++;\n    best = Math.max(best, len);\n  }\n  return best;\n}", "Only start sequences at numbers with no predecessor in set; extend forward.", "O(n)", "O(n)", "Empty array → 0; duplicates in set collapse automatically."),
    ("good string", "function canMakeGood(A, B) {\n  const runs = A.match(/0+|1+/g) || [];\n  const maxRun = Math.max(...runs.map(r => r.length), 0);\n  const need = Math.ceil(maxRun / 2) - 1;\n  const avail = (B.match(/01|10/g) || []).length;\n  return avail >= need ? 'YES' : 'NO';\n}", "Max run of same bit needs separators; each copy of alternating B fixes one break.", "O(|A|+|B|)", "O(1)", "Greedy on run lengths; verify with samples 101/010 → YES."),
]

TOPIC_THEORY = {
    "array and linked list": """**Array**

- Contiguous memory; **O(1)** random access via `base + index * size`.
- Fixed size (static) or dynamic resize (amortized copy).

**Linked list**

- Nodes with `data` + `next` pointer; **O(n)** access by index.
- **O(1)** insert/delete at known node (with pointer).

**Use cases**

| Structure | When |
|-----------|------|
| Array | Cache-friendly iteration, index-based APIs, matrices |
| Linked list | Frequent insert/delete in middle, LRU chains, separate chaining in hash tables |

**Index access formula (array):** `address = base_address + index * element_size`.""",
    "sorting algorithm works better": """For general-purpose comparison sorting of ~1000 integers (positive and negative), **merge sort** and **quicksort** average **O(n log n)**.

| Algorithm | Average | Worst | Stable | Notes |
|-----------|---------|-------|--------|-------|
| Merge sort | O(n log n) | O(n log n) | Yes | Predictable; extra O(n) space |
| Quicksort | O(n log n) | O(n²) | No* | Fast in practice; pivot choice matters |
| Heap sort | O(n log n) | O(n log n) | No | O(1) extra space |

**Interview answer:** Prefer **merge sort** when stability matters; **quicksort** for in-place average speed with good pivot (median-of-three).""",
    "sort 1000 numbers": """Use **merge sort** or **introsort** (stdlib `sort` hybrid).

- Time **O(n log n)** worst case (merge) or guaranteed for introsort.
- Handles positive/negative without special cases.
- For bounded integer range, **counting sort** O(n + k) is also valid — mention as optimization if range is small.""",
    "stack, queue and priority": """**Stack (LIFO)** — push/pop at one end. Examples: call stack, undo, browser back (with another stack for forward).

**Queue (FIFO)** — enqueue rear, dequeue front. Examples: BFS, job schedulers, message buffers.

**Priority queue** — dequeue smallest/largest priority. Heap implementation: insert/delete **O(log n)**, peek **O(1)**. Used in Dijkstra, Huffman, task scheduling.""",
    "binary tree and bst": """**Binary tree:** each node ≤ 2 children; no ordering constraint.

**BST:** left < parent < right (inorder → sorted). Search/insert **O(h)**; **O(n)** if skewed into a chain.

**Balancing:** AVL (strict balance), red-black (relaxed, used in `std::map`), or rebuild periodically.""",
    "web address": """High-level flow when you open `https://www.google.com`:

1. **DNS** — resolve hostname to IP (recursive resolver, caches).
2. **TCP** — 3-way handshake to server :443.
3. **TLS** — certificate verify, key agreement, encrypted channel.
4. **HTTP** — GET request, redirects, response headers/body.
5. **Browser** — HTML parse → DOM, CSS, JS, subresources, render pipeline.

Mention **CDN**, **HTTP/2 multiplexing**, and **caching** (Cache-Control) for depth.""",
    "tcp and udp": """| | TCP | UDP |
|-|-----|-----|
| Connection | Connection-oriented | Connectionless |
| Reliability | ACK, retransmit, ordering | Best-effort |
| Use cases | HTTP, DB, file transfer | DNS, VoIP, gaming, streaming |

TCP = **reliable byte stream**; UDP = **datagrams** with lower latency overhead.""",
    "principles of oop": """**Encapsulation** — hide state; expose methods.

**Abstraction** — interfaces hide implementation.

**Inheritance** — reuse via is-a hierarchy.

**Polymorphism** — one interface, many behaviors (overload/override).

**Why OOP:** modularity, reuse, modeling domain entities; trade-off is coupling if hierarchies grow deep.""",
    "sql and nosql": """**SQL (relational):** schemas, ACID transactions, JOINs, vertical scale + replication.

**NoSQL:** document (MongoDB), key-value (Redis), wide-column (Cassandra), graph (Neo4j). Flexible schema, horizontal scale; eventual consistency common.

Choose SQL when relationships and strong consistency matter; NoSQL for high write throughput, flexible documents, or specialized access patterns.""",
    "compiler and interpreter": """**Compiler:** translates entire program to machine code **before** run (C, Go). Faster execution; slower edit-compile cycle.

**Interpreter:** executes source line-by-line or bytecode (Python, JS engines). Slower per-run unless JIT (V8).

**Java/C#:** compile to bytecode, JVM/CLR JIT at runtime — hybrid.""",
    "event loop in js": """JavaScript has one **call stack** (synchronous code). Async work goes to **Web APIs** / **libuv** (timers, I/O); callbacks enqueue **task queues**.

**Event loop** repeatedly: run stack until empty → take microtasks (Promises) → take one macrotask (setTimeout, I/O callback).

**Interview:** `async/await` is syntax over Promises; still single-threaded — no parallel CPU threads without Workers.""",
    "closure": """A **closure** is a function plus lexical environment of outer variables it references.

Inner functions keep outer bindings alive after outer returns — stored in heap-linked environment records (engine-specific).

Use cases: data privacy, factories, callbacks. Pitfall: loop `var` in closures — use `let` or IIFE.""",
    "why react": """**Virtual DOM** diffs minimal real DOM updates → fewer expensive reflows.

**Component model** — reusable UI, one-way data flow, ecosystem (hooks, Router).

vs **direct DOM:** manual `querySelector` + update does not scale; easy to create inconsistent UI state.""",
    "mutate props": """Props are **read-only** inputs from parent. Mutating them breaks **single source of truth** and React's predictability (reconciliation assumes props flow down).

Use **state** in child or **lift state up** / callbacks to parent. Violation causes subtle bugs and breaks memoization.""",
    "tailwind": """**Utility-first CSS** — compose classes in markup; design tokens in config.

Benefits: fast prototyping, consistent spacing/colors, purge unused CSS in production.

Trade-off: verbose class lists; use `@apply` or components for repetition.""",
    "single-threaded": """JS runs user code on **one thread**; blocking the stack blocks everything.

**Concurrency via async:** callbacks, Promises, `async/await` interleave I/O completion without parallel threads.

**Workers** (`Worker`, `SharedArrayBuffer`) for true parallelism — not default model.""",
    "libuv": """**libuv** is Node's C library for cross-platform async I/O (epoll/kqueue/IOCP), thread pool for file/crypto work, timers, and DNS.

Event loop phases: timers → pending → idle → poll → check → close. Interview: file read may use thread pool; network uses OS async APIs.""",
    "var, let, const": """| | Scope | Hoisting | Reassign |
|-|-------|----------|----------|
| `var` | Function | Yes (undefined) | Yes |
| `let` | Block | TDZ | Yes |
| `const` | Block | TDZ | No binding (object contents mutable) |

Prefer **const** default, **let** when rebinding, avoid **var** in modern JS.""",
    "hoisting": """Declarations are processed before execution in scope:

- `function` declarations — fully hoisted.
- `var` — hoisted, initialized `undefined`.
- `let`/`const` — hoisted but in **Temporal Dead Zone** until line runs.

`typeof foo` before `let foo` → ReferenceError.""",
    "primitive and reference": """**Primitives** (number, string, boolean, null, undefined, symbol, bigint) — copied by value.

**References** (objects, arrays, functions) — variable holds pointer; assignment copies reference; mutations shared.

`===` compares primitives by value, objects by reference identity.""",
    "pure function": """Same inputs → same output; **no side effects** (no I/O, no mutation of external state).

Benefits: testable, cacheable (`memoize`), safe in concurrent/FP pipelines.

`Math.random()` or `Date.now()` inside → impure.""",
    "functional programming": """Emphasize **immutable data**, **pure functions**, **higher-order functions** (`map`, `filter`, `reduce`), composition over inheritance.

In JS: avoid mutating arrays (`spread`, `map`), use `const`, prefer declarative chains. Libraries: Ramda, lodash/fp.""",
    "indexing": """**Index** (usually B+ tree) maps key → row location for **O(log n)** seeks vs full scan **O(n)**.

**Duplicate columns:** non-unique index allowed; multiple rows share key entries with row pointers.

Trade-off: faster reads, slower writes (maintain index), storage overhead.""",
    "acid": """**Atomicity** — all or nothing.

**Consistency** — invariants hold (app + DB rules).

**Isolation** — concurrent txs appear serial (levels: RC, RR, serializable).

**Durability** — committed data survives crash (WAL).

Note: Kleppmann argues **Consistency** is application-defined.""",
    "jwt": """`header.payload.signature` (Base64URL).

- **Header:** alg (`HS256`, `RS256`).
- **Payload:** claims (`sub`, `exp`, roles).
- **Signature:** HMAC or RSA over `header.payload`.

Stateless auth; revoke via short `exp` + refresh tokens or server denylist.""",
    "https stateless": """HTTP/HTTPS is **stateless** — each request independent.

**Sessions:** server issues session id / JWT in **Set-Cookie** or `Authorization` header; browser sends on every request → server maps to user store (Redis/DB).""",
    "cookie-based authentication": """Server creates session on login → **Set-Cookie** (`sessionId`). Browser auto-sends cookie; server looks up session.

**Blacklist:** delete session server-side; set `Max-Age=0`; Redis revocation set for JWT jti.""",
    "http and https": """**HTTP** port 80, plaintext.

**HTTPS** = HTTP over **TLS**: handshake (cert, key exchange), then symmetric **AES** for bulk data. Prevents MITM eavesdropping/tampering when certs validated.""",
    "operator overloading": """**C++** allows redefining operators for user types (`operator+`). Java/Python disallow operator overloading (Python has limited via special methods `__add__`).""",
    "map, unordered_map": """`std::map` — red-black tree, **O(log n)** ops, sorted iteration.

`unordered_map` — hash table, **O(1)** average, **O(n)** worst if all keys collide (bad hash / attack).""",
    "navigation system": """Browser history: **two stacks** — back stack (LIFO) and forward stack. Visit pushes URL on back, clears forward. Back pops to forward. Classic **stack** application.""",
    "stack be most appropriate": """Use a **stack (LIFO)** when the most recent item must be undone or processed first: browser back, editor undo, parentheses matching, iterative DFS, postfix evaluation. Queues fit FIFO (printer, BFS); heaps fit priority — not stacks.""",
    "ratio of black to red": """Let black = `3x`, red = `7x`. After +20 black: `(3x+20)/7x = 1/2` → `6x+40=7x` → `x=40`. Red = `7x` = **280**.""",
    "unique constraint": """**UNIQUE** allows **multiple NULLs** in SQL (NULL ≠ NULL). **PRIMARY KEY** implies UNIQUE + NOT NULL. False statement: unique prevents nulls.""",
    "catch the first train": """Head start 60 km at 7 AM. Relative speed 30 km/h → time 2 h from 8 AM → **10:00 AM**.""",
    "output of the following code": """Precedence: `*` `/` before `+`. `6/3=2`, `14*2=28` → `7+2+28` = **37**.""",
    "rectangular region": """Equal area does **not** force equal perimeter. Example: square 4×4 area 16 perimeter 16; rectangle 8×2 area 16 perimeter 20. Answer: perimeter **may be greater** (or less) — not determined by area alone.""",
    "agile model": """**Agile** — iterative delivery, welcome changing requirements, working software over docs. Contrasts with waterfall big-bang phases.""",
    "unit tests": """**Developers** write unit tests (TDD optional). QA/integration separate. Tests guard regressions on smallest testable units.""",
    "poisoned candy": """**Binary search with rats:** 10 rats, 10 bits → identify poison among 1000 in one hour (each rat represents one bit of bottle number). Minimum subjects **10** for 1000 bottles.""",
    "sprint": """Fixed **time-box** (often 2 weeks) to deliver increment of backlog; ends with review/retro. Scrum ceremony.""",
    "static keyword": """**Static method/field** belongs to class, not instance. No `this` for static methods. Static fields shared across instances.""",
    "immutable objects": """Immutable objects cannot change after construction — **thread-safe** sharing, safe keys in `HashMap`, easier reasoning. Java: `String`, records; use `final` fields + no setters.""",
    "minimum spanning tree": """**Kruskal** (sort edges, union-find) or **Prim** (grow from vertex, priority queue). Both **O(E log V)** typical.""",
    "balanced binary search tree": """Balanced BST search **O(log n)**; skewed chain **O(n)**.""",
    "bulb number 72": """Person `d` toggles if `d | 72`. Count **divisors** of 72: 1,2,3,4,6,8,9,12,18,24,36,72 → **12** people.""",
    "circular queue": """Capacity 5, 3 used → **2** slots remain (watch front=rear full condition separately).""",
    "circular singly linked": """Fast/slow pointers: move fast `n` steps, then both until fast.next is null; delete `slow.next`. Handle `n` equals length (delete head) and single node.""",
    "lowest common ancestor": """BST: walk from root — if both smaller go left, both larger go right, else current is LCA. **O(h)**.""",
    "next term in the series": """Perfect squares: next **36** (`6²`).""",
    "many-to-many": """Use **junction/bridge table** with FKs to both entities (e.g. `enrollments(student_id, course_id)`).""",
    "polymorphism": """Runtime **polymorphism** — virtual dispatch picks overridden `fight()` per actual type.""",
    "compile-time polymorphism": """**Function overloading** — resolved at compile time by signature (C++/Java).""",
    "missing room number": """XOR all listed ids with XOR `0..n` → missing id. **O(n)** time, **O(1)** space.""",
    "bipartite graph": """No odd cycle; 2-colorable with BFS/DFS. Odd cycle graph → not bipartite.""",
    "final keyword": """`final` class — no subclass; `final` method — no override; `final` field — assign once.""",
    "customers who have placed": """`JOIN` + `GROUP BY` + `HAVING SUM(total) > 1000` or subquery on aggregated orders.""",
    "diamond problem": """Two parents share grandparent method — ambiguous which `foo()` inherits. Java: no multiple class inheritance; interfaces + default methods need explicit `Interface.super.method()`.""",
    "multiple inheritence": """Java: **one class**, many interfaces. C++: multiple inheritance with virtual base to fix diamond.""",
    "spring boot": """Mention: auto-configuration, starter dependencies, embedded Tomcat, `@RestController`, Spring Data JPA, Spring Security, Actuator — only what you used.""",
    "e-commerce site": """**List view:** denormalized summary table or `products` with indexed columns for cards.

**Detail view:** `product_id` PK; lazy-load description, images, specs.

API: `GET /products?page=` vs `GET /products/:id`. Cache list; CDN images.""",
    "ticket management": """Roles: Admin, TicketMaster, Cashier, Checker, User. ERD: `users`, `roles`, `ticket_types`, `tickets`, `payments`, `validations`. RBAC on endpoints. Wireframe checkout + admin flows.""",
    "task management system": """REST API: auth JWT, CRUD tasks scoped to `user_id`. Postgres + ORM, bcrypt passwords, validation, unit tests, OpenAPI docs.""",
    "favourite project": """Structure: problem, your role, stack, trade-offs, metrics, what you'd improve. Align with BS23 Java/Spring if claimed.""",
    "primitive and non primitive": """Primitives: fixed size, stack/value (Java). Reference types: objects on heap, variables hold reference. Primitives reassigned by copy; object fields mutable unless immutable class.""",
    "strings immutable": """Security (thread-safe), string pool interning, stable hash keys. Changing requires new object (`StringBuilder` for builds).""",
    "algorithm is best suited": """Match problem to algorithm: shortest path unweighted → BFS; weighted → Dijkstra; MST → Kruskal/Prim; connectivity → Union-Find; strings → KMP/trie.""",
    "time complexity of the code": """Count nested loops, recurrences, log factors. Common: single loop O(n), nested O(n²), halving O(log n), sort inside loop O(n log n).""",
    "compiled or interpreted": """JavaScript is **interpreted** with **JIT** compilation (V8, SpiderMonkey). Source → AST → bytecode → optimized machine code on hot functions.

Not AOT-compiled like C. TypeScript only strips types; output is still JS.

**Interview:** contrast Java bytecode + JVM JIT; mention WebAssembly for native speed in browser.""",
    "divisible by m": """Count digit permutations of `N` divisible by `M` without leading zeros (digit DP / backtracking with remainder).

State: bitmask of used positions + `rem % M` + `started` flag. Answer for `104`, `M=2`: 104, 140, 410 → **3**.""",
    "permuting the digits": """Count digit permutations of `N` divisible by `M` without leading zeros (digit DP / backtracking with remainder).

State: bitmask of used positions + `rem % M` + `started` flag. Answer for `104`, `M=2`: 104, 140, 410 → **3**.""",
    "customer reaches out": """**SJT:** balance policy vs customer obsession. Acknowledge frustration; explore credits/escalation; avoid cold policy-only response (strong A).""",
    "coworker are working": """**SJT:** prefer discussing disagreement before committing (B). Shows Earn Trust / disagree and commit.""",
    "poisoned candy": """**10 rats** for 1000 bottles — binary encoding: rat `i` drinks all bottles whose index has bit `i` set. One hour → **⌈log₂ 1000⌉ = 10** rats minimum.""",
    "rectangular region": """Equal **area** does not determine **perimeter**. 4×4 square vs 8×2 rectangle: same area 16, perimeters 16 vs 20.""",
    "food to eat": """Open-ended aptitude/HR — answer sincerely; shows communication, not CS.""",
    "actor do you like": """Personality/aptitude — brief answer with reason; assess culture fit.""",
    "feel sad the most": """Emotional intelligence question — honest, professional tone.""",
    "favourite project": """STAR format: Situation, Task, Action, Result. Mention stack, your role, measurable outcome.""",
    "ticket management system": """Role-based ticket system: Admin, TicketMaster, Cashier, Checker, User. ERD + wireframes + SQL for reports; RBAC on actions.""",
    "task management system": """Week-long project: JWT auth, CRUD tasks, REST, validation, tests, README, public Git repo.""",
    "this' refer": """`this` refers to the **current instance** being constructed; `this.name = name` disambiguates parameter from field.""",
}


def match_topic_theory(question: str) -> str | None:
    q = question.lower()
    for key in sorted(TOPIC_THEORY.keys(), key=len, reverse=True):
        if key in q:
            return TOPIC_THEORY[key]
    return None


def match_js(question: str):
    q = question.lower()
    for key, code, walk, t, s, e in JS_SOLUTIONS:
        if key in q:
            return (code, walk, t, s, e)
    return None


def enrich_article(block: str, company: str) -> str:
    block = rename_show_answer(block)
    pre = re.split(r"<details>", block, maxsplit=1)[0]
    if pre.startswith("<article>"):
        pre_body = pre[len("<article>"):].strip()
    else:
        pre_body = pre.strip()
    pre_body = re.sub(r"\s*</article>\s*$", "", pre_body, flags=re.I).strip()

    question = extract_question(pre_body)
    details_parts = re.findall(r"<details><summary>([^<]+)</summary>\s*(.*?)</details>", block, re.S)

    main_theory_body = ""
    cpp_block = None
    other_details = []

    for title, body in details_parts:
        t = title.strip()
        if t == "Theory and explanation":
            main_theory_body, cpp = split_cpp_from_details(body)
            if cpp:
                cpp_block = cpp
        else:
            other_details.append((title, body))

    topic = match_topic_theory(question)
    if topic:
        topic_key = re.sub(r"\s+", " ", topic.strip().lower())[:120]
        body_key = re.sub(r"\s+", " ", main_theory_body.strip().lower())[:120]
        if topic_key != body_key and topic_key not in main_theory_body.lower():
            main_theory_body = (
                (topic + "\n\n" + main_theory_body).strip() if main_theory_body else topic
            )

    if not main_theory_body:
        main_theory_body = match_topic_theory(question) or (
            "**Study note:** Original prompt was incomplete in sources. Review the standard CS definition for this MCQ pattern.\n\n"
            f"**Prompt:** {question[:300]}"
        )

    main_theory_body = wrap_theory_body(main_theory_body, question)

    # Behavioural SJT intro (prepend theory section; keep Show Options)
    sjt_theory = ""
    if any(t == "Show Options" for t, _ in other_details) and "customer reaches out" in question.lower() or "coworker" in question.lower():
        pass  # generic wrap_theory_body covers

    new_parts = ["<article>", "", pre_body, ""]

    new_parts.append("<details><summary>Theory and explanation</summary>")
    new_parts.append("")
    new_parts.append(main_theory_body.strip())
    new_parts.append("")
    new_parts.append("</details>")
    new_parts.append("")

    js_match = match_js(question)
    if js_match and js_match[0]:
        code, walk, t, s, e = js_match
        new_parts.append(add_js_section(code, walk, t, s, e).strip())
        new_parts.append("")

    if cpp_block:
        new_parts.append(add_cpp_section(cpp_block).strip())
        new_parts.append("")

    for title, body in other_details:
        new_parts.append(f"<details><summary>{title}</summary>")
        new_parts.append("")
        new_parts.append(body.strip())
        new_parts.append("")
        new_parts.append("</details>")
        new_parts.append("")

    new_parts.append("</article>")
    return "\n".join(new_parts)


def process_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    company = path.stem
    header_match = re.search(r"^(.*?)(<article>)", text, re.S)
    if not header_match:
        print(f"No articles in {path}")
        return
    header = header_match.group(1)
    article_blocks = re.findall(r"<article>.*?</article>", text, re.S)
    enriched = [enrich_article(b, company) for b in article_blocks]
    out = header.rstrip() + "\n\n" + "\n\n".join(enriched) + "\n"
    path.write_text(out, encoding="utf-8")
    theory_count = out.count("Theory and explanation")
    print(f"{path.name}: {len(article_blocks)} articles, {theory_count} theory sections")


def add_missing_js(text: str) -> str:
    """Append JavaScript tab to articles that lack one."""
    generic_js = """```js
// Illustrative pattern — adapt naming and types in the interview
function solve(input) {
  // 1. Validate input
  // 2. Apply algorithm from theory tab
  // 3. Return result
  return input;
}
```
"""
    generic_footer = js_footer(
        "Walk through validation, core logic from the theory section, and return value.",
        "See theory tab (typical O(n)–O(n log n) for array/graph MCQs)",
        "O(1)–O(n) auxiliary depending on approach",
        "Empty input, single element, duplicates, overflow, and off-by-one bounds.",
    )

    def replacer(match: re.Match) -> str:
        block = match.group(0)
        if "Solution (JavaScript)" in block:
            return block
        q = extract_question(block)
        js_match = match_js(q)
        if js_match:
            code, walk, t, s, e = js_match
            section = add_js_section(code, walk, t, s, e)
        else:
            q_lower = q.lower()
            if any(
                k in q_lower
                for k in (
                    "what is",
                    "difference between",
                    "why ",
                    "explain",
                    "principle",
                    "advantage",
                    "disadvantage",
                    "sjt",
                    "feel ",
                    "food ",
                    "actor ",
                )
            ) and "code" not in q_lower and "snippet" not in q_lower:
                section = f"""<details><summary>Solution (JavaScript)</summary>

```js
// Conceptual demo — not always required for pure theory MCQs
const example = {{ topic: "interview-answer", depth: "definition + example + trade-off" }};
console.log(JSON.stringify(example, null, 2));
```

{js_footer(
    "Use this tab to show you can express ideas in code when asked; focus verbal answer on theory.",
    "N/A (conceptual)",
    "N/A (conceptual)",
    "N/A — no algorithmic edge cases.",
)}
</details>"""
            else:
                section = f"<details><summary>Solution (JavaScript)</summary>\n\n{generic_js}\n{generic_footer}\n</details>"
        return block.replace("</article>", f"\n{section.strip()}\n\n</article>")

    return re.sub(r"<article>.*?</article>", replacer, text, flags=re.S)


def cleanup_generic_theory(text: str) -> str:
    text = re.sub(
        r"Prepare a structured verbal answer: definition, example, and trade-off\.\s*",
        "",
        text,
    )
    for art in reversed(list(re.finditer(r"<article>.*?</article>", text, re.S))):
        block = art.group(0)
        if "Tie your answer to Exabyting/BS23" not in block:
            continue
        q = extract_question(block)
        topic = match_topic_theory(q)
        if topic and "Theory and explanation" in block:
            block2 = re.sub(
                r"(<details><summary>Theory and explanation</summary>\s*\n\n)(.*?)(\n\n\*\*Interview talking points\*\*)",
                lambda m: m.group(1)
                + (topic + "\n\n" + m.group(2).strip() + "\n\n").replace(
                    "Tie your answer to Exabyting/BS23 stack (Java, Spring, Node, React) when relevant.\n- Mention trade-offs (time vs space, consistency vs availability) if applicable.",
                    "Lead with a direct answer, then one example and one trade-off.",
                )
                + m.group(3),
                block,
                count=1,
                flags=re.S,
            )
            text = text[: art.start()] + block2 + text[art.end() :]
    return text


def main():
    print("Use scripts/cleanup_enrichment.py to fix duplicates and placeholder tabs.")
    for p in (EXABYTING, BS23):
        process_file(p)


if __name__ == "__main__":
    main()
