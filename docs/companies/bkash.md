---
description: Bkash, Bkash Software Engineer, Bkash interview questions, Bkash interview stages, Bkash interview details, Bkash interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/bkash
---
# Bkash

| <img width="441" height="1"> | <img width="441" height="1"> |
| :--------------------------- | :--------------------------- |
| Founding year                | 2010                         |
| Company Website              | https://www.bkash.com/       |
| Career Website               | https://careers.bkash.com/   |
| Technologies Used            | Java, Spring Boot, React, FastAPI, PostgreSQL, Redis, Microservices |

## Introduction
Bkash Ltd. is a leading mobile financial service (MFS) provider in Bangladesh, focused on enabling digital financial inclusion. It is a subsidiary of BRAC Bank and partners with global players like Ant Financial.

Core Products & Services:

- Mobile Wallet Services: Send money, cash out, pay bills, mobile recharge, savings, donations, etc.
- Enterprise API Integration: For merchant payments and corporate disbursements.
- bKash App: Their core platform available on Android/iOS.

## Interview Stages:

Bkash interviews generally involve 3–4 rounds:
Stage	Format	Description
1. **Written Test**:	In-person/Online	Algorithms, data structures, OOP concepts, OS questions
2. **Technical Interview**:	Face-to-face/Virtual	Problem solving, system design, React/REST APIs, DB
3. **Engineering/Team Round**:	Panel	Deeper technical dive with team leads/managers
4. **HR Round** (optional):	Virtual/In-person	Behavioral questions, salary expectations, career plans

## Topics:

- Real-time coding
- Time & space complexity analysis
- System design (OOP-focused)
- REST API, CRUD operations
- Frontend/backend practicals (React, FastAPI)
- Database & OS-level concepts

## Questions

<article>

Given the head of a linked list, remove all duplicate elements so that each value appears only once. Return the modified head of the linked list.

[**💻 Submit Code**](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

<details><summary>Theory and explanation</summary>

If the list is **sorted**, duplicates are **adjacent** — scan once and skip repeated values (LeetCode 83). If **unsorted**, track seen values with a **hash set** and rebuild or use dummy-head pointer surgery.

**Sorted approach (one pass)**

- Keep pointer `cur`; while `cur.next` exists, if `cur.val === cur.next.val`, skip all nodes with that value (`cur.next = cur.next.next`).
- Else advance `cur`.

**Unsorted approach**

- Use `Set` of seen values; dummy node before head; if value already seen, remove node; else add to set.

**bKash interview angle**

- State whether input is sorted — MFS pipelines often assume ordered transaction IDs but clarify.
- Mention **stable** vs **in-place** mutation; O(1) extra space only for sorted case.

#### Further reading

- [LeetCode 83: Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) — adjacent duplicate removal
- [LeetCode 82: Remove Duplicates II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) — remove all nodes with duplicate values
- [Visualgo: Linked List](https://visualgo.net/en/list) — pointer manipulation animation

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function ListNode(val, next = null) {
  this.val = val;
  this.next = next;
}

// Assumes sorted ascending list
function deleteDuplicates(head) {
  let cur = head;
  while (cur && cur.next) {
    if (cur.val === cur.next.val) {
      cur.next = cur.next.next;
    } else {
      cur = cur.next;
    }
  }
  return head;
}

// Unsorted variant
function deleteDuplicatesUnsorted(head) {
  const seen = new Set();
  const dummy = new ListNode(0, head);
  let prev = dummy;
  let cur = head;
  while (cur) {
    if (seen.has(cur.val)) {
      prev.next = cur.next;
    } else {
      seen.add(cur.val);
      prev = cur;
    }
    cur = cur.next;
  }
  return dummy.next;
}
```

#### Code walkthrough

1. **Sorted**: compare `cur` with `cur.next`; on duplicate, bypass without moving `cur`.
2. **Unsorted**: dummy head simplifies head removal; `prev` trails valid chain.
3. Return new head (`head` or `dummy.next`).

#### Complexity

| Case | Time | Space |
|------|------|-------|
| Sorted | O(n) | O(1) |
| Unsorted | O(n) | O(n) set |

#### Edge cases

- **Empty list** — return `null`.
- **All duplicates** — list becomes single node or empty depending on variant.
- **Single node** — unchanged.

</details>

</article>

<article>

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

[**💻 Submit Code**](https://leetcode.com/problems/valid-parentheses/description/)

<details><summary>Theory and explanation</summary>

**Valid parentheses** means every closing bracket matches the **most recent unmatched** opening bracket in LIFO order — classic **stack** problem.

**Algorithm**

1. Push opening brackets onto stack.
2. On closing bracket: stack empty → invalid; pop top must pair with current char.
3. End: stack must be empty.

**Pair map**

`{ ')': '(', '}': '{', ']': '[' }` for O(1) match checks.

**Why stack**

Nested structures are inherently last-opened, first-closed — stack models that exactly.

#### Further reading

- [LeetCode 20: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) — problem statement
- [GeeksforGeeks: Stack data structure](https://www.geeksforgeeks.org/stack-data-structure/) — LIFO operations
- [CP-Algorithms: Stack](https://cp-algorithms.com/data_structures/stack_queue.html) — implementation notes

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function isValid(s) {
  const pairs = { ')': '(', '}': '{', ']': '[' };
  const stack = [];

  for (const ch of s) {
    if (ch === '(' || ch === '{' || ch === '[') {
      stack.push(ch);
    } else {
      if (stack.pop() !== pairs[ch]) return false;
    }
  }
  return stack.length === 0;
}

isValid('()[]{}'); // true
isValid('([)]');  // false
```

#### Code walkthrough

1. Opening chars push onto stack.
2. Closing chars pop and compare to expected opener via `pairs`.
3. `pop()` on empty stack yields `undefined` → mismatch → false.
4. Valid only if stack empty at end.

#### Complexity

| | |
|-|-|
| Time | O(n) — each char pushed/popped once |
| Space | O(n) — worst-case all openings |

#### Edge cases

- **Empty string** — valid (stack empty).
- **Odd length** — cannot be valid.
- **Wrong close order** — `([)]` fails at `)`.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        for (int i = 0; i < s.length(); i++) {
            // if opening bracket, push to stack
            if (s[i] ==  '(' or s[i] == '{' or s[i] == '[') {
                st.push(s[i]);
            } else {
                // if stack is empty, then no matching opening bracket 
                if (st.empty()) {
                    return false;
                } else {
                    char tp = st.top();

                    // check for matching pairs
                    if ((s[i] == ')' and tp == '(') 
                        or (s[i] == '}' and tp == '{') 
                        or s[i] == ']' and tp == '[') {
                            st.pop();
                    }  else {
                        return false;
                    }
                }
            }
        }

        return st.empty(); // if stack is empty, all pairs matched
    }
};
```

</details>
</article>

<article>

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

[**💻 Submit Code**](https://leetcode.com/problems/two-sum/description/)

<details><summary>Theory and explanation</summary>

**Two Sum** — find indices `i, j` with `nums[i] + nums[j] = target`.

**Brute force**: nested loops O(n²).

**Optimal — hash map**

Single pass: for each `nums[i]`, need `target - nums[i]`. If complement exists in map, return indices; else store `nums[i] → i`.

**Why one pass works**

When you see `nums[i]`, only **previous** indices are in the map — guarantees `i ≠ j` and no duplicate use of same element (unless problem allows same index twice, which it does not).

#### Further reading

- [LeetCode 1: Two Sum](https://leetcode.com/problems/two-sum/) — canonical hash-map problem
- [MDN: Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) — key-value lookups in JS
- [GeeksforGeeks: Two Sum](https://www.geeksforgeeks.org/check-if-pair-with-given-sum-exists-in-array/) — alternative approaches

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function twoSum(nums, target) {
  const idx = new Map();

  for (let i = 0; i < nums.length; i++) {
    const need = target - nums[i];
    if (idx.has(need)) {
      return [idx.get(need), i];
    }
    idx.set(nums[i], i);
  }
  return [];
}

twoSum([2, 7, 11, 15], 9); // [0, 1]
```

#### Code walkthrough

1. `need = target - nums[i]` is the complement.
2. If complement already in map, return `[storedIndex, i]`.
3. Otherwise record current value and index before moving on.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(n) hash map |

#### Edge cases

- **No solution** — return `[]` or throw per spec.
- **Negative numbers / duplicates** — hash map handles both.
- **Same value twice** — e.g. `[3,3], 6` works when second 3 finds first in map.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> idx;  // stores number -> index
        idx.reserve(nums.size());     // reserve space to optimize rehashing
        
        vector<int> ans;

        for (int i = 0; i < (int)nums.size(); i++) {
            int need = target - nums[i]; // number we need to reach target

            // if the "need" is already in the map, we found the pair
            auto it = idx.find(need);
            if (it != idx.end()) {
                ans = {it->second, i}; // return indices of the pair
                break;
            }

            // otherwise, store current number with its index
            idx[nums[i]] = i;
        }

        return ans;
    }
};
```

</details>
</article>

<article>

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

[**💻 Submit Code**](https://leetcode.com/problems/reverse-linked-list/description/)

<details><summary>Theory and explanation</summary>

**Iterative reversal** — three pointers: `prev`, `curr`, `next`. For each node, save `curr.next`, point `curr.next` to `prev`, shift window forward.

**Recursive reversal** — reverse rest of list, then attach `head` at tail of reversed suffix.

**Interview talking points**

- Time **O(n)**, space **O(1)** iterative vs **O(n)** recursion stack.
- Dummy head not required for pure reversal but helps when reversing sublists.

#### Further reading

- [LeetCode 206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) — iterative and recursive solutions
- [Visualgo: Linked List](https://visualgo.net/en/list) — reversal animation
- [GeeksforGeeks: Reverse a linked list](https://www.geeksforgeeks.org/reverse-a-linked-list/) — step-by-step diagrams

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function ListNode(val, next = null) {
  this.val = val;
  this.next = next;
}

function reverseList(head) {
  let prev = null;
  let curr = head;
  while (curr) {
    const next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
  }
  return prev;
}
```

#### Code walkthrough

1. `prev` starts `null` (new tail's next).
2. Save `next`, reverse link, advance both pointers.
3. `prev` is new head when `curr` becomes null.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(1) iterative |

#### Edge cases

- **`head === null`** — return `null`.
- **Single node** — returns same node with `next = null`.

</details>

<details><summary>Solution (other languages)</summary>

::: code-group

```C++ [C++ Solution]
#include <bits/stdc++.h>
using namespace std;
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution
{
public:
    void append(ListNode *&head, int value)
    {
        ListNode *newNode = new ListNode(value);
        if (!head)
        {
            head = newNode;
            return;
        }
        ListNode *curr = head;
        while (curr->next)
        {
            curr = curr->next;
        }
        curr->next = newNode;
    }
    void traverse(ListNode *head)
    {
        ListNode *curr = head;
        while (curr)
        {
            cout << curr->val << " ";
            curr = curr->next;
        }
        cout << endl;
    }
    ListNode *reverseList(ListNode *head)
    {
        ListNode *curr = head;
        ListNode *prev = nullptr;

        while (curr)
        {
            ListNode *temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;
    }
};
int main()
{
    Solution solution;
    ListNode *head = nullptr;

    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int value;
        cin >> value;
        solution.append(head, value);
    }

    cout << "Original list: ";
    solution.traverse(head);

    head = solution.reverseList(head);
    cout << "Reversed list: ";
    solution.traverse(head);

    return 0;
}
```

```java [Java Solution]
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode nxt = head.next;
        head.next = null;
        ListNode tail = reverseList(nxt);
        nxt.next = head;
        return tail;
    }
}
```

:::

</details>
</article>

<article>

What is concurrency control in databases? Why is it important?

<details><summary>Theory and explanation</summary>

**Concurrency control** ensures multiple transactions can read/write shared data **simultaneously** without corrupting integrity.

**Problems without it**

- **Lost update** — two writes; last wins, first lost.
- **Dirty read** — read uncommitted data that rolls back.
- **Non-repeatable read** — same row read twice, different values.
- **Phantom read** — range query returns different rows on repeat.

**ACID — Isolation**

Concurrency control implements **I (Isolation)** — each transaction appears to run alone even when interleaved.

**Techniques**

| Technique | Idea |
|-----------|------|
| **Two-phase locking (2PL)** | Growing phase acquire locks; shrinking releases; prevents some conflicts |
| **Timestamp ordering** | Order txs by timestamp; older txs abort on conflict |
| **MVCC** | Keep versions; readers see snapshot (PostgreSQL, InnoDB) |
| **Optimistic concurrency** | Read, validate at commit; retry on conflict |

**Why bKash cares**

Wallet transfers, balance updates, and ledger entries require **serializable** or **repeatable read** semantics — double-spend and race conditions are financial bugs.

#### Further reading

- [PostgreSQL: Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — isolation levels explained
- [CMU 15-445: Concurrency Control](https://15445.courses.cs.cmu.edu/) — academic deep dive
- [GeeksforGeeks: Concurrency Control in DBMS](https://www.geeksforgeeks.org/concurrency-control-in-dbms/) — lock-based protocols
- [Martin Kleppmann: Designing Data-Intensive Applications](https://dataintensive.net/) — MVCC and isolation in production systems

</details>

<details><summary>Solution (JavaScript)</summary>

Illustrative **optimistic locking** pattern (version column) common in payment APIs:

```js
async function transfer(db, fromId, toId, amount) {
  return db.transaction(async (tx) => {
    const from = await tx.query(
      'SELECT balance, version FROM accounts WHERE id = $1 FOR UPDATE',
      [fromId]
    );
    if (from.balance < amount) throw new Error('Insufficient funds');

    await tx.query(
      'UPDATE accounts SET balance = balance - $1, version = version + 1 WHERE id = $2 AND version = $3',
      [amount, fromId, from.version]
    );
    await tx.query(
      'UPDATE accounts SET balance = balance + $1 WHERE id = $2',
      [amount, toId]
    );
  });
}
```

#### Code walkthrough

- **`FOR UPDATE`** — row-level lock (pessimistic) during transaction.
- **Version check** — optimistic layer detects concurrent writers.
- Wrap in **transaction** so debit/credit commit atomically.

#### Complexity

| | |
|-|-|
| Time | O(1) per account row touched |
| Space | O(1) — DB handles lock tables |

#### Edge cases

- **Deadlock** between two transfers — DB deadlock detector aborts one tx.
- **Isolation level too weak** — phantom reads in reporting queries.
- **Long-running tx** — holds locks; keep transactions short in MFS systems.

</details>

</article>

<article>

What is function overriding in Object-Oriented Programming? How is it different from overloading?

<details><summary>Theory and explanation</summary>

**Overloading (compile-time polymorphism)**

- Same **function name**, different **parameter lists** (count, types, order) in the **same scope/class**.
- Resolved at **compile time** by signature matching.
- Return type alone does not distinguish overloads in most languages.

**Overriding (runtime polymorphism)**

- **Subclass** provides specific implementation of a method **already declared** in parent.
- Same name, parameters, and compatible return type (covariant returns in Java/C++).
- Resolved at **runtime** via **virtual dispatch** / vtable (Java `@Override`, C++ `virtual`).
- Enables **Liskov substitution** — treat subclass as parent.

| | Overloading | Overriding |
|-|-------------|------------|
| When bound | Compile time | Runtime |
| Scope | Same class | Parent ↔ child |
| Signature | Must differ | Must match |
| Purpose | Convenience APIs | Specialized behavior |

**bKash stack note**

Java Spring services use overriding for interface implementations; REST controllers overload is rare — prefer default parameters or optional DTO fields in JavaScript/TypeScript frontends.

#### Further reading

- [Oracle Java Tutorial: Overriding and Hiding](https://docs.oracle.com/javase/tutorial/java/IandI/override.html) — `@Override` rules
- [GeeksforGeeks: Overloading vs Overriding](https://www.geeksforgeeks.org/difference-between-method-overloading-and-method-overriding-in-java/) — comparison table
- [MDN: Classes (JS)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) — JS uses overriding; no true overloading

</details>

<details><summary>Solution (JavaScript)</summary>

JavaScript has **overriding** via prototype chain; **overloading** is simulated with optional/rest args or separate names:

```js
class PaymentGateway {
  charge(amount) {
    return { ok: true, amount };
  }
}

class BkashGateway extends PaymentGateway {
  // overriding — same method name, specialized behavior
  charge(amount) {
    const fee = amount * 0.01;
    return { ok: true, amount, fee, provider: 'bkash' };
  }
}

// "Overloading" simulation — one function, multiple arities
function sendMoney(to, amount, note = '') {
  if (typeof to === 'object') {
    ({ to, amount, note = '' } = to);
  }
  return { to, amount, note };
}

new BkashGateway().charge(100); // override at runtime
sendMoney('017…', 500);
sendMoney({ to: '017…', amount: 500, note: 'rent' });
```

#### Code walkthrough

- **`BkashGateway.charge`** overrides parent — runtime picks subclass method.
- **`sendMoney`** uses parameter patterns instead of compile-time overloads.

#### Complexity

| | |
|-|-|
| Time | O(1) dispatch |
| Space | O(1) |

#### Edge cases

- **JS**: accidental "override" if method names collide on plain objects.
- **Java**: `@Override` catches signature typos at compile time.
- **C++**: must mark `virtual` in base for true runtime polymorphism.

</details>

</article>

<article>

What is inheritance in Object-Oriented Programming?

<details><summary>Theory and explanation</summary>

**Inheritance** lets a **derived (child) class** acquire fields and methods of a **base (parent) class**, enabling **reuse**, **extension**, and **polymorphism**.

**Types**

- **Single inheritance** — one parent (Java classes, C++ class).
- **Multiple inheritance** — several parents (C++ classes; Java uses interfaces).
- **Multilevel** — chain of parents (A → B → C).
- **Hierarchical** — one parent, many children.

**Benefits**

- **DRY** — shared logic in base class.
- **Polymorphism** — `Base ref = new Derived()` calls overridden methods.
- **Modeling IS-A** — `SavingsAccount IS-A BankAccount`.

**Risks**

- **Fragile base class** — parent change breaks children.
- **Deep hierarchies** — hard to reason; prefer **composition over inheritance**.

**Family tree analogy**

Grandfather (base) → Father (derived, adds traits) → Son (further derived). Each level inherits upstream behavior and may override or extend.

#### Further reading

- [Oracle Java Tutorial: Inheritance](https://docs.oracle.com/javase/tutorial/java/IandI/subclasses.html) — extends keyword
- [GeeksforGeeks: Inheritance in OOP](https://www.geeksforgeeks.org/inheritance-in-object-oriented-programming/) — types and examples
- [Martin Fowler: Composition over Inheritance](https://martinfowler.com/bliki/CompositionOverInheritance.html) — design guidance

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class Account {
  constructor(owner, balance = 0) {
    this.owner = owner;
    this.balance = balance;
  }
  deposit(amount) {
    this.balance += amount;
  }
}

class MobileWallet extends Account {
  constructor(owner, balance, provider) {
    super(owner, balance); // inherit + extend
    this.provider = provider;
  }
  cashOut(amount, agentId) {
    if (amount > this.balance) throw new Error('Insufficient balance');
    this.balance -= amount;
    return { agentId, amount, provider: this.provider };
  }
}

const wallet = new MobileWallet('User', 1000, 'bkash');
wallet.deposit(500);      // inherited
wallet.cashOut(200, 'A1'); // extended behavior
```

#### Code walkthrough

1. `MobileWallet extends Account` — inherits `balance`, `deposit`.
2. `super()` calls parent constructor — required before `this` in derived class.
3. Child adds `cashOut` — MFS-specific behavior.

#### Complexity

| | |
|-|-|
| Time | O(1) per method call |
| Space | O(1) per instance |

#### Edge cases

- **Circular inheritance** — invalid in typed languages.
- **Overriding without `super`** — may skip important base initialization logic.
- **JS**: plain object prototypes differ from `class` sugar but same idea.

</details>

</article>

<article>

List and explain some basic Linux commands and their typical use cases.

<details><summary>Theory and explanation</summary>

Essential commands for backend/devops interviews at fintech companies running Linux servers:

| Command | Purpose | Typical use |
|---------|---------|-------------|
| **`ls`** | List directory contents | `ls -la` shows hidden files and permissions |
| **`cd`** | Change directory | Navigate project/deploy paths |
| **`pwd`** | Print working directory | Confirm location in scripts |
| **`cp` / `mv` / `rm`** | Copy, move, delete | Deploy artifacts; **rm -rf** is destructive |
| **`mkdir` / `touch`** | Create dir / empty file | Scaffold configs |
| **`cat` / `less` / `head` / `tail`** | View files | `tail -f app.log` live logs |
| **`grep`** | Search text | `grep ERROR /var/log/app.log` |
| **`find`** | Locate files | `find . -name "*.jar"` |
| **`chmod` / `chown`** | Permissions / ownership | Fix script execute bit |
| **`ps` / `top` / `htop`** | Processes / CPU memory | Debug hung JVM/Node |
| **`kill` / `kill -9`** | Signal processes | Restart stuck service |
| **`curl` / `wget`** | HTTP / download | Health-check REST APIs |
| **`ssh` / `scp`** | Remote shell / copy | Server access |
| **`df` / `du`** | Disk free / usage | Full disk incidents |
| **`netstat` / `ss` / `lsof`** | Sockets / open files | Port already in use |
| **`systemctl`** | Manage systemd services | `systemctl restart nginx` |
| **`docker` / `kubectl`** | Containers / orchestration | Microservice deployments |

**Permissions recap**

`rwx` for user/group/other — e.g. `chmod 755 script.sh`.

#### Further reading

- [Linux man pages online](https://man7.org/linux/man-pages/) — authoritative reference
- [DigitalOcean Linux Command Cheat Sheet](https://www.digitalocean.com/community/tutorials/linux-commands) — beginner-friendly
- [ExplainShell](https://explainshell.com/) — parse complex commands

</details>

<details><summary>Solution (JavaScript)</summary>

Node.js **`child_process`** wraps common shell operations (server-side only):

```js
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';

const execFileAsync = promisify(execFile);

async function tailErrors(logPath, lines = 50) {
  const { stdout } = await execFileAsync('tail', ['-n', String(lines), logPath]);
  return stdout.split('\n').filter((line) => line.includes('ERROR'));
}

async function diskUsage(path = '/') {
  const { stdout } = await execFileAsync('df', ['-h', path]);
  return stdout;
}

// await tailErrors('/var/log/payment.log');
```

#### Code walkthrough

- **`execFile`** runs binary with args array — safer than shell string concatenation.
- **`tail -n`** mirrors CLI log inspection.
- **`df -h`** human-readable disk stats.

#### Complexity

| | |
|-|-|
| Time | Depends on command output size |
| Space | O(output) for captured stdout |

#### Edge cases

- **Shell injection** — never pass untrusted input to `exec`; use `execFile` with args.
- **Missing command** — ENOENT if not in PATH.
- **Windows dev machines** — these commands require WSL or remote Linux.

</details>

</article>

<article>

What is a deadlock in computing? How can it be prevented or resolved?

<details><summary>Theory and explanation</summary>

**Deadlock** — a set of processes/threads each **waiting for a resource held by another** in the set, so **none can proceed**.

**Coffman conditions** (all four needed for deadlock)

1. **Mutual exclusion** — resource used by one at a time.
2. **Hold and wait** — hold resources while waiting for more.
3. **No preemption** — resources released only voluntarily.
4. **Circular wait** — circular chain of waiters.

**Prevention** — break one condition:

- **Ordering locks** — always acquire mutex A before B globally.
- **Try-lock with backoff** — don't wait indefinitely.
- **Banker's algorithm** — avoid unsafe states (theoretical).
- **Timeouts** — detect stuck waits ( JDBC, Redis lock TTL).

**Detection & recovery**

- Detect wait-for graph cycle; **abort** or **rollback** one transaction.
- DBMS: pick **victim** transaction with lowest cost.

**Avoidance in practice**

- Keep lock **hold time** minimal.
- Use **MVCC** instead of aggressive locking for reads.
- **Idempotent** APIs with retry for transient deadlocks.

#### Further reading

- [GeeksforGeeks: Deadlock in OS](https://www.geeksforgeeks.org/deadlock-in-operating-system/) — Coffman conditions
- [PostgreSQL: Deadlocks](https://www.postgresql.org/docs/current/explicit-locking.html) — automatic detection
- [MDN: Atomics and locks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics) — low-level JS synchronization

</details>

<details><summary>Solution (JavaScript)</summary>

Lock ordering prevents circular wait (classic dining philosophers fix):

```js
class AccountLock {
  constructor() {
    this.queue = Promise.resolve();
  }
  run(fn) {
    const next = this.queue.then(fn);
    this.queue = next.catch(() => {}); // keep chain alive on error
    return next;
  }
}

const locks = new Map();
function lockFor(id) {
  if (!locks.has(id)) locks.set(id, new AccountLock());
  return locks.get(id);
}

async function transfer(from, to, amount) {
  const first = from < to ? from : to;
  const second = from < to ? to : from;
  return lockFor(first).run(async () =>
    lockFor(second).run(async () => {
      // both locks acquired in global order — no deadlock
      await debit(from, amount);
      await credit(to, amount);
    })
  );
}
```

#### Code walkthrough

1. Sort account IDs — always lock **lower ID first**.
2. Serial queue per account simulates mutex.
3. Nested `run` acquires two locks without circular wait.

#### Complexity

| | |
|-|-|
| Time | O(1) lock acquisition per transfer (queued) |
| Space | O(accounts) lock objects |

#### Edge cases

- **Forgotten lock ordering** — classic deadlock returns.
- **Lock timeout** — retry with exponential backoff in distributed systems.
- **Same account transfer** — reject early.

</details>

</article>

<article>

What is database normalization? What are its benefits and common normal forms?

<details><summary>Theory and explanation</summary>

**Normalization** organizes tables to **reduce redundancy** and **anomaly risk** (insert/update/delete anomalies) by splitting data based on **functional dependencies**.

**Benefits**

- Less duplicate data → smaller storage, fewer inconsistent copies.
- Easier updates — change fact in one place.
- Clearer schema semantics.

**Normal forms (progressive)**

| NF | Rule (simplified) |
|----|-------------------|
| **1NF** | Atomic columns; no repeating groups |
| **2NF** | 1NF + no partial dependency on composite key |
| **3NF** | 2NF + no transitive dependency (non-key → non-key) |
| **BCNF** | Every determinant is a candidate key |
| **4NF / 5NF** | Multivalued / join dependencies (advanced) |

**Example anomaly without normalization**

`Orders(customer_id, customer_name, product, qty)` — customer name repeated per order row; update one row misses others.

**Denormalization trade-off**

Read-heavy analytics (ledger summaries) may **denormalize** for speed — bKash OLTP core stays normalized; reporting may use materialized views.

#### Further reading

- [GeeksforGeeks: Normal Forms in DBMS](https://www.geeksforgeeks.org/normal-forms-in-dbms/) — 1NF through BCNF
- [IBM: Database normalization](https://www.ibm.com/topics/database-normalization) — business perspective
- [PostgreSQL docs: Schema design](https://www.postgresql.org/docs/current/ddl-schemas.html) — practical DDL

</details>

<details><summary>Solution (JavaScript)</summary>

Schema sketch showing **3NF** split for wallet transactions:

```js
// Denormalized (bad) — customer_phone repeated per txn
const bad = {
  transactions: [
    { id: 1, user_phone: '017…', user_name: 'Ali', amount: 100 },
    { id: 2, user_phone: '017…', user_name: 'Ali', amount: 50 },
  ],
};

// Normalized (3NF)
const users = [{ id: 1, phone: '017…', name: 'Ali' }];
const transactions = [
  { id: 1, user_id: 1, amount: 100 },
  { id: 2, user_id: 1, amount: 50 },
];

function getUserTransactions(userId) {
  return transactions
    .filter((t) => t.user_id === userId)
    .map((t) => ({ ...t, ...users.find((u) => u.id === userId) }));
}
```

#### Code walkthrough

1. **`users`** holds facts about user once.
2. **`transactions`** references `user_id` — no transitive dependency.
3. Join at read time (ORM/SQL `JOIN`) reconstructs view.

#### Complexity

| | |
|-|-|
| Time | O(n) naive join for demo |
| Space | O(users + transactions) |

#### Edge cases

- **Over-normalization** — too many joins hurt latency; use indexes.
- **Historical name changes** — store `user_id`, not duplicated name in txn.
- **Reporting** — aggregate tables denormalize intentionally.

</details>

</article>

<article>

How can you generate random numbers in your preferred programming language?

<details><summary>Theory and explanation</summary>

**Pseudorandom number generators (PRNGs)** produce deterministic sequences from a **seed** — fine for simulations/games, not for **cryptography**.

**JavaScript**

- `Math.random()` — `[0, 1)` uniform; not cryptographically secure.
- `crypto.getRandomValues()` — CSPRNG for tokens/OTP.
- Libraries: `seedrandom` for reproducible tests.

**Java**

- `Random` — general purpose.
- `SecureRandom` — security-sensitive (PINs, session IDs).

**C++**

- `<random>` — `std::mt19937`, distributions (`uniform_int_distribution`).

**Python**

- `random` module vs `secrets` module (secure).

**Interview distinction**

- **Range mapping**: `Math.floor(Math.random() * (max - min + 1)) + min` for integers.
- **Modulo bias** when using `%` on raw bytes — use rejection sampling for crypto.

#### Further reading

- [MDN: Math.random()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random) — non-crypto PRNG
- [MDN: crypto.getRandomValues()](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues) — secure bytes
- [OWASP: Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) — when to use CSPRNG

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function randomOTP(length = 6) {
  const digits = new Uint32Array(length);
  crypto.getRandomValues(digits);
  return Array.from(digits, (n) => n % 10).join('');
}

function randomFrom(arr) {
  return arr[randomInt(0, arr.length - 1)];
}

randomInt(1, 100);
randomOTP(6); // e.g. '482910' for 2FA demo
```

#### Code walkthrough

1. **`randomInt`** — inclusive range via floor scaling.
2. **`randomOTP`** — CSPRNG bytes mod 10 (acceptable for short OTP demo; production uses larger alphabet/rejection).
3. **`randomFrom`** — pick array element uniformly.

#### Complexity

| | |
|-|-|
| Time | O(length) for OTP generation |
| Space | O(length) |

#### Edge cases

- **`Math.random()` for security** — never for payment PINs.
- **`max < min`** — validate inputs.
- **Seed reproducibility** — only in test environments with seeded PRNG.

</details>

</article>

<article>

How can you compare the contents of two text files to determine if they are identical?

<details><summary>Theory and explanation</summary>

**Approaches**

1. **Byte-by-byte / streaming compare** — read chunks, compare; stop at first mismatch. O(size) time, O(1) extra space.
2. **Hash then compare** — compute SHA-256 of each file; equal hashes → very likely equal (check collision risk for security contexts).
3. **Diff tools** — `diff`, `git diff` show *where* files differ, not just equality.
4. **Line-by-line** — normalize `\r\n` vs `\n` before comparing text logs.

**Linux CLI**

- `cmp file1 file2` — silent if equal; exit code 0/1.
- `diff -q file1 file2` — quick equality check.
- `sha256sum file1 file2` — compare digests.

**When hashes suffice**

Large deployment artifacts — compare checksum manifest instead of transferring files again.

#### Further reading

- [GNU cmp manual](https://www.gnu.org/software/diffutils/manual/html_node/cmp-Invocation.html) — byte comparison
- [Node.js fs API](https://nodejs.org/api/fs.html) — file read streams
- [MDN: SubtleCrypto.digest](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/digest) — SHA-256 in browser/Node

</details>

<details><summary>Solution (JavaScript)</summary>

```js
import { createReadStream } from 'node:fs';
import { createHash } from 'node:crypto';
import { pipeline } from 'node:stream/promises';

async function hashFile(path) {
  const hash = createHash('sha256');
  await pipeline(createReadStream(path), hash);
  return hash.digest('hex');
}

async function filesEqual(pathA, pathB) {
  const [hashA, hashB] = await Promise.all([hashFile(pathA), hashFile(pathB)]);
  return hashA === hashB;
}

async function filesEqualStreaming(pathA, pathB) {
  const streamA = createReadStream(pathA);
  const streamB = createReadStream(pathB);
  // ... chunk compare implementation for early exit without full hash
}
```

#### Code walkthrough

1. Stream file into SHA-256 hasher — memory-efficient for large logs.
2. Compare hex digests — equal → files identical (for practical purposes).
3. Streaming byte compare stops early on first differing chunk.

#### Complexity

| | |
|-|-|
| Time | O(n) — n = file size |
| Space | O(1) with streaming |

#### Edge cases

- **Different line endings** — text mode vs binary compare may disagree.
- **Same content, different metadata** — compare content only, not inode/timestamp.
- **Empty files** — both hash to same known empty SHA-256.

</details>

</article>

<article>

What happens when you type google.com and press enter in your search bar

<details><summary>Theory and explanation</summary>

End-to-end path from URL bar to rendered page:

1. **URL parsing** — browser interprets scheme (`https`), host (`google.com`), path.
2. **DNS lookup** — resolve domain → IP (browser cache → OS cache → recursive resolver → root/TLD/authoritative).
3. **TCP handshake** — SYN, SYN-ACK, ACK to server IP:443.
4. **TLS handshake** — certificate validation, key exchange, encrypted channel.
5. **HTTP request** — `GET / HTTP/1.1`, headers (`Host`, `User-Agent`, cookies).
6. **Server processing** — load balancers, app servers, caches.
7. **HTTP response** — status, headers (`Content-Type`, `Set-Cookie`), body (HTML).
8. **Browser rendering** — HTML parse → DOM; CSS → CSSOM; JS download/execute; layout/paint/composite.

**Performance extras**

- **HTTP/2 multiplexing**, **CDN edge**, **HSTS preload**, **OCSP stapling**.

#### Further reading

- [What Happens When (alex/github)](https://github.com/alex/what-happens-when) — exhaustive community guide
- [MDN: How the Web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works) — beginner overview
- [Cloudflare: DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) — resolution steps
- [TLS 1.3 RFC 8446](https://datatracker.ietf.org/doc/html/rfc8446) — handshake details

</details>

<details><summary>Solution (JavaScript)</summary>

Browser-side steps you can observe with DevTools / fetch:

```js
// 1. DNS + TCP + TLS handled by browser before fetch runs
async function probe(url) {
  const start = performance.now();
  const res = await fetch(url, { method: 'HEAD', redirect: 'follow' });
  return {
    status: res.status,
    headers: Object.fromEntries(res.headers.entries()),
    ms: Math.round(performance.now() - start),
  };
}

// await probe('https://google.com');
// Network tab shows: DNS, Initial connection, SSL, Waiting (TTFB), Content Download
```

#### Code walkthrough

1. `fetch` triggers full network stack for HTTPS URL.
2. `HEAD` minimizes body download while measuring TTFB.
3. Performance API / Network panel breaks down DNS/TLS phases.

#### Complexity

| | |
|-|-|
| Time | Dominated by RTT and server response |
| Space | O(1) for HEAD request |

#### Edge cases

- **Cached DNS/TLS session** — subsequent visits faster.
- **Redirect chain** — `google.com` → `www.google.com`.
- **Offline** — browser error page before TCP.

</details>
</article>

<article>

What happens when you copy a file in a computer? Are the copied file and the original file the same?

<details><summary>Theory and explanation</summary>

**Copy operation (conceptual)**

1. User/system calls copy (GUI, `cp`, `CopyFile` API).
2. OS reads **source file data** (via filesystem) in blocks.
3. OS allocates **new inode/metadata** for destination path.
4. Writes same byte content to new blocks on storage (copy-on-write filesystems may defer physical duplication).
5. Updates directory entry pointing to new file.

**Are they the same?**

| Aspect | Same? |
|--------|-------|
| **Byte content** | Yes (identical data after successful copy) |
| **Inode / file identity** | No — different files |
| **Path/name** | Usually different (user chooses destination) |
| **Timestamps** | No — creation time set at copy |
| **Hard link** | No — separate inode unless hard-linked intentionally |

**Copy vs hard link vs symlink**

- **Copy** — duplicate data (usually), independent lifecycle.
- **Hard link** — same inode, shared data; delete one if link count > 0 keeps data.
- **Symlink** — pointer to path; breaking target breaks link.

**MFS context**

Backup/audit logs often copy files for compliance — content match verified via hash.

#### Further reading

- [Linux `cp` man page](https://man7.org/linux/man-pages/man1/cp.1.html) — copy semantics
- [Wikipedia: Inode](https://en.wikipedia.org/wiki/Inode) — file metadata vs data blocks
- [Apple File System (APFS) copy-on-write](https://developer.apple.com/documentation/foundation/file_system/about_apfs) — modern FS behavior

</details>

<details><summary>Solution (JavaScript)</summary>

```js
import { copyFile, stat } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { createReadStream } from 'node:fs';
import { pipeline } from 'node:stream/promises';

async function sha256(path) {
  const hash = createHash('sha256');
  await pipeline(createReadStream(path), hash);
  return hash.digest('hex');
}

async function copyAndCompare(src, dest) {
  await copyFile(src, dest);
  const [s1, s2, h1, h2] = await Promise.all([
    stat(src), stat(dest), sha256(src), sha256(dest),
  ]);
  return {
    sameContent: h1 === h2,
    sameInode: s1.ino === s2.ino, // false on Unix after copy
    samePath: src === dest,
  };
}
```

#### Code walkthrough

1. `copyFile` creates new file with duplicated bytes.
2. Compare SHA-256 — `sameContent: true` if copy succeeded.
3. `ino` differs on Unix — proves distinct file identities.

#### Complexity

| | |
|-|-|
| Time | O(file size) for hash |
| Space | O(1) streaming |

#### Edge cases

- **Partial copy failure** — content differs; handle errors.
- **Copy-on-write FS** — may share blocks until one file modified.
- **Permissions** — copy may not preserve all extended attributes without flags (`cp -a`).

</details>
</article>
