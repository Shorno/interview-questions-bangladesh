---
description: Spectrum Software interview questions, Spectrum Software interview stages, Spectrum Software interview details, Spectrum Software interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/spectrum
---
# Spectrum

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-| :- |
| Founding year | |
| Company Website | https://www.spectrum-bd.com |
| Career Website |  |
| Technologies Used|  |

## Introduction
Spectrum Engineering Consortium Ltd. specializes in IP/DWDM/SDH Network infrastructure, Data Center-Cloud solutions Facility, Server, Storage/Virtualizations. 

## Questions
<article>

What is heap? How heap sort works? what is its run time?

<details><summary>Theory and explanation</summary>

A **binary heap** is a complete binary tree stored in an array where each node satisfies the **heap property**:

- **Max-heap**: parent ≥ both children (root is maximum).
- **Min-heap**: parent ≤ both children (root is minimum).

Because the tree is **complete**, the array representation has no gaps: for index `i`, parent is `(i - 1) >> 1`, children are `2i + 1` and `2i + 2`.

**Core operations**

| Operation | Description | Time |
|-----------|-------------|------|
| `heapify` / `siftDown` | Restore heap property at a node | O(log n) |
| `insert` | Add at end, sift up | O(log n) |
| `extract-max/min` | Swap root with last, pop, sift down | O(log n) |
| `build-heap` | Heapify from last non-leaf down to root | **O(n)** |

**Heap sort algorithm**

1. **Build a max-heap** from the input array in O(n).
2. Repeatedly swap the root (current max) with the last unsorted element, shrink the heap by one, and **sift down** the new root.
3. After `n - 1` extractions, the array is sorted in ascending order.

**Runtime**

- **Time**: **O(n log n)** in all cases (each of `n` extractions costs O(log n)).
- **Space**: **O(1)** if sorting in place (only a few index variables); O(n) if copying to a new array.

**When to mention in interviews**

- Heaps power **priority queues** (Dijkstra, scheduling, top-K).
- **Not stable** — equal keys may reorder.
- **Cache behavior** is worse than quicksort in practice, so standard libraries often use introsort (quicksort + heap sort fallback).

#### Further reading

- [Visualgo: Heap Sort](https://visualgo.net/en/heapsort) — interactive heap construction and extraction
- [CLRS / MIT: Heaps and heap sort (OpenCourseWare)](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-9-heaps-and-heap-sort/) — build-heap O(n) proof
- [GeeksforGeeks: Heap Sort](https://www.geeksforgeeks.org/heap-sort/) — sift-up/down walkthrough
- [Wikipedia: Binary heap](https://en.wikipedia.org/wiki/Binary_heap) — array indexing formulas

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function siftDown(arr, start, end) {
  let i = start;
  while (true) {
    let largest = i;
    const left = 2 * i + 1;
    const right = 2 * i + 2;
    if (left <= end && arr[left] > arr[largest]) largest = left;
    if (right <= end && arr[right] > arr[largest]) largest = right;
    if (largest === i) break;
    [arr[i], arr[largest]] = [arr[largest], arr[i]];
    i = largest;
  }
}

function buildMaxHeap(arr) {
  for (let i = (arr.length >> 1) - 1; i >= 0; i--) {
    siftDown(arr, i, arr.length - 1);
  }
}

function heapSort(arr) {
  buildMaxHeap(arr);
  for (let end = arr.length - 1; end > 0; end--) {
    [arr[0], arr[end]] = [arr[end], arr[0]];
    siftDown(arr, 0, end - 1);
  }
  return arr;
}

heapSort([5, 3, 8, 1, 2, 7]); // [1, 2, 3, 5, 7, 8]
```

#### Code walkthrough

1. **`buildMaxHeap`** — start from the last internal node and sift down each index; total O(n).
2. **`siftDown`** — compare node with left/right child in the active heap range `[0..end]`; swap with larger child and repeat.
3. **Sort phase** — swap max (root) to position `end`, reduce heap size, restore heap on root.

#### Complexity

| | |
|-|-|
| Time | O(n log n) — n extractions × O(log n) sift |
| Space | O(1) — in-place |

#### Edge cases

- **Already sorted** — still O(n log n); no quicksort-style best case.
- **All equal** — works; unstable ordering of equals.
- **Length 0 or 1** — loops no-op; array unchanged.
- **Duplicates / negatives** — max-heap comparison handles any orderable values.

</details>

</article>

<article>

What is AVL tree?

<details><summary>Theory and explanation</summary>

An **AVL tree** is a **self-balancing binary search tree (BST)** named after Adelson-Velsky and Landis. For every node, the heights of its left and right subtrees differ by at most **1** (balance factor ∈ {−1, 0, +1}).

**Why AVL trees**

Plain BSTs degrade to O(n) height on sorted input. AVL trees guarantee **height h = O(log n)**, so search, insert, and delete remain **O(log n)**.

**Balance factor**

```
balance(node) = height(left) - height(right)
```

If after insert/delete the factor becomes ±2, **rotations** restore balance:

| Case | Shape | Fix |
|------|-------|-----|
| LL | imbalance on left-left | **Right rotation** |
| RR | imbalance on right-right | **Left rotation** |
| LR | left-right | Left rotate child, then right rotate |
| RL | right-left | Right rotate child, then left rotate |

**Insert outline**

1. BST insert as usual.
2. Walk up to root updating heights.
3. At first unbalanced ancestor, apply the appropriate single or double rotation.

**Delete outline**

1. BST delete (replace with inorder successor/predecessor if two children).
2. Rebalance upward — may require O(log n) rotations on the path.

**AVL vs red-black trees**

- AVL is **stricter** (more balanced) → faster lookups, slightly costlier inserts/deletes.
- Red-black allows more imbalance → fewer rotations on write-heavy workloads.
- Database indexes often use B-trees/B+ trees instead for disk block locality.

#### Further reading

- [Visualgo: AVL Tree](https://visualgo.net/en/bst?mode=AVL) — rotations and rebalancing animations
- [GeeksforGeeks: AVL Tree](https://www.geeksforgeeks.org/avl-tree-set-1-insertion/) — insertion with all four cases
- [Wikipedia: AVL tree](https://en.wikipedia.org/wiki/AVL_tree) — balance factor definition and history
- [Open Data Structures: AVL Trees](https://opendatastructures.org/versions/edition-0.1d/ods-java/node36.html) — textbook-style proofs

</details>

<details><summary>Solution (JavaScript)</summary>

Conceptual sketch — a production AVL is lengthy; interviews usually want rotations and balance factor, not full production code. Below is a minimal **insert + LL/RR rebalance** illustration.

```js
class AVLNode {
  constructor(key) {
    this.key = key;
    this.left = null;
    this.right = null;
    this.height = 1;
  }
}

function height(n) {
  return n ? n.height : 0;
}

function balanceFactor(n) {
  return height(n.left) - height(n.right);
}

function updateHeight(n) {
  n.height = 1 + Math.max(height(n.left), height(n.right));
}

function rotateRight(y) {
  const x = y.left;
  y.left = x.right;
  x.right = y;
  updateHeight(y);
  updateHeight(x);
  return x;
}

function rotateLeft(x) {
  const y = x.right;
  x.right = y.left;
  y.left = x;
  updateHeight(x);
  updateHeight(y);
  return y;
}

function insert(node, key) {
  if (!node) return new AVLNode(key);
  if (key < node.key) node.left = insert(node.left, key);
  else if (key > node.key) node.right = insert(node.right, key);
  else return node;

  updateHeight(node);
  const bf = balanceFactor(node);

  // LL
  if (bf > 1 && key < node.left.key) return rotateRight(node);
  // RR
  if (bf < -1 && key > node.right.key) return rotateLeft(node);
  // LR
  if (bf > 1 && key > node.left.key) {
    node.left = rotateLeft(node.left);
    return rotateRight(node);
  }
  // RL
  if (bf < -1 && key < node.right.key) {
    node.right = rotateRight(node.right);
    return rotateLeft(node);
  }
  return node;
}
```

#### Code walkthrough

- **`height` / `balanceFactor`** — detect when a subtree is left-heavy (+2) or right-heavy (−2).
- **`rotateRight` / `rotateLeft`** — standard pointer rewiring; update heights bottom-up after rotation.
- **`insert`** — recursive BST insert, then rebalance on unwind using the four cases.

#### Complexity

| | |
|-|-|
| Time | O(log n) search, insert, delete — tree height bounded |
| Space | O(n) nodes; O(log n) recursion stack |

#### Edge cases

- **Duplicate keys** — policy varies; sample ignores duplicates.
- **Delete** — hardest part (successor swap + multiple rebalance steps); often asked separately.
- **Sequential insert 1..n** — AVL stays balanced; plain BST would not.

</details>

</article>

<article>

Given a singly linked list, more specifically the head of the linked list. Return the reverse of the list.

<details><summary>Theory and explanation</summary>

Reversing a **singly linked list** means reversing `next` pointers so traversal from the head visits nodes in opposite order. The list is often defined as:

```js
function ListNode(val, next = null) {
  this.val = val;
  this.next = next;
}
```

**Approaches**

1. **Iterative (three pointers)** — `prev`, `curr`, `next`. For each node, save `next`, point `curr.next` to `prev`, advance. **O(n) time, O(1) space**. Preferred in interviews.
2. **Recursive** — reverse rest of list, then `head.next.next = head`, `head.next = null`. **O(n) time, O(n) stack space**.
3. **Stack** — push all nodes, pop to rebuild. O(n) time and space; less elegant.

**Key invariants (iterative)**

- `prev` is the head of the reversed prefix.
- `curr` is the first node of the unreversed suffix.
- Never lose the tail of the unreversed suffix (`next` saved before rewiring).

**Interview extras**

- Return new head (old tail).
- Empty list / single node — return as-is.
- Clarify whether to mutate in place or return a new list.

#### Further reading

- [LeetCode 206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) — canonical statement
- [NeetCode: Reverse Linked List (video)](https://neetcode.io/problems/reverse-a-linked-list) — pointer diagram walkthrough
- [MDN: Linked list patterns (general CS)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures) — JS object references
- [GeeksforGeeks: Reverse a linked list](https://www.geeksforgeeks.org/reverse-a-linked-list/) — iterative and recursive

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function ListNode(val, next = null) {
  this.val = val;
  this.next = next;
}

// Iterative — O(1) extra space
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

// Recursive
function reverseListRecursive(head) {
  if (!head || !head.next) return head;
  const newHead = reverseListRecursive(head.next);
  head.next.next = head;
  head.next = null;
  return newHead;
}
```

#### Code walkthrough

- **Iterative**: save `next`, reverse link, shift `prev` and `curr` forward; when `curr` is null, `prev` is the new head.
- **Recursive**: base case single/empty node; reverse suffix first; attach current node after reversed tail.

#### Complexity

| | Iterative | Recursive |
|-|-|-|
| Time | O(n) | O(n) |
| Space | O(1) | O(n) call stack |

#### Edge cases

- **`head === null`** — return `null`.
- **Single node** — return same node.
- **Two nodes** — swap link once.
- **Cycles in input** — would infinite-loop; assume valid DAG-like list.

</details>

<details><summary>Solution (other languages)</summary>

```C++
ListNode* reverseList(ListNode* head) {
    if( head == nullptr || head->next == nullptr ) return head;
    ListNode* tail = reverseList(head->next);
    head->next->next = head;
    head->next = nullptr;
    return tail;
}
```

</details>
</article>

<article>

[System Design] Design a url shortener like tiny url. Ensure uniqueness of the shortened link and scalability of the system.

<details><summary>Theory and explanation</summary>

A **URL shortener** maps long URLs to short codes (e.g. `https://short.ly/abc12`) and **redirects** HTTP requests to the original URL. Spectrum’s infra background makes **availability, storage, and cache** talking points especially relevant.

**Functional requirements**

- Shorten a long URL → unique short code.
- Redirect `GET /{code}` → original URL (301 permanent or 302 temporary).
- Optional: custom aliases, expiration, analytics (click counts), auth for creation.

**High-level components**

```
Client → API Gateway / LB → Shorten service + Redirect service
                              ↓
                         Cache (Redis)
                              ↓
                         Database (SQL or NoSQL)
```

**Short code generation (uniqueness)**

| Strategy | Pros | Cons |
|----------|------|------|
| **Base62 counter** (auto-increment ID → encode) | No collisions; O(1) | Need distributed ID (Snowflake, DB sequence, Redis INCR) |
| **Hash (MD5/SHA) + truncate** | Fast | Collisions → must check DB and retry |
| **Random + retry** | Simple | Birthday paradox; needs uniqueness check |

**Base62** uses `[a-zA-Z0-9]` — 6 chars ≈ 62⁶ ≈ 56 billion URLs.

**Redirect path (read-heavy)**

1. Lookup code in **Redis**; on miss, read DB and populate cache.
2. Return **301** if URL immutable (cacheable by browsers/CDN) or **302** if stats/AB tests need per-hit logic.
3. **CDN edge** can cache 301 responses globally.

**Database schema (example)**

```sql
CREATE TABLE urls (
  id          BIGINT PRIMARY KEY,
  short_code  VARCHAR(10) UNIQUE NOT NULL,
  long_url    TEXT NOT NULL,
  created_at  TIMESTAMP,
  expires_at  TIMESTAMP NULL,
  user_id     BIGINT NULL
);
CREATE INDEX idx_short_code ON urls(short_code);
```

**Scalability**

- **Read:write ratio** often 100:1 or higher → aggressive caching, read replicas.
- **Horizontal scale** — stateless app servers behind LB; shard DB by `short_code` hash if needed.
- **Rate limiting** — prevent abuse of shorten API.
- **Analytics** — async queue (Kafka) + worker writes click events; do not block redirect.

**Security**

- Block phishing/malware URLs (scan + blocklists).
- Do not expose sequential IDs if guessing is a concern (use random-looking codes or auth on private links).

#### Further reading

- [System Design Primer: URL shortening](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/pastebin/README.md) — end-to-end paste/URL design (same pattern)
- [ByteByteGo: Design A URL Shortener](https://bytebytego.com/courses/system-design-interview/design-a-url-shortener) — diagrams and traffic estimates
- [TinyURL (product reference)](https://tinyurl.com/) — real-world behavior
- [AWS: ElastiCache for Redis caching pattern](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html) — redirect hot-path cache

</details>

<details><summary>Solution (JavaScript)</summary>

Illustrative **shorten + redirect** core — not production-ready, but shows encoding, uniqueness, and cache-aside.

```js
const BASE62 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';

function encodeBase62(num) {
  if (num === 0) return BASE62[0];
  let s = '';
  while (num > 0) {
    s = BASE62[num % 62] + s;
    num = Math.floor(num / 62);
  }
  return s;
}

class UrlShortener {
  constructor() {
    this.nextId = 1;
    this.db = new Map();      // code -> longUrl
    this.cache = new Map();   // code -> longUrl (Redis stand-in)
  }

  shorten(longUrl) {
    const id = this.nextId++;
    const code = encodeBase62(id);
    this.db.set(code, longUrl);
    this.cache.set(code, longUrl);
    return `https://short.ly/${code}`;
  }

  resolve(code) {
    if (this.cache.has(code)) return this.cache.get(code);
    const longUrl = this.db.get(code);
    if (longUrl) this.cache.set(code, longUrl);
    return longUrl ?? null;
  }
}

const svc = new UrlShortener();
const short = svc.shorten('https://spectrum-bd.com/products/dwdm');
svc.resolve(short.split('/').pop()); // original URL
```

#### Code walkthrough

- **`encodeBase62`** — maps monotonic ID to fixed-length-looking codes; distributed systems use a global ID service instead of `nextId++`.
- **`shorten`** — write-through to DB and cache after allocation.
- **`resolve`** — cache-aside read: Redis first, DB on miss, backfill cache.

#### Complexity

| | |
|-|-|
| Time | N/A (system design); O(1) encode/lookup per request at steady state |
| Space | O(number of URLs stored) |

#### Edge cases

- **Duplicate long URL** — dedupe (same code) vs new code per request (product choice).
- **Expired links** — TTL in DB + cache eviction.
- **Collision on hash-based schemes** — retry with salt or use counter IDs.
- **Hot keys** — viral link saturates one Redis shard; use local LRU + replication.

</details>

</article>

<article>

What is RAID? Describe RAID 0-5.

<details><summary>Theory and explanation</summary>

**RAID (Redundant Array of Independent Disks)** combines multiple physical drives into one logical unit for **performance**, **capacity**, or **fault tolerance**. A **RAID controller** (hardware or software) presents the array to the OS.

**Common levels (0–5)**

| Level | Technique | Min disks | Fault tolerance | Read perf | Write perf | Usable capacity |
|-------|-----------|-----------|-----------------|-----------|------------|-----------------|
| **RAID 0** | Striping (split blocks across disks) | 2 | **None** — one disk failure loses all data | High | High | 100% |
| **RAID 1** | Mirroring (duplicate data) | 2 | 1 disk (N−1 in N-way mirror) | High | Medium | 50% (2-disk) |
| **RAID 2** | Bit-level striping + Hamming ECC | 3+ | 1 disk | Rare in practice | Rare | Low efficiency |
| **RAID 3** | Byte-level striping + dedicated parity disk | 3+ | 1 disk | Good sequential | Parity disk bottleneck | (N−1)/N |
| **RAID 4** | Block striping + dedicated parity | 3+ | 1 disk | Good | Parity disk bottleneck on writes | (N−1)/N |
| **RAID 5** | Block striping + **distributed parity** | 3+ | **1 disk** | Good | Medium (parity update) | (N−1)/N |

**RAID 0** — maximum speed/capacity; zero redundancy. Used when data is ephemeral or replicated elsewhere.

**RAID 1** — simple mirror; good for OS/boot volumes and low-latency reads.

**RAID 5** — parity spread across all disks avoids a single dedicated parity bottleneck of RAID 4; still vulnerable during **rebuild** after a failure (second disk failure = data loss). **Write penalty** — small random writes read-modify-write parity.

**Beyond level 5 (worth mentioning)**

- **RAID 6** — dual parity; survives 2 disk failures.
- **RAID 10 (1+0)** — mirror then stripe; popular for databases (performance + redundancy).

**Spectrum context** — data-center and storage interviews expect you to connect RAID to **IOPS**, **rebuild time**, **hot spares**, and when to prefer **replication at application level** vs hardware RAID.

#### Further reading

- [Oracle: RAID levels explained](https://docs.oracle.com/en/storage/storage-software/storage-administrator-s-guide/raid-levels.html) — vendor-neutral summary
- [Wikipedia: Standard RAID levels](https://en.wikipedia.org/wiki/Standard_RAID_levels) — diagrams for 0–6
- [Red Hat: What is RAID?](https://www.redhat.com/en/topics/storage/what-is-RAID) — enterprise storage perspective
- [Backblaze: RAID Reliability](https://www.backblaze.com/blog/raid/) — real-world failure and rebuild considerations

</details>

<details><summary>Solution (JavaScript)</summary>

RAID is hardware/storage design — no algorithmic code. Below is a **reference table helper** you might use in a monitoring dashboard or study flashcards.

```js
const RAID_LEVELS = {
  0: {
    name: 'Striping',
    minDisks: 2,
    faultTolerance: 0,
    usableFraction: (n) => 1,
    summary: 'No redundancy; one failure destroys the array.',
  },
  1: {
    name: 'Mirroring',
    minDisks: 2,
    faultTolerance: 1,
    usableFraction: (n) => 1 / n,
    summary: 'Full duplicate; survives one disk failure (2-disk mirror).',
  },
  2: {
    name: 'Bit striping + Hamming',
    minDisks: 3,
    faultTolerance: 1,
    usableFraction: (n) => (n - Math.ceil(Math.log2(n) + 1)) / n,
    summary: 'Legacy; rarely deployed today.',
  },
  3: {
    name: 'Byte striping + parity disk',
    minDisks: 3,
    faultTolerance: 1,
    usableFraction: (n) => (n - 1) / n,
    summary: 'Dedicated parity disk; good sequential reads.',
  },
  4: {
    name: 'Block striping + parity disk',
    minDisks: 3,
    faultTolerance: 1,
    usableFraction: (n) => (n - 1) / n,
    summary: 'Block-level; parity disk can bottleneck writes.',
  },
  5: {
    name: 'Block striping + distributed parity',
    minDisks: 3,
    faultTolerance: 1,
    usableFraction: (n) => (n - 1) / n,
    summary: 'Parity rotated across disks; survives one failure.',
  },
};

function describeRaid(level, diskCount) {
  const spec = RAID_LEVELS[level];
  if (!spec) return null;
  const usable = Math.floor(diskCount * spec.usableFraction(diskCount));
  return { ...spec, diskCount, usableCapacityDisks: usable };
}

describeRaid(5, 4); // 3 disks usable of 4
```

#### Code walkthrough

- **`usableFraction`** — encodes capacity formulas for interview recall.
- **`describeRaid`** — combines static metadata with a concrete disk count for ops tooling or flashcards.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases

- **RAID is not backup** — deletion/corruption mirrors to all members; still need off-site backup.
- **Rebuild stress** — second failure during rebuild on RAID 5 is a classic risk (motivates RAID 6).
- **Nested RAID (10, 50)** — interview may ask to compare vs flat levels.

</details>

</article>

<article>

Why disk IO time increases if the chunk size is small?

<details><summary>Theory and explanation</summary>

**Disk I/O time** is commonly modeled as:

```
Total time ≈ (seek time) + (rotational latency) + (transfer time)
```

For **HDDs**, **seek** and **rotation** are mechanical fixed costs per access. For **SSDs**, analogous costs include **FTL mapping**, **erase/program cycles**, and **controller overhead** — still often **per-operation** rather than purely proportional to bytes moved.

**Why small chunks hurt**

1. **Fixed overhead dominates** — each read/write pays setup cost (command issue, seek/lookup, DMA setup). Many tiny transfers → overhead repeated, **throughput collapses**.
2. **Low transfer efficiency** — transfer time = `bytes / bandwidth`; if bytes is tiny, almost all time is non-transfer overhead.
3. **Fragmentation & alignment** — sub-sector or misaligned chunks may trigger read-modify-write on SSDs or extra sector reads on HDDs.
4. **System call & kernel cost** — user space issuing thousands of 512-byte `read()` calls vs one 1 MiB buffered read adds CPU and context-switch tax.
5. **Queue depth underutilization** — modern disks parallelize commands; microscopic I/Os fail to keep the device busy (cannot hide latency).

**Rule of thumb**

- **Sequential large I/O** (streaming, backup) → high MB/s.
- **Random small I/O** (OLTP row fetch without buffering) → low IOPS efficiency and high latency.

**Mitigations**

- **Buffering / read-ahead / write-behind** in OS and DB.
- **Application batching** — aggregate records into page-sized chunks (often 4 KiB–64 KiB or more).
- **mmap or direct I/O** tuned to match filesystem block size.
- **RAID stripe size** aligned with workload access pattern.

**Interview angle for Spectrum** — tie to **storage virtualization**, **SAN/NAS tuning**, and why databases use **page size** (e.g. 8 KiB) and **write-ahead logs** batched in large sequential writes.

#### Further reading

- [IBM: Disk performance factors](https://www.ibm.com/docs/en/power9/0009-ESS/essperformance) — seek, latency, transfer breakdown
- [Brendan Gregg: Storage performance analysis](https://www.brendangregg.com/storage.html) — latency vs throughput visualization
- [Linux disk I/O size and scheduling (Red Hat KB)](https://access.redhat.com/solutions/2319) — practical tuning
- [Wikipedia: Hard disk drive performance characteristics](https://en.wikipedia.org/wiki/Hard_disk_drive_performance_characteristics) — seek time and rotational latency

</details>

<details><summary>Solution (JavaScript)</summary>

Simulation model — not how disks are programmed, but clarifies **fixed overhead per I/O** vs **transfer time**.

```js
/**
 * @param {number} totalBytes - payload to move
 * @param {number} chunkBytes - per-operation size
 * @param {number} fixedMs - seek + setup per operation (ms)
 * @param {number} bandwidthMBps - sustained transfer rate once reading
 */
function estimateIoTimeMs(totalBytes, chunkBytes, fixedMs = 5, bandwidthMBps = 200) {
  const ops = Math.ceil(totalBytes / chunkBytes);
  const transferMsPerOp = (chunkBytes / (bandwidthMBps * 1024 * 1024)) * 1000;
  let total = 0;
  for (let i = 0; i < ops; i++) {
    const thisChunk = Math.min(chunkBytes, totalBytes - i * chunkBytes);
    const transferMs = (thisChunk / (bandwidthMBps * 1024 * 1024)) * 1000;
    total += fixedMs + transferMs;
  }
  return total;
}

// 1 MiB total; small chunks pay fixedMs many times
estimateIoTimeMs(1024 * 1024, 512);   // much higher
estimateIoTimeMs(1024 * 1024, 65536); // lower total time
```

#### Code walkthrough

- **`ops`** — number of discrete I/O operations = ceil(total / chunk).
- Each operation adds **`fixedMs`** (seek/setup) plus transfer proportional to chunk size.
- Shrinking **`chunkBytes`** increases **`ops`**, so fixed cost accumulates.

#### Complexity

| | |
|-|-|
| Time | O(totalBytes / chunkBytes) in simulation loop — illustrates ops count |
| Space | O(1) |

#### Edge cases

- **Chunk larger than total** — single operation; minimum time.
- **SSDs** — lower `fixedMs` but small random writes still amplify write amplification.
- **Buffered sequential access** — OS read-ahead hides small logical reads; raw small I/O worst case is direct unbuffered O_DIRECT.

</details>

</article>

