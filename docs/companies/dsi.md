---
description: DSI interview questions, DSI interview stages, DSI interview details, DSI interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/dsi
---
# DSI

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-| :- |
| Founding year | 2001  |
| Company Website | https://www.dsinnovators.com/ |
| Career Website | https://app.hrythmic.com/recruit/openings/company/dsinnovators/ |
| Technologies Used| Java, Springboot, Nodejs(hapi), Hibernate, ReactJs, NextJs, AngularJS, Android, iOS |

## Introduction
[Dynamic Solution Innovators Ltd](https://www.dsinnovators.com/) is an international software company based in Dhaka, Bangladesh. They have been successfully providing software services since 2001 in both the local and global market.
## Interview Stages
DSI takes a on campus written test first. The questions contain some coding problem, Database, writting sql, OOP etc
The second stage is face to face interview

## Questions
<article>

There is an array initially containing n numbers. then each of the numbers of the array is multiplied by 2. Now the array is 2 * n size and each element of the array gets shuffled. You are given the shuffled array of size 2 * n. You have to restore the original array.

[**💻 Submit Code**](https://supecoder.dev/questions/Find%20Original%20Array%20From%20Doubled%20Array?questionId=66ae10189e71a163cdd2011b)

<details><summary>Theory and explanation</summary>

[Find Original Array From Doubled Array](https://leetcode.com/problems/find-original-array-from-doubled-array/) — given `changed` of length `2n`, recover original `arr` of length `n` where each `x` in `arr` appears as `x` and `2x` in the doubled multiset (after shuffle).

**Greedy with sorting**

1. Sort `changed`.
2. Use a **frequency map** (or multiset) of available counts.
3. For each value `x` in ascending order:
   - If `x` has positive count, it must be an original element (or half of a pair — process smallest unpaired first).
   - Push `x` to answer; consume one `x` and one `2x` from counts.
4. If any `2x` is missing, impossible.

**Why sort ascending?** Smallest unmatched value must be an original — doubles would have been paired already.

**Interview talking points**

- Odd-length array → impossible.
- Zeros need special care: pairs `(0,0)`.
- Time O(n log n) from sort; O(n) with bucket sort if value range is small.

#### Further reading

- [LeetCode: Find Original Array From Doubled Array](https://leetcode.com/problems/find-original-array-from-doubled-array/) — official tests
- [GeeksforGeeks: Restore array from doubled](https://www.geeksforgeeks.org/) — multiset pairing
- [Supecoder: Find Original Array](https://supecoder.dev/questions/Find%20Original%20Array%20From%20Doubled%20Array?questionId=66ae10189e71a163cdd2011b) — practice link

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function findOriginalArray(changed) {
  if (changed.length % 2 !== 0) return [];

  const freq = new Map();
  for (const x of changed) freq.set(x, (freq.get(x) || 0) + 1);

  const sorted = [...changed].sort((a, b) => a - b);
  const ans = [];

  for (const x of sorted) {
    if (!freq.get(x)) continue;
    const double = x * 2;
    if (!freq.get(double)) return [];
    freq.set(x, freq.get(x) - 1);
    freq.set(double, freq.get(double) - 1);
    ans.push(x);
  }

  return ans.length === changed.length / 2 ? ans : [];
}
```

#### Code walkthrough

- **`freq`** — tracks how many of each value remain unused.
- **Skip processed** — `freq.get(x) === 0` means already paired.
- **Pair `x` with `2x`** — append `x` to original; decrement both counts.
- **Validate** — answer length must be `n`.

#### Complexity

| | |
|-|-|
| Time | O(n log n) due to sort |
| Space | O(n) for map |

#### Edge cases

- **Cannot restore** — return `[]` or `false` per API.
- **Negative numbers** — doubling still works; sort handles sign.
- **Duplicates** — map counts essential.

</details>

<details><summary>Solution (other languages)</summary>

```C++
bool restoreDouble(vector<int> input,vector<int>& output){
    int n = input.size();
    map<int,int> marked;
    sort(input.begin(),input.end());
    for(int i=0;i<n;i++){
        if( marked[ input[i] ] == 0 ) {
            output.push_back( input[i] );
            marked[ 2*input[i] ] ++;
        }else{
            marked[ input[i] ]--;
        }
    }
    for( auto entry:marked ){
        if( entry.second != 0 ) return false;
    }
    return true;
}
```

</details>

</article>

<article>

Given n inputs each with n bits, output a number which was not in the given inputs and has n bits too.

<details><summary>Theory and explanation</summary>

You have **n** distinct (typically) **n-bit** binary numbers. There are **2^n** possible n-bit strings, but only **n** are used — so **many** missing values exist; you need **any** n-bit integer not in the set.

**Approach 1: Bitwise trie / prefix tree**

- Insert each number’s bit representation (MSB first).
- Walk the trie; at each depth choose a child bit (0 or 1) that has **fewer** entries or is **empty** — guarantees a number not in the set (pigeonhole on branches).
- O(n²) bit operations for n numbers of n bits.

**Approach 2: XOR / parity (when n = 2^k - 1 special cases)**

- Classic “find missing duplicate” variants use XOR of all values and all indices — only works for specific structured sets.

**Approach 3: Brute for small n**

- Put all inputs in a `Set`; try `0 … 2^n - 1` until not in set.

**Interview talking points**

- Clarify bit width n and whether numbers can have leading zeros.
- Mention pigeonhole: 2^n slots, n inputs → at least 2^n - n missing values.
- Prefer constructive O(n²) bit walk over exponential brute when n is up to ~20–30.

#### Further reading

- [GeeksforGeeks: Trie](https://www.geeksforgeeks.org/trie-insert-and-search/) — prefix tree for bit strings
- [MIT 6.006: Finding a missing integer](https://ocw.mit.edu/) — XOR tricks and variants
- [CP-Algorithms: Trie](https://cp-algorithms.com/string/trie.html) — bitwise insertion

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function findMissingNBitNumber(inputs, n) {
  const used = new Set(inputs);
  for (let x = 0; x < 1 << n; x++) {
    if (!used.has(x)) return x;
  }
  return -1;
}
```

#### Code walkthrough

- **`used` Set** — O(1) membership.
- **Brute** — acceptable when `2^n` is small (n ≤ 20).
- **Greedy prefix** — builds a number bit-by-bit avoiding collisions with existing prefixes.

#### Complexity

| | |
|-|-|
| Time | O(2^n) brute; O(n²) greedy bit trie walk |
| Space | O(n) for the set |

#### Edge cases

- **All 2^n values present** — impossible if exactly n inputs and n &lt; 2^n.
- **n = 0** — define separately.
- **Signed vs unsigned** — use unsigned n-bit range `0 … 2^n-1`.

</details>

</article>

<article>

What are the 7 layers in OSI networking model? 

<details><summary>Theory and explanation</summary>

The **OSI model** (Open Systems Interconnection) splits network communication into **7 layers**. Memorize bottom-up:

| Layer | Name | Role |
|-------|------|------|
| 7 | **Application** | HTTP, DNS, SMTP — user-facing protocols |
| 6 | **Presentation** | Encoding, encryption, compression (TLS often grouped here) |
| 5 | **Session** | Session management, dialogs |
| 4 | **Transport** | TCP, UDP — end-to-end delivery, ports |
| 3 | **Network** | IP, routing — logical addressing |
| 2 | **Data Link** | Ethernet, MAC, frames |
| 1 | **Physical** | Bits on wire / radio |

**Mnemonic (bottom → top):** “Please Do Not Throw Sausage Pizza Away” (Physical → Application).

**Interview talking points**

- **TCP/IP model** has 4 layers — map OSI to it (Application ≈ 5–7, Transport = 4, Internet = 3, Link = 2–1).
- Real stacks blur layers 5–6 into application libraries.
- Example path: browser HTTPS = Application + TLS (presentation) over TCP (transport) over IP (network).

![](https://cf-assets.www.cloudflare.com/slt3lc6tev37/6ZH2Etm3LlFHTgmkjLmkxp/59ff240fb3ebdc7794ffaa6e1d69b7c2/osi_model_7_layers.png)

#### Further reading

- [Cloudflare: OSI model](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/) — diagram and summary
- [IBM: OSI model explained](https://www.ibm.com/topics/osi-model) — layer responsibilities
- [RFC 1122](https://datatracker.ietf.org/doc/html/rfc1122) — Internet host requirements (TCP/IP)
- [MDN: HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview) — application layer example

</details>

<details><summary>Solution (JavaScript)</summary>

Use as a **study map** (not executable networking code):

```js
const OSI_LAYERS = [
  { layer: 7, name: 'Application', examples: ['HTTP', 'DNS', 'FTP'] },
  { layer: 6, name: 'Presentation', examples: ['TLS', 'JPEG', 'ASCII'] },
  { layer: 5, name: 'Session', examples: ['RPC session', 'NetBIOS'] },
  { layer: 4, name: 'Transport', examples: ['TCP', 'UDP'] },
  { layer: 3, name: 'Network', examples: ['IP', 'ICMP', 'routing'] },
  { layer: 2, name: 'Data Link', examples: ['Ethernet', 'MAC', 'ARP'] },
  { layer: 1, name: 'Physical', examples: ['cables', 'fiber', 'Wi-Fi radio'] },
];
```

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases

- **Where is TLS?** — often cited at Presentation; practically spans Application too.
- **ICMP** — Network layer (layer 3), not Transport.

</details>

</article>

<article>

Given a string s, find the longest substring between two identical character.ex: afgksia -> ans: fgksi

<details><summary>Theory and explanation</summary>

For each character `c`, track **first index** where `c` appeared. When `c` appears again at `i`, the substring **strictly between** the two `c`s has length `i - first[c] - 1`.

Example `afgksia`:

- `a` at 0 and 6 → between = `s[1..5]` = `fgksi` (length 5).
- Track **maximum** length over all characters.

This is related to [LeetCode 1629 — Maximum Difference Between Even and Odd Frequency](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency/) style “between same char” problems and simple **first/last index** tracking.

**Interview talking points**

- O(n) one pass with a map of first indices.
- Only **strictly between** — exclude the boundary characters.
- If no char repeats, answer is `''` or `0` length.

#### Further reading

- [LeetCode: Longest Substring Between Equal Characters](https://leetcode.com/problems/longest-substring-between-equal-characters/) — same pattern
- [GeeksforGeeks: Longest substring between repeats](https://www.geeksforgeeks.org/) — first/last index
- [MDN: String slice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice) — extract answer substring

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function longestBetweenEqual(s) {
  const first = new Map();
  let bestLen = -1;
  let best = '';

  for (let i = 0; i < s.length; i++) {
    const ch = s[i];
    if (first.has(ch)) {
      const len = i - first.get(ch) - 1;
      if (len > bestLen) {
        bestLen = len;
        best = s.slice(first.get(ch) + 1, i);
      }
    } else {
      first.set(ch, i);
    }
  }

  return best;
}
```

#### Code walkthrough

- **`first`** — earliest index per character.
- **On repeat** — compute inner length `i - first - 1`; update global max.
- **`slice(first+1, i)`** — substring excluding both boundary chars.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(alphabet) for the map |

#### Edge cases

- **No repeated character** — return `''`.
- **Adjacent duplicate** `aa` — inner length 0.
- **Multiple pairs** — keep longest only.

</details>

</article>

<article>

Given a number n.return true if you find a middle element k such that sum of 1 to k and sum from k to n are equal.if there no one return false.
    ex: 49.
	output: true.
	explanation: 1 + 2 + ... + 35 = 35 + 36 + ... + 49

<details><summary>Theory and explanation</summary>

Let `S(n) = 1 + 2 + … + n = n(n+1)/2`.

We need an integer `k` (the “middle” in the sum sense) such that:

`1 + 2 + … + k = k + (k+1) + … + n`

Left side: `k(k+1)/2`.

Right side: `S(n) - S(k-1) = n(n+1)/2 - k(k-1)/2`.

Equating and simplifying yields:

`k² = n(n+1)/2`

So **`n(n+1)/2` must be a perfect square**. Then `k = sqrt(n(n+1)/2)`.

For `n = 49`: `49×50/2 = 1225 = 35²` → `k = 35` ✓.

**Interview talking points**

- This is a **triangular number** split, not “middle index” of an array.
- Check integer `k` in `[1, n]`.
- O(1) math after verifying perfect square.

#### Further reading

- [Wikipedia: Triangular number](https://en.wikipedia.org/wiki/Triangular_number) — sum formulas
- [LeetCode: Sum of Two Integers (math tricks)](https://leetcode.com/problems/sum-of-two-integers/) — bit/math fluency
- [GeeksforGeeks: Sum of first n natural numbers](https://www.geeksforgeeks.org/program-to-find-sum-of-first-n-natural-numbers/) — `S(n)` formula

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function hasEqualSplitSum(n) {
  const total = (n * (n + 1)) / 2;
  const k = Math.sqrt(total);
  if (!Number.isInteger(k)) return false;
  const left = (k * (k + 1)) / 2;
  const right = total - (k * (k - 1)) / 2;
  return left === right;
}
```

#### Code walkthrough

- **`total`** — sum 1..n.
- **`k = sqrt(total)`** — candidate split point from `k² = total`.
- **Verify** — recompute left and right sums to guard floating-point edge cases (use integer math for large n).

#### Complexity

| | |
|-|-|
| Time | O(1) |
| Space | O(1) |

#### Edge cases

- **n = 1** — no valid k (typically false).
- **Perfect square fails** — return false.
- **Large n** — use `BigInt` if n exceeds safe integer range.

</details>

</article>

<article>

Apply database normalization technique to the following table

student table:
|student_id | name    | course_name | course_fee |
| :-: | :- | :- | :-: |
| 1 	   | shakib  | DSA         | 400	  |
| 2 	   | rakib   | Algorithms  | 100	  |
| 3 	   | showrov | Networking  | 300	  |
| 4 	   | kalam   | Algorithms  | 100	  |

<details><summary>Theory and explanation</summary>

The table violates **1NF** if repeating groups exist; it clearly violates **2NF** and **3NF** because `course_fee` depends on **`course_name`**, not on the whole key `(student_id, course_name)` if enrollment is the intent — and `name` depends only on `student_id`.

**Decompose to 3NF**

1. **`Student(student_id, name)`**
2. **`Course(course_name, course_fee)`**
3. **`Enrollment(student_id, course_name)`** — many-to-many link

| student_id | name    |
|------------|---------|
| 1 | shakib |
| 2 | rakib |
| … | … |

| course_name | course_fee |
|-------------|------------|
| DSA | 400 |
| Algorithms | 100 |
| Networking | 300 |

| student_id | course_name |
|------------|-------------|
| 1 | DSA |
| 2 | Algorithms |
| … | … |

**Anomalies in original**

- **Update anomaly** — change Algorithms fee in multiple rows.
- **Insert anomaly** — cannot add a course without a student.
- **Delete anomaly** — delete last enrollment loses course fee info.

#### Further reading

- [GeeksforGeeks: Normal forms](https://www.geeksforgeeks.org/normal-forms-in-dbms/) — 1NF–BCNF summary
- [IBM: Database normalization](https://www.ibm.com/topics/database-normalization) — practical guide
- [W3Schools SQL JOIN](https://www.w3schools.com/sql/sql_join.asp) — query normalized schema
- [Martin Kleppmann: Designing Data-Intensive Applications](https://dataintensive.net/) — when to denormalize

</details>

<details><summary>Solution (JavaScript)</summary>

Normalized schema as executable documentation:

```js
const schema = {
  Student: ['student_id', 'name'],
  Course: ['course_name', 'course_fee'],
  Enrollment: ['student_id', 'course_name'],
};

// Example query: students in Algorithms with fee
const sql = `
SELECT s.student_id, s.name, c.course_fee
FROM Student s
JOIN Enrollment e ON e.student_id = s.student_id
JOIN Course c ON c.course_name = e.course_name
WHERE c.course_name = 'Algorithms';
`;
```

#### Complexity

| | |
|-|-|
| Time | N/A (design) |
| Space | N/A |

#### Edge cases

- **Same course name, different fees** — not allowed; course is entity with one fee.
- **Composite key** — enrollment PK `(student_id, course_name)`.

</details>

</article>

<article>

Explain ACID properties

<details><summary>Theory and explanation</summary>

**ACID** describes guarantees of **database transactions**:

| Property | Meaning |
|----------|---------|
| **Atomicity** | All statements in a transaction commit or **none** do (rollback on failure). |
| **Consistency** | Transaction moves DB from one **valid state** to another (constraints, invariants). |
| **Isolation** | Concurrent transactions do not **interfere** as if run serially (isolation levels: READ COMMITTED, REPEATABLE READ, SERIALIZABLE). |
| **Durability** | After commit, data survives **crash** (WAL, disk flush). |

> [!IMPORTANT]
> Atomicity, isolation, and durability are primarily **DBMS** mechanisms; **consistency** also depends on **application** rules (valid balances, foreign keys). Martin Kleppmann notes the “C” was partly acronym convenience in *Designing Data-Intensive Applications*.

**Interview talking points**

- Contrast with **BASE** (eventual consistency) in NoSQL.
- Example: bank transfer — debit and credit must be atomic.
- Mention isolation anomalies: dirty read, non-repeatable read, phantom read.

#### Further reading

- [IBM: ACID properties](https://www.ibm.com/topics/acid-properties) — overview
- [PostgreSQL: Transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — levels in practice
- [Martin Kleppmann: DDIA](https://dataintensive.net/) — deep consistency discussion
- [MySQL: InnoDB ACID](https://dev.mysql.com/doc/refman/8.0/en/mysql-acid.html) — engine implementation

</details>

<details><summary>Solution (JavaScript)</summary>

Illustrate **atomicity** with a transactional pseudo-API:

```js
async function transfer(db, fromId, toId, amount) {
  await db.beginTransaction();
  try {
    await db.execute('UPDATE accounts SET balance = balance - ? WHERE id = ?', [
      amount,
      fromId,
    ]);
    await db.execute('UPDATE accounts SET balance = balance + ? WHERE id = ?', [
      amount,
      toId,
    ]);
    await db.commit(); // durability + isolation handled by engine
  } catch (e) {
    await db.rollback(); // atomicity: neither update persists
    throw e;
  }
}
```

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases

- **Partial failure** — rollback required for atomicity.
- **Long transactions** — isolation locks hurt throughput.

</details>

</article>

<article>

Explain static keyword

<details><summary>Theory and explanation</summary>

Meaning depends on **language**:

### Java / C# / C++

- **`static` field** — one copy per **class**, shared by all instances.
- **`static` method** — called on class; no implicit `this` / instance.
- **`static` nested class** — no outer instance required (Java).
- **Static initialization block** — runs once when class loads.

### C

- **`static` global** — internal linkage (file scope).
- **`static` local** — persists between calls, not thread-safe by default.

### JavaScript

- No `static` keyword in classic JS; **class static** fields/methods in ES2022: `static foo() {}`.
- Module-level `const` acts like shared singleton.

**Interview talking points**

- Use static for **utilities** (`Math.abs`), **counters**, **caches** — avoid when instance state is needed.
- Thread safety: static mutable fields need synchronization in multi-threaded apps.
- Contrast with **singleton pattern**.

#### Further reading

- [Oracle Java Tutorial: static](https://docs.oracle.com/javase/tutorial/java/javaOO/classvars.html) — fields and methods
- [MDN: static (JavaScript classes)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static) — ES class syntax
- [cppreference: static storage duration](https://en.cppreference.com/w/cpp/language/storage_duration) — C++ semantics

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class Counter {
  static count = 0;

  static increment() {
    Counter.count++;
  }
}

Counter.increment();
Counter.increment();
console.log(Counter.count); // 2
```

Java-style example (for pen-and-paper comparison):

```java
class App {
  static int instances = 0;
  App() { instances++; }
  static int getInstances() { return instances; }
}
```

#### Complexity

| | |
|-|-|
| Time | N/A (language feature) |
| Space | Static fields live for program lifetime |

#### Edge cases

- **Static vs instance method** — cannot access instance fields without object.
- **Classloader / hot reload** — static state may survive unexpectedly in servers.

</details>

</article>

<article>

What is significance of this below operation?

```
a=a^b;
b=a^b;
a=a^b;
```
   
<details><summary>Theory and explanation</summary>

This **XOR swap** exchanges values of `a` and `b` **without a temporary third variable**, using the identity:

- `x ^ x = 0`
- `x ^ 0 = x`
- XOR is **associative and commutative**

**Step trace**

1. `a = a ^ b` — holds combined XOR
2. `b = a ^ b` — cancels old `a`, leaves original `b`
3. `a = a ^ b` — cancels old `b`, leaves original `a`

**Caveats**

- In C/C++, **undefined behavior** if `a` and `b` alias the same memory (`a` and `b` are the same variable).
- Modern compilers optimize `tmp` swap better — XOR swap is mostly **interview trivia**.

#### Further reading

- [GeeksforGeeks: Swap two numbers without temp](https://www.geeksforgeeks.org/swap-two-numbers-without-using-temporary-variable/) — XOR and arithmetic tricks
- [Wikipedia: XOR swap algorithm](https://en.wikipedia.org/wiki/XOR_swap_algorithm) — history and pitfalls
- [MDN: Bitwise XOR](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_XOR) — operator reference

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function xorSwap(a, b) {
  if (a === b) return [a, b]; // same reference/value — avoid broken swap
  a = a ^ b;
  b = a ^ b;
  a = a ^ b;
  return [a, b];
}
```

#### Code walkthrough

- Three XOR assignments rotate values through combined XOR state.
- **Guard** when `a === b` — in JS numbers, XOR still works; issue is aliasing same variable in C.

#### Complexity

| | |
|-|-|
| Time | O(1) |
| Space | O(1) |

#### Edge cases

- **Aliasing** `swap(&x, &x)` — never do in C++.
- **Floating-point** — XOR swap applies to integer bit patterns only.

</details>

<details><summary>Solution (other languages)</summary>

Swaps the value of a and b without a third variable using bit manipulation

</details>

</article>

<article>

Difference between authentication and authorization

<details><summary>Theory and explanation</summary>

| | **Authentication (AuthN)** | **Authorization (AuthZ)** |
|--|---------------------------|---------------------------|
| **Question** | Who are you? | What may you do? |
| **When** | Login, token issue | After identity known |
| **Examples** | Password, OAuth, MFA, biometrics | RBAC, ACL, policy engine, scopes |
| **Failure** | 401 Unauthorized | 403 Forbidden |

**Flow**

1. User **authenticates** → receives session/JWT.
2. Each request: system **authorizes** action against roles/policies.

**Interview talking points**

- JWT **claims** (`sub`, `roles`, `scope`) bridge both steps.
- **OAuth 2.0** — authorization framework; **OpenID Connect** adds authentication on top.
- Least privilege: authorize minimal permissions per role.

#### Further reading

- [OWASP: Authentication vs Authorization](https://cheatsheetseries.owasp.org/) — security cheat sheets
- [Auth0: AuthN vs AuthZ](https://auth0.com/docs/get-started/identity-fundamentals/authentication-and-authorization) — clear definitions
- [RFC 6749: OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749) — delegated authorization
- [NIST Digital Identity Guidelines](https://pages.nist.gov/800-63-3/) — modern identity practices

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function login(username, password, users) {
  const user = users.find((u) => u.username === username);
  if (!user || user.passwordHash !== hash(password)) {
    return { authenticated: false };
  }
  return { authenticated: true, userId: user.id, roles: user.roles };
}

function canDeleteInvoice(user, invoice) {
  if (!user.authenticated) return false; // AuthN first
  if (user.roles.includes('admin')) return true; // AuthZ
  return invoice.ownerId === user.userId;
}
```

#### Complexity

| | |
|-|-|
| Time | N/A (policy-dependent) |
| Space | N/A |

#### Edge cases

- **Authenticated but forbidden** — 403, not 401.
- **Anonymous public routes** — skip AuthN; still check resource-level AuthZ if needed.

</details>

</article>

<article>

Given three value `a,b,c`, write a program to determine if we can make a traingle using these as side lengths.

<details><summary>Theory and explanation</summary>

Three lengths `a`, `b`, `c` form a **non-degenerate triangle** iff:

1. `a + b > c`
2. `a + c > b`
3. `b + c > a`

Equivalently: sort `[x ≤ y ≤ z]` and check **`x + y > z`** only.

**Interview talking points**

- Strict inequality — equality `a+b=c` is a **degenerate** line, not a triangle.
- Negative sides — invalid immediately.
- Float sides — beware precision; use epsilon or rational math.

#### Further reading

- [GeeksforGeeks: Check triangle validity](https://www.geeksforgeeks.org/check-if-three-sides-form-a-valid-triangle/) — inequality check
- [Wikipedia: Triangle inequality](https://en.wikipedia.org/wiki/Triangle_inequality) — math definition
- [LeetCode: Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/) — array variant

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function isTriangle(a, b, c) {
  if (a <= 0 || b <= 0 || c <= 0) return false;
  const sides = [a, b, c].sort((x, y) => x - y);
  return sides[0] + sides[1] > sides[2];
}
```

#### Code walkthrough

- **Reject non-positive** sides.
- **Sort** — single check `smallest + middle > largest` covers all three inequalities.

#### Complexity

| | |
|-|-|
| Time | O(1) |
| Space | O(1) |

#### Edge cases

- **Equal sides** — equilateral: `1,1,1` → true.
- **Almost degenerate** `1,2,3` → `1+2` is not `> 3` → false.

</details>

</article>
