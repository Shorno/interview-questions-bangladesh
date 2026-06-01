---
description: Relisource interview questions, Relisource interview stages, Relisource interview details, Relisource interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/relisource
---
# Relisource

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-| :- |
| Founding year | |
| Company Website | https://www.relisource.com/ |
| Career Website | https://www.relisource.com/careers/ |
| Technologies Used| Desktop, Mobile, Web, System & Network, Cloud Computing, AWS, Azure & Open Source DevOps |

## Introduction

For the Junior .NET Developer Position at first there was a 1 hour long written Exam which consisted 3 Questions (SQL Query, Problem Solving, JavaScript-HTML)

## Software Engineering Questions
<article>

Select The Company name which has the lowest total emoployee count.

|Company|Position|Employee|
| :-: | :-: | :-: |
|ABC|blah|20|
|ABC|blah|15|
|ABC|blah|5|
|XYZ|blah|10|
|XYZ|blah|12|
|XYZ|blah|5|
|MNO|blah|20|
|MNO|blah|5|

<details><summary>Theory and explanation</summary>

This is a classic **SQL aggregation** question. The table lists employees per company and position row; you must find the **company with the smallest total employee count** when rows are summed **per company**.

**Relational algebra view**

1. **Filter** — no filter needed unless excluding nulls.
2. **Group by** `Company` — collapse rows sharing the same company name.
3. **Aggregate** — `SUM(Employee)` for each group.
4. **Order** — ascending by total so the smallest is first.
5. **Limit** — `TOP 1` (SQL Server) or `LIMIT 1` (PostgreSQL/MySQL) to return one company.

**Sample totals from the given data**

| Company | Rows | Sum |
|---------|------|-----|
| ABC | 20 + 15 + 5 | **40** |
| XYZ | 10 + 12 + 5 | **27** |
| MNO | 20 + 5 | **25** |

**MNO** has the lowest total (**25**).

**Variations to clarify in exam**

- **Tie-breaking** — if two companies share the lowest sum, return both (`RANK()` / `DENSE_RANK()`) or one row depending on instructions.
- **Table name** — assume something like `CompanyEmployees(Company, Position, Employee)`.
- **SQL dialect** — Relisource .NET roles often use **SQL Server** (`TOP 1`, `GROUP BY`).

**Common mistakes**

- Using `MIN(Employee)` instead of `SUM(Employee)` — that returns the smallest single row, not smallest company total.
- Forgetting `GROUP BY Company` — aggregates without grouping are invalid or return one global row.

#### Further reading

- [MDN/SQL: GROUP BY (W3Schools reference)](https://www.w3schools.com/sql/sql_groupby.asp) — grouping and aggregates
- [Microsoft: SELECT — TOP clause](https://learn.microsoft.com/en-us/sql/t-sql/queries/top-transact-sql) — SQL Server TOP
- [PostgreSQL: Aggregate functions](https://www.postgresql.org/docs/current/functions-aggregate.html) — SUM and GROUP BY
- [SQLBolt: Lesson on SUM and COUNT](https://sqlbolt.com/lesson/aggregates) — interactive aggregation practice

</details>

<details><summary>Solution (JavaScript)</summary>

For the written exam the expected answer is **SQL**. Below is an equivalent **in-memory JavaScript** approach if you need to compute the same result from row objects (e.g. in a Node test harness).

```js
const rows = [
  { Company: 'ABC', Position: 'blah', Employee: 20 },
  { Company: 'ABC', Position: 'blah', Employee: 15 },
  { Company: 'ABC', Position: 'blah', Employee: 5 },
  { Company: 'XYZ', Position: 'blah', Employee: 10 },
  { Company: 'XYZ', Position: 'blah', Employee: 12 },
  { Company: 'XYZ', Position: 'blah', Employee: 5 },
  { Company: 'MNO', Position: 'blah', Employee: 20 },
  { Company: 'MNO', Position: 'blah', Employee: 5 },
];

function companyWithLowestEmployeeTotal(data) {
  const totals = new Map();

  for (const row of data) {
    totals.set(
      row.Company,
      (totals.get(row.Company) || 0) + row.Employee
    );
  }

  let minCompany = null;
  let minSum = Infinity;

  for (const [company, sum] of totals) {
    if (sum < minSum) {
      minSum = sum;
      minCompany = company;
    }
  }

  return minCompany;
}

companyWithLowestEmployeeTotal(rows); // 'MNO'
```

**SQL (SQL Server)**

```sql
SELECT TOP 1 Company
FROM CompanyEmployees
GROUP BY Company
ORDER BY SUM(Employee) ASC;
```

#### Code walkthrough

- **SQL** — `GROUP BY Company` computes `SUM(Employee)` per company; `ORDER BY SUM(Employee) ASC` puts the minimum total first; `TOP 1` returns that company name.
- **JavaScript** — `Map` accumulates sums in one pass, then a second pass finds the minimum total and associated company key.

#### Complexity

| | |
|-|-|
| Time | O(R) for R rows — single aggregation pass |
| Space | O(C) for C distinct companies |

#### Edge cases

- **Empty table** — query returns no rows; JS returns `null`.
- **Tied minimum** — `TOP 1` returns one arbitrary tied company unless secondary sort is specified.
- **NULL Employee values** — `SUM` ignores nulls in SQL; handle null coalescing in JS with `(row.Employee || 0)`.

</details>

</article>

<article>

Problem Solving

There is a food track consisting of cells marked with 0, 1, or other numbers. Here, 0 signifies the cell is not traceable, 1 signifies it is traceable, and any other number represents the destination. Starting from the top-left point, determine the longest path to reach the destination. If no path exists, print -1.

|   |   |   |
|---|---|---|
|1|1|1|
|1|0|1|
|1|9|1|

<details><summary>Theory and explanation</summary>

This is a **grid pathfinding** problem on a small matrix:

- **`0`** — blocked / not traceable; cannot enter.
- **`1`** — traceable; can traverse.
- **Any other value** (e.g. **`9`**) — the **destination** cell; reachable and ends the path.

You start at **top-left** `(0, 0)`. Movement is typically **4-directional** (up, down, left, right) unless the exam states otherwise. The goal is the **longest simple path** — a path that does not revisit cells — from start to the destination. If no path exists, return **`-1`**.

**Why DFS + backtracking**

- **BFS** finds the **shortest** path in an unweighted grid, not the longest.
- **Longest path in a general graph with cycles** is NP-hard; here paths are constrained to **simple paths** on a tiny grid, so **depth-first search (DFS)** with backtracking is feasible.
- At each step, mark the cell visited, explore neighbors, unmark on backtrack to try alternate routes.

**Algorithm outline**

1. Locate the destination cell (value ∉ `{0, 1}`).
2. If start is blocked (`0`) or no destination, return `-1`.
3. Run DFS from `(0, 0)` with a `visited` matrix.
4. When DFS reaches the destination, update `maxLength` with current path length (define whether length counts steps or cells — be consistent).
5. Return `maxLength`, or `-1` if never reached.

**Example grid**

```
(0,0)=1  (0,1)=1  (0,2)=1
(1,0)=1  (1,1)=0  (1,2)=1
(2,0)=1  (2,1)=9  (2,2)=1
```

Destination at `(2, 1)` with value `9`. Multiple routes exist around the blocked `(1,1)`; DFS explores all simple paths and keeps the maximum.

**Interview talking points**

- Confirm whether the destination cell’s value may be stepped on (yes — it terminates the path).
- Confirm 4-way vs 8-way movement.
- State time complexity exponential in grid size for worst-case DFS, acceptable for small exam grids.

#### Further reading

- [GeeksforGeeks: Find longest path in a matrix](https://www.geeksforgeeks.org/find-longest-possible-route-in-a-matrix/) — DFS backtracking on grids
- [LeetCode 79: Word Search](https://leetcode.com/problems/word-search/) — similar grid DFS with backtracking
- [CP-Algorithms: DFS](https://cp-algorithms.com/graph/depth-first-search.html) — depth-first search fundamentals
- [Visualgo: DFS/BFS](https://visualgo.net/en/dfsbfs) — interactive grid traversal

</details>

<details><summary>Solution (JavaScript)</summary>

```js
/**
 * Longest simple path from top-left to the destination cell.
 * @param {number[][]} grid
 * @returns {number} path length in steps, or -1
 */
function longestPathToDestination(grid) {
  if (!grid.length || !grid[0].length) return -1;

  const rows = grid.length;
  const cols = grid[0].length;

  if (grid[0][0] === 0) return -1;

  let destR = -1;
  let destC = -1;

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const v = grid[r][c];
      if (v !== 0 && v !== 1) {
        destR = r;
        destC = c;
      }
    }
  }

  if (destR === -1) return -1;

  const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
  let best = -1;
  const visited = Array.from({ length: rows }, () => Array(cols).fill(false));

  function dfs(r, c, steps) {
    if (r === destR && c === destC) {
      best = Math.max(best, steps);
      return;
    }

    for (const [dr, dc] of dirs) {
      const nr = r + dr;
      const nc = c + dc;
      if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
      if (visited[nr][nc]) continue;
      if (grid[nr][nc] === 0) continue;

      visited[nr][nc] = true;
      dfs(nr, nc, steps + 1);
      visited[nr][nc] = false;
    }
  }

  visited[0][0] = true;
  dfs(0, 0, 0);

  return best;
}

const grid = [
  [1, 1, 1],
  [1, 0, 1],
  [1, 9, 1],
];

longestPathToDestination(grid); // e.g. 6 (depends on longest simple route)
```

#### Code walkthrough

1. **Find destination** — scan for the cell whose value is neither `0` nor `1`.
2. **Early exits** — blocked start or missing destination → `-1`.
3. **`dfs(r, c, steps)`** — on reaching destination, update `best`; otherwise try four neighbors that are in bounds, unvisited, and not blocked.
4. **Backtracking** — unmark `visited` after recursion to allow other paths through the same cell in different routes.
5. **Start** — mark `(0,0)` visited and begin with `steps = 0`; arriving at destination records step count to that cell.

#### Complexity

| | |
|-|-|
| Time | O(4^(R×C)) worst case — exponential in grid cells for DFS on all simple paths |
| Space | O(R × C) for `visited` and recursion stack |

#### Edge cases

- **Start equals destination** — if top-left is the destination value, return `0`.
- **No path around walls** — blocked region isolates destination → `-1`.
- **Multiple destination markers** — problem implies one; if several, clarify whether any qualifies.
- **1×1 grid with destination** — handle without out-of-bounds errors.

</details>

</article>

<article>

JavaScript & HTML

Write JavaScript code to check if a button is clicked in an HTML element using an EventListener. Upon clicking, the size of the HTML element should increase by 10%.

<details><summary>Theory and explanation</summary>

This question tests **DOM events** and **element sizing** in the browser.

**Event-driven UI**

- HTML elements emit events when users interact (click, input, focus).
- **`addEventListener('click', handler)`** registers a handler without overwriting existing ones (unlike `onclick = …`).
- The handler receives an **Event** object; `event.currentTarget` is the element the listener was attached to.

**Increasing size by 10%**

Two common approaches:

1. **CSS `transform: scale()`** — multiplies visual size from a transform origin; does not affect layout flow. Each click can multiply current scale by `1.1`.
2. **Layout dimensions (`width` / `height`)** — read computed size, multiply by `1.1`, write inline style or CSS variable. Affects document layout.

For “increase by 10% **each click**”, compound the factor: `scale *= 1.1` or `width = width * 1.1`.

**Best practices**

- Select element with `document.getElementById` or `querySelector`.
- Use `addEventListener` in a `<script defer>` or end of body so DOM exists.
- Prefer **`currentTarget`** over `target` when the listener is on the element that should grow (child clicks still bubble).

**Accessibility**

- Use a real `<button>` or add `role="button"`, `tabindex="0"`, and keyboard handler if the clickable region is a `<div>`.

#### Further reading

- [MDN: EventTarget.addEventListener()](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) — registering click handlers
- [MDN: Element: click event](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event) — click event semantics
- [MDN: transform](https://developer.mozilla.org/en-US/docs/Web/CSS/transform) — scale transforms
- [MDN: Element.getBoundingClientRect()](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect) — measuring element size

</details>

<details><summary>Solution (JavaScript)</summary>

```html
<div id="box" style="width: 200px; height: 100px; background: #4a90d9;">
  Click the button to grow this box
</div>
<button id="growBtn" type="button">Grow box 10%</button>

<script>
  const box = document.getElementById('box');
  const growBtn = document.getElementById('growBtn');

  growBtn.addEventListener('click', () => {
    const w = box.offsetWidth;
    const h = box.offsetHeight;
    box.style.width = `${w * 1.1}px`;
    box.style.height = `${h * 1.1}px`;
  });
</script>
```

**Alternative using `transform: scale` (compounding visual size)**

```html
<div id="box">Grow me</div>
<button id="growBtn" type="button">Grow 10%</button>

<script>
  const box = document.getElementById('box');
  const growBtn = document.getElementById('growBtn');
  let scale = 1;

  growBtn.addEventListener('click', () => {
    scale *= 1.1;
    box.style.transform = `scale(${scale})`;
    box.style.transformOrigin = 'top left';
  });
</script>
```

#### Code walkthrough

- **`addEventListener('click', …)`** on the button detects clicks without inline HTML handlers.
- **Layout approach** — read `offsetWidth` / `offsetHeight`, multiply by `1.1`, assign to `style.width` and `style.height`.
- **Transform approach** — maintain a `scale` variable, multiply by `1.1` each click, apply via `transform: scale(...)`.

#### Complexity

| | |
|-|-|
| Time | O(1) per click — constant DOM reads/writes |
| Space | O(1) |

#### Edge cases

- **First click from zero size** — ensure element has initial dimensions in CSS.
- **Max size / overflow** — long-term growth may break layout; not required for exam.
- **Double listeners** — registering the same handler twice on reload duplicates growth; use one script block or remove listener.
- **Click on disabled button** — disabled buttons do not fire click; use enabled state or wrap in accessible container.

</details>

</article>

## Embedded Software Engineering Questions
<article>

Problem Solving

Your task is to write a function in the C programming language to find an optimal route cost to a target location inside a maze and return the highest 4 bits (MSB + 3 bits) of the optimal route cost value. Your function should take as input two integer numbers for the starting index on the maze array. An optimal route is defined as a complete path from the start point to the target location that requires the least effort/cost. Diagonal movement in the maze is not allowed. An example maze is given below: 
<table >
<tbody>
    <tr>
        <td>4</td>
        <td>3</td>
        <td>7</td>
        <td>8</td>
        <td>3</td>
        <td>6</td>
        <td>5</td>
        <td>4</td>
        <td style="background-color: grey;">-1</td>
        <td>2</td>
        <td>3</td>
    </tr>
    <tr>
        <td>6</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td>5</td>
        <td>2</td>
        <td style="background-color: #00b300;">0</td>
        <td>94</td>
    </tr>
    <tr>
        <td>7</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td>16</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td>7</td>
        <td>1</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td>5</td>
    </tr>
    <tr>
        <td>1</td>
        <td>15</td>
        <td>25</td>
        <td style="background-color: #00b300;">0</td>
        <td>3</td>
        <td>5</td>
        <td>6</td>
        <td style="background-color: grey;">-1</td>
        <td>6</td>
        <td>2</td>
        <td>6</td>
    </tr>
    <tr>
        <td>9</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td>21</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td>5</td>
        <td style="background-color: grey;">-1</td>
        <td>2</td>
    </tr>
    <tr>
        <td>2</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td>22</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td>5</td>
        <td style="background-color: grey;">-1</td>
        <td>4</td>
        <td style="background-color: grey;">-1</td>
        <td>7</td>
    </tr>
    <tr>
        <td>8</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td>26</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td>5</td>
        <td style="background-color: grey;">-1</td>
        <td>3</td>
        <td style="background-color: grey;">-1</td>
        <td>6</td>
    </tr>
    <tr>
        <td>20</td>
        <td>5</td>
        <td>3</td>
        <td>4</td>
        <td>11</td>
        <td>23</td>
        <td>11</td>
        <td style="background-color: grey;">-1</td>
        <td>2</td>
        <td style="background-color: grey;">-1</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td>20</td>
        <td style="background-color: grey;">-1</td>
        <td>2</td>
        <td style="background-color: grey;">-1</td>
        <td>4</td>
    </tr>
    <tr>
        <td>4</td>
        <td style="background-color: grey;">-1</td>
        <td>4</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: grey;">-1</td>
        <td>4</td>
        <td style="background-color: grey;">-1</td>
        <td>1</td>
        <td style="background-color: grey;">-1</td>
        <td>3</td>
    </tr>
    <tr>
        <td>6</td>
        <td>7</td>
        <td>8</td>
        <td>8</td>
        <td>7</td>
        <td>6</td>
        <td>5</td>
        <td>10</td>
        <td>4</td>
        <td style="background-color: grey;">-1</td>
        <td style="background-color: #66ccff;">2</td>
    </tr>
</tbody>
</table>

Maze Details:
- The starting block location will be provided as a function parameter (Blue block in the example).
- Blocks with a value of -1 are impassable (Grey blocks in the example).
- The Goal block and only the Goal block will always have a cost of 0 (Green blocks in the example).
- The maze will not have any circular routes that do not go through the Goal block first.
- The maze is stored in a 2D array. The 2D maze array will be defined globally.
- The maze size will be a pair of positive integer numbers, you can assume that the size parameters, length, and height of the maze will fit in a C integer (int) type.
- The cost values, excluding the impassable blocks, will always be a positive integer that will fit in a C integer (int) type.
- The maze length and height are not guaranteed to be equal but will be global fixed defined constants for each problem.

<details><summary>Theory and explanation</summary>

This embedded **maze routing** problem asks for the **minimum-cost path** from a given start cell to the **goal** (the unique cell with cost **0**), then returns the **top 4 bits** of that optimal cost.

**Problem elements**

- **Grid graph** — each passable cell is a node; edges connect 4-neighbors (no diagonals).
- **Cell cost** — entering or traversing a cell adds its positive integer cost; **`-1`** means impassable; the **goal** has cost **`0`**.
- **Optimal route** — path from start to goal with **minimum total cost** (classic shortest path with non-negative weights).
- **Output** — not the full cost, but **`(cost >> (sizeof(int)*8 - 4)) & 0xF`** — the highest 4 bits (MSB and next 3 bits) of the 32-bit cost on typical platforms.

**Algorithm: Dijkstra’s algorithm**

Non-negative edge weights → **Dijkstra** (or uniform-cost BFS if all costs were 1). Here step costs vary by cell value, so use a **min-priority queue** keyed by accumulated cost.

1. Find goal cell `(goalR, goalC)` where `maze[r][c] === 0`.
2. Initialize distance matrix to `Infinity`; `dist[startR][startC] = cost[startR][startC]` (or 0 if start cost is excluded — follow exam spec; usually include entering start cell).
3. Push `(startR, startC)` with its cost onto the priority queue.
4. Pop minimum; if at goal, return top 4 bits of cost.
5. For each 4-neighbor that is not `-1`, relax: `newCost = dist[r][c] + maze[nr][nc]`; if improved, update and push.

**Why not BFS**

BFS minimizes **number of steps**, not **sum of cell costs**. Variable positive weights require Dijkstra.

**Top 4 bits**

For 32-bit `int` cost `C`:

```c
unsigned int u = (unsigned int)C;
int top4 = (int)(u >> 28);  // bits 31..28
```

On platforms where `int` is 32 bits, shift by `sizeof(int) * 8 - 4`.

**Constraints from problem statement**

- No invalid cycles that bypass the goal — simplifies path structure but Dijkstra still applies.
- Maze dimensions are global constants; array may be jagged in C if row lengths differ — exam usually uses rectangular grid.

#### Further reading

- [CP-Algorithms: Dijkstra's algorithm](https://cp-algorithms.com/graph/dijkstra.html) — shortest paths with non-negative weights
- [GeeksforGeeks: Dijkstra's Shortest Path Algorithm](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/) — grid application
- [C bitwise operations (cppreference)](https://en.cppreference.com/w/c/language/operator_arithmetic) — shifts and masks for top bits
- [LeetCode 778: Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) — grid shortest path with cell costs

</details>

<details><summary>Solution (JavaScript)</summary>

Reference implementation using a binary min-heap priority queue. The exam expects **C**; see **Solution (other languages)** below.

```js
/**
 * @param {number[][]} maze
 * @param {number} startR
 * @param {number} startC
 * @returns {number} top 4 bits of optimal path cost, or -1 if unreachable
 */
function mazeTopFourBits(maze, startR, startC) {
  const rows = maze.length;
  const cols = maze[0].length;

  let goalR = -1;
  let goalC = -1;

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (maze[r][c] === 0) {
        goalR = r;
        goalC = c;
      }
    }
  }

  if (goalR === -1 || maze[startR][startC] === -1) return -1;

  const dist = Array.from({ length: rows }, () => Array(cols).fill(Infinity));
  const pq = new MinHeap((a, b) => a.cost - b.cost);

  dist[startR][startC] = maze[startR][startC];
  pq.push({ r: startR, c: startC, cost: dist[startR][startC] });

  const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];

  while (!pq.isEmpty()) {
    const { r, c, cost } = pq.pop();
    if (cost !== dist[r][c]) continue;

    if (r === goalR && c === goalC) {
      return topFourBits(cost);
    }

    for (const [dr, dc] of dirs) {
      const nr = r + dr;
      const nc = c + dc;
      if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
      if (maze[nr][nc] === -1) continue;

      const next = cost + maze[nr][nc];
      if (next < dist[nr][nc]) {
        dist[nr][nc] = next;
        pq.push({ r: nr, c: nc, cost: next });
      }
    }
  }

  return -1;
}

function topFourBits(cost) {
  // Assume 32-bit signed int semantics
  const u = cost >>> 0;
  return u >>> 28;
}

class MinHeap {
  constructor(cmp) {
    this.cmp = cmp;
    this.data = [];
  }
  push(x) {
    this.data.push(x);
    this.bubbleUp(this.data.length - 1);
  }
  pop() {
    const top = this.data[0];
    const last = this.data.pop();
    if (this.data.length) {
      this.data[0] = last;
      this.bubbleDown(0);
    }
    return top;
  }
  isEmpty() {
    return this.data.length === 0;
  }
  bubbleUp(i) {
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (this.cmp(this.data[i], this.data[p]) >= 0) break;
      [this.data[i], this.data[p]] = [this.data[p], this.data[i]];
      i = p;
    }
  }
  bubbleDown(i) {
    const n = this.data.length;
    while (true) {
      let s = i;
      const l = 2 * i + 1;
      const r = 2 * i + 2;
      if (l < n && this.cmp(this.data[l], this.data[s]) < 0) s = l;
      if (r < n && this.cmp(this.data[r], this.data[s]) < 0) s = r;
      if (s === i) break;
      [this.data[i], this.data[s]] = [this.data[s], this.data[i]];
      i = s;
    }
  }
}
```

#### Code walkthrough

1. **Locate goal** — scan for cell value `0`.
2. **Dijkstra** — priority queue ordered by accumulated cost; skip stale entries when popped cost ≠ best known.
3. **Relax neighbors** — add neighbor cell cost if passable; push improved distances.
4. **At goal** — return `topFourBits(optimalCost)` using unsigned right shift by 28.
5. **Unreachable** — return `-1` if queue empties without reaching goal.

#### Complexity

| | |
|-|-|
| Time | O(R × C × log(R × C)) with binary heap; each cell pushed limited times |
| Space | O(R × C) for `dist` and heap |

#### Edge cases

- **Start on goal** — cost is `0`; top 4 bits are `0`.
- **Start impassable (`-1`)** — return `-1` immediately.
- **Large costs** — ensure 32-bit int range; top 4 bits still well-defined via unsigned cast.
- **Stale PQ entries** — lazy deletion via `cost !== dist[r][c]` check.

</details>

<details><summary>Solution (other languages)</summary>

**C (exam language)** — assumes global `maze[HEIGHT][LENGTH]`, constants `HEIGHT`, `LENGTH`, and a simple min-heap or linear scan for smallest distance.

```c
#include <limits.h>

extern int maze[HEIGHT][LENGTH];
extern const int HEIGHT, LENGTH;

typedef struct {
    int r, c, cost;
} Node;

static int dist[HEIGHT][LENGTH];
static int visited[HEIGHT][LENGTH];

static int top_four_bits(int cost) {
    unsigned int u = (unsigned int)cost;
    return (int)(u >> (sizeof(int) * CHAR_BIT - 4));
}

int solve_maze(int startR, int startC) {
    int goalR = -1, goalC = -1;

    for (int r = 0; r < HEIGHT; r++) {
        for (int c = 0; c < LENGTH; c++) {
            dist[r][c] = INT_MAX;
            visited[r][c] = 0;
            if (maze[r][c] == 0) {
                goalR = r;
                goalC = c;
            }
        }
    }

    if (goalR < 0 || maze[startR][startC] == -1)
        return -1;

    dist[startR][startC] = maze[startR][startC];

    for (;;) {
        int bestR = -1, bestC = -1, bestCost = INT_MAX;

        for (int r = 0; r < HEIGHT; r++) {
            for (int c = 0; c < LENGTH; c++) {
                if (!visited[r][c] && dist[r][c] < bestCost) {
                    bestCost = dist[r][c];
                    bestR = r;
                    bestC = c;
                }
            }
        }

        if (bestR < 0)
            return -1;

        if (bestR == goalR && bestC == goalC)
            return top_four_bits(bestCost);

        visited[bestR][bestC] = 1;

        const int dr[] = {0, 1, 0, -1};
        const int dc[] = {1, 0, -1, 0};

        for (int k = 0; k < 4; k++) {
            int nr = bestR + dr[k];
            int nc = bestC + dc[k];
            if (nr < 0 || nr >= HEIGHT || nc < 0 || nc >= LENGTH)
                continue;
            if (maze[nr][nc] == -1 || visited[nr][nc])
                continue;

            int next = bestCost + maze[nr][nc];
            if (next < dist[nr][nc])
                dist[nr][nc] = next;
        }
    }
}
```

This C version uses **Dijkstra with a linear scan** for the minimum node (O(V²)) — acceptable for small embedded mazes. A binary heap reduces time for larger grids.

#### Code walkthrough

- **`top_four_bits`** — cast cost to `unsigned int`, shift right by `sizeof(int)*CHAR_BIT - 4`.
- **Outer loop** — pick unvisited cell with smallest `dist` (Dijkstra).
- **Termination** — when extracted node is goal, return top four bits of `bestCost`.
- **Relaxation** — update neighbors with `bestCost + maze[nr][nc]`.

#### Complexity

| | |
|-|-|
| Time | O((R×C)²) with linear scan; O(R×C×log(R×C)) with heap |
| Space | O(R×C) |

#### Edge cases

- **INT_MAX overflow on relax** — with exam constraints costs fit in `int`; use `long` if summing huge paths.
- **Multiple pushes** — linear-scan Dijkstra marks visited once when extracted; do not revisit.

</details>

</article>

