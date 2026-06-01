---
description: Samsung Research Bangladesh interview questions, Samsung Research Bangladesh interview stages, Samsung Research Bangladesh interview details, Samsung Research Bangladesh interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/srbd
---
# SRBD

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-| :- |
| Founding year | |
| Company Website | https://research.samsung.com/srbd |
| Career Website |  |
| Technologies Used| Windows, IOS, Android, Tizen, C/C++, Java, Objective-C, Swift, C#, Kotlin, Spring, WPF, UWP, MFC, Machine Learning |

## Introduction
[Samsung R&D Institute Bangladesh (SRBD)](https://research.samsung.com/srbd) started its journey in February 2011. Located in the heart of Dhaka, it is the first ever R&D hub set up by a multinational company in Bangladesh.

> [!TIP]
> SRBD organizes a coding contest every year. The prize money is very handsome. Apart from that, if you do advance to round 2 or 3 means you might get a call for interview skipping the initial screening
## Interview Stages
SRBD takes interview in two round.

1. **Coding round:** Round 1 is coding round. The problems are typically from leetcode. You can only proceed to round 2 if you can solve round 1 correctly.

1. **Technical round:** Round 2 is a technical round. You might get asked about basic theories or solve some simple problems

## Coding Round Questions

<article>

You are given `n` balloons, indexed from `0` to `n - 1`. Each balloon is painted with a number on it represented by an array `nums`. You are asked to burst all the balloons.

If you burst the `ith` balloon, you will get `nums[i - 1] * nums[i] * nums[i + 1]` coins. If `i - 1` or `i + 1` goes out of bounds of the array, then treat it as if there is a balloon with a `1` painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Variants: coins achieved is nums[i-1]*nums[i+1]

[**💻 Submit Code**](https://leetcode.com/problems/burst-balloons/description/)

<details><summary>Theory and explanation</summary>

[LeetCode 312 — Burst Balloons](https://leetcode.com/problems/burst-balloons/) is classic **interval DP**.

Pad `nums` with `1` at both ends so boundary bursts multiply by 1. After bursts, only **neighbors** matter — order of removal defines which values become adjacent.

**State**

`dp[left][right]` = max coins from bursting all balloons **strictly between** `left` and `right` (exclusive endpoints).

**Transition**

Choose last balloon `k` to burst in `(left, right)`:

`dp[left][right] = max over k of (nums[left]*nums[k]*nums[right] + dp[left][k] + dp[k][right])`

Bursting `k` **last** means neighbors `left` and `right` were already cleared on both sides — they are the adjacent balloons when `k` is popped.

**Variant** `nums[i-1]*nums[i+1]` — same DP skeleton; change the coin formula in the transition.

**Interview talking points**

- Length `n ≤ 500` needs `O(n³)` DP — brute force permutation is impossible.
- Fill by increasing interval length.
- Space can be optimized with rolling arrays if needed.

#### Further reading

- [LeetCode: Burst Balloons](https://leetcode.com/problems/burst-balloons/) — official statement
- [GeeksforGeeks: Burst balloons DP](https://www.geeksforgeeks.org/burst-balloon-to-maximize-coins/) — walkthrough
- [CP-Algorithms: DP on intervals](https://cp-algorithms.com/dynamic_programming/intro-to-dp.html) — interval DP mindset

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function maxCoins(nums) {
  const a = [1, ...nums, 1];
  const n = a.length;
  const dp = Array.from({ length: n }, () => Array(n).fill(0));

  for (let len = 3; len <= n; len++) {
    for (let left = 0; left + len - 1 < n; left++) {
      const right = left + len - 1;
      for (let k = left + 1; k < right; k++) {
        const coins =
          a[left] * a[k] * a[right] + dp[left][k] + dp[k][right];
        dp[left][right] = Math.max(dp[left][right], coins);
      }
    }
  }

  return dp[0][n - 1];
}
```

#### Code walkthrough

- **Padding** — `a[0]` and `a[n-1]` are `1` (virtual balloons).
- **`len` loop** — intervals of increasing size; inner `k` is the **last** burst index.
- **Coin term** — `a[left]*a[k]*a[right]` uses neighbors after inner balloons are gone.

#### Complexity

| | |
|-|-|
| Time | O(n³) |
| Space | O(n²) |

#### Edge cases

- **Single real balloon** — answer is `1 * nums[0] * 1`.
- **Zeros in `nums`** — product may be 0; DP still valid.
- **Variant formula** — swap coin term only; keep interval structure.

</details>

</article>

<article>

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or null. Construct a deep copy of the list.

The deep copy should consist of exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

<details><summary>Theory and explanation</summary>

[LeetCode 138 — Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)

**Challenge** — when setting `copy.random`, the target node may not exist yet in a one-pass clone.

**Approach 1: Hash map** (original → copy)

- First pass: create clone for every original node; store in `Map`.
- Second pass: wire `next` and `random` using the map.

**Approach 2: Interleaving** (O(1) extra space)

- Insert clone after each original: `A → A' → B → B' → …`
- Assign `random` for clones using `orig.random.next`.
- Separate lists.

**Interview talking points**

- Deep copy means **new objects**, not reusing old nodes.
- DFS + map works for graphs; linked list is linear with one random edge per node.
- Time O(n), space O(n) with map.

#### Further reading

- [LeetCode: Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) — problem and constraints
- [GeeksforGeeks: Clone linked list with random pointer](https://www.geeksforgeeks.org/a-linked-list-with-next-and-arbit-pointer/) — interleaving method
- [NeetCode: Clone graph / list patterns](https://neetcode.io/) — pointer wiring practice

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function copyRandomList(head) {
  if (!head) return null;
  const map = new Map();

  let cur = head;
  while (cur) {
    map.set(cur, { val: cur.val, next: null, random: null });
    cur = cur.next;
  }

  cur = head;
  while (cur) {
    const clone = map.get(cur);
    clone.next = cur.next ? map.get(cur.next) : null;
    clone.random = cur.random ? map.get(cur.random) : null;
    cur = cur.next;
  }

  return map.get(head);
}
```

#### Code walkthrough

- **Pass 1** — create clone node per original; store mapping.
- **Pass 2** — set `next` and `random` on clones using mapped targets.
- **Return** — clone head from `map.get(head)`.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(n) for the map and clone nodes |

#### Edge cases

- **Empty list** — return `null`.
- **`random` is null** — clone `random` stays `null`.
- **Self-loop random** — `random` points to self; map handles correctly.

</details>

<details><summary>Solution (other languages)</summary>

```C++
class Solution {
public:
    unordered_map<Node*,Node*> random;
    Node* copyRandomList(Node* head) {
        if( head == NULL ) return NULL;
        Node* node = new Node(head->val);
        random[head] = node;
        node->next = copyRandomList(head->next);
        node->random = random[head->random];
        return node;
    }
};
```

</details>

</article>

<article>

 
Mr. Kim has to deliver refrigerators to `N` customers. From the office, he is going to visit all the customers and then return to his home. 
Each location of the office, his home, and the customers is given in the form of integer coordinates (x,y) (0≤x≤100, 0≤y≤100) . 
The distance between two arbitrary locations (x1, y1) and (x2, y2) is computed by |x1-x2| + |y1-y2|, where |x| denotes the absolute value 
of x; for instance, |3|=|-3|=3. The locations of the office, his home, and the customers are all distinct. You should plan an optimal way 
to visit all the N customers and return to his among all the possibilities. 

You are given the locations of the office, Mr. Kim’s home, and the customers; the number of the customers is in the range of 5 to 10. 

Write a program that, starting at the office, finds a (the) shortest path visiting all the customers and returning to his home. 
Your program only have to report the distance of a (the) shortest path.

<details><summary>Theory and explanation</summary>

This is **TSP with fixed start and end** on a small graph (`N` customers ≈ 5–10).

- **Metric**: Manhattan distance `|x1-x2| + |y1-y2|`.
- **Route**: office → visit all customers in some order → home.
- **Goal**: minimize total distance (report distance only).

With `N ≤ 10`, **bitmask DP (Held–Karp)** is standard:

`dp[mask][i]` = min distance to visit customer set `mask`, ending at customer `i`, starting from office.

Alternatively **permutations** (`N!`) are feasible when `N = 5` (120 orders).

**Interview talking points**

- Precompute pairwise distances O(N²).
- Include office and home in the tour endpoints (not in the mask).
- Mention that general TSP is NP-hard; small `N` allows exact DP.

#### Further reading

- [GeeksforGeeks: Travelling Salesman Problem](https://www.geeksforgeeks.org/travelling-salesman-problem-set-1/) — problem definition
- [CP-Algorithms: TSP bitmask DP](https://cp-algorithms.com/graph/travelling-salesman.html) — Held–Karp
- [LeetCode: Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) — related state-space search

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function manhattan(a, b) {
  return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
}

function shortestDeliveryRoute(office, home, customers) {
  const n = customers.length;
  const dist = (i, j) =>
    i < 0 || j < 0
      ? manhattan(i === -1 ? office : home, j === -1 ? office : home)
      : manhattan(customers[i], customers[j]);

  const fromStart = (i) => manhattan(office, customers[i]);
  const toHome = (i) => manhattan(customers[i], home);

  const size = 1 << n;
  const dp = Array.from({ length: size }, () => Array(n).fill(Infinity));

  for (let i = 0; i < n; i++) dp[1 << i][i] = fromStart(i);

  for (let mask = 1; mask < size; mask++) {
    for (let i = 0; i < n; i++) {
      if (!(mask & (1 << i))) continue;
      for (let j = 0; j < n; j++) {
        if (mask & (1 << j)) continue;
        const next = mask | (1 << j);
        dp[next][j] = Math.min(
          dp[next][j],
          dp[mask][i] + manhattan(customers[i], customers[j])
        );
      }
    }
  }

  const full = size - 1;
  let best = Infinity;
  for (let i = 0; i < n; i++) {
    best = Math.min(best, dp[full][i] + toHome(i));
  }
  return best;
}
```

#### Code walkthrough

- **`dp[mask][i]`** — min cost to reach customer `i` having visited exactly the set `mask`.
- **Initialize** — single-customer masks from office.
- **Transitions** — add one unvisited customer per step.
- **Finish** — add Manhattan leg from last customer to home.

#### Complexity

| | |
|-|-|
| Time | O(N² · 2^N) |
| Space | O(N · 2^N) |

#### Edge cases

- **N = 0** — distance office → home only.
- **N = 1** — office → customer → home.
- **Duplicate coordinates** — problem states distinct locations.

</details>

</article>

<article>

You are given a directed graph represented by an adjacency list. Your task is to detect if there exists a cycle in the graph.
If a cycle is found, print the nodes of the cycle in sorted order. Additionally, provide the results for each test case in the format 
"#testCaseNo node1 node2 ... nodeK". If no cycle is present, print 0.

<details><summary>Theory and explanation</summary>

**Cycle detection in a directed graph** uses **DFS** with a **recursion stack** (or “visiting” state):

- `0` unvisited, `1` visiting (on current path), `2` finished.
- If DFS reaches an edge to a `1` node, a **back edge** exists → cycle.
- Record `parent` to reconstruct the cycle; output nodes in **sorted order** per problem format.

**Multiple test cases** — loop test cases, reset arrays per case.

**Interview talking points**

- Distinguish directed vs undirected cycle rules.
- For “print cycle sorted,” collect nodes on the cycle, then `sort()`.
- BFS (Kahn) detects cycles via incomplete topological sort — alternative approach.

#### Further reading

- [GeeksforGeeks: Detect cycle in directed graph](https://www.geeksforgeeks.org/detect-cycle-in-a-graph/) — DFS colors
- [CP-Algorithms: Finding cycles](https://cp-algorithms.com/graph/finding-cycle.html) — directed case
- [LeetCode: Course Schedule](https://leetcode.com/problems/course-schedule/) — cycle existence variant

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function detectDirectedCycle(adj) {
  const n = adj.length;
  const state = Array(n).fill(0); // 0 unvisited, 1 visiting, 2 done
  const parent = Array(n).fill(-1);
  let cycleNodes = null;

  function dfs(u) {
    state[u] = 1;
    for (const v of adj[u] || []) {
      if (state[v] === 0) {
        parent[v] = u;
        if (dfs(v)) return true;
      } else if (state[v] === 1) {
        // back edge u -> v: reconstruct cycle
        const path = [v];
        let cur = u;
        while (cur !== v) {
          path.push(cur);
          cur = parent[cur];
        }
        path.push(v);
        cycleNodes = [...new Set(path)].sort((a, b) => a - b);
        return true;
      }
    }
    state[u] = 2;
    return false;
  }

  for (let i = 0; i < n; i++) {
    if (state[i] === 0 && dfs(i)) break;
  }
  return cycleNodes;
}
```

#### Code walkthrough

- **`state[v] === 1`** — back edge to node still on DFS stack → cycle found.
- **Reconstruct** — walk `parent` from `u` back toward `v`.
- **Sorted output** — `sort` before printing `#t n1 n2 …`.

#### Complexity

| | |
|-|-|
| Time | O(V + E) per test case |
| Space | O(V) |

#### Edge cases

- **No cycle** — print `0` or `#t` only per spec.
- **Multiple cycles** — usually report one discovered cycle.
- **Disconnected graph** — DFS from every unvisited node.

</details>

<details><summary>Solution (other languages)</summary>

```C++
#include<bits/stdc++.h>
using namespace std;
int firstNodeOfTheCycle, lastNodeOfTheCycle;
bool detectCycle(int node, vector<vector<int>>& adjList, vector<bool> &visited, vector<bool> &dfsVisited, vector<int> &parent){
    visited[node] = true;
    dfsVisited[node] = true;

    for(auto neighbour : adjList[node]){
        if(!visited[neighbour]){
            parent[neighbour] = node;
            bool isCycleDetected = detectCycle(node, adjList, visited, dfsVisited, parent);
            if(isCycleDetected){
                firstNodeOfTheCycle = neighbour, lastNodeOfTheCycle = node;
                return true;
            }
        }
    }

    dfsVisited[node] = false;
    return false;
}

void calculateCycle(vector<int>& ans, vector<int>& parent){
    int curNode = lastNodeOfTheCycle;
    while(curNode != firstNodeOfTheCycle){
        ans.push_back(curNode);
        curNode = parent[curNode];
    }
    ans.push_back(curNode);
}
int main(){
    int tc = 10;
    for(int t = 1; t < tc; t++){
        int n,m;
        bool wasVisited = false;
        cin >> n >> m;
        vector<vector<int>>& adjList(n + 1);
        vector<bool> visited(n + 1, false), dfsVisited(n + 1, false);
        vector<int> parent(n + 1, -1), ans;
        for(int i = 0; i < m; i++){
            int u, v;
            cin >> u >> v;
            adjList[u].push_back(v);
        }
        for(int i = 1; i <= n; i++){
            if(!visited[i]){
                bool isCycleDetected = detectCycle(i, adjList, visited, dfsVisited, parent);
                if(isCycleDetected){
                    wasVisited = true;
                    calculateCycle(ans, parent);
                    sort(ans.begin(), ans.end());
                    cout<<"#"<<t;
                    for(auto it: ans){
                        cout<<" "<<it;
                    }
                    cout<<endl;
                    break;
                }
            }
        }
        if(!wasVisited){
            cout<<"#"<<t<<" "<<endl;
        }
    }
}
```

</details>

</article>

<article>

You have string with repeated character. Example : `abcaade`. Count the number of characters that occur more than once. You can't use array or map. 

<details><summary>Theory and explanation</summary>

Count **distinct characters** that appear **at least twice** in the string, without `array` or `map` (hash table).

**Approach 1: Sort and scan** — sort the string (`O(n log n)`), scan runs of equal characters; if run length ≥ 2, count that character once.

**Approach 2: 26-bit bitmask** (if only `a–z`)

- For each char, if bit already set in `seen`, set bit in `duplicate`.
- Answer = popcount(`duplicate`).
- Communicate with interviewer that alphabet is lowercase English only.

**Interview talking points**

- Sorting uses no extra hash structure; only comparison sort.
- Bitmask uses O(1) integer space — fits “no array/map” spirit.
- Clarify whether to count **unique repeated letters** (e.g. `aa` → 1) vs **total duplicate occurrences**.

#### Further reading

- [GeeksforGeeks: Count repeated characters](https://www.geeksforgeeks.org/count-characters-string/)- character frequency ideas
- [MDN: Bitwise operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_AND) — bitmask technique
- [LeetCode: First Unique Character](https://leetcode.com/problems/first-unique-character-in-a-string/) — related frequency thinking

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// Bitmask — assumes lowercase a-z only
function countCharsRepeatedMoreThanOnce(s) {
  let seen = 0;
  let dup = 0;
  for (const ch of s) {
    const bit = 1 << (ch.charCodeAt(0) - 97);
    if (seen & bit) dup |= bit;
    seen |= bit;
  }
  let count = 0;
  while (dup) {
    dup &= dup - 1;
    count++;
  }
  return count;
}

// Sort-and-scan — no hash map
function countRepeatedSort(s) {
  const arr = [...s].sort();
  let count = 0;
  let i = 0;
  while (i < arr.length) {
    let j = i;
    while (j + 1 < arr.length && arr[j + 1] === arr[i]) j++;
    if (j > i) count++;
    i = j + 1;
  }
  return count;
}
```

#### Code walkthrough

- **Bitmask** — `seen` marks first occurrence; second occurrence sets `dup` bit.
- **Popcount on `dup`** — number of characters that repeated.
- **Sort scan** — group equal chars; groups of size ≥ 2 increment answer once.

#### Complexity

| | |
|-|-|
| Time | O(n) bitmask / O(n log n) sort |
| Space | O(1) extra (bitmask) or O(n) for sort copy |

#### Edge cases

- **No repeats** — return `0`.
- **All same char** — one distinct repeated character.
- **Non a–z** — bitmask invalid; use sort approach or ask interviewer.

</details>

<details><summary>Solution (other languages)</summary>

[Answer 1]
My approach : Sort & search concurrent character `nlog(n)`.  

[Answer 2] 
Optimize approach : An integer have 32 bit. We have 26 small letter character.  We just need to allocate each bit for position of a character. If an element is present set the concurrent bit and  finally count the number of set bit.  
(Comment from Tamim: Before trying this approach communicate with the interviewer to make sure about the characters present in the string ie only a-z is present and nothing else)

</details>

</article>

## Technical Round Questions
<article>

In pen and paper write the inner workings of a BST. How does a BST work? How to insert and retrieve a value from a BST?

<details><summary>Theory and explanation</summary>

A **Binary Search Tree (BST)** is a binary tree where for every node `N`:

- All keys in the **left subtree** are **&lt; N.key**
- All keys in the **right subtree** are **&gt; N.key** (or ≤ / ≥ per tie-breaking rule)

**Operations**

| Operation | Steps | Average time |
|-----------|--------|--------------|
| **Search** | Compare at root; go left or right | O(h) |
| **Insert** | Search for position; attach new leaf | O(h) |
| **Delete** | Three cases: leaf, one child, two children (use inorder successor/predecessor) | O(h) |

`h` = height. Balanced BST (AVL, red-black) keeps `h = O(log n)`; skewed tree degrades to O(n).

**Insert (pen and paper)**

1. Start at root.
2. If value &lt; node, go left; if greater, go right.
3. When child is null, place new node there.

**Retrieve / search**

Same comparisons; stop when found or null.

**Interview talking points**

- Inorder traversal of BST yields **sorted order**.
- Duplicates policy must be stated (left subtree or count in node).
- Contrast BST with hash table (O(1) average vs ordered traversal).

#### Further reading

- [Visualgo: BST](https://visualgo.net/en/bst) — interactive insert/search
- [GeeksforGeeks: Binary Search Tree](https://www.geeksforgeeks.org/binary-search-tree-data-structure/) — operations
- [CLRS — Introduction to Algorithms](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/) — formal BST analysis
- [LeetCode: Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) — BST property checks

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class BSTNode {
  constructor(key) {
    this.key = key;
    this.left = null;
    this.right = null;
  }
}

class BST {
  constructor() {
    this.root = null;
  }

  search(key) {
    let cur = this.root;
    while (cur) {
      if (key === cur.key) return cur;
      cur = key < cur.key ? cur.left : cur.right;
    }
    return null;
  }

  insert(key) {
    if (!this.root) {
      this.root = new BSTNode(key);
      return;
    }
    let cur = this.root;
    while (true) {
      if (key < cur.key) {
        if (!cur.left) {
          cur.left = new BSTNode(key);
          return;
        }
        cur = cur.left;
      } else if (key > cur.key) {
        if (!cur.right) {
          cur.right = new BSTNode(key);
          return;
        }
        cur = cur.right;
      } else {
        return; // duplicate — policy: ignore
      }
    }
  }
}
```

#### Code walkthrough

- **`search`** — walk from root following BST comparisons until match or null.
- **`insert`** — same path; attach leaf at first empty child position.
- **Duplicates** — ignored here; state your rule on the exam.

#### Complexity

| | |
|-|-|
| Time | O(h) per operation; O(log n) if balanced |
| Space | O(1) iterative / O(h) recursive call stack |

#### Edge cases

- **Empty tree** — insert creates root.
- **Skewed insert order** — height becomes O(n).
- **Delete with two children** — mention successor swap on paper if asked.

</details>

</article>

<article>

Thread A and Thread B are running parallely. What will be the output of following code?   
<img src= "../resource/thread_question_srbd.png">

<details><summary>Theory and explanation</summary>

When two threads increment a **shared variable** `cnt` without synchronization, execution **interleaves** unpredictably. Each thread may read the same stale value, increment, and write back — **lost updates** occur.

**Therefore:** output is **non-deterministic** (unpredictable). It is not guaranteed which thread reads or writes `cnt` at any moment.

**Fix (follow-up)**

- **Mutex / lock** around `cnt++`
- **`std::atomic<int>`** with `fetch_add`
- **Synchronized** blocks in Java

**Interview talking points**

- Data race = undefined behavior in C++ without atomics.
- Mention memory visibility (cache lines) at a high level if asked.
- Java `volatile` does not make `cnt++` atomic.

#### Further reading

- [cppreference: std::thread](https://en.cppreference.com/w/cpp/thread/thread) — threading basics
- [MDN: Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) — parallel JS (different model)
- [Java Tutorials: Intrinsic Locks](https://docs.oracle.com/javase/tutorial/essential/concurrency/locksync.html) — `synchronized`
- [Herb Sutter: atomic<> and concurrency](https://herbsutter.com/elements-of-modern-c-style/) — safe counters

</details>

<details><summary>Solution (JavaScript)</summary>

JavaScript on a **single main thread** does not run true parallel threads for this snippet; the SRBD question targets **C++/Java** threading. Conceptual answer:

```js
// Unsynchronized shared counter — outcome depends on interleaving (conceptual)
let cnt = 0;
// Thread A and B both: read cnt, add 1, write cnt
// Possible lost updates → final cnt may be 1 instead of 2
```

**Expected interview answer:** **Unpredictable** — cannot guarantee a single output value.

#### Complexity

| | |
|-|-|
| Time | N/A (concurrency behavior) |
| Space | N/A |

#### Edge cases

- **More than two threads** — race worsens; need same synchronization.
- **Read-only sharing** — no race for plain reads of immutable data.

</details>

<details><summary>Solution (other languages)</summary>

<img src="../resource/thread_answer_srbd.png">

</details>

</article>

<article>

Given 5 element. We want to search million time that will return if the searched element is present or no. What is the best time complexity.

<details><summary>Theory and explanation</summary>

With only **5 elements**, **linear search** is often **faster in practice** than **binary search** on a sorted array.

**Why**

- Binary search has **branching and overhead** per probe (mid calculation, comparisons).
- For `n = 5`, scanning at most 5 items is cache-friendly and branch-predictable.
- Asymptotically binary search is O(log n), but **constants dominate** at tiny n.

**Tamim’s note from the interview:** linear search measured ~**5× faster** than binary search for this size in their experiment.

**When binary search wins**

- Large `n` (thousands+), sorted static data, many queries — O(log n) dominates.

**Alternatives for millions of queries on 5 fixed values**

- **Hard-code** comparisons or **unroll** the loop.
- Put the five values in a **Set** — O(1) average with hash overhead still small.

#### Further reading

- [GeeksforGeeks: Linear vs Binary search](https://www.geeksforgeeks.org/linear-search-vs-binary-search/) — trade-offs
- [Stack Overflow: Binary search slower for small n](https://stackoverflow.com/questions/tagged/binary-search) — constant factors
- [Big-O cheat sheet](https://www.bigocheatsheet.com/) — asymptotic vs real-world

</details>

<details><summary>Solution (JavaScript)</summary>

```js
const FIVE = [3, 7, 11, 19, 23]; // example fixed set

function searchFiveLinear(target) {
  for (let i = 0; i < FIVE.length; i++) {
    if (FIVE[i] === target) return true;
  }
  return false;
}

function searchFiveSet(target) {
  const set = new Set(FIVE); // build once, reuse for 1e6 queries
  return set.has(target);
}
```

#### Code walkthrough

- **Linear** — at most 5 comparisons; minimal setup.
- **Set** — preprocess once O(1); each of 1e6 queries O(1) average — good if allowed to preprocess.

#### Complexity

| | |
|-|-|
| Per query (linear) | O(1) — bounded by 5 |
| Per query (binary on sorted 5) | O(log 5) but larger constants |
| Preprocess (Set) | O(1) for fixed 5 elements |

#### Edge cases

- **Unsorted 5 elements** — still use linear or sort once if using binary.
- **Duplicates in set** — clarify with interviewer.

</details>

<details><summary>Solution (other languages)</summary>

You might be tempted to answer using binary search on sorted list but it might be better to use linear search. The internal mechanism for binary search has some constant overhead. For small number that overhead overshadows the benefit of logarithmic complexity. I ran both linear search and binary search. Linear search is about 5 times faster than binary search

</details>

</article>

<article>

Follow up question. We are guaranteed that each time new search element would be front the next position of previous search. Write code on pen & paper.

<details><summary>Theory and explanation</summary>

After sorting the 5 elements, searches follow a **locality pattern**: each new target lies **near the previous search index** (one position ahead in the cyclic order). You can **exploit locality**:

- Keep `lastPos` (last found index).
- Instead of full binary search from `[0..4]`, search a **small window** around `lastPos` or adjust pointers with **biased binary search** toward the expected direction.

The provided C++ solution uses binary search on `[0, lastElementPosition]` and updates `lastElementPosition` when narrowing — a form of **range-restricted binary search** leveraging monotonic search targets.

**Interview talking points**

- Clarify “front the next position” on a **circular sorted** view of 5 elements.
- Worst case still O(log 5) but average probes drop.
- Pen-and-paper: write loop invariant for `l`, `r`, `lastElementPosition`.

#### Further reading

- [GeeksforGeeks: Interpolation search](https://www.geeksforgeeks.org/interpolation-search/) — locality-exploiting search
- [LeetCode: Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) — narrowed range search

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function createLocalitySearcher(sortedArr) {
  let lastPos = 0;

  function search(element) {
    let l = 0;
    let r = lastPos;
    while (l <= r) {
      const mid = (l + r) >> 1;
      if (sortedArr[mid] === element) {
        lastPos = mid;
        return mid;
      }
      if (element < sortedArr[mid]) {
        r = mid - 1;
      } else {
        lastPos = l;
        l = mid + 1;
      }
    }
    return -1;
  }

  return search;
}
```

#### Code walkthrough

- **`lastPos`** — shrinks search range based on previous hit (matches SRBD C++ intent).
- **Binary search** on `[0, lastPos]` then expand logic per problem’s cyclic “next position” rule on paper.
- Adapt `lastPos` updates exactly as interviewer defines the guarantee.

#### Complexity

| | |
|-|-|
| Time | O(log n) worst case, often fewer steps with locality |
| Space | O(1) |

#### Edge cases

- **First search** — initialize `lastPos = n - 1` or full range per spec.
- **Miss** — define return value and whether `lastPos` resets.

</details>

<details><summary>Solution (other languages)</summary>

```C++
int lastElementPosition = 0;
int solve( vector<int> arr, int element){
	int l =  0 , r = lastElementPosition;
	while( l <= r){
		int mid = l + (r - l) / 2;
        if( arr[mid] == element ){
            lastElementPosition = mid;
            return mid;
        }
        else if( element < arr[mid] ){
            r = mid - 1;
        }else{
            lastElementPosition = l;
            l = mid + 1;
        }
    }
}
```

</details>

</article>

<article>

Follow up question. Suppose we have 5000 number each 500 digit. Now how will you search? 

<details><summary>Theory and explanation</summary>

Large integers (500 digits each, 5000 values) are not practical for comparison-based array scan alone — use a **Trie** (prefix tree) on **digit strings** (or big-int normalized form).

**Trie search**

- Insert each number digit-by-digit: O(L) per insert, L = digit count.
- Query presence: walk trie O(L).
- **Space** — shared prefixes among 500-digit numbers.

**Alternatives (mention briefly)**

- **Hash set** of string keys — O(L) hash per lookup.
- **Sort + binary search** on string representation — O(L log n) per query after O(n L log n) sort.

**Interview talking points**

- 500-digit numbers exceed native `int`; use strings or bigint.
- Trie excels when many keys share prefixes.
- For exact match only, hash set is simpler; trie wins prefix / autocomplete extensions.

#### Further reading

- [GeeksforGeeks: Trie](https://www.geeksforgeeks.org/trie-insert-and-search/) — insert and search
- [CP-Algorithms: Trie](https://cp-algorithms.com/string/trie.html) — structure
- [LeetCode: Design Add and Search Words](https://leetcode.com/problems/design-add-and-search-words-data-structure/) — trie API practice

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class TrieNode {
  constructor() {
    this.children = new Map();
    this.end = false;
  }
}

class BigIntTrie {
  constructor() {
    this.root = new TrieNode();
  }

  insert(numStr) {
    let node = this.root;
    for (const d of numStr) {
      if (!node.children.has(d)) node.children.set(d, new TrieNode());
      node = node.children.get(d);
    }
    node.end = true;
  }

  search(numStr) {
    let node = this.root;
    for (const d of numStr) {
      if (!node.children.has(d)) return false;
      node = node.children.get(d);
    }
    return node.end;
  }
}
```

#### Code walkthrough

- **Digits as edges** — each of 500 characters is one trie level.
- **`end` flag** — marks complete key stored.
- **Build once** — insert 5000 numbers; answer 1e6 queries in O(500) each.

#### Complexity

| | |
|-|-|
| Insert | O(L) per number, L = 500 |
| Query | O(L) |
| Space | O(total digits stored) with prefix sharing |

#### Edge cases

- **Leading zeros** — normalize representation (fixed width or strip consistently).
- **Negative numbers** — separate sign bit or separate trie.
- **Duplicate inserts** — idempotent `end = true`.

</details>

<details><summary>Solution (other languages)</summary>

Trie Data structure

</details>

</article>

## Benefits, Perks and Things to Consider
- **Bonuses**: SRBD offers 4 festival bonuses each year.
- **Meals and Snacks**: Free snacks and drinks are available in the office.
