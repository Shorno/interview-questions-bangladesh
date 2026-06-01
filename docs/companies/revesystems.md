---
description: REVE Systems interview questions, REVE Systems interview stages, REVE Systems interview details, REVE Systems interview questions and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/revesystems
---
# REVE Systems

|  | |
| :-| :- |
| Founding year | 2003 |
| Company Website | https://www.revesoft.com/ |
| Career Website | https://www.revesoft.com/ |
| Technologies Used| Java, Kotlin, Swift |

## Introduction
[REVE Systems](https://www.revesoft.com/) specializes in delivering VoIP (Voice over IP) software solutions, with a focus on mobile VoIP, softswitch, and billing solutions. They have different departments such as Research & Development (R&D), E-Gov, Reve Chat, etc. 

In this article, the recruitment process for the R&D department for the DEV roles (Junior Software Engineer) is presented. They perform campus recruitment.

## Interview Stages
1. **Online Screening Test**: This round is conducted via Zoom. All the participants are required to keep their microphones and cameras on during the MCQ exam via Google form. Questions were given from the following areas:

    1. Basic problem solving
    1. Data structure and algorithms
    1. Time Complexity
    1. Finding error in code snippets
    1. Finding the output of code blocks
    1. Object-oriented programming
    1. SQL
    1. Computer networking
    1. Software engineering and design patterns

1. **Technical Round I**: Two interviewers conducted this round via Skype. During the whole interview, the camera and microphone have to be on. At the beginning of the interview, a Google Doc might be shared for writing the code or any answers. Candidates are not allowed to use a pen or paper. Only the shared doc has to be used.

1. **Technical Round II**: This round is also conducted via Skype, and two interviewers (project managers) might be there. This is a bit more technical than round 1. Topics may include - Java socket programming, computer networking, focusing on TCP and UDP protocols, software engineering and design patterns, SOLID principles, string matching algorithms      (Naive, KMP).
4. **CTO Round**: This will be an onsite round where the CTO and any other senior engineer. Candidates might be asked to solve problems using pen and paper.

## Technical Round I Questions
<article>
	
Reverse a given singly linked list.
  
[**💻 Submit Code**](https://leetcode.com/problems/reverse-linked-list/description/)

At first, I used extra memory to store the reversed array.

<details><summary>Theory and explanation</summary>

Reversing a **singly linked list** reverses `next` pointers so traversal visits nodes in opposite order.

**Approaches (in order of interview preference)**

1. **Iterative three-pointer** — `prev`, `curr`, `next`; rewire each node. **O(n) time, O(1) space**. REVE explicitly rejected extra array.
2. **Recursive** — reverse tail, attach head at end. **O(n) stack space**.
3. **Array copy** — store values, rewrite nodes. **O(n) extra space** — acceptable first attempt but follow-up expects in-place.

**Interview talking points**

- Return new head (old tail).
- Empty / single node — return unchanged.
- VoIP stacks care about in-place mutation for memory-bound embedded clients.

#### Further reading

- [LeetCode 206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) — canonical problem
- [NeetCode: Reverse Linked List](https://neetcode.io/problems/reverse-a-linked-list) — visual walkthrough
- [GeeksforGeeks: Reverse a linked list](https://www.geeksforgeeks.org/reverse-a-linked-list/) — iterative and recursive

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

1. Save `next` before overwriting `curr.next`.
2. Point `curr.next` to `prev` (reversed prefix).
3. Advance `prev` and `curr`; return `prev` as new head.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases

- **null head** — return null.
- **Single node** — return same node.

</details>

<details><summary>Solution (other languages)</summary>

**Extra memory (first attempt — not preferred)**

```cpp
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == NULL || head->next == NULL)
            return head;
        
        int i;
        vector<int> v;
        ListNode* cur = head;
        while (cur != NULL) {
            v.push_back(cur->val);
            cur = cur->next;
        }
        
        i = v.size()-1;
        cur = head;
        while (head != NULL) {
            head->val = v[i];
            i--;
            head = head->next;
        }
        return cur;
    }
};
```

**In-place (preferred)**

```cpp
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == NULL || head->next == NULL)
            return head;
        
        ListNode* prev = NULL;
        while (head != NULL) {
            ListNode* tmp = head->next;
            head->next = prev;
            prev = head;
            head = tmp;
        }
        return prev;
    }
};
```

</details>

</article>

<article>
  
Given a sequence `1`, `1`, `2`, `3`, `5`, `8`, `13`, `21`..., where the indices start at `1`. For any given index, find the value of the sequence. For example, when the input is `3`, the output is `2`, and when the input is `6`, the output is `8`.
  
[**💻 Submit Code**](https://leetcode.com/problems/fibonacci-number/description/)

At first, I used an array for storing the calculated results of the intermediate steps and built the array going forward.

<details><summary>Theory and explanation</summary>

**Fibonacci** with `F(1)=F(2)=1`, `F(n)=F(n-1)+F(n-2)`.

**Approaches REVE asked about**

| Method | Time | Extra space |
|--------|------|-------------|
| Iterative + array | O(n) | O(n) |
| Iterative three vars | O(n) | O(1) |
| Naive recursion | O(2^n) | O(n) stack |
| Memoized recursion | O(n) | O(n) |

Interviewers progressively removed array, then asked recursion, then complexity comparison.

**Interview talking points**

- State base cases `n=1`, `n=2`.
- Naive recursion explodes — memoization or DP fixes it.
- Matrix exponentiation achieves O(log n) for huge n (bonus).

#### Further reading

- [LeetCode 509: Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) — problem statement
- [CP-Algorithms: Fibonacci](https://cp-algorithms.com/algebra/fibonacci-numbers.html) — fast doubling / matrix
- [GeeksforGeeks: Fibonacci DP](https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/) — approaches compared

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function fib(n) {
  if (n <= 2) return 1;
  let a = 1, b = 1;
  for (let i = 3; i <= n; i++) {
    const c = a + b;
    a = b;
    b = c;
  }
  return b;
}

function fibMemo(n, memo = {}) {
  if (n <= 2) return 1;
  if (memo[n]) return memo[n];
  return (memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo));
}
```

#### Code walkthrough

1. **O(1) space loop** — roll `a,b` forward from 3 to n.
2. **Memo** — cache subproblems to avoid exponential recomputation.

#### Complexity

| Approach | Time | Space |
|----------|------|-------|
| Three variables | O(n) | O(1) |
| Memoized | O(n) | O(n) |
| Naive recursive | O(2^n) | O(n) stack |

#### Edge cases

- **n = 1 or 2** — return 1.
- **Large n** — use BigInt if values overflow 32-bit.

</details>

<details><summary>Solution (other languages)</summary>

**Array DP**

```cpp
int fib(int n){
  	int arr[n + 1];
  	arr[1] = 1;
  	arr[2] = 1;
  
  	int i;
  	for (i = 3; i <= n; i++) {
          arr[i] = arr[i-1] + arr[i-2];
  	}
  	return arr[n];
 }
```

**O(1) space**

```cpp
int fib(int n){
  	int a, b, c = 1;
  	a = 1;
  	b = 1;
  
  	int i;
  	for (i = 3; i <= n; i++) {
          c =  a + b; 
          a = b; 
          b = c; 
  	}
	return c;
 }
```

**Naive recursion**

```cpp
 int fib(int n){
	if (n == 1)
            return 1;
	else if (n == 2)
            return 1;
	else
	    return fib(n-1) + fib(n-2);
 }
```

</details>

</article>

<article>
	
Given the `root` of a binary tree and an integer `targetSum`, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`.
  
[**💻 Submit Code**](https://leetcode.com/problems/path-sum/description/)

<details><summary>Theory and explanation</summary>

**Root-to-leaf path sum** — DFS from root, subtract node value from remaining target; at **leaf**, remaining must be 0.

**Approaches**

- **Recursive DFS** — pass `remaining = targetSum - node.val`.
- **Iterative stack** — pair `(node, remaining)`.
- **BFS** — same with queue.

Must check **leaf** (no children), not any node.

#### Further reading

- [LeetCode 112: Path Sum](https://leetcode.com/problems/path-sum/) — base problem
- [LeetCode 113: Path Sum II](https://leetcode.com/problems/path-sum-ii/) — enumerate all paths
- [GeeksforGeeks: Root to leaf path sum](https://www.geeksforgeeks.org/root-to-leaf-path-sum-equal-to-a-given-number/) — DFS walkthrough

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function TreeNode(val, left = null, right = null) {
  this.val = val;
  this.left = left;
  this.right = right;
}

function hasPathSum(root, targetSum) {
  if (!root) return false;
  if (!root.left && !root.right) return targetSum === root.val;
  const rem = targetSum - root.val;
  return hasPathSum(root.left, rem) || hasPathSum(root.right, rem);
}
```

#### Code walkthrough

1. Null node → false.
2. Leaf → check if remaining equals node value.
3. Internal node → recurse on either child with reduced target.

#### Complexity

| | |
|-|-|
| Time | O(n) worst case visit all nodes |
| Space | O(h) recursion stack, h = height |

#### Edge cases

- **Empty tree** — false.
- **Negative values** — still valid; don't greedy-pick path.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
class Solution {
public:
    bool isLeaf(TreeNode* root) {
        return root->left == nullptr and root->right == nullptr;
    }
    bool hasPathSum(TreeNode* root, int targetSum, int currentSum = 0) {
        if(root == nullptr) return false;
        currentSum+=root->val;
        if(isLeaf(root)) return targetSum == currentSum;
        return hasPathSum(root->left,targetSum, currentSum) or
                hasPathSum(root->right,targetSum, currentSum);
    }
};
```

</details>
</article>

<article>
	
Why are getters and setters used in Java?

<details><summary>Theory and explanation</summary>

**Getters and setters** (accessors/mutators) expose controlled read/write access to private fields — core **encapsulation** in Java beans and OOP.

**Why use them**

1. **Encapsulation** — hide internal representation; change fields without breaking callers.
2. **Validation** — setter rejects invalid state (negative age, null email).
3. **Computed properties** — getter derives value lazily (full name from first+last).
4. **Side effects / auditing** — log changes, notify observers, fire property events.
5. **Framework integration** — JavaBeans, JPA, Jackson, Spring often expect `getX`/`setX` conventions.
6. **Immutability option** — expose getter only for read-only fields.

**When not to overuse**

- Plain data carriers (records in Java 16+) may use compact constructors instead.
- Public fields in performance-critical inner loops (rare in enterprise code).

**REVE interview angle**

- Tie to **VoIP billing models** — rate fields validated on set, currency never negative.

#### Further reading

- [Oracle Java Tutorial: Encapsulation](https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html) — access modifiers
- [Effective Java (Item 16): Prefer accessors over public fields](https://www.oracle.com/java/technologies/effective-java.html) — Joshua Bloch
- [Baeldung: Getters and Setters](https://www.baeldung.com/java-getters-setters) — practical examples

</details>

<details><summary>Solution (JavaScript)</summary>

JavaScript uses conventions or `#private` fields; equivalent pattern:

```js
class UserAccount {
  #balance = 0;

  get balance() {
    return this.#balance;
  }

  set balance(value) {
    if (value < 0) throw new Error('balance cannot be negative');
    this.#balance = value;
  }
}
```

#### Code walkthrough

- Private field `#balance` hidden from outside.
- Getter exposes read; setter validates before write.

#### Complexity

N/A (conceptual)

#### Edge cases

- **Null in setter** — reject or coerce per domain rules.
- **Serialization** — frameworks may bypass getters unless configured.

</details>

<details><summary>Solution (other languages)</summary>

```java
public class Account {
    private double balance;

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        if (balance < 0) throw new IllegalArgumentException("negative balance");
        this.balance = balance;
    }
}
```

</details>
</article>

<article>
	
Describe the Singleton design pattern and write the code in Java.

<details><summary>Theory and explanation</summary>

**Singleton** ensures a class has **at most one instance** and provides global access — used for config managers, connection pools, loggers.

**Requirements**

- Private constructor prevents external `new`.
- Static holder or instance method returns the sole instance.
- Thread-safe in multi-threaded VoIP servers.

**Variants**

| Style | Thread-safe | Lazy |
|-------|-------------|------|
| Eager static field | Yes | No |
| Synchronized getInstance | Yes | Yes (slow) |
| Double-checked locking | Yes | Yes |
| **Bill Pugh holder** | Yes | Yes (recommended) |
| Enum singleton | Yes | No |

**Pitfalls**

- Hidden global state complicates testing.
- Serialization/reflection can break singleton — use enum or readResolve.

#### Further reading

- [Refactoring Guru: Singleton](https://refactoring.guru/design-patterns/singleton) — structure and variants
- [Effective Java Item 3: Enum singleton](https://www.oracle.com/java/technologies/effective-java.html) — best practice
- [Baeldung: Singletons in Java](https://www.baeldung.com/java-singleton) — implementations compared

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// Module pattern / ES module singleton
let instance;

class ConfigService {
  constructor() {
    if (instance) return instance;
    this.settings = {};
    instance = this;
  }
}

export const config = new ConfigService();
```

#### Code walkthrough

- Constructor returns existing `instance` if already created.
- ES modules are naturally singleton per import graph.

#### Complexity

N/A (design pattern)

#### Edge cases

- **Subclassing** — breaks singleton unless constructor guarded.
- **Multi-process** — not a singleton across JVMs/containers.

</details>

<details><summary>Solution (other languages)</summary>

**Bill Pugh holder (recommended)**

```java
public class Singleton {
    private Singleton() {}

    private static class Holder {
        static final Singleton INSTANCE = new Singleton();
    }

    public static Singleton getInstance() {
        return Holder.INSTANCE;
    }
}
```

**Enum (Effective Java)**

```java
public enum Singleton {
    INSTANCE;
    public void doWork() { /* ... */ }
}
```

</details>
</article>

<article>
	
What are REST APIs? Tell about the HTTP verbs and the differences between PUT and POST in REST API.

<details><summary>Theory and explanation</summary>

**REST (Representational State Transfer)** — architectural style for networked APIs using **resources** (nouns) identified by URLs, manipulated via **HTTP methods** (verbs), stateless requests, standard status codes, and representations (usually JSON).

**Common HTTP verbs**

| Verb | Purpose | Idempotent | Safe |
|------|---------|------------|------|
| GET | Read resource | Yes | Yes |
| POST | Create / action | No | No |
| PUT | Replace resource at URI | Yes | No |
| PATCH | Partial update | Usually no | No |
| DELETE | Remove resource | Yes | No |

**POST vs PUT**

- **POST** — create subordinate resource or trigger process; server often assigns ID (`POST /calls` → new call id). Repeating may create **duplicates**.
- **PUT** — upsert/replace at **known URI** (`PUT /users/42`); repeating same body leaves server in same state (**idempotent**).

**REVE context**

- VoIP provisioning APIs: POST to initiate call session; PUT to update full user profile at fixed endpoint.

#### Further reading

- [MDN: HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) — verb semantics
- [REST API Tutorial](https://restfulapi.net/) — resource modeling
- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — normative spec

</details>

<details><summary>Solution (JavaScript)</summary>

Illustrative Express-style routes:

```js
// POST — create (non-idempotent)
app.post('/api/users', (req, res) => {
  const id = createUser(req.body);
  res.status(201).location(`/api/users/${id}`).json({ id });
});

// PUT — replace at known URI (idempotent)
app.put('/api/users/:id', (req, res) => {
  replaceUser(req.params.id, req.body);
  res.status(200).json({ ok: true });
});
```

#### Code walkthrough

- POST returns 201 Created with new id.
- PUT targets explicit id; repeated identical PUT yields same final state.

#### Complexity

N/A (conceptual)

#### Edge cases

- **PUT on missing resource** — create (upsert) vs 404 — document API contract.
- **Partial updates** — prefer PATCH over PUT.

</details>
</article>

<article>
	
Given a large input string without `\n` present. Output the string of sentences where we will input the max letter count in a line. output the modified string, so if line breaks occur in the middle of a word, place it after a newline.

Input:
```
reve systems is a software company
11
```
Output:
```
reve
systems is
a software
company
```

<details><summary>Theory and explanation</summary>

**Word wrap / greedy line breaking** — pack words into lines of at most `maxWidth` characters without splitting words; break before word that would overflow.

**Algorithm**

1. Split text into words.
2. Greedily add words to current line while `line.length + word.length + spaces ≤ maxWidth`.
3. When next word doesn't fit, emit line and start new line with that word.

**Interview talking points**

- Clarify spaces count toward width.
- **Justification** (DP for minimal raggedness) is harder — REVE asks greedy wrap.
- O(n) over words.

#### Further reading

- [LeetCode 68: Text Justification](https://leetcode.com/problems/text-justification/) — advanced variant
- [GeeksforGeeks: Word wrap problem](https://www.geeksforgeeks.org/word-wrap-problem-dp-16/) — DP optimal version
- [MDN: String split](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split) — tokenization

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function wordWrap(text, maxWidth) {
  const words = text.split(/\s+/);
  const lines = [];
  let line = '';

  for (const w of words) {
    const candidate = line ? `${line} ${w}` : w;
    if (candidate.length <= maxWidth) {
      line = candidate;
    } else {
      if (line) lines.push(line);
      line = w;
    }
  }
  if (line) lines.push(line);
  return lines.join('\n');
}

wordWrap('reve systems is a software company', 11);
// reve\nsystems is\na software\ncompany
```

#### Code walkthrough

1. Tokenize on whitespace.
2. Extend current line while within width.
3. On overflow, push line and start fresh with current word.

#### Complexity

| | |
|-|-|
| Time | O(n) characters |
| Space | O(n) output |

#### Edge cases

- **Single word longer than maxWidth** — place alone on its own line (or error per spec).
- **Empty string** — empty output.

</details>
</article>

## Technical Round II Questions

<article>

What are the four pillars of OOP? 

<details><summary>Theory and explanation</summary>

The **four pillars of object-oriented programming**:

1. **Encapsulation** — bundle data + behavior; hide internals behind public interface (private fields, getters/setters).
2. **Abstraction** — expose essential behavior, hide complexity (interfaces, abstract classes, APIs).
3. **Inheritance** — reuse and extend parent class (`extends`); is-a relationships.
4. **Polymorphism** — one interface, many implementations; runtime method dispatch (method overriding), overloads, interface implementations.

**Interview tip**

- Give one-line definition + one example each — REVE Round II and CTO repeat this topic.

#### Further reading

- [Oracle: Object-Oriented Programming Concepts](https://docs.oracle.com/javase/tutorial/java/concepts/) — official tutorial
- [GeeksforGeeks: Four pillars of OOP](https://www.geeksforgeeks.org/object-oriented-programming-oops-concept-in-java/) — Java-centric examples
- [Refactoring Guru: OOP basics](https://refactoring.guru/design-patterns/what-is-design-patterns) — design pattern context

</details>

<details><summary>Solution (JavaScript)</summary>

JavaScript supports OOP via prototypes/classes:

```js
class Shape { area() { throw new Error('abstract'); } }
class Circle extends Shape {
  #r;
  constructor(r) { super(); this.#r = r; } // encapsulation
  area() { return Math.PI * this.#r ** 2; } // polymorphism
}
```

#### Complexity

N/A (conceptual)

</details>
</article>

<article>

Explain about `Encapsulation`, `Abstraction`, `Inheritance`, and `Polymorphism` with real-world examples.

<details><summary>Theory and explanation</summary>

**Real-world examples for REVE-style answers**

| Pillar | Real-world example |
|--------|-------------------|
| **Encapsulation** | ATM machine — you insert card and press buttons; cash dispensing mechanics hidden inside. |
| **Abstraction** | Car driver uses steering/brake; engine ECU complexity hidden. Software: `CallService.dial(number)` hides SIP/RTP stack. |
| **Inheritance** | `Smartphone extends Phone extends Device` — shared power/boot behavior, specialized apps. |
| **Polymorphism** | Universal remote sends "power" — TV, AC, soundbar each respond differently to same button (interface `Powerable`). |

**VoIP mapping**

- Encapsulation: `RtpSession` hides packet buffer.
- Abstraction: `MediaGateway` interface for codec swap.
- Inheritance: `SecureCall extends BasicCall`.
- Polymorphism: `BillingStrategy` implementations per country.

#### Further reading

- [Oracle Java Tutorial: Inheritance](https://docs.oracle.com/javase/tutorial/java/IandI/subclasses.html) — extends examples
- [Refactoring Guru: Encapsulation](https://refactoring.guru/fundamental-design-patterns) — design linkage
- [Baeldung: Polymorphism in Java](https://www.baeldung.com/java-polymorphism) — override vs overload

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// Abstraction + polymorphism
class PaymentProcessor {
  charge(amount) { throw new Error('implement'); }
}
class StripeProcessor extends PaymentProcessor {
  charge(amount) { /* stripe API */ return { ok: true, amount }; }
}
class BkashProcessor extends PaymentProcessor {
  charge(amount) { /* bkash API */ return { ok: true, amount }; }
}

function checkout(processor, amount) {
  return processor.charge(amount); // polymorphic call
}
```

#### Complexity

N/A (conceptual)

</details>
</article>

<article>

Please tell us about Java Socket Programming.

<details><summary>Theory and explanation</summary>

**Java socket programming** — network I/O via `java.net` using **Socket** (TCP client), **ServerSocket** (TCP server), **DatagramSocket** (UDP).

**TCP server flow**

1. `ServerSocket` bind to port, `accept()` blocks for client.
2. `Socket` returns streams: `getInputStream()`, `getOutputStream()`.
3. Read/write bytes or wrap with `BufferedReader`/`PrintWriter`.
4. Close sockets in `finally`.

**TCP client**

- `new Socket(host, port)` → streams → protocol exchange → close.

**UDP**

- Connectionless `DatagramPacket` send/receive; no guaranteed delivery.

**REVE focus**

- They ask TCP vs UDP in Round II — sockets are the Java API layer for those protocols.
- Mention thread-per-connection vs thread pool for VoIP signaling servers.

#### Further reading

- [Oracle: Socket programming](https://docs.oracle.com/javase/tutorial/networking/sockets/) — official tutorial
- [Baeldung: Java sockets](https://www.baeldung.com/java-sockets) — client/server examples
- [GeeksforGeeks: Socket programming in Java](https://www.geeksforgeeks.org/socket-programming-in-java/) — walkthrough

</details>

<details><summary>Solution (JavaScript)</summary>

Node.js net module equivalent for discussion:

```js
import net from 'net';

const server = net.createServer(socket => {
  socket.write('Hello from REVE mock server\n');
  socket.on('data', data => socket.write(data));
});
server.listen(5060, () => console.log('TCP listening'));
```

#### Complexity

N/A (conceptual / API demo)

</details>

<details><summary>Solution (other languages)</summary>

```java
// Minimal TCP echo server
try (ServerSocket ss = new ServerSocket(8080)) {
    while (true) {
        Socket client = ss.accept();
        try (BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
             PrintWriter out = new PrintWriter(client.getOutputStream(), true)) {
            String line;
            while ((line = in.readLine()) != null) out.println(line);
        }
    }
}
```

</details>
</article>

<article>

What models are used in the Software development life cycle? Please tell us about the waterfall model.

<details><summary>Theory and explanation</summary>

**SDLC models** organize phases from idea to maintenance:

- **Waterfall** — sequential: Requirements → Design → Implementation → Testing → Deployment → Maintenance.
- **V-Model** — waterfall with testing phase paired to each dev phase.
- **Iterative / Incremental** — build slices repeatedly.
- **Agile** (Scrum, Kanban) — short iterations, continuous feedback.
- **Spiral** — risk-driven cycles.
- **DevOps / CI-CD** — continuous delivery overlay.

**Waterfall characteristics**

| Pros | Cons |
|------|------|
| Clear milestones, documentation | Late discovery of requirement errors |
| Easy to manage contractually | No working software until late |
| Works when requirements stable | Expensive to change course |

**Phases are gated** — next starts when previous sign-off complete.

#### Further reading

- [GeeksforGeeks: SDLC models](https://www.geeksforgeeks.org/software-development-life-cycle-sdlc/) — comparison table
- [Atlassian: Waterfall vs Agile](https://www.atlassian.com/agile/project-management/waterfall-methodology) — when to use each
- [Sommerville: Software Engineering](https://www.pearson.com/en-us/subject-catalog/p/software-engineering/P200000003380) — textbook reference

</details>

<details><summary>Solution (JavaScript)</summary>

N/A — conceptual. Timeline sketch for whiteboard:

```
Requirements ──► Design ──► Build ──► Test ──► Release ──► Maintain
     │              │          │         │
   (frozen)    (frozen)   (frozen)  (sign-off)
```

#### Complexity

N/A (conceptual)

</details>
</article>

<article>

Please explain the Agile model in software engineering.

<details><summary>Theory and explanation</summary>

**Agile** — iterative delivery, customer collaboration, responding to change over rigid plans (see [Agile Manifesto](https://agilemanifesto.org/)).

**Core ideas**

- Short **sprints** (1–4 weeks) producing shippable increment.
- **Product backlog** prioritized by PO; team pulls into sprint backlog.
- Daily standups, sprint review, retrospective.
- **Continuous feedback** — refine requirements each iteration.

**Scrum roles**

- Product Owner — what to build.
- Scrum Master — process facilitator.
- Development Team — how to build.

**vs Waterfall**

- Agile embraces changing VoIP feature priorities (new codec, billing rule) mid-project.
- Waterfall suits fixed regulatory deliverables.

#### Further reading

- [Agile Manifesto](https://agilemanifesto.org/) — values and principles
- [Scrum Guide](https://scrumguides.org/) — official Scrum definition
- [Atlassian: Agile methodology](https://www.atlassian.com/agile) — practical guide

</details>

<details><summary>Solution (JavaScript)</summary>

N/A — conceptual. Sample sprint backlog item format:

```js
const sprintItem = {
  title: 'Add UDP fallback for RTP',
  storyPoints: 5,
  acceptanceCriteria: ['packets recover after 3s loss', 'unit tests pass'],
};
```

#### Complexity

N/A (conceptual)

</details>
</article>

<article>

What are the SOLID principles?

<details><summary>Theory and explanation</summary>

**SOLID** — five OOP design principles for maintainable systems:

| Letter | Principle | Summary |
|--------|-----------|---------|
| **S** | Single Responsibility | One class, one reason to change |
| **O** | Open/Closed | Open for extension, closed for modification |
| **L** | Liskov Substitution | Subtypes must be substitutable for base types |
| **I** | Interface Segregation | Many specific interfaces > one fat interface |
| **D** | Dependency Inversion | Depend on abstractions, not concretions |

**REVE angle**

- Apply to billing plugins (OCP), codec adapters (DIP), segregated `Signaling` vs `Media` interfaces (ISP).

#### Further reading

- [Robert C. Martin: SOLID](https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html) — origin author
- [Refactoring Guru: SOLID](https://refactoring.guru/solid-principles) — examples
- [DigitalOcean: SOLID Java](https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design) — concise guide

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// D — depend on abstraction
class CallRouter {
  constructor(signaling) { this.signaling = signaling; }
  route(call) { return this.signaling.connect(call); }
}
```

#### Complexity

N/A (conceptual)

</details>
</article>

<article>

What are the differences between the TCP and UDP protocols?

<details><summary>Theory and explanation</summary>

Both are **transport-layer** protocols on IP.

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Connection-oriented (3-way handshake) | Connectionless |
| Reliability | Guaranteed delivery, ordering, retransmit | Best effort, may lose/reorder |
| Flow control | Yes (windowing) | No |
| Congestion control | Yes | No |
| Header size | 20+ bytes | 8 bytes |
| Speed | Higher latency, slower | Lower latency |
| Use cases | HTTP, SIP signaling, file transfer | VoIP media (RTP), DNS, gaming |

**VoIP at REVE**

- Often **SIP over TCP/TLS** for signaling; **RTP over UDP** for real-time audio (loss tolerable, latency critical).

#### Further reading

- [MDN: TCP vs UDP (overview)](https://developer.mozilla.org/en-US/docs/Glossary/TCP) — web context
- [RFC 793: TCP](https://www.rfc-editor.org/rfc/rfc793) — specification
- [RFC 768: UDP](https://www.rfc-editor.org/rfc/rfc768) — specification
- [Cloudflare: TCP vs UDP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) — practical comparison

</details>

<details><summary>Solution (JavaScript)</summary>

N/A — conceptual. When to pick:

```js
// Pseudocode decision
function pickTransport(payload) {
  return payload.requiresReliability ? 'TCP' : 'UDP';
}
```

#### Complexity

N/A (conceptual)

</details>
</article>

<article>

Given two input strings, you have to find whether the second string is present in the first string. Please explain all the approaches for solving this problem. 

<details><summary>Theory and explanation</summary>

**Substring search** — find if `pattern` occurs in `text`.

**Approaches**

| Algorithm | Time | Notes |
|-----------|------|-------|
| **Naive** | O(n·m) | Try every start index, compare pattern |
| **KMP** | O(n + m) | Prefix (LPS) function avoids re-comparing |
| **Rabin-Karp** | O(n + m) avg | Rolling hash; good multiple patterns |
| **Boyer-Moore** | O(n/m) best | Skip bytes from bad-character rule |
| **Built-in** | Varies | `indexOf`, `strstr`, `String.contains` |

**REVE Round II** explicitly mentions **Naive and KMP** — explain LPS construction and how it shifts pattern on mismatch without moving text pointer backward.

#### Further reading

- [CP-Algorithms: KMP](https://cp-algorithms.com/string/knuth-morris-pratt.html) — full algorithm
- [GeeksforGeeks: KMP](https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/) — walkthrough
- [LeetCode 28: Find the Index of First Occurrence](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) — application

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function naiveSearch(text, pattern) {
  const n = text.length, m = pattern.length;
  for (let i = 0; i <= n - m; i++) {
    let j = 0;
    while (j < m && text[i + j] === pattern[j]) j++;
    if (j === m) return i;
  }
  return -1;
}

function buildLps(pattern) {
  const lps = Array(pattern.length).fill(0);
  for (let i = 1, len = 0; i < pattern.length; ) {
    if (pattern[i] === pattern[len]) lps[i++] = ++len;
    else if (len) len = lps[len - 1];
    else lps[i++] = 0;
  }
  return lps;
}

function kmpSearch(text, pattern) {
  const lps = buildLps(pattern);
  let i = 0, j = 0;
  while (i < text.length) {
    if (text[i] === pattern[j]) { i++; j++; }
    else if (j) j = lps[j - 1];
    else i++;
    if (j === pattern.length) return i - j;
  }
  return -1;
}
```

#### Code walkthrough

1. **Naive** — outer loop start positions; inner verifies match.
2. **KMP** — on mismatch, shift pattern by `lps[j-1]` instead of restarting text.

#### Complexity

| Algorithm | Time | Space |
|-----------|------|-------|
| Naive | O(n·m) | O(1) |
| KMP | O(n + m) | O(m) |

#### Edge cases

- **Empty pattern** — found at 0.
- **Pattern longer than text** — not found.

</details>
</article>

<article>

Do you have a plan for higher studies? When will you go abroad for higher studies?

<details><summary>Theory and explanation</summary>

**Behavioral / HR question** — assess retention risk and honesty, not a trick question.

**How to answer well**

1. **Be honest** — if no plans, say you are focused on industry growth now; mention skills you will learn on the job.
2. **If considering MS later** — frame as 3–5+ year horizon after gaining production experience; emphasize commitment to current role.
3. **Connect to REVE** — VoIP domain expertise is rare; you want to deepen engineering before any academic pursuit.
4. **Avoid** — saying "I will leave in 1 year for abroad" unless true.

**What interviewers want**

- Stability for training investment.
- Genuine interest in software engineering vs academia (see CTO round companion question).

#### Further reading

- [Harvard Business Review: Behavioral interviews](https://hbr.org/2014/10/how-to-succeed-at-the-interview) — framing honest answers
- [LinkedIn: Answering career plan questions](https://www.linkedin.com/advice/0/how-do-you-answer-question-about-your-career-plan) — recruiter perspective

</details>

<details><summary>Solution (JavaScript)</summary>

N/A — prepare a 30-second spoken answer outline:

```
Present: Excited about REVE R&D and VoIP products.
Near term (2–3 yrs): Grow as backend/mobile engineer, ship production features.
Long term: Open to specialized certifications / MS only if aligned with company; no fixed abroad timeline.
```

#### Complexity

N/A (behavioral)

</details>
</article>


## CTO Round Questions

<article>

Please tell us about yourself.

<details><summary>Theory and explanation</summary>

**"Tell me about yourself"** — 60–90 second structured pitch, not life story.

**Suggested structure**

1. **Present** — degree, current focus (e.g., Java, algorithms, final-year project).
2. **Past highlight** — one internship/project with measurable outcome.
3. **Why REVE** — VoIP, R&D, campus hire path, product domain.
4. **Forward** — what you want to learn in first year.

**CTO round tips**

- Confident but concise; they may interrupt — that's normal.
- Tie project experience to **networking**, **concurrency**, or **telecom** if possible.

#### Further reading

- [The Muse: Tell me about yourself](https://www.themuse.com/advice/tell-me-about-yourself-interview-question-answer-examples) — templates
- [REVE Systems careers](https://www.revesoft.com/) — tailor "why REVE"

</details>

<details><summary>Solution (JavaScript)</summary>

N/A — spoken answer. Bullet template:

```
- CSE @ [University], graduating [year]
- Built [project]: [tech], [impact]
- Competitive programming / coursework in DS & networking
- Want REVE R&D: real-time comms, learn from senior engineers
```

#### Complexity

N/A (behavioral)

</details>
</article>

<article>

Why do you want to join a software company instead of joining a university as a faculty member?

<details><summary>Theory and explanation</summary>

**Motivation question** — CTO probes career intent: industry vs academia.

**Strong industry angles**

- Prefer **building production systems** used by real users (millions of calls/messages).
- Faster feedback loop — ship, measure, iterate vs multi-year research cycles.
- Team environment, code review, mentorship from senior engineers.
- VoIP/domain problems combine **theory (networks, algorithms)** with **practice**.

**Acknowledge academia positively**

- Respect teaching/research; may contribute via internal tech talks, open source, or part-time mentoring later.

**Avoid**

- Dismissing universities harshly.
- Sounding unsure about engineering.

#### Further reading

- [Stack Overflow Developer Survey](https://survey.stackoverflow.co/) — industry career paths
- [Paul Graham: How to choose what to work on](http://www.paulgraham.com/work.html) — motivation framing

</details>

<details><summary>Solution (JavaScript)</summary>

N/A — sample 3-sentence answer:

```
I enjoy turning ideas into reliable software that people use daily.
REVE's VoIP products combine algorithms, networking, and OOP — exactly where I want to grow.
While I respect academia, my current goal is engineering impact on real products before considering teaching roles.
```

#### Complexity

N/A (behavioral)

</details>
</article>

<article>

Write the code of the Singleton pattern and explain.

<details><summary>Theory and explanation</summary>

CTO round revisits **Singleton** — expect to write on paper and explain thread safety.

**Explain while coding**

1. Private constructor.
2. Static access method.
3. Why Bill Pugh holder or enum avoids synchronized bottleneck.
4. Testability concerns (dependency injection alternative).

See Technical Round I Singleton article for full theory — CTO expects handwritten Java.

#### Further reading

- [Refactoring Guru: Singleton](https://refactoring.guru/design-patterns/singleton/java/example) — Java examples
- [Effective Java Item 3](https://www.oracle.com/java/technologies/effective-java.html) — enum singleton

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class AppConfig {
  static #instance;
  constructor() {
    if (AppConfig.#instance) return AppConfig.#instance;
    AppConfig.#instance = this;
  }
  static getInstance() {
    return AppConfig.#instance ?? new AppConfig();
  }
}
```

#### Code walkthrough

- Private static field holds sole instance.
- Constructor guard prevents second instance.

#### Complexity

N/A (design pattern)

</details>

<details><summary>Solution (other languages)</summary>

```java
public class Singleton {
    private Singleton() {}
    private static class Holder {
        static final Singleton INSTANCE = new Singleton();
    }
    public static Singleton getInstance() { return Holder.INSTANCE; }
}
```

</details>
</article>

<article>

Explain the four pillars of OOP with examples.

<details><summary>Theory and explanation</summary>

CTO repeat of Round II — expect **deeper examples** and possibly whiteboard UML.

Cover each pillar with **definition + Java example + real world**:

1. **Encapsulation** — `private balance; public withdraw()` validates amount.
2. **Abstraction** — `interface CallTransport { send(); }` hides SIP details.
3. **Inheritance** — `class VideoCall extends AudioCall`.
4. **Polymorphism** — `List<Transport> transports; transports.forEach(t -> t.connect());`

Mention when **composition over inheritance** is preferable (favor has-a over fragile is-a).

#### Further reading

- [Oracle: OOP concepts](https://docs.oracle.com/javase/tutorial/java/concepts/) — official
- [GeeksforGeeks: OOP in Java](https://www.geeksforgeeks.org/object-oriented-programming-oops-concept-in-java/) — examples

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class AudioCall {
  connect() { return 'audio connected'; }
}
class VideoCall extends AudioCall {
  connect() { return super.connect() + ' + video'; }
}
```

#### Complexity

N/A (conceptual)

</details>
</article>

<article>

Actually they asked all the questions from the previous rounds where I made mistakes.

<details><summary>Theory and explanation</summary>

**CTO remediation pattern** — senior interview revisits **weak spots** from earlier rounds, not necessarily new topics.

**How to prepare**

1. Review your Google Doc submissions — list every follow-up you struggled on (extra memory linked list, Fibonacci recursion complexity, etc.).
2. For each mistake, prepare **corrected answer + complexity + one sentence why prior answer was insufficient**.
3. Practice **calm correction** — "In round I I used O(n) space; the in-place approach is…"

**Mindset**

- CTO round tests **learning agility**, not perfection on first try.
- Acknowledge gap briefly, then demonstrate mastery.

#### Further reading

- [Cal Newport: Deep work preparation](https://www.calnewport.com/books/deep-work/) — structured review habits
- Prior sections in this document — all Round I/II topics

</details>

<details><summary>Solution (JavaScript)</summary>

N/A — create a personal mistake log:

```js
const reviewTopics = [
  { topic: 'reverse linked list', fix: 'iterative O(1) space' },
  { topic: 'fibonacci', fix: 'memo vs naive O(2^n)' },
  { topic: 'singleton', fix: 'Bill Pugh holder thread safety' },
];
```

#### Complexity

N/A (meta-interview strategy)

</details>
</article>

