---
description: Welldev interview questions, Welldev interview stages, Welldev interview details, Welldev interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/welldev
---
# WellDev Ltd

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-| :- |
| Founding year | |
| Company Website | https://www.welldev.io/ |
| Career Website | https://www.welldev.io/careers |
| Technologies Used| Ruby on Rails, Android, iOS, ReactJS |

## Introduction

WellDev Ltd is a software company based in Zurich, Switzerland, specializing in software development and IT services. It has offices in Bangladesh (Dhaka), South Africa, Canada etc.

## Interview Stages

1. **Initial Screening:** After dropping CV they take a MCQ Round, almost every candidate gets an email for participation in this round.
2. **Round 1:** The first round is a technical round and generally lasts for an hour.
3. **Round 2:** The second round is divided into two part. The first part is a behavioural part taken by HR of the company. For the second part two software engineer conducts the technical sessions.
4. **COO Round:** The final round is taken by the COO of the company

## MCQ Round

A Broad Range of Topics

This round consisted of a multiple-choice questionnaire covering these topics. The test required me to share my screen with Quillgo and keep my camera on. It covers wide range of topics like JavaScript fundamentals, OOP, DBMS, SWE principles, Networking, Rest API knowledge, Analytical reasoning, DSA (time complexity, sorting, binary trees, MST, greedy algorithms).

## First Round Questions

Hands-On Problem Solving

<article>

What will the output of this code in C Programming Language and why?

```C
int arr[3] = {1, 2, 3};

if(&arr[0] == &arr){
    printf("They are the same!");
}else {
    printf("Not same");
}
```

<details><summary>Theory and explanation</summary>

In C, **array name decays to pointer to first element** in most expressions. `&arr[0]` and `arr` compare equal; `&arr` is pointer to whole array (same address, different type).

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// In C: array name decays to &arr[0]; see preserved C examples.
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases
Ask clarifying questions before coding.

</details>

<details><summary>Solution (other languages)</summary>

The name of the array is a pointer to the first item of the Array.
So it will print "They are the same!"

</details>

</article>


<article>

Given an array, what will be the base address if we print the array name only (e.g., printf(ara))?

<details><summary>Theory and explanation</summary>

Printing array name gives address of first element (decay). `arr == &arr[0]`; `&arr` is address of array object.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// In C: array name decays to &arr[0]; see preserved C examples.
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases
Ask clarifying questions before coding.

</details>

<details><summary>Solution (other languages)</summary>

It will print the address of the first item of the array.
In C, you can't pass array to functions by "Pass by value".
So when you pass an array to an function (for example: printf(arr)),
the compiler will actually pass the pointer to the first element. 
You can easily test this hypothesis by doing something like this:

```C
int arr[1] = {100};

if(arr == &arr){
    printf("Yay!\n");
}

if(arr == &arr[0]){
    printf("Damn!");
}
```

The above code should print

```bash
Yay!
Damn!
```

</details>

</article>


<article>

What is the time complexity of the print statement?
if it's `O(1)` why is that? Is it the same case for Linked List?
If it's not, why it isn't the same case?
```python
arr = [1, 2, 3, 4]

print(arr[2])
```

<details><summary>Theory and explanation</summary>

Array index access is **O(1)** — base + offset. Linked list traversal to index i is **O(i)** — no random access.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
const arr = [1,2,3,4];
console.log(arr[2]); // O(1) random access
```

#### Code walkthrough
Array index is O(1); linked list would be O(n).

#### Complexity
| | |
|-|-|
| Time | O(1) |
| Space | O(1) |

#### Edge cases
Ask clarifying questions before coding.

</details>

<details><summary>Solution (other languages)</summary>

`Tip:`
Learn about stack and heap memory and their use cases when memory is allocated.
Learn about compile time and runtime memory allocation.

</details>

</article>


<article>

Can we run binary search on a sorted LinkedList? If we can, what issues we might face?

<details><summary>Theory and explanation</summary>

Possible but **O(n)** per mid find without auxiliary structure; loses BS advantage. Use skip list or copy to array for O(log n) searches.

**Hint recap:** Think about how and why arrays can be divided easily but LinkedList can't be.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// Possible but O(n) per step — use array or skip list for O(log n).
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | O(n) per query |
| Space | O(1) |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

Write a code to delete the middle element of a stack without using any additional data structure while preserving the original order. Input: [1, 2, 3, 4, 5]. Output: [1, 2, 4, 5]

<details><summary>Theory and explanation</summary>

Recursion or two-stack trick: pop all to temp, skip middle on push back.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function deleteMiddle(stack) {
  const temp = [];
  while (stack.length) temp.push(stack.pop());
  const mid = Math.floor(temp.length / 2);
  temp.splice(mid, 1);
  while (temp.length) stack.push(temp.pop());
  return stack;
}
```

#### Code walkthrough
Pop to temp, remove middle, restore.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(n) |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

```python
def fn(n):
    if n == 0:
        return 0

    return n + fn(n-1)
```

Given the above function, rename the function according to what the function tries to achive.

`2nd Iteration:`
Write the same function but in a iterative manner.
Does the both implementations have same Time Complexity and Space Complxity?

<details><summary>Theory and explanation</summary>

Recursive sum 1..n = **triangular number** n(n+1)/2. Iterative loop O(n) time O(1) space vs recursion O(n) stack.

**Hint recap:** Write down the stack trace of the recursive function and try to speak aloud while doing so.
After getting what the function returns, rename the function accordingly.

For the second iterations, a simple loop will be the answer.
However, think deeply about the fundamental difference between the two implementations.
One of the implementation uses a Data structure, one doesn't. So their space complexity won't be same.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function triangularNumber(n) {
  return (n * (n + 1)) / 2;
}
// iterative: O(n) time O(1) space vs recursive O(n) stack
```

#### Code walkthrough
Sum 1..n; iterative avoids call stack.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

What is the time complexity of the following code?

```C
int fun(int n) {
    if(n <= 1) return n;
    int x = fun(n - 1);
    int y = fun(n - 2);
    return x + y;
}
```

<details><summary>Theory and explanation</summary>

Naive recursive Fibonacci **O(2^n)** — repeated subproblems. Memoization O(n).

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function fib(n) {
  if (n <= 1) return n;
  return fib(n-1) + fib(n-2); // O(2^n) naive
}
```

#### Code walkthrough
Naive recursion exponential; memoize for O(n).

#### Complexity
| | |
|-|-|
| Time | O(2^n) |
| Space | O(n) stack |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

Explain the order of SQL query execution (e.g., FROM, WHERE, GROUP BY, HAVING, SELECT).

<details><summary>Theory and explanation</summary>

Logical order: **FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT**. Optimizer may reorder if equivalent.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// See Theory tab for full explanation.
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | Varies |
| Space | Varies |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

Given a table with redundant data in multiple columns, how would you optimize it? (Hint: Normalization)

<details><summary>Theory and explanation</summary>

**Normalization** — 1NF atomic columns, 2NF no partial deps, 3NF no transitive deps; split tables, use FKs.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```sql
-- Split redundant columns into Student, Course, Enrollment tables
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

Given a Java code, identify issues that violate access modifiers.

<details><summary>Theory and explanation</summary>

Watch **access modifiers** — private fields accessed from wrong class, package-private across packages, violating encapsulation.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// Java: private fields must not be accessed from unrelated classes; use getters.
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

Explain the basic concepts of Object-Oriented Programming (OOP).

<details><summary>Theory and explanation</summary>

Encapsulation, Abstraction, Inheritance, Polymorphism — see OOP pillars.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class Animal {
  speak() { return '...'; }
}
class Dog extends Animal {
  speak() { return 'woof'; } // polymorphism
}
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

What are the ACID properties in DBMS?

<details><summary>Theory and explanation</summary>

Atomicity, Consistency, Isolation, Durability — transactional guarantees.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// Transaction: BEGIN; ... COMMIT; or ROLLBACK on failure
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Ask clarifying questions before coding.

</details>

<details><summary>Solution (other languages)</summary>

ACID is a set of properties of database transactions intended to guarantee data validity despite errors, power failures, and other mishaps. Databases that support this are called ACID compliance. The properties are

- **Atomicity:** Each statement in a transaction (to read, write, update or delete data) is treated as a single unit. Either the entire statement is executed, or none of it is executed.
- **Consistency:** Ensures the databases remain consistent following some predefined business logic both before and after the transaction
- **Isolation:** Each transaction executes in such a way that one is not affected by other s though they were occurring only one.
- **Durability:** The data changes by a successfull transaction is saved even in the event of system failure

> [!IMPORTANT]
> Atomicity, isolation and durability are properties of the database, whereas consistency is a property of the application. The C in ACID was tossed in to make the acronym work. [ref: Martin Kleppmann, Designing Data Intensive Applications]

</details>

</article>


<article>

A basic GRE-like math question.

<details><summary>Theory and explanation</summary>

Practice ratios, percentages, combinatorics under time pressure.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// Practice ratios, percentages, combinations under time limit
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

Write a SQL query to show all the duplicate rows in a table.

<details><summary>Theory and explanation</summary>

`GROUP BY cols HAVING COUNT(*) > 1` or self-join on key.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```sql
SELECT col, COUNT(*) FROM t GROUP BY col HAVING COUNT(*) > 1;
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | O(n log n) with sort/group |
| Space | O(n) |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

Can we make a stack with a queue?

<details><summary>Theory and explanation</summary>

Two-queue method: costly push or costly pop — amortized O(1) with two queues.

**Hint recap:** Think multiple queue.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// Two queues: push costly or pop costly — amortized O(1)
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | O(1) amortized |
| Space | O(n) |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

Write an API call to check whether the system is running properly and explain a GET API call.

<details><summary>Theory and explanation</summary>

**Health check endpoint** GET /health returns 200 + status JSON; idempotent, no side effects.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
const res = await fetch('/api/health', { method: 'GET' });
console.log(await res.json());
```

#### Code walkthrough
GET is idempotent read; check status 200.

#### Complexity
| | |
|-|-|
| Time | O(1) network |
| Space | O(1) |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

Write a code to create a directory and a text file inside it with “Hello World” written.

<details><summary>Theory and explanation</summary>

Use fs.mkdir / os.makedirs with error handling.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
const fs = require('fs');
fs.mkdirSync('dir', { recursive: true });
fs.writeFileSync('dir/hello.txt', 'Hello World');
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | Varies |
| Space | Varies |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

What happens if two people try to reserve the same ticket simultaneously in a ticket reservation system? How would you solve this problem in a ticket management system? What will be your idea in this regard?

<details><summary>Theory and explanation</summary>

**Race condition** — use DB transaction + row lock (`SELECT FOR UPDATE`) or optimistic concurrency (version column).

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// Use DB transaction + SELECT ... FOR UPDATE or optimistic locking with version column
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

How many APIs are required to solve the above ticket reservation problem?

<details><summary>Theory and explanation</summary>

Typical: search availability, hold/reserve, payment confirm, cancel — discuss RESTfully.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// Typical: GET seats, POST hold, POST pay, DELETE cancel — discuss REST design
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

How can passwords be secured so that no one (even the administrator) can view them? How can password hashing be strengthened? What techniques do you know? (Hint: Salting and hashing techniques)

<details><summary>Theory and explanation</summary>

**bcrypt/Argon2** + unique salt per user; never store plaintext; pepper in KMS optional.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
const hash = await bcrypt.hash(password, 12); // store hash+salt only
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

What is a trigger in DBMS, and what does cascading mean?

<details><summary>Theory and explanation</summary>

Trigger runs SQL on INSERT/UPDATE/DELETE; **CASCADE** propagates FK changes/deletes.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// See Theory tab for full explanation.
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | Varies |
| Space | Varies |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

If we need to display a large amount of data on a website, what technique should be followed? (Hint: Pagination)

<details><summary>Theory and explanation</summary>

**Pagination** cursor or offset; virtual scrolling on frontend.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
fetch(`/api/items?page=${page}&limit=20`)
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | O(limit) per page |
| Space | O(1) |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

What happens when we browse a website? How are the contents rendered?

<details><summary>Theory and explanation</summary>

DNS → TCP/TLS → HTTP request → server → HTML/CSS/JS → render pipeline.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// DNS → TCP/TLS → HTTP → parse HTML → CSSOM → render tree → paint
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

What is the difference between SQL and NoSQL?

<details><summary>Theory and explanation</summary>

SQL relational schema ACID; NoSQL document/KV/graph flexible scale-out.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// See Theory tab for full explanation.
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | Varies |
| Space | Varies |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

For storing values from cache memory to RAM, should we use SQL or NoSQL?

<details><summary>Theory and explanation</summary>

Often **Redis**/in-memory KV (NoSQL) — speed over relational joins.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// See Theory tab for full explanation.
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | Varies |
| Space | Varies |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

[**💻 Submit Code**](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)

<details><summary>Theory and explanation</summary>

Monotonic stack — largest rectangle in histogram.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function largestRectArea(heights) {
  const st = [];
  let best = 0;
  heights.push(0);
  for (let i = 0; i < heights.length; i++) {
    while (st.length && heights[st.at(-1)] > heights[i]) {
      const h = heights[st.pop()];
      const w = st.length ? i - st.at(-1) - 1 : i;
      best = Math.max(best, h * w);
    }
    st.push(i);
  }
  return best;
}
```

#### Code walkthrough
Monotonic stack tracks increasing bars.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(n) |

#### Edge cases
Ask clarifying questions before coding.

</details>

<details><summary>Solution (other languages)</summary>

::: code-group

```C++ [Stack]
// src: https://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-using-stack/
int largestRectangleArea(vector<int>& hist) {
    int n = hist.size();
    stack<int> s;

    int max_area = 0;
    int tp;
    int area_with_top;
    int i = 0;
    while (i < n) {
        if (s.empty() || hist[s.top()] <= hist[i]){
            s.push(i++);
        } else {
            tp = s.top();
            s.pop();

            area_with_top = hist[tp] * (s.empty() ? i : i - s.top() - 1);
            max_area = max(max_area,area_with_top);
        }
    }

    while (s.empty() == false) {
        tp = s.top();
        s.pop();

        area_with_top = hist[tp] * (s.empty() ? i : i - s.top() - 1);
        max_area = max(max_area,area_with_top);
    }

    return max_area;
}
```

```C++ [Segment Tree]
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pii pair<ll,ll>
#define F first
#define S second
const int MAX = 1e9+5;
const int N = 200005;
pii segtree[4*N];
int ara[N],n;

void build(int node,int l,int r ){
    if( l == r ){
        segtree[node] = {ara[l],l};
        return;
    }
    int mid = (l+r)/2;
    build(node*2,l,mid);
    build(node*2+1,mid+1,r);
    segtree[node] = min( segtree[node*2],segtree[node*2+1] );
}

pii query(int node,int L,int R,int l,int r){
    if( l>R or r<L ) return {MAX,-1};
    if( l>=L and r<=R ) return segtree[node];
    int mid = (l+r)/2;
    return min( query(node*2,L,R,l,mid), query(node*2+1,L,R,mid+1,r) );
}

ll getRect(int l,int r){
    if( l>r ) return 0;
    auto pp = query(1,l,r,0,n-1);
    ll res = (r-l+1)*pp.F;
    return max({ res, getRect(l,pp.S-1),getRect(pp.S+1,r) });
}
int main(){
    cin>>n;
    for(int i=0;i<n;i++) cin>>ara[i];
    build(1,0,n-1);

    cout<<getRect(0,n-1);
}
```

:::

</details>

</article>


<article>

You have a `n`-story building, and two eggs. An egg will break if dropped from a certain height (ie above a floor `f`).  Determine the minimum number of moves that you need to determine with certainty what the value of `f` is.

[**💻 Submit Code**](https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/description/)

<details><summary>Theory and explanation</summary>

Two-egg drop — sqrt(2n) moves optimal strategy.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function twoEggDrop(n) {
  return Math.ceil((Math.sqrt(8*n + 1) - 1) / 2);
}
```

#### Code walkthrough
Optimal block strategy ~ sqrt(2n).

#### Complexity
| | |
|-|-|
| Time | O(sqrt n) |
| Space | O(1) |

#### Edge cases
Ask clarifying questions before coding.

</details>

<details><summary>Solution (other languages)</summary>

```C++
class Solution {
public:
    int twoEggDrop(int n) {
        int sq = sqrt(2*n);
        if ( sq * (sq+1) < 2*n ) sq++;
        return sq;
    }
};
```

</details>

</article>


<article>

Given a table with product_id, price, and product_name, write a query to find products with the same price.

<details><summary>Theory and explanation</summary>

Self-join or window `COUNT(*) OVER (PARTITION BY price) > 1`.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```sql
SELECT p1.product_name, p1.price FROM products p1
JOIN products p2 ON p1.price = p2.price AND p1.product_id < p2.product_id;
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | Varies |
| Space | Varies |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

What is the difference between DELETE, TRUNCATE, and DROP in SQL?

<details><summary>Theory and explanation</summary>

DELETE row-wise with WHERE; TRUNCATE fast clear table; DROP removes table object.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```sql
DELETE FROM t WHERE id=1; -- row-level, rollback possible
TRUNCATE t; -- fast, resets identity
DROP TABLE t; -- removes definition
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

Explain threading in OOP.

<details><summary>Theory and explanation</summary>

Threads share process memory; sync with mutex/semaphore; avoid race on shared state.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// See Theory tab for full explanation.
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | Varies |
| Space | Varies |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

How do you check for changes in a database?

<details><summary>Theory and explanation</summary>

Audit columns, triggers, CDC (Debezium), binlog replication, temporal tables.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// updated_at column, triggers, or CDC stream from binlog/WAL
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

Many questions from my CV (all practical, not just asking what you have done).

<details><summary>Theory and explanation</summary>

Prepare STAR stories for each resume bullet with metrics.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// Prepare STAR stories with metrics for each resume bullet
```

#### Code walkthrough
Apply concept directly or use preserved answer.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Ask clarifying questions before coding.

</details>

</article>


<article>

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

[**💻 Submit Code**](https://leetcode.com/problems/move-zeroes/description/)

<details><summary>Theory and explanation</summary>

Two-pointer move zeroes — same as Therap SWE question.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function moveZeroes(nums) {
  let i = 0;
  for (let j = 0; j < nums.length; j++) {
    if (nums[j] !== 0) [nums[i++], nums[j]] = [nums[j], nums[i]];
  }
}
```

#### Code walkthrough
Two-pointer in-place stable move.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases
Ask clarifying questions before coding.

</details>

<details><summary>Solution (other languages)</summary>

```C++
void moveZeroes(vector<int>& nums) {
    int i = 0;
    for(int j=0;j<nums.size();j++){
        swap(nums[i], nums[j]);
        if( nums[i] != 0 ) i++;
    }
}
```

</details>

</article>

## Contributors

1. [Salman Farsi](https://www.linkedin.com/in/salmanfarsi0/)
