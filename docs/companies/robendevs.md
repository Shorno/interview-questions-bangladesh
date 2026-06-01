---
description: RoBenDevs interview questions, RoBenDevs interview stages, RoBenDevs interview details, RoBenDevs interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/robendevs
---
# RoBenDevs

|  |  |
| :-| :- |
| Founding year | |
| Company Website | https://robendevs.com/ |
| Career Website | https://robendevs.com/careers/ |
| Technologies Used|  |

## Introduction
[RoBenDevs](https://robendevs.com//) specializes in building SaaS solutions. 
## Interview Stages
RoBenDevs has a 3 stage interview process for Software Engineer, Intern role.
1. **Initial Screening:** A project description is given to the candidate. The candidate is expected to complete the project within given timeframe. The project is then reviewed by the team.
2. **Problem Solving:** The candidate is given several problems to solve. The problems are mostly related to data structures and algorithms. The candidate is expected to explain the solution and the reasoning behind it.
3. **Whiteboard System Design:** The candidate is tasked with designing a system on a whiteboard from a high level perspective. The candidate is expected to explain the reasoning behind the design.

## Coding Round Questions

<article>

Given the `root` of a binary tree, return the inorder traversal of its nodes values.

[**💻 Submit Code**](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)

<details><summary>Theory and explanation</summary>

**Inorder traversal** visits nodes in order: **left subtree → current node → right subtree**. For a binary search tree (BST), inorder yields **sorted values**.

**Approaches**

1. **Recursive** — naturally follows definition; O(n) time, O(h) stack space for tree height `h`.
2. **Iterative with stack** — simulate recursion; push left chain, pop, visit, go right.
3. **Morris traversal** — O(1) extra space using threaded tree (advanced).

**Interview talking points**

- State time **O(n)** — every node visited once.
- For skewed tree, recursive depth is O(n); iterative avoids stack overflow on deep trees.
- Return type: `number[]` or list of values in visit order.

#### Further reading

- [LeetCode 94: Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) — problem statement
- [Visualgo: BST traversal](https://visualgo.net/en/bst) — inorder animation
- [MDN: Array.prototype.push](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push) — collecting results in JS

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function inorderTraversal(root) {
  const result = [];
  const stack = [];
  let cur = root;

  while (cur || stack.length) {
    while (cur) {
      stack.push(cur);
      cur = cur.left;
    }
    cur = stack.pop();
    result.push(cur.val);
    cur = cur.right;
  }
  return result;
}
```

#### Code walkthrough

1. Push all left children onto the stack (deepest left first).
2. Pop one node — that is the next inorder node — append `val`.
3. Move to its **right** subtree and repeat.
4. Loop until stack empty and `cur` is null.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(h) stack; O(n) worst case for skewed tree |

#### Edge cases

- **`root === null`** — return `[]`.
- **Single node** — return `[root.val]`.
- **Only left or only right spine** — still O(n) time.

</details>

</article>

<article>

Given a Directed Cyclic graph find the sum of all the nodes at level three from the root node

<details><summary>Theory and explanation</summary>

Model the graph as **adjacency list** with a designated **root**. **Level 3** means nodes at **distance 3** from the root (BFS layers: root = level 0 or level 1 — **clarify with interviewer**; RoBenDevs hint implies BFS level counting from root as level 0, so "level three" = distance 3).

**Algorithm: BFS**

1. Queue `(node, depth)` starting `(root, 0)`.
2. Dequeue; if `depth === 3`, add `node` value to sum.
3. Enqueue unvisited neighbors with `depth + 1`.
4. Track **visited** to handle cycles — a directed cyclic graph requires visited set or distance cap to avoid infinite loops.

**Directed cyclic graph caveat**

- Cycles do not change BFS **shortest distance** from root if you mark visited on first visit.
- Nodes unreachable from root are excluded.

**Original hint preserved:** To solve this problem we can use a BFS traversal of the graph. We can keep track of the level of each node and when we reach the third level we can sum all the nodes at that level.

#### Further reading

- [LeetCode 752: Open the Lock](https://leetcode.com/problems/open-the-lock/) — BFS level-by-level pattern
- [GeeksforGeeks: BFS for graphs](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/) — level-order traversal
- [CP-Algorithms: BFS](https://cp-algorithms.com/graph/breadth-first-search.html) — shortest paths in unweighted graphs

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function sumAtLevel(graph, root, targetLevel = 3) {
  const visited = new Set([root]);
  const queue = [[root, 0]];
  let sum = 0;

  while (queue.length) {
    const [node, depth] = queue.shift();
    if (depth === targetLevel) {
      sum += node; // or node.val if objects
    }
    if (depth >= targetLevel) continue;

    for (const next of graph.get(node) || []) {
      if (!visited.has(next)) {
        visited.add(next);
        queue.push([next, depth + 1]);
      }
    }
  }
  return sum;
}
```

#### Code walkthrough

1. BFS from `root` with depth tracking.
2. When `depth === targetLevel`, accumulate node value in `sum`.
3. Stop expanding beyond `targetLevel` for efficiency (optional prune).
4. `visited` prevents cycle re-entry.

#### Complexity

| | |
|-|-|
| Time | O(V + E) |
| Space | O(V) for queue and visited |

#### Edge cases

- **No nodes at level 3** — return `0`.
- **Multiple nodes at level 3** — sum all.
- **1-based vs 0-based level** — confirm whether "level three" means depth 2 or 3.

</details>

</article>

<article>

Given the `head` of a linked list, remove the `n`th node from the end of the list and return its head.

[**💻 Submit Code**](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

<details><summary>Theory and explanation</summary>

**Two-pointer technique** on a singly linked list:

1. Advance **fast** pointer `n` steps ahead.
2. Move **fast** and **slow** together until `fast` reaches the end.
3. `slow` will be just before the node to remove — unlink `slow.next`.

Use a **dummy head** node to simplify removing the head in one pass.

**Alternative**: compute length in two passes — first count nodes, second find `(length - n)`-th node.

**Interview talking points**

- One pass vs two pass — prefer one pass with two pointers.
- 1-indexed `n` from the end (LeetCode convention).
- Return new head if head is removed.

#### Further reading

- [LeetCode 19: Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) — official problem
- [Floyd's cycle detection](https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare) — related two-pointer skill on lists

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function removeNthFromEnd(head, n) {
  const dummy = { val: 0, next: head };
  let fast = dummy;
  let slow = dummy;

  for (let i = 0; i < n; i++) fast = fast.next;

  while (fast.next) {
    fast = fast.next;
    slow = slow.next;
  }

  slow.next = slow.next.next;
  return dummy.next;
}
```

#### Code walkthrough

1. **Dummy** handles edge case when head is removed.
2. Gap of `n` between fast and slow before joint advance.
3. When `fast.next` is null, `slow` is predecessor of target node.
4. Skip target with `slow.next = slow.next.next`.

#### Complexity

| | |
|-|-|
| Time | O(L) list length |
| Space | O(1) |

#### Edge cases

- **Single node, n = 1** — return `null`.
- **n equals list length** — remove head via dummy.
- **Invalid n** — validate `1 <= n <= length`.

</details>

</article>

<article>

Solve a problem related to finding the Minimum Spanning Tree in a graph.

<details><summary>Theory and explanation</summary>

A **Minimum Spanning Tree (MST)** of a connected, undirected, weighted graph is a spanning tree with **minimum total edge weight** (connects all vertices, acyclic).

**Classic algorithms**

| Algorithm | Idea | Time |
|-----------|------|------|
| **Kruskal** | Sort edges; add if no cycle (Union-Find) | O(E log E) |
| **Prim** | Grow tree from start; always add cheapest edge to fringe | O(E log V) with heap |

**When to use which**

- **Sparse graphs** — Kruskal often simpler.
- **Dense graphs** — Prim with adjacency matrix O(V²).

**Interview talking points**

- MST exists only for **connected** undirected graphs; clarify directed vs undirected variant (directed: arborescence, different problem).
- Return **total weight** or **list of edges** — state output format.
- Related: **Max spanning tree** — negate weights or reverse sort.

#### Further reading

- [LeetCode 1584: Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) — MST-style problem
- [CP-Algorithms: Minimum spanning tree](https://cp-algorithms.com/graph/mst_kruskal.html) — Kruskal with DSU
- [Visualgo: MST](https://visualgo.net/en/mst) — Prim/Kruskal visualization

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class DSU {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
  }
  find(x) {
    if (this.parent[x] !== x) this.parent[x] = this.find(this.parent[x]);
    return this.parent[x];
  }
  union(a, b) {
    a = this.find(a);
    b = this.find(b);
    if (a === b) return false;
    this.parent[b] = a;
    return true;
  }
}

function kruskalMST(n, edges) {
  // edges: [u, v, weight]
  const sorted = [...edges].sort((a, b) => a[2] - b[2]);
  const dsu = new DSU(n);
  let cost = 0;
  const mst = [];

  for (const [u, v, w] of sorted) {
    if (dsu.union(u, v)) {
      cost += w;
      mst.push([u, v, w]);
      if (mst.length === n - 1) break;
    }
  }
  return { cost, mst };
}
```

#### Code walkthrough

1. Sort edges ascending by weight.
2. **Union-Find** rejects edges that would form a cycle.
3. Accept edge → add weight, push to MST.
4. Stop when `n - 1` edges selected.

#### Complexity

| | |
|-|-|
| Time | O(E log E) dominated by sort |
| Space | O(V) for DSU |

#### Edge cases

- **Disconnected graph** — MST does not exist; detect when MST has fewer than `n-1` edges.
- **Duplicate edges** — Kruskal handles naturally.
- **Negative weights** — allowed for MST (unlike Dijkstra).

</details>

</article>

<article>

Given the `root` of a binary tree, invert/mirror the tree, and return its root.

[**💻 Submit Code**](https://leetcode.com/problems/invert-binary-tree/description/)

<details><summary>Theory and explanation</summary>

**Invert** a binary tree by swapping **left and right** children at every node. The result is the mirror image across the vertical axis through the root.

**Approaches**

1. **Recursive DFS** — swap children, recurse left and right.
2. **Iterative BFS/DFS** — queue/stack of nodes; swap at each pop.

**Interview talking points**

- In-place mutation vs new tree — LeetCode expects in-place swap, return root.
- Famous quote: homebrew Max Howell tweeted Google rejected him for not inverting a tree — know this problem cold.
- Time O(n), space O(h) recursive stack.

#### Further reading

- [LeetCode 226: Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) — problem link
- [Max Howell tweet (reference)](https://twitter.com/mxcl/status/558031314119245824) — interview folklore

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function invertTree(root) {
  if (!root) return null;
  [root.left, root.right] = [root.right, root.left];
  invertTree(root.left);
  invertTree(root.right);
  return root;
}
```

#### Code walkthrough

1. Base case: null node returns null.
2. Swap `left` and `right` pointers at current node.
3. Recursively invert both subtrees.
4. Return original root (now inverted).

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(h) recursion stack |

#### Edge cases

- **Empty tree** — return null.
- **Single node** — swap no-ops, return root.
- **Perfectly balanced large tree** — watch stack depth on skewed variants.

</details>

</article>

<article>

Determine the number of connected components in an undirected graph.

[**💻 Submit Code**](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

<details><summary>Theory and explanation</summary>

A **connected component** is a maximal set of nodes pairwise reachable via edges. Count components by running **graph traversal** (DFS or BFS) from each unvisited node and incrementing a counter each time you start a new traversal.

**Union-Find alternative**

- Initialize each node as its own set.
- For each edge `(u, v)`, `union(u, v)`.
- Answer = number of distinct roots after all unions.

**Original hint preserved:** Use DFS to identify and count the connected components.

**Interview talking points**

- Works for undirected graphs; directed graphs use **strongly connected components** (Kosaraju/Tarjan) — different problem.
- Disconnected nodes with no edges still count as one component each if listed in `n` nodes.

#### Further reading

- [LeetCode 323: Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) — problem statement
- [LeetCode 547: Number of Provinces](https://leetcode.com/problems/number-of-provinces/) — same idea disguised as matrix
- [CP-Algorithms: DFS](https://cp-algorithms.com/graph/depth-first-search.html) — component search

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function countComponents(n, edges) {
  const adj = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) {
    adj[u].push(v);
    adj[v].push(u);
  }

  const visited = new Array(n).fill(false);
  let components = 0;

  function dfs(node) {
    visited[node] = true;
    for (const nei of adj[node]) {
      if (!visited[nei]) dfs(nei);
    }
  }

  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      components++;
      dfs(i);
    }
  }
  return components;
}
```

#### Code walkthrough

1. Build undirected adjacency list.
2. Loop all nodes; on first unvisited, increment `components` and DFS flood-fill.
3. Each DFS marks one entire component.
4. Return total count.

#### Complexity

| | |
|-|-|
| Time | O(n + e) |
| Space | O(n + e) for adjacency and visited |

#### Edge cases

- **`n > 0`, empty edges** — answer is `n` isolated nodes.
- **Self-loops / duplicate edges** — handle in adjacency build if present.
- **Single component** — return `1`.

</details>

</article>

## Whiteboard System Design

<article>

Design a system that will be used to monitor the usage of electricity of meters across a area. The system should be able to show the usage of electricity in real time and also be able to show the usage of electricity over a period of time.

<details><summary>Theory and explanation</summary>

This is an **IoT telemetry + time-series analytics** design. Smart meters (or AMR devices) report consumption readings to a central platform; users and operators view **real-time dashboards** and **historical aggregates**.

**Functional requirements**

- Ingest meter readings (kWh, voltage, optional power factor) at high frequency.
- **Real-time view** — current usage per meter / per area (last N minutes).
- **Historical view** — hourly/daily/monthly charts, comparisons, export.
- Alerts on anomalies (spike, outage, tamper).

**High-level architecture**

1. **Meters / gateways** — batch or stream readings over MQTT/HTTP.
2. **Ingestion layer** — Kafka/Kinesis message bus; schema validation; idempotent writes.
3. **Stream processing** — Flink/Spark Streaming for real-time aggregates per area.
4. **Time-series store** — TimescaleDB, InfluxDB, or Cassandra for readings; hot path in Redis for "last reading."
5. **API layer** — REST/GraphQL: `GET /meters/{id}/current`, `GET /meters/{id}/usage?from=&to=&granularity=`.
6. **Dashboard** — WebSocket push for live charts; query TSDB for history.
7. **Batch/analytics** — nightly rollups to cheaper object storage (Parquet) for long retention.

**Data model sketch**

- `meters(id, area_id, install_address, …)`
- `readings(meter_id, timestamp, kwh_cumulative, …)` — partition by time
- `area_rollups(area_id, bucket_start, sum_kwh, peak_kw)`

**Non-functional**

- **Scale**: millions of meters, readings every 15 min (or finer).
- **Latency**: sub-second for "current" via cache; historical queries seconds acceptable.
- **Durability**: at-least-once ingestion with dedup keys `(meter_id, ts)`.
- **Security**: TLS, device auth, RBAC for operators vs consumers.

**Original hint preserved:** Answer varies from person to person. The interviewers are looking for a high level design of the system and are interested in the reasoning behind the design.

#### Further reading

- [AWS IoT Core architecture](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/iot-services.html) — device ingestion patterns
- [TimescaleDB: Time-series data model](https://docs.timescale.com/use-timescale/latest/hypertables/) — hypertables for meter readings
- [Apache Kafka: IoT use cases](https://kafka.apache.org/powered-by) — streaming ingestion reference deployments
- [System Design Primer](https://github.com/donnemartin/system-design-primer) — scalable backend checklist

</details>

<details><summary>Solution (JavaScript)</summary>

Reference **API contracts** and a simple rollup sketch (implementation would be Java/Go/Python in production):

```js
// GET /areas/:areaId/usage/realtime
function getRealtimeUsage(areaId, redis, tsdb) {
  // Hot path: last reading per meter from Redis hash `area:{id}:last`
  // Fallback: TSDB query last 5 minutes, sum delta kWh
}

// GET /meters/:meterId/usage?from=ISO&to=ISO&bucket=1h
async function getHistoricalUsage(meterId, from, to, bucket, tsdb) {
  return tsdb.query(`
    SELECT time_bucket($bucket, ts) AS bucket,
           max(kwh_cumulative) - min(kwh_cumulative) AS kwh_used
    FROM readings
    WHERE meter_id = $1 AND ts BETWEEN $2 AND $3
    GROUP BY bucket ORDER BY bucket
  `, [meterId, from, to, bucket]);
}
```

#### Code walkthrough

- **Real-time** — cache latest cumulative reading; usage rate = delta over window / time.
- **Historical** — cumulative meters: consumption in interval = max − min of cumulative register.
- **Area aggregation** — sum meter deltas grouped by `area_id` in stream processor.

#### Complexity

| | |
|-|-|
| Time | Real-time O(1) per meter from cache; historical O(rows in range) |
| Space | Retention tiering: hot TSDB + cold object storage |

#### Edge cases

- **Late/out-of-order readings** — watermarks in stream job; idempotent upserts.
- **Meter replacement** — reset cumulative counter; metadata flag for analytics.
- **Clock skew on devices** — server-side ingestion timestamp as source of truth.

</details>

</article>

<article>

Design a system where a single restaurant offers home delivery services across the entire country. You don't need to worry about the payment gateway, as that is handled by a third party.

<details><summary>Theory and explanation</summary>

One **central kitchen/restaurant** delivering nationwide implies **long-distance logistics**, **order orchestration**, and **inventory** — not a multi-vendor marketplace like Pathao Food.

**Core services**

1. **Order service** — create order, line items, status machine (placed → preparing → dispatched → delivered).
2. **Menu & inventory** — SKUs, daily capacity, regional availability (some items may not ship far).
3. **Delivery / logistics** — integrate third-party couriers or own fleet; assign by pin code / SLA zone.
4. **Routing & ETA** — distance from kitchen hubs or dark stores; may need **regional prep kitchens** for national reach.
5. **Notification service** — SMS/push for status updates.
6. **Customer app + admin** — place order, track driver.

**Scaling patterns (from original hint)**

- **Load balancer** — distribute API traffic across stateless app servers.
- **API gateway** — auth, rate limit, routing to microservices.
- **Caching** — menu catalog in Redis/CDN; reduce DB read on every browse.
- **Database design** — critical for orders, inventory, delivery zones:
  - `users`, `addresses` (geo indexed)
  - `orders`, `order_items`, `order_status_history`
  - `delivery_zones` (polygon or pin ranges → SLA, fee)
  - `shipments` (courier_id, tracking, ETA)
- **Token refresh** — JWT access + refresh for mobile clients; gateway validates.

**National delivery nuance**

- Single kitchen cannot serve whole country in 30 minutes — clarify **shipping tiers** (express from local hubs vs overnight cold chain).
- **Partition data** by region; **CQRS** for read-heavy tracking pages.

**Original hint preserved:** Focus on key system design concepts such as load balancing, scaling, API gateway, caching, and token refresh. The interviewer is mainly interested in how you approach solving real-world problems and all of above. Database design is mostly important here.

#### Further reading

- [Uber engineering: Marketplace simulation](https://www.uber.com/blog/engineering/) — dispatch and scaling lessons
- [Martin Fowler: Microservices](https://martinfowler.com/articles/microservices.html) — service boundaries
- [Redis: Caching best practices](https://redis.io/docs/manual/patterns/) — catalog and session cache
- [PostGIS: Geographic queries](https://postgis.net/) — delivery zone polygons

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// Simplified order placement flow
async function placeOrder({ userId, items, addressId }, services) {
  const zone = await services.zones.resolve(addressId);
  if (!zone.serviceable) throw new Error('Address outside delivery area');

  await services.inventory.reserve(items, zone.fulfillmentCenterId);

  const order = await services.orders.create({
    userId,
    items,
    addressId,
    fulfillmentCenterId: zone.fulfillmentCenterId,
    deliveryFee: zone.fee,
    etaMinutes: zone.eta,
  });

  await services.dispatch.requestCourier(order.id);
  await services.notify.send(userId, `Order ${order.id} confirmed`);
  return order;
}
```

#### Code walkthrough

1. **Zone resolution** — map address to serviceable region, fee, and fulfillment center.
2. **Inventory reserve** — prevent overselling per hub capacity.
3. **Persist order** — transactional write with status `PLACED`.
4. **Async dispatch** — courier assignment via queue worker.
5. **Notify customer** — decouple via message bus.

#### Complexity

| | |
|-|-|
| Time | Order path O(items) DB ops; dominated by I/O |
| Space | Stateless services; data in PostgreSQL + Redis |

#### Edge cases

- **Inventory race** — use DB row locks or Redis atomic decrement.
- **Courier cancellation** — saga/compensation to reassign or refund (payment external).
- **Peak lunch hour** — queue orders, dynamic ETA, autoscale workers.

</details>

</article>
