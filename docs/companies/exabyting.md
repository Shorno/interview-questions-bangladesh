---
description: Exabyting interview questions, Exabyting interview stages, Exabyting interview details, Exabyting interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/exabyting
---
# Exabyting

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-| :- |
| Founding year | |
| Company Website | http://exabyting.com/ |
| Career Website | https://exabyting.com/join-our-team/ |
| Technologies Used| JAVA, Spring, PHP, Laravel, JavaScript, NodeJS, ExpressJS, Python, Django, REST, Microservices, SQL, NoSQL, SQS, SNS |

## Introduction

[Exabyting](https://exabyting.com/) is an international software company based in Dhaka, Bangladesh. They have been successfully providing software services since 2018 in both the local and global market.

## Interview Stages

For the Trainee Software Engineer Position, Exabyting follows a 4-stage interview process.
They often give job advertisements on LinkedIn. We have to apply using the Google form mentioned in the post. In the Google form, some questionnaires about yourself and some basic technical questions are given sometimes. I applied several times through the Google form but never got a call. Last time, I applied through a referral from an employee of theirs and got shortlisted. The interview process is as follows:

1. **Phone Interview:** After applying and getting shortlisted, one of the employees will call you and ask you some basic questions about Computer Science.
2. **Round 1:** The first round is a technical round and generally lasts for half an hour. An engineering manager will join in this stage and ask about you, your hobbies, currently what are you doing and some basic questions.
3. **Round 2:** The second round is also a technical round. This interview session is taken by 3 software engineers and runs for around one and a half hours. In this round, they ask you about your projects, your role in the projects, and some technical questions. They will ask questions based on your recent used tech stack.
4. **CEO Round:** This is a behavioural interview with the CEO of the company. In this meeting, he briefs you about the vision and mission of the company. What is the long-term goal of the company, what is their expectation from the company and what is your expectation from the company? He also briefs about the culture of the company. He tries to understand whether you are aligned with their company culture or not. He also asks if you have any preference for any department like backend, frontend mobile application etc.

## Phone Interview

<article>

Difference between Array and Linked List.

<details><summary>Theory and explanation</summary>

**Array**

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

**Index access formula (array):** `address = base_address + index * element_size`.

**Array**

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

**Index access formula (array):** `address = base_address + index * element_size`.

- **Array**: An array is a collection of elements of the same data type stored in contiguous memory locations. It has a fixed size and allows random access to elements using an index.
- **Linked List**: A linked list is a data structure that consists of nodes where each node contains data and a reference (link) to the next node in the sequence. It does not require contiguous memory allocation and allows dynamic memory allocation.

Read more from [Array vs Linked List | GeeksforGeeks](https://www.geeksforgeeks.org/array-vs-linked-list/)

#### Further reading
- [VisuAlgo](https://visualgo.net/en) — interactive data structure visualizations

</details>





</article>

<article>

Which sorting algorithm works better in the average case?

<details><summary>Theory and explanation</summary>

For general-purpose comparison sorting of ~1000 integers (positive and negative), **merge sort** and **quicksort** average **O(n log n)**.

| Algorithm | Average | Worst | Stable | Notes |
|-----------|---------|-------|--------|-------|
| Merge sort | O(n log n) | O(n log n) | Yes | Predictable; extra O(n) space |
| Quicksort | O(n log n) | O(n²) | No* | Fast in practice; pivot choice matters |
| Heap sort | O(n log n) | O(n log n) | No | O(1) extra space |

**Interview answer:** Prefer **merge sort** when stability matters; **quicksort** for in-place average speed with good pivot (median-of-three).

For general-purpose comparison sorting of ~1000 integers (positive and negative), **merge sort** and **quicksort** average **O(n log n)**.

| Algorithm | Average | Worst | Stable | Notes |
|-----------|---------|-------|--------|-------|
| Merge sort | O(n log n) | O(n log n) | Yes | Predictable; extra O(n) space |
| Quicksort | O(n log n) | O(n²) | No* | Fast in practice; pivot choice matters |
| Heap sort | O(n log n) | O(n log n) | No | O(1) extra space |

**Interview answer:** Prefer **merge sort** when stability matters; **quicksort** for in-place average speed with good pivot (median-of-three).

Merge sort and Quick sort work better in the average case. Merge sort has a time complexity of `O(nlogn)` in the worst case. Quick sort has a time complexity of `O(nlogn)` in the average case. Both are stable sorting algorithms and work well with large and medium datasets.

#### Further reading
- [VisuAlgo](https://visualgo.net/en) — interactive data structure visualizations

</details>





</article>

<article>

Suppose, you have to sort 1000 numbers, numbers can be positive and negative. Which algorithm will you use?

<details><summary>Theory and explanation</summary>

Use **merge sort** or **introsort** (stdlib `sort` hybrid).

- Time **O(n log n)** worst case (merge) or guaranteed for introsort.
- Handles positive/negative without special cases.
- For bounded integer range, **counting sort** O(n + k) is also valid — mention as optimization if range is small.

Use **merge sort** or **introsort** (stdlib `sort` hybrid).

- Time **O(n log n)** worst case (merge) or guaranteed for introsort.
- Handles positive/negative without special cases.
- For bounded integer range, **counting sort** O(n + k) is also valid — mention as optimization if range is small.

We can use merge sort to sort the 1000 numbers. Merge sort has a time complexity of `O(nlogn)` in the worst case. It is a stable sorting algorithm and works well with large and medium datasets. Merge sort is a divide and conquer algorithm.

#### Further reading
- [VisuAlgo](https://visualgo.net/en) — interactive data structure visualizations

</details>





</article>

<article>

What is Stack, Queue and Priority Queue?

<details><summary>Theory and explanation</summary>

**Stack (LIFO)** — push/pop at one end. Examples: call stack, undo, browser back (with another stack for forward).

**Queue (FIFO)** — enqueue rear, dequeue front. Examples: BFS, job schedulers, message buffers.

**Priority queue** — dequeue smallest/largest priority. Heap implementation: insert/delete **O(log n)**, peek **O(1)**. Used in Dijkstra, Huffman, task scheduling.

**Stack (LIFO)** — push/pop at one end. Examples: call stack, undo, browser back (with another stack for forward).

**Queue (FIFO)** — enqueue rear, dequeue front. Examples: BFS, job schedulers, message buffers.

**Priority queue** — dequeue smallest/largest priority. Heap implementation: insert/delete **O(log n)**, peek **O(1)**. Used in Dijkstra, Huffman, task scheduling.

- **Stack**: A stack is a linear data structure that follows the Last In First Out (LIFO) principle. It has two main operations: push (insert) and pop (remove).
- **Queue**: A queue is a linear data structure that follows the First In First Out (FIFO) principle. It has two main operations: enqueue (insert) and dequeue (remove).
- **Priority Queue**: A priority queue is a data structure that stores elements based on their priority. It allows elements with higher priority to be dequeued before elements with lower priority.

#### Further reading
- [GeeksforGeeks](https://www.geeksforgeeks.org/) — interview CS topics
- [MDN Web Docs](https://developer.mozilla.org/) — web and JS reference

</details>





</article>

<article>

Difference between Binary Tree and BST.

<details><summary>Theory and explanation</summary>

**Binary tree:** each node ≤ 2 children; no ordering constraint.

**BST:** left < parent < right (inorder → sorted). Search/insert **O(h)**; **O(n)** if skewed into a chain.

**Balancing:** AVL (strict balance), red-black (relaxed, used in `std::map`), or rebuild periodically.

**Binary tree:** each node ≤ 2 children; no ordering constraint.

**BST:** left < parent < right (inorder → sorted). Search/insert **O(h)**; **O(n)** if skewed into a chain.

**Balancing:** AVL (strict balance), red-black (relaxed, used in `std::map`), or rebuild periodically.

- **Binary Tree**:A binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child. 
- **Binary Search Tree**: A binary search tree is a binary tree in which the value of the left child is less than the parent node and the value of the right child is greater than the parent node.

If the binary search tree is imbalanced, then we can make it balanced by using AVL tree or Red-Black tree. These trees are self-balancing binary search trees.

#### Further reading
- [VisuAlgo](https://visualgo.net/en) — interactive data structure visualizations

</details>





</article>

<article>

When we type a web address (www.google.com) in a web browser, what happens before we get the response?

<details><summary>Theory and explanation</summary>

High-level flow when you open `https://www.google.com`:

1. **DNS** — resolve hostname to IP (recursive resolver, caches).
2. **TCP** — 3-way handshake to server :443.
3. **TLS** — certificate verify, key agreement, encrypted channel.
4. **HTTP** — GET request, redirects, response headers/body.
5. **Browser** — HTML parse → DOM, CSS, JS, subresources, render pipeline.

Mention **CDN**, **HTTP/2 multiplexing**, and **caching** (Cache-Control) for depth.

High-level flow when you open `https://www.google.com`:

1. **DNS** — resolve hostname to IP (recursive resolver, caches).
2. **TCP** — 3-way handshake to server :443.
3. **TLS** — certificate verify, key agreement, encrypted channel.
4. **HTTP** — GET request, redirects, response headers/body.
5. **Browser** — HTML parse → DOM, CSS, JS, subresources, render pipeline.

Mention **CDN**, **HTTP/2 multiplexing**, and **caching** (Cache-Control) for depth.

This is a very important question and aims to check the knowledge of networking. A very thorough explanation of this question is answered here in [What Happens When](https://github.com/alex/what-happens-when)

#### Further reading
- [GeeksforGeeks](https://www.geeksforgeeks.org/) — interview CS topics
- [MDN Web Docs](https://developer.mozilla.org/) — web and JS reference

</details>





</article>

<article>

Difference between TCP and UDP.

<details><summary>Theory and explanation</summary>

| | TCP | UDP |
|-|-----|-----|
| Connection | Connection-oriented | Connectionless |
| Reliability | ACK, retransmit, ordering | Best-effort |
| Use cases | HTTP, DB, file transfer | DNS, VoIP, gaming, streaming |

TCP = **reliable byte stream**; UDP = **datagrams** with lower latency overhead.

| | TCP | UDP |
|-|-----|-----|
| Connection | Connection-oriented | Connectionless |
| Reliability | ACK, retransmit, ordering | Best-effort |
| Use cases | HTTP, DB, file transfer | DNS, VoIP, gaming, streaming |

TCP = **reliable byte stream**; UDP = **datagrams** with lower latency overhead.

- TCP (Transmission Control Protocol) is a connection-oriented protocol. It is used to establish a connection between two devices before transferring data. It is reliable but slower than UDP.
- UDP (User Datagram Protocol) is a connectionless protocol. It does not establish a connection before transferring data. It is faster but less reliable than TCP.

The main difference between TCP (transmission control protocol) and UDP (user datagram protocol) is that TCP is a connection-based protocol and UDP is connectionless. While TCP is more reliable, it transfers data more slowly. UDP is less reliable but works more quickly. This makes each protocol suited to different types of data transfers.

Read more from [TCP vs UDP: What's the Difference? | Cloudflare](https://www.cloudflare.com/learning/ddos/glossary/tcp-vs-udp/)

#### Further reading
- [Cloudflare Learning Center](https://www.cloudflare.com/learning/) — networking concepts

</details>





</article>

<article>

What are the principles of OOP and why do we use OOP?

<details><summary>Theory and explanation</summary>

**Encapsulation** — hide state; expose methods.

**Abstraction** — interfaces hide implementation.

**Inheritance** — reuse via is-a hierarchy.

**Polymorphism** — one interface, many behaviors (overload/override).

**Why OOP:** modularity, reuse, modeling domain entities; trade-off is coupling if hierarchies grow deep.

**Encapsulation** — hide state; expose methods.

**Abstraction** — interfaces hide implementation.

**Inheritance** — reuse via is-a hierarchy.

**Polymorphism** — one interface, many behaviors (overload/override).

**Why OOP:** modularity, reuse, modeling domain entities; trade-off is coupling if hierarchies grow deep.

The four main principles of Object-Oriented Programming (OOP) are:

- **Encapsulation** – Bundling data and methods within a class while restricting direct access to some details.
- **Abstraction** – Hiding implementation details and exposing only essential functionalities.
- **Inheritance** – Enabling a class to derive properties and behavior from another class.
- **Polymorphism** – Allowing a single interface to represent different data types or methods (e.g., method overloading and overriding).

OOP is used to model real-world entities and relationships in software development. It promotes code reusability, modularity, and maintainability by organizing code into classes and objects. OOP also supports concepts like inheritance, polymorphism, and encapsulation, making it easier to manage complex systems.

#### Further reading
- [Oracle Java Tutorials: OOP](https://docs.oracle.com/javase/tutorial/java/concepts/) — class design

</details>





</article>

<article>

Difference between SQL and NoSQL.

<details><summary>Theory and explanation</summary>

**SQL (relational):** schemas, ACID transactions, JOINs, vertical scale + replication.

**NoSQL:** document (MongoDB), key-value (Redis), wide-column (Cassandra), graph (Neo4j). Flexible schema, horizontal scale; eventual consistency common.

Choose SQL when relationships and strong consistency matter; NoSQL for high write throughput, flexible documents, or specialized access patterns.

**SQL (relational):** schemas, ACID transactions, JOINs, vertical scale + replication.

**NoSQL:** document (MongoDB), key-value (Redis), wide-column (Cassandra), graph (Neo4j). Flexible schema, horizontal scale; eventual consistency common.

Choose SQL when relationships and strong consistency matter; NoSQL for high write throughput, flexible documents, or specialized access patterns.

- **SQL**: Full form of SQL is Structured Query Language . SQL databases are primarily called Relational Databases (RDBMS). They use structured query language (SQL) for defining and manipulating the data. These are table-based databases. SQL databases are good for complex queries and relationships between the tables.
- **NoSQL**: NoSQL databases are primarily called non-relational or distributed databases. They can be document-based, key-value pairs, graph databases, or wide-column stores. They have dynamic schemas for unstructured data. NoSQL databases are horizontally scalable.

Read more from [Understanding SQL vs NoSQL Databases | MongoDB](https://www.mongodb.com/resources/basics/databases/nosql-explained/nosql-vs-sql)

#### Further reading
- [PostgreSQL: Indexes](https://www.postgresql.org/docs/current/indexes.html) — B-tree index internals

</details>





</article>

<article>

Difference between Compiler and Interpreter.

<details><summary>Theory and explanation</summary>

**Compiler:** translates entire program to machine code **before** run (C, Go). Faster execution; slower edit-compile cycle.

**Interpreter:** executes source line-by-line or bytecode (Python, JS engines). Slower per-run unless JIT (V8).

**Java/C#:** compile to bytecode, JVM/CLR JIT at runtime — hybrid.

**Compiler:** translates entire program to machine code **before** run (C, Go). Faster execution; slower edit-compile cycle.

**Interpreter:** executes source line-by-line or bytecode (Python, JS engines). Slower per-run unless JIT (V8).

**Java/C#:** compile to bytecode, JVM/CLR JIT at runtime — hybrid.

- **Compiler**: A compiler translates code from a high-level programming language into machine code before the program runs.
- **Interpreter**: An interpreter translates code written in a high-level programming language into machine code line-by-line as the code runs.

To learn more about the difference between Compiler and Interpreter, read this article: [Difference between Compiler and Interpreter](https://www.geeksforgeeks.org/difference-between-compiler-and-interpreter/)

#### Further reading
- [GeeksforGeeks](https://www.geeksforgeeks.org/) — interview CS topics
- [MDN Web Docs](https://developer.mozilla.org/) — web and JS reference

</details>





</article>

<article>

Explain BST.

<details><summary>Theory and explanation</summary>

**Binary Search Tree**: A binary search tree is a binary tree in which the value of the left child is less than the parent node and the value of the right child is greater than the parent node.

#### Further reading
- [VisuAlgo](https://visualgo.net/en) — interactive data structure visualizations

</details>





</article>

<article>

Suppose, we insert `[1, 2, 3, 4]` this array in BST. What will it look like after insertion? What is the search complexity in this tree? What if we want to make the search complexity  O(logn)?

<details><summary>Theory and explanation</summary>

The tree will look like this:

```
    1
     \
      2
       \
        3
         \
          4
```
And the search complexity will be `O(n)` in this case. To make the search complexity `O(logn)`, we have to make the tree balanced. We can use AVL tree or Red-Black tree to make the tree balanced.

#### Further reading
- [VisuAlgo](https://visualgo.net/en) — interactive data structure visualizations

</details>





</article>

<article>

Left Join VS Full Join. Describe a scenario where we need to use Left Join.

<details><summary>Theory and explanation</summary>

![Left Join VS Full Join](https://thecrazyprogrammer.com/wp-content/uploads/2019/05/Joins-in-SQL-Inner-Outer-Left-and-Right-Join.jpg)
Here are the different types of the JOINs in SQL:

- **(INNER) JOIN**: Returns records that have matching values in both tables.
- **LEFT (OUTER) JOIN**: Returns all records from the left table, and the matched records from the right table. The result is NULL from the right side if there is no match
- **RIGHT (OUTER) JOIN**: Returns all records from the right table, and the matched records from the left table. The result is NULL from the left side when there is no match
- **FULL (OUTER) JOIN**: Returns all records when there is a match in either left or right table.

A scenario where we need to use Left Join is when we want to get all the records from the left table and the matched records from the right table. For example, we have two tables, one is the `students` table and another is the `marks` table. We want to get all the students' information and their marks. If a student has no marks, then we want to show `NULL` in the marks column. In this case, we will use Left Join. The SQL query will look like this:

```sql
SELECT students.name, marks.marks
FROM students
LEFT JOIN marks ON students.id = marks.student_id;
```

#### Further reading
- [PostgreSQL: Indexes](https://www.postgresql.org/docs/current/indexes.html) — B-tree index internals

</details>





</article>

<article>

Describe the ACID properties of the database.

<details><summary>Theory and explanation</summary>

**Atomicity** — all or nothing.

**Consistency** — invariants hold (app + DB rules).

**Isolation** — concurrent txs appear serial (levels: RC, RR, serializable).

**Durability** — committed data survives crash (WAL).

Note: Kleppmann argues **Consistency** is application-defined.

**Atomicity** — all or nothing.

**Consistency** — invariants hold (app + DB rules).

**Isolation** — concurrent txs appear serial (levels: RC, RR, serializable).

**Durability** — committed data survives crash (WAL).

Note: Kleppmann argues **Consistency** is application-defined.

ACID is a set of properties of database transactions intended to guarantee data validity despite errors, power failures, and other mishaps. Databases that support this are called ACID compliance. The properties are

- **Atomicity:** Each statement in a transaction (to read, write, update or delete data) is treated as a single unit. Either the entire statement is executed, or none of it is executed.
- **Consistency:** Ensures the databases remain consistent following some predefined business logic both before and after the transaction
- **Isolation:** Each transaction executes in such a way that one is not affected by other s though they were occurring only one.
- **Durability:** The data changes by a successfull transaction is saved even in the event of system failure

> [!IMPORTANT]
> Atomicity, isolation and durability are properties of the database, whereas consistency is a property of the application. The C in ACID was tossed in to make the acronym work. [ref: Martin Kleppmann, Designing Data Intensive Applications]

#### Further reading
- [PostgreSQL: Indexes](https://www.postgresql.org/docs/current/indexes.html) — B-tree index internals

</details>





</article>

<article>

Describe the indexing of the database. Can we index with a column that has duplicate elements?

<details><summary>Theory and explanation</summary>

**Index** (usually B+ tree) maps key → row location for **O(log n)** seeks vs full scan **O(n)**.

**Duplicate columns:** non-unique index allowed; multiple rows share key entries with row pointers.

Trade-off: faster reads, slower writes (maintain index), storage overhead.

**Index** (usually B+ tree) maps key → row location for **O(log n)** seeks vs full scan **O(n)**.

**Duplicate columns:** non-unique index allowed; multiple rows share key entries with row pointers.

Trade-off: faster reads, slower writes (maintain index), storage overhead.

Indexing is a data structure technique that is used to quickly locate and access the data in a database. it is created mainly using B+ trees.

If a column has duplicate elements, then we can still create index on that column.

Read more from [What is Indexing in Database? | Medium](https://medium.com/@rtawadrous/introduction-to-database-indexes-9b488e243cc1)

#### Further reading
- [PostgreSQL: Indexes](https://www.postgresql.org/docs/current/indexes.html) — B-tree index internals

</details>





</article>

<article>

Describe the Event loop in JS.

<details><summary>Theory and explanation</summary>

JavaScript has one **call stack** (synchronous code). Async work goes to **Web APIs** / **libuv** (timers, I/O); callbacks enqueue **task queues**.

**Event loop** repeatedly: run stack until empty → take microtasks (Promises) → take one macrotask (setTimeout, I/O callback).

**Interview:** `async/await` is syntax over Promises; still single-threaded — no parallel CPU threads without Workers.

JavaScript has one **call stack** (synchronous code). Async work goes to **Web APIs** / **libuv** (timers, I/O); callbacks enqueue **task queues**.

**Event loop** repeatedly: run stack until empty → take microtasks (Promises) → take one macrotask (setTimeout, I/O callback).

**Interview:** `async/await` is syntax over Promises; still single-threaded — no parallel CPU threads without Workers.

#### Further reading
- [MDN: JavaScript guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) — language reference
- [Oracle Java Tutorials: OOP](https://docs.oracle.com/javase/tutorial/java/concepts/) — class design

</details>





</article>

<article>

What is closure? Describe.

<details><summary>Theory and explanation</summary>

A **closure** is a function plus lexical environment of outer variables it references.

Inner functions keep outer bindings alive after outer returns — stored in heap-linked environment records (engine-specific).

Use cases: data privacy, factories, callbacks. Pitfall: loop `var` in closures — use `let` or IIFE.

A **closure** is a function plus lexical environment of outer variables it references.

Inner functions keep outer bindings alive after outer returns — stored in heap-linked environment records (engine-specific).

Use cases: data privacy, factories, callbacks. Pitfall: loop `var` in closures — use `let` or IIFE.

#### Further reading
- [MDN: JavaScript guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) — language reference

</details>





</article>

<article>

Why React? What advantages does React give us over direct DOM manipulation?

<details><summary>Theory and explanation</summary>

**Virtual DOM** diffs minimal real DOM updates → fewer expensive reflows.

**Component model** — reusable UI, one-way data flow, ecosystem (hooks, Router).

vs **direct DOM:** manual `querySelector` + update does not scale; easy to create inconsistent UI state.

**Virtual DOM** diffs minimal real DOM updates → fewer expensive reflows.

**Component model** — reusable UI, one-way data flow, ecosystem (hooks, Router).

vs **direct DOM:** manual `querySelector` + update does not scale; easy to create inconsistent UI state.

#### Further reading
- [MDN: JavaScript guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) — language reference

</details>





</article>

<article>

Why shouldn’t we mutate props in the child component?

<details><summary>Theory and explanation</summary>

Props are **read-only** inputs from parent. Mutating them breaks **single source of truth** and React's predictability (reconciliation assumes props flow down).

Use **state** in child or **lift state up** / callbacks to parent. Violation causes subtle bugs and breaks memoization.

Props are **read-only** inputs from parent. Mutating them breaks **single source of truth** and React's predictability (reconciliation assumes props flow down).

Use **state** in child or **lift state up** / callbacks to parent. Violation causes subtle bugs and breaks memoization.

#### Further reading
- [GeeksforGeeks](https://www.geeksforgeeks.org/) — interview CS topics
- [MDN Web Docs](https://developer.mozilla.org/) — web and JS reference

</details>





</article>

<article>

Why Tailwind? What benefits Tailwind give us compared to other CSS libraries?

<details><summary>Theory and explanation</summary>

**Utility-first CSS** — compose classes in markup; design tokens in config.

Benefits: fast prototyping, consistent spacing/colors, purge unused CSS in production.

Trade-off: verbose class lists; use `@apply` or components for repetition.

**Utility-first CSS** — compose classes in markup; design tokens in config.

Benefits: fast prototyping, consistent spacing/colors, purge unused CSS in production.

Trade-off: verbose class lists; use `@apply` or components for repetition.

#### Further reading
- [GeeksforGeeks](https://www.geeksforgeeks.org/) — interview CS topics
- [MDN Web Docs](https://developer.mozilla.org/) — web and JS reference

</details>





</article>

<article>

What type of language is JavaScript? Compiled or Interpreted? How do they work?

<details><summary>Theory and explanation</summary>

JavaScript is **interpreted** with **JIT** compilation (V8, SpiderMonkey). Source → AST → bytecode → optimized machine code on hot functions.

Not AOT-compiled like C. TypeScript only strips types; output is still JS.

**Interview talking points**

- Contrast Java bytecode + JVM JIT.
- Mention WebAssembly for near-native modules in browsers.

#### Further reading
- [MDN: JavaScript guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) — language reference

</details>





</article>

<article>

JavaScript is a single-threaded language, so how does it maintain asynchronous tasks?

<details><summary>Theory and explanation</summary>

JS runs user code on **one thread**; blocking the stack blocks everything.

**Concurrency via async:** callbacks, Promises, `async/await` interleave I/O completion without parallel threads.

**Workers** (`Worker`, `SharedArrayBuffer`) for true parallelism — not default model.

JS runs user code on **one thread**; blocking the stack blocks everything.

**Concurrency via async:** callbacks, Promises, `async/await` interleave I/O completion without parallel threads.

**Workers** (`Worker`, `SharedArrayBuffer`) for true parallelism — not default model.

#### Further reading
- [MDN: JavaScript guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) — language reference

</details>





</article>

<article>

Explain the event loop. Have you ever seen the implementations of libuv?

<details><summary>Theory and explanation</summary>

**libuv** is Node's C library for cross-platform async I/O (epoll/kqueue/IOCP), thread pool for file/crypto work, timers, and DNS.

Event loop phases: timers → pending → idle → poll → check → close. Interview: file read may use thread pool; network uses OS async APIs.

**libuv** is Node's C library for cross-platform async I/O (epoll/kqueue/IOCP), thread pool for file/crypto work, timers, and DNS.

Event loop phases: timers → pending → idle → poll → check → close. Interview: file read may use thread pool; network uses OS async APIs.

#### Further reading
- [MDN: JavaScript guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) — language reference
- [Oracle Java Tutorials: OOP](https://docs.oracle.com/javase/tutorial/java/concepts/) — class design

</details>





</article>

<article>

Explain var, let, const in JavaScript.

<details><summary>Theory and explanation</summary>

| | Scope | Hoisting | Reassign |
|-|-------|----------|----------|
| `var` | Function | Yes (undefined) | Yes |
| `let` | Block | TDZ | Yes |
| `const` | Block | TDZ | No binding (object contents mutable) |

Prefer **const** default, **let** when rebinding, avoid **var** in modern JS.

| | Scope | Hoisting | Reassign |
|-|-------|----------|----------|
| `var` | Function | Yes (undefined) | Yes |
| `let` | Block | TDZ | Yes |
| `const` | Block | TDZ | No binding (object contents mutable) |

Prefer **const** default, **let** when rebinding, avoid **var** in modern JS.

- **let**: Block-scoped and can be reassigned. 
- **var**: Function-scoped and can be reassigned. 
- **const**: Block-scoped and cannot be reassigned

Read more from [Var, Let, and Const – What's the Difference? | FreeCodeCamp](https://www.freecodecamp.org/news/var-let-and-const-whats-the-difference/)

#### Further reading
- [MDN: JavaScript guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) — language reference

</details>





</article>

<article>

Explain hoisting.

<details><summary>Theory and explanation</summary>

Declarations are processed before execution in scope:

- `function` declarations — fully hoisted.
- `var` — hoisted, initialized `undefined`.
- `let`/`const` — hoisted but in **Temporal Dead Zone** until line runs.

`typeof foo` before `let foo` → ReferenceError.

Declarations are processed before execution in scope:

- `function` declarations — fully hoisted.
- `var` — hoisted, initialized `undefined`.
- `let`/`const` — hoisted but in **Temporal Dead Zone** until line runs.

`typeof foo` before `let foo` → ReferenceError.

Hoisting is a JavaScript mechanism where variables and function declarations are moved to the top of their containing scope before code execution. This means that no matter where functions and variables are declared, they are moved to the top of their scope regardless of whether their scope is global or local.

Read more from [JavaScript Hoisting Explained | DigitalOcean](https://www.digitalocean.com/community/tutorials/understanding-hoisting-in-javascript)

#### Further reading
- [MDN: JavaScript guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) — language reference

</details>





</article>

<article>

Explain primitive and reference data types.

<details><summary>Theory and explanation</summary>

**Primitives** (number, string, boolean, null, undefined, symbol, bigint) — copied by value.

**References** (objects, arrays, functions) — variable holds pointer; assignment copies reference; mutations shared.

`===` compares primitives by value, objects by reference identity.

**Primitives** (number, string, boolean, null, undefined, symbol, bigint) — copied by value.

**References** (objects, arrays, functions) — variable holds pointer; assignment copies reference; mutations shared.

`===` compares primitives by value, objects by reference identity.

- **Primitive Data Types**: Primitive values are data that are stored directly in a variable. These include numbers, booleans, strings, null, and undefined. When we assign a primitive value to a variable, a copy of that value is created and stored in memory. Any changes made to the variable do not affect the original value.
- **Reference Data Types**: Reference values, on the other hand, are objects that are stored in memory and accessed through a reference. These include arrays, objects, and functions. When we assign a reference value to a variable, a reference to the original value is created and stored in memory. Any changes made to the variable affect the original value.

Read more from [JavaScript Primitive Values vs Reference Values | FreeCodeCamp](https://www.freecodecamp.org/news/javascript-assigning-values-vs-assigning-references/)

#### Further reading
- [GeeksforGeeks](https://www.geeksforgeeks.org/) — interview CS topics
- [MDN Web Docs](https://developer.mozilla.org/) — web and JS reference

</details>





</article>

<article>

Explain closure. The inner function (which is returned) of the closure has access to its outer scope, how is it possible, where the variable is stored in that time?

<details><summary>Theory and explanation</summary>

A **closure** is a function plus lexical environment of outer variables it references.

Inner functions keep outer bindings alive after outer returns — stored in heap-linked environment records (engine-specific).

Use cases: data privacy, factories, callbacks. Pitfall: loop `var` in closures — use `let` or IIFE.

A **closure** is a function plus lexical environment of outer variables it references.

Inner functions keep outer bindings alive after outer returns — stored in heap-linked environment records (engine-specific).

Use cases: data privacy, factories, callbacks. Pitfall: loop `var` in closures — use `let` or IIFE.

#### Further reading
- [MDN: JavaScript guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) — language reference

</details>





</article>

<article>

What is a pure function?

<details><summary>Theory and explanation</summary>

Same inputs → same output; **no side effects** (no I/O, no mutation of external state).

Benefits: testable, cacheable (`memoize`), safe in concurrent/FP pipelines.

`Math.random()` or `Date.now()` inside → impure.

Same inputs → same output; **no side effects** (no I/O, no mutation of external state).

Benefits: testable, cacheable (`memoize`), safe in concurrent/FP pipelines.

`Math.random()` or `Date.now()` inside → impure.

A pure function is a function where the return value is determined by its input values, without observable side effects. This is how a pure function works:

- The function always returns the same result if the same arguments are passed in.
- The function does not depend on any state, or data, change during its execution.
- The function does not modify any state, or data, outside of its scope.

Read more from [Pure Functions in JavaScript | Medium]https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-pure-function-d1c076bec976)

#### Further reading
- [GeeksforGeeks](https://www.geeksforgeeks.org/) — interview CS topics
- [MDN Web Docs](https://developer.mozilla.org/) — web and JS reference

</details>





</article>

<article>

Do you follow any functional programming philosophy?

<details><summary>Theory and explanation</summary>

Emphasize **immutable data**, **pure functions**, **higher-order functions** (`map`, `filter`, `reduce`), composition over inheritance.

In JS: avoid mutating arrays (`spread`, `map`), use `const`, prefer declarative chains. Libraries: Ramda, lodash/fp.

Emphasize **immutable data**, **pure functions**, **higher-order functions** (`map`, `filter`, `reduce`), composition over inheritance.

In JS: avoid mutating arrays (`spread`, `map`), use `const`, prefer declarative chains. Libraries: Ramda, lodash/fp.

#### Further reading
- [GeeksforGeeks](https://www.geeksforgeeks.org/) — interview CS topics
- [MDN Web Docs](https://developer.mozilla.org/) — web and JS reference

</details>





</article>

<article>

Explain the ACID properties of the database.

<details><summary>Theory and explanation</summary>

**Atomicity** — all or nothing.

**Consistency** — invariants hold (app + DB rules).

**Isolation** — concurrent txs appear serial (levels: RC, RR, serializable).

**Durability** — committed data survives crash (WAL).

Note: Kleppmann argues **Consistency** is application-defined.

**Atomicity** — all or nothing.

**Consistency** — invariants hold (app + DB rules).

**Isolation** — concurrent txs appear serial (levels: RC, RR, serializable).

**Durability** — committed data survives crash (WAL).

Note: Kleppmann argues **Consistency** is application-defined.

ACID is a set of properties of database transactions intended to guarantee data validity despite errors, power failures, and other mishaps. Databases that support this are called ACID compliance. The properties are

- **Atomicity:** Each statement in a transaction (to read, write, update or delete data) is treated as a single unit. Either the entire statement is executed, or none of it is executed.
- **Consistency:** Ensures the databases remain consistent following some predefined business logic both before and after the transaction
- **Isolation:** Each transaction executes in such a way that one is not affected by other s though they were occurring only one.
- **Durability:** The data changes by a successfull transaction is saved even in the event of system failure

> [!IMPORTANT]
> Atomicity, isolation and durability are properties of the database, whereas consistency is a property of the application. The C in ACID was tossed in to make the acronym work. [ref: Martin Kleppmann, Designing Data Intensive Applications]

#### Further reading
- [PostgreSQL: Indexes](https://www.postgresql.org/docs/current/indexes.html) — B-tree index internals

</details>





</article>

<article>

Explain indexing. Why do we need indexing? What benefit does it give us?

<details><summary>Theory and explanation</summary>

**Index** (usually B+ tree) maps key → row location for **O(log n)** seeks vs full scan **O(n)**.

**Duplicate columns:** non-unique index allowed; multiple rows share key entries with row pointers.

Trade-off: faster reads, slower writes (maintain index), storage overhead.

**Index** (usually B+ tree) maps key → row location for **O(log n)** seeks vs full scan **O(n)**.

**Duplicate columns:** non-unique index allowed; multiple rows share key entries with row pointers.

Trade-off: faster reads, slower writes (maintain index), storage overhead.

Indexing is a data structure technique that is used to quickly locate and access the data in a database. it is created mainly using B+ trees.

Indexing is important because it helps to speed up the retrieval of data from the database. It is used to quickly locate and access the data in a database. Without an index, the database engine has to scan the entire table to find the data. This can be very slow if the table is large. However, creating an unnecessary index can slow down the database system because the database engine has to update the index every time the table is updated.

Read more from [What is Indexing in Database? | Medium](https://medium.com/@rtawadrous/introduction-to-database-indexes-9b488e243cc1)

#### Further reading
- [PostgreSQL: Indexes](https://www.postgresql.org/docs/current/indexes.html) — B-tree index internals

</details>





</article>

<article>

Suppose, we want to use user_email as index. How can we do it?

<details><summary>Theory and explanation</summary>

```sql
CREATE INDEX user_email_index ON users (user_email);
```

#### Further reading
- [PostgreSQL: Indexes](https://www.postgresql.org/docs/current/indexes.html) — B-tree index internals

</details>





</article>

<article>

Explain tree, binary tree, binary search tree. In a binary search tree, if the tree is imbalanced, then how can we make it balanced?

<details><summary>Theory and explanation</summary>

- **Binary Tree**:A binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child. 
- **Binary Search Tree**: A binary search tree is a binary tree in which the value of the left child is less than the parent node and the value of the right child is greater than the parent node.

If the binary search tree is imbalanced, then we can make it balanced by using AVL tree or Red-Black tree. These trees are self-balancing binary search trees.

#### Further reading
- [VisuAlgo](https://visualgo.net/en) — interactive data structure visualizations

</details>





</article>

<article>

Explain the map, unordered_map and their complexity. Why does the complexity of the unordered_map go to O(n) in some cases?

<details><summary>Theory and explanation</summary>

`std::map` — red-black tree, **O(log n)** ops, sorted iteration.

`unordered_map` — hash table, **O(1)** average, **O(n)** worst if all keys collide (bad hash / attack).

`std::map` — red-black tree, **O(log n)** ops, sorted iteration.

`unordered_map` — hash table, **O(1)** average, **O(n)** worst if all keys collide (bad hash / attack).

- **Map**: A map is a data structure that stores key-value pairs. It is typically implemented as a balanced binary search tree, which gives it a time complexity of O(logn) for insertion, deletion, and search.
- **Unordered Map**: An unordered map is a data structure that stores key-value pairs. It is typically implemented as a hash table, which gives it an average time complexity of O(1) for insertion, deletion, and search. However, in the worst case, the time complexity can go up to O(n) if there are many collisions.

Read more from [Map vs Unordered Map in C++ | GeeksforGeeks](https://www.geeksforgeeks.org/map-vs-unordered_map-c/)

#### Further reading
- [GeeksforGeeks](https://www.geeksforgeeks.org/) — interview CS topics
- [MDN Web Docs](https://developer.mozilla.org/) — web and JS reference

</details>





</article>

<article>

Explain the four principles of OOP.

<details><summary>Theory and explanation</summary>

**Encapsulation** — hide state; expose methods.

**Abstraction** — interfaces hide implementation.

**Inheritance** — reuse via is-a hierarchy.

**Polymorphism** — one interface, many behaviors (overload/override).

**Why OOP:** modularity, reuse, modeling domain entities; trade-off is coupling if hierarchies grow deep.

**Encapsulation** — hide state; expose methods.

**Abstraction** — interfaces hide implementation.

**Inheritance** — reuse via is-a hierarchy.

**Polymorphism** — one interface, many behaviors (overload/override).

**Why OOP:** modularity, reuse, modeling domain entities; trade-off is coupling if hierarchies grow deep.

The four main principles of Object-Oriented Programming (OOP) are:

- **Encapsulation** – Bundling data and methods within a class while restricting direct access to some details.
- **Abstraction** – Hiding implementation details and exposing only essential functionalities.
- **Inheritance** – Enabling a class to derive properties and behavior from another class.
- **Polymorphism** – Allowing a single interface to represent different data types or methods (e.g., method overloading and overriding).

#### Further reading
- [Oracle Java Tutorials: OOP](https://docs.oracle.com/javase/tutorial/java/concepts/) — class design

</details>





</article>

<article>

Do you know there is an OOP feature which is only in C/C++?

<details><summary>Theory and explanation</summary>

Operator overloading is a feature in C++ that allows operators to be redefined so that they work with user-defined types. This feature is not available in all OOP languages like Java or Python.

#### Further reading
- [Oracle Java Tutorials: OOP](https://docs.oracle.com/javase/tutorial/java/concepts/) — class design

</details>





</article>

<article>

Explain the difference between an array and a linked list. Tell me some use cases for each of them. How can we access an element of an array with the index?

<details><summary>Theory and explanation</summary>

**Answer framework:** State the direct answer first, then explain with one example and one trade-off.

**Question:** Explain the difference between an array and a linked list. Tell me some use cases for each of them. How can we access an element of an array with the index?

#### Further reading
- [PostgreSQL: Indexes](https://www.postgresql.org/docs/current/indexes.html) — B-tree index internals
- [VisuAlgo](https://visualgo.net/en) — interactive data structure visualizations


</details>





</article>

<article>

Explain HTTP and HTTPS. Why HTTPS? How does data transfer in HTTPS? What is used under the hood to encrypt the communication between the sender and the receiver?

<details><summary>Theory and explanation</summary>

**HTTP** port 80, plaintext.

**HTTPS** = HTTP over **TLS**: handshake (cert, key exchange), then symmetric **AES** for bulk data. Prevents MITM eavesdropping/tampering when certs validated.

**HTTP** port 80, plaintext.

**HTTPS** = HTTP over **TLS**: handshake (cert, key exchange), then symmetric **AES** for bulk data. Prevents MITM eavesdropping/tampering when certs validated.

- HTTP (HyperText Transfer Protocol) is a communication protocol used for transferring data between web browsers and servers. It operates over port 80 and does not encrypt data, making it vulnerable to attacks like Man-in-the-Middle (MITM). 
- HTTPS (HyperText Transfer Protocol Secure) is the secure version of HTTP, using encryption to protect data from interception and tampering. It operates over port 443 and ensures confidentiality, integrity, and authentication.

In HTTPS, data transfer is encrypted using SSL/TLS (Secure Sockets Layer / Transport Layer Security). When a user connects to a secure website, the browser and server perform an SSL/TLS handshake, exchanging encryption keys and verifying the server’s identity using an SSL certificate issued by a trusted Certificate Authority (CA). The encryption uses asymmetric cryptography (RSA, ECC) for key exchange and symmetric encryption (AES) for actual data transfer, ensuring secure communication.

#### Further reading
- [Cloudflare Learning Center](https://www.cloudflare.com/learning/) — networking concepts

</details>





</article>

<article>

Is HTTPS stateful or stateless? If stateless, then how can we browse Facebook after login once?

<details><summary>Theory and explanation</summary>

HTTPS itself is stateless because it follows the HTTP protocol, which does not retain session information between requests. However, websites like Facebook manage user sessions using **cookies** and **tokens** to maintain state.

When we log in, the server sends a session ID (stored in a cookie) to our browser. This session ID is sent with every request, allowing the server to recognize and authenticate us. Additionally, modern web applications use JWT (JSON Web Tokens) or OAuth tokens for secure authentication and session management. This way, even though HTTPS is stateless, the session is maintained through these mechanisms.

#### Further reading
- [Cloudflare Learning Center](https://www.cloudflare.com/learning/) — networking concepts

</details>





</article>

<article>

Explain cookie-based authentication. How can we blacklist a cookie?

<details><summary>Theory and explanation</summary>

Server creates session on login → **Set-Cookie** (`sessionId`). Browser auto-sends cookie; server looks up session.

**Blacklist:** delete session server-side; set `Max-Age=0`; Redis revocation set for JWT jti.

Server creates session on login → **Set-Cookie** (`sessionId`). Browser auto-sends cookie; server looks up session.

**Blacklist:** delete session server-side; set `Max-Age=0`; Redis revocation set for JWT jti.

**Cookie-based authentication** is a method where a server issues a session cookie upon successful login. This cookie, stored in the user's browser, is sent with every subsequent request, allowing the server to identify the user without requiring reauthentication. The server typically stores session details in a database or in-memory store (e.g., Redis). Cookies can have attributes like HttpOnly (prevents JavaScript access), Secure (only sent over HTTPS), and SameSite (prevents CSRF attacks).

#### How to Blacklist a Cookie?
- Server-Side Invalidation – Remove the session from the database or cache, making the cookie useless.
- Set Expiry in the Past – Send a new Set-Cookie header with an expired timestamp.
- Revoke the Cookie via Logout – Overwrite it with an empty value.
- Use a Token Blacklist – If using JWT, maintain a blacklist of revoked tokens.

Read more from [Cookie-Based Authentication: A Comprehensive Guide | Auth0](https://auth0.com/blog/cookies-vs-tokens-definitive-guide/)

#### Further reading
- [Cloudflare Learning Center](https://www.cloudflare.com/learning/) — networking concepts

</details>





</article>

<article>

Do you know the structure of JWT? Explain.

<details><summary>Theory and explanation</summary>

`header.payload.signature` (Base64URL).

- **Header:** alg (`HS256`, `RS256`).
- **Payload:** claims (`sub`, `exp`, roles).
- **Signature:** HMAC or RSA over `header.payload`.

Stateless auth; revoke via short `exp` + refresh tokens or server denylist.

`header.payload.signature` (Base64URL).

- **Header:** alg (`HS256`, `RS256`).
- **Payload:** claims (`sub`, `exp`, roles).
- **Signature:** HMAC or RSA over `header.payload`.

Stateless auth; revoke via short `exp` + refresh tokens or server denylist.

JWT (JSON Web Token) is a compact, URL-safe means of representing claims to be transferred between two parties. The structure of a JWT consists of three parts separated by dots: `xxxxx.yyyyy.zzzzz`

- **Header**: Contains metadata about the token (e.g., type and signing algorithm).
- **Payload**: Contains claims (e.g., user ID, role, and expiration time).
- **Signature**: Ensures the integrity of the token and verifies that it has not been tampered with.

Read more from [Introduction to JSON Web Tokens | JWT.io](https://jwt.io/introduction/)

#### Further reading
- [Cloudflare Learning Center](https://www.cloudflare.com/learning/) — networking concepts

</details>





</article>

<article>

**Problem Statement:**
You'll be given two strings `A` and `B`, with lengths `1 <= length <= 10^6`. The strings will contain only `1`'s and `0`'s. To make `A` a good string, you can insert `B` into `A` at any place, as many times as you want (or don't insert if you don't want). You have to print `YES` or `NO` depending on whether making `A` as a good string is possible.

<details><summary>Theory and explanation</summary>

**The Definition of GOOD:** A good string will never consecutively have two `1`'s or two `0`'s.

**Input/Output:**
The input will consist of two strings in two lines, strings `A` and `B`.

The output must be only one word, "YES" or "NO".

**Sample Input/Output:**

| Input            | Output |
| ---------------- | ------ |
| 101<br>010       | YES    |
| 111<br>010       | YES    |
| 1110011<br>01010 | NO     |
| 1001001000<br>10 | NO     |

#### Further reading
- [GeeksforGeeks](https://www.geeksforgeeks.org/) — interview CS topics
- [MDN Web Docs](https://developer.mozilla.org/) — web and JS reference

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function canMakeGood(A, B) {
  const runs = A.match(/0+|1+/g) || [];
  const maxRun = Math.max(...runs.map(r => r.length), 0);
  const need = Math.ceil(maxRun / 2) - 1;
  const avail = (B.match(/01|10/g) || []).length;
  return avail >= need ? 'YES' : 'NO';
}
```


#### Code walkthrough
Max run of same bit needs separators; each copy of alternating B fixes one break.

#### Complexity

| | |
|-|-|
| Time | O(|A|+|B|) |
| Space | O(1) |


#### Edge cases
Greedy on run lengths; verify with samples 101/010 → YES.

</details>

</article>

<article>

Convert a decimal number to binary and show the output in string.

<details><summary>Theory and explanation</summary>

**Answer framework:** State the direct answer first, then explain with one example and one trade-off.

**Question:** Convert a decimal number to binary and show the output in string.

#### Further reading
- [GeeksforGeeks](https://www.geeksforgeeks.org/) — interview CS topics
- [MDN Web Docs](https://developer.mozilla.org/) — web and JS reference


</details>

<details><summary>Solution (JavaScript)</summary>

```js
function decimalToBinary(n) {
  if (n === 0) return '0';
  let bits = '';
  while (n > 0) {
    bits = (n % 2) + bits;
    n = Math.floor(n / 2);
  }
  return bits;
}
```


#### Code walkthrough
Repeatedly take `n % 2` and prepend; divide by 2 until zero.

#### Complexity

| | |
|-|-|
| Time | O(log n) |
| Space | O(log n) |


#### Edge cases
Handle `n === 0`; negative integers need a separate convention if required.

</details>

<details><summary>Solution (C++)</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;

string decimalToBinary(int n) {
    string binary = "";
    while (n > 0) {
        binary += to_string(n % 2);
        n /= 2;
    }
    reverse(binary.begin(), binary.end());
    return binary;
}
```

#### Code walkthrough

See theory section; original onsite/phone-round C++ solution preserved above.

#### Complexity

| | |
|-|-|
| Time | Depends on problem — see JavaScript tab for typical bounds |
| Space | Depends on problem |

</details>

</article>

<article>

Explain JOIN and composite keys in the database.

<details><summary>Theory and explanation</summary>

- **JOIN**: JOIN is used to combine rows from two or more tables based on a related column between them. There are different types of JOINs in SQL, such as INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN.
- **Composite Key**: A composite key is a combination of two or more columns in a table that can be used to uniquely identify each row in the table. A composite key is also known as a compound key.

#### Further reading
- [PostgreSQL: Indexes](https://www.postgresql.org/docs/current/indexes.html) — B-tree index internals

</details>





</article>

<article>

Learn about polymorphism and inheritance in DB in your free time. (This is not a question).

<details><summary>Theory and explanation</summary>

Runtime **polymorphism** — virtual dispatch picks overridden `fight()` per actual type.

#### Further reading
- [Oracle Java Tutorials: OOP](https://docs.oracle.com/javase/tutorial/java/concepts/) — class design

</details>





</article>
