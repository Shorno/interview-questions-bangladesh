# ShopUp

|                   |                               |
| :---------------- | :---------------------------- |
| Founding year     | 2017                          |
| Company Website   | https://www.shopup.org        |
| Career Website    | https://www.shopup.org/career |
| Technologies Used |                               |

## Introduction
ShopUp is a B2B e-commerce platform connecting small retailers to manufacturers and suppliers, digitizing supply chain. 

## Interview Stages:

These are the steps for the ShopUp Fast track launchpad
1. **Aptitude Test**:	Online aptitude test
2. **SQL Test**:   Online SQL test
3. **In Person Interviews**: One technical and one behavioral in person interview
4. **Final on-site Test and Interview**: Final on-site test short informal interview

## Aptitude Test:

The first round was an
online aptitude test consisting of 23 questions to be solved within 1 hour. The questions covered
topics like pattern matching, profit and interest calculations, and age-related math problems
(e.g., father and children age problems).

## SQL Test:

There were three SQL problems to solve and record a video
explaining the thought process, and submit via a Google Form. Two of the problems were
very challenging—comparable to the "Hard" category on HackerRank.

## In Person Interviews:

### First Interview
<br>
<article>

- During internships, you often face challenging tasks with no existing resources. Have
you faced such a situation in your previous projects? How did you solve it?
- Internship tasks can sometimes be boring or unglamorous. Have you encountered this
before? How did you handle it?
- Internships can present problems outside your knowledge area. Have you experienced
this? How did you deal with it?

<details><summary>Theory and explanation</summary>

ShopUp's first in-person round mixes **behavioral** prompts about **internship resilience**. Interviewers want evidence you can learn independently, stay motivated on unglamorous work, and grow when thrown into unfamiliar domains — all common in B2B supply-chain product teams.

**How to structure each answer: STAR**

- **Situation** — Brief project/internship context (team, timeline, constraint).
- **Task** — What you were responsible for delivering.
- **Action** — Specific steps: documentation search, asking seniors, spikes, breaking problems down, maintaining quality on "boring" CRUD tasks.
- **Result** — Measurable outcome (feature shipped, bug reduced, skill gained).

**Prompt 1 — No existing resources**

Highlight: reading official docs, finding reference implementations, building a minimal prototype, time-boxing research, communicating blockers early.

**Prompt 2 — Boring or unglamorous tasks**

Highlight: professionalism, finding learning in fundamentals (tests, logging, data quality), how reliability on small tasks earned trust for bigger ones. Avoid sounding dismissive of maintenance work.

**Prompt 3 — Outside knowledge area**

Highlight: structured learning (course, pair programming), admitting gaps honestly, delivering a thin vertical slice while learning, documenting for the team.

**ShopUp context**

Supply-chain software involves integrations, ops tooling, and data cleanup — not always greenfield features. Tie answers to **ownership** and **retailer impact**.

#### Further reading

- [MIT CAPD: STAR method](https://capd.mit.edu/resources/the-star-method-for-behavioral-interviews/) — behavioral answer structure
- [ShopUp careers](https://www.shopup.org/career) — company mission and values
- [Google re:Work — Structured behavioral interviews](https://rework.withgoogle.com/guides/hiring-use-structured-interviewing/) — what good signals look like

</details>

<details><summary>Solution (JavaScript)</summary>

Use as a **response outline** — replace with your real stories:

```js
const internshipStories = {
  noResources: {
    situation: 'Tasked to integrate a supplier CSV feed with no API docs during internship.',
    task: 'Parse and validate 50k rows nightly without breaking existing orders.',
    action:
      'Sampled files, wrote schema validator, asked ops for edge cases, built retry queue.',
    result: 'Pipeline ran 30 days without manual fixes; promoted to own next integration.',
  },
  boringWork: {
    situation: 'Two sprints of fixing legacy SQL reports before feature work.',
    task: 'Improve report accuracy used by ops daily.',
    action: 'Added tests, documented assumptions, suggested one automation script.',
    result: 'Ticket volume dropped 40%; team trusted me with greenfield module.',
  },
  unknownDomain: {
    situation: 'First exposure to inventory reconciliation logic.',
    task: 'Debug stock mismatch between warehouse and app.',
    action: 'Shadowed ops, drew state diagram, read existing jobs, pair-debugged with senior.',
    result: 'Found rounding bug; learned domain enough to propose UI warning for retailers.',
  },
};
```

#### Complexity

| | |
|-|-|
| Time | N/A (behavioral) |
| Space | N/A (behavioral) |

#### Edge cases

- **No internship yet** — use university project, hackathon, or open-source contribution with same STAR structure.
- **Negative outcome** — still valuable if you show learning and changed approach.

</details>

</article>

### Second Interview
<br>
<article>

- Tell us about yourself.
- In many e-commerce sites, customers provide incorrect addresses. For example, they
list Dinajpur when their actual delivery location is Rangpur. The parcel goes to Dinajpur,
and then the customer says they are in Rangpur. You have 2 minutes to come up with
both technical and non-technical solutions.
- Would you run a business or software company in the future if given the
opportunity?

<details><summary>Theory and explanation</summary>

**Tell me about yourself**

- 60–90 second pitch: present role/education → relevant skills → why ShopUp/supply chain → what you want next.
- End with a bridge to their B2B retailer mission.

**Incorrect address problem (2-minute brainstorm)**

ShopUp cares about **last-mile cost** and **retailer trust**. Split solutions:

| Category | Ideas |
|----------|--------|
| **Technical** | Map pin / GPS capture at checkout; geocode validation against postal database; flag city-district mismatch; OTP call before dispatch; address confidence score; duplicate address clustering; photo proof at delivery; integrate Pathao/redx hub routing checks |
| **Non-technical** | Clear UI copy ("select delivery district"); SMS confirm address; small fee for address change after ship; ops callback for high-value orders; retailer education on capturing correct buyer phone |

Prioritize **prevention at order time** over **recovery after wrong dispatch**.

**Future business / software company**

- Answer authentically; show ambition balanced with commitment to learning.
- Good angle: experience at ShopUp as foundation for understanding SME digitization in Bangladesh.

#### Further reading

- [Google Maps Platform: Geocoding](https://developers.google.com/maps/documentation/geocoding/overview) — validate addresses programmatically
- [ShopUp about](https://www.shopup.org/) — B2B supply chain context for tailoring "why ShopUp"
- [Harvard Business Review: Behavioral interview tips](https://hbr.org/2014/10/how-to-succeed-at-the-interview) — concise self-intro guidance

</details>

<details><summary>Solution (JavaScript)</summary>

**Address validation sketch** (technical portion of the 2-minute answer):

```js
function addressRiskScore({ city, district, geoPin, geocodedDistrict }) {
  let score = 0;
  if (city && district && city !== geocodedDistrict) score += 50;
  if (!geoPin) score += 30;
  if (district === 'Dinajpur' && geocodedDistrict === 'Rangpur') score += 40; // example mismatch
  return score; // block or confirm if score > threshold
}
```

**Self-intro outline**

```js
const intro = [
  'Current: CS student / junior dev with X stack',
  'Highlight: one project with data or e-commerce touchpoint',
  'Why ShopUp: B2B retailers + supply chain impact in BD',
  'Close: excited about launchpad and learning production systems',
];
```

#### Complexity

| | |
|-|-|
| Time | N/A (behavioral / design brainstorm) |
| Space | N/A |

#### Edge cases

- **Rural addresses** — landmark-based validation vs strict geocoding failure.
- **Privacy** — GPS permission UX on low-end Android devices common among retailers.

</details>

</article>

## Final on-site Test and Interview:

### Exam (conducted while on a live Google Meet)
<br>
<article>

String Frequency Problem:

Given a string, find the character with the highest frequency and print both the character
and its count.
- Input: `aaabccd`
- Output: `a 3`

<details><summary>Theory and explanation</summary>

Count character frequencies with a **hash map** (object/`Map` in JS, `Counter` in Python). Track the character with maximum count while scanning.

**Single pass**

- For each char: increment count; if count > max, update max char.
- Time **O(n)**, space **O(k)** unique characters (k ≤ alphabet size).

**Tie-breaking**

- If multiple chars share max frequency, clarify output rule (first seen, lexicographically smallest, or print all).

#### Further reading

- [LeetCode 451: Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) — related frequency problem
- [MDN: Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) — frequency counting in JS

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function maxFrequencyChar(s) {
  const freq = new Map();
  let bestChar = '';
  let bestCount = 0;

  for (const ch of s) {
    const count = (freq.get(ch) || 0) + 1;
    freq.set(ch, count);
    if (count > bestCount) {
      bestCount = count;
      bestChar = ch;
    }
  }
  return `${bestChar} ${bestCount}`;
}

maxFrequencyChar('aaabccd'); // "a 3"
```

#### Code walkthrough

1. Iterate each character, update frequency in `Map`.
2. Track global max while scanning — no second pass needed.
3. Return formatted string `"char count"`.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(k) unique characters |

#### Edge cases

- **Empty string** — define behavior (error or empty output).
- **Single character** — returns that char with count 1.
- **Unicode** — JS string iteration handles UTF-16 code units; for full grapheme clusters use specialized libraries.

</details>

</article>

<article>

Cluster Detection Problem:

Given a 2D axis with `n` circles, where each circle has a center `(x, y)` and a radius `R`,
determine the number of clusters (groups of intersecting circles). Only a diagram was
provided; no test cases.

<details><summary>Theory and explanation</summary>

Two circles **intersect or touch** if distance between centers ≤ sum of radii. Clusters are **connected components** in the graph where each circle is a node and an edge exists if circles overlap.

**Algorithm**

1. Build graph: for each pair `(i, j)`, add edge if `dist(i, j) <= R_i + R_j`.
2. Count connected components via **DFS/BFS** or **Union-Find**.

**Alternative**

- For n small, O(n²) pairwise check is fine.
- For large n, spatial indexing (grid, R-tree) reduces neighbor checks.

**Interview talking points**

- Clarify whether **tangential touch** counts as same cluster (typically yes).
- Circles fully inside another still intersect — one cluster.
- Transitive: A touches B, B touches C → one cluster even if A and C don't touch.

#### Further reading

- [LeetCode 547: Number of Provinces](https://leetcode.com/problems/number-of-provinces/) — connected components template
- [Computational geometry: Circle-circle intersection](https://en.wikipedia.org/wiki/Circle_intersection) — distance condition
- [Union-Find (Disjoint Set Union)](https://cp-algorithms.com/data_structures/disjoint_set_union.html) — efficient component merging

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function circleClusters(circles) {
  const n = circles.length;
  const parent = Array.from({ length: n }, (_, i) => i);

  function find(i) {
    if (parent[i] !== i) parent[i] = find(parent[i]);
    return parent[i];
  }
  function unite(a, b) {
    parent[find(b)] = find(a);
  }

  function intersects(a, b) {
    const dx = a.x - b.x;
    const dy = a.y - b.y;
    const dist = Math.hypot(dx, dy);
    return dist <= a.r + b.r;
  }

  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      if (intersects(circles[i], circles[j])) unite(i, j);
    }
  }

  const roots = new Set();
  for (let i = 0; i < n; i++) roots.add(find(i));
  return roots.size;
}
```

#### Code walkthrough

1. **Pairwise intersection** using Euclidean distance vs sum of radii.
2. **Union-Find** merges overlapping circles into same cluster.
3. Count distinct roots = number of clusters.

#### Complexity

| | |
|-|-|
| Time | O(n²) pairwise checks |
| Space | O(n) for DSU |

#### Edge cases

- **n = 0** — return 0.
- **No overlaps** — each circle is its own cluster → n.
- **All overlap chain** — return 1.

</details>

</article>

<article>

Load Balancer Problem:

1000 requests hit a load balancer every second and are distributed to 5 servers.
10% of requests get delayed and must be requeued.
- How many requests are handled per second?
- How many requests are handled by each server?

<details><summary>Theory and explanation</summary>

**Steady-state throughput**

- Incoming: **1000 req/s**.
- **10% delayed** → 100 req/s requeued (still in system, not lost).
- If "handled" means **successfully processed on first attempt**: **900 req/s** complete immediately; 100 req/s recycle (may add backlog if not processed in same second — clarify assumptions).

Common interview assumption: requeued requests are **still processed within the same second** by the same pool → total **1000 req/s processed**, with 100 experiencing retry/delay path.

**Per-server distribution (ideal round-robin)**

- Equal split: **1000 / 5 = 200 req/s per server** if requeued work is spread across servers too.
- If only **900** count as "handled" first pass: **180 req/s per server** on first pass; remaining 20/server enter retry queue.

**Load balancer concepts**

- Round-robin, least connections, weighted routing.
- Retries can **amplify load** — cap retry rate, use exponential backoff, idempotency keys.
- Monitor **p99 latency** for delayed 10%.

**Interview talking points**

- State assumptions explicitly — exam likely expects **200/server/s** and **1000 total processed** OR **900 successful + 100 retry** — ask clarifier if live.
- Mention health checks and shedding load if servers fail.

#### Further reading

- [NGINX: Load balancing methods](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/) — distribution algorithms
- [AWS: Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) — retry and target health
- [Google SRE Book: Handling overload](https://sre.google/sre-book/handling-overload/) — queueing under retry storms

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function loadBalancerStats({
  incomingPerSec = 1000,
  servers = 5,
  delayedFraction = 0.1,
  retrySameSecond = true,
}) {
  const delayed = incomingPerSec * delayedFraction;
  const firstPass = incomingPerSec - delayed;
  const handledPerSec = retrySameSecond ? incomingPerSec : firstPass;
  const perServer = handledPerSec / servers;

  return {
    handledPerSec,
    perServer,
    delayedPerSec: delayed,
    firstPassPerSec: firstPass,
  };
}

loadBalancerStats({});
// handledPerSec: 1000, perServer: 200, delayed: 100, firstPass: 900
```

#### Code walkthrough

- Compute delayed volume: 10% of 1000 = 100.
- If retries complete same second, throughput stays 1000/s, 200 per server.
- If not, first-pass throughput 900/s → 180 per server until queue drains.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases

- **Persistent retry backlog** — stable system needs `processing_capacity >= incoming`.
- **Uneven server weights** — adjust per-server share (e.g. 2:2:2:2:2 vs weighted).

</details>

</article>

<article>

There are two tables:

- Table 1: id, name, supervisor_id, branch_id
- Table 2: branch_id, branch_name
  
Task: Write a query to print each employee's id, name, supervisor name, and
branch name.

<details><summary>Theory and explanation</summary>

This is a **self-join** on the employee table plus a join to branch dimension.

**Relationships**

- `employees.supervisor_id` → `employees.id` (supervisor is also an employee row).
- `employees.branch_id` → `branches.branch_id`.

Use **LEFT JOIN** for supervisor if top-level employees have `NULL supervisor_id`; **INNER JOIN** to branches if every employee must have a branch.

#### Further reading

- [SQLBolt: JOINs](https://sqlbolt.com/lesson/select_queries_with_joins) — multi-table joins
- [LeetCode 197: Rising Temperature](https://leetcode.com/problems/rising-temperature/) — SQL practice environment
- [PostgreSQL: Table aliases](https://www.postgresql.org/docs/current/queries-table-expressions.html#QUERIES-FROM) — self-join syntax

</details>

<details><summary>Solution (JavaScript)</summary>

```sql
SELECT
  e.id,
  e.name,
  s.name AS supervisor_name,
  b.branch_name
FROM employees e
LEFT JOIN employees s ON e.supervisor_id = s.id
INNER JOIN branches b ON e.branch_id = b.branch_id
ORDER BY e.id;
```

#### Code walkthrough

1. Alias `employees` as `e` (employee) and `s` (supervisor).
2. **LEFT JOIN** supervisor — keeps employees without supervisor (NULL name).
3. **INNER JOIN** `branches` for branch name.
4. Select requested columns.

#### Complexity

| | |
|-|-|
| Time | O(n + m) with indexes on FK columns |
| Space | O(result rows) |

#### Edge cases

- **Circular supervisor references** — data bug; query still runs.
- **Duplicate branch names** — use `branch_id` if names not unique.
- **CEO row** — `supervisor_name` IS NULL.

</details>

</article>

<article>

You have to build a robust coupon system of two types. one is user specific, a user can only redeem it once. an other is time specific, a user can redeem it x times within a period. You have to implement microservices for both generating these coupon and validation. Response time is preferred to be <100ms for 1M users with 5K coupons active, inactive or expired. You have to record all coupon validation attempts asynchronously including key details. 

Allowed to use any combination of the following: 
NodeJS/TypeScript, Golang, kafka, docker, postgresql, MySQL, Lua, Redis 

Time Constraint: 3 Hours

<details><summary>Theory and explanation</summary>

This is a **timed system-design + partial implementation** exercise. Optimize for **correct rules**, **fast validation path**, and **async audit**.

**Coupon types**

| Type | Rule |
|------|------|
| **User-specific** | One redemption per `(user_id, coupon_code)` ever |
| **Time-window** | Up to **x** redemptions per user within `[start, end]` |

**Service split**

1. **Coupon Admin / Generator** — CRUD coupons, set rules, status (active/inactive/expired); writes authoritative record to PostgreSQL.
2. **Validation API** — read-heavy, <100ms; checks eligibility, atomically records redemption.
3. **Audit Consumer** — Kafka topic `coupon.validation.attempts`; worker persists full payload (user, coupon, result, latency, IP) without blocking response.

**Hot path architecture (<100ms at scale)**

- **Redis** for:
  - Active coupon metadata cache (5K keys trivial).
  - **Atomic counters**: `INCR user:{id}:coupon:{code}` with TTL for time-window caps.
  - **SET** `user:{id}:coupon:{code}:once` for user-specific redeemed flag.
- **Lua script in Redis** — atomic check-and-set (type rules + increment) in one round trip.
- **PostgreSQL** — source of truth; async sync or write-through on success only.

**Validation flow**

1. Load coupon from Redis (fallback DB on miss).
2. Reject fast if inactive/expired/wrong type.
3. Run Lua: enforce once OR window count ≤ x.
4. Return `{ valid, reason }` immediately.
5. Publish attempt event to Kafka (fire-and-forget with local buffer).

**3-hour scope triage**

- Implement validation service + Redis Lua + one generator endpoint + Kafka stub consumer.
- Docker Compose: api, redis, postgres, kafka.
- Document trade-offs vs full production (sharding, fraud, idempotency keys).

#### Further reading

- [Redis: EVAL Lua scripts](https://redis.io/docs/manual/programmability/eval-intro/) — atomic validation logic
- [Apache Kafka: Introduction](https://kafka.apache.org/documentation/) — async audit pipeline
- [Stripe: Idempotent requests](https://stripe.com/docs/api/idempotent_requests) — safe retries on validation API

</details>

<details><summary>Solution (JavaScript)</summary>

**Redis Lua sketch** (user-specific + time-window):

```lua
-- KEYS[1]=userKey, ARGV[1]=maxUses, ARGV[2]=ttlSeconds, ARGV[3]=mode ('once'|'window')
local count = tonumber(redis.call('GET', KEYS[1]) or '0')
if ARGV[3] == 'once' and count >= 1 then return 0 end
if ARGV[3] == 'window' and count >= tonumber(ARGV[1]) then return 0 end
count = redis.call('INCR', KEYS[1])
if ARGV[3] == 'window' then redis.call('EXPIRE', KEYS[1], ARGV[2]) end
return 1
```

**TypeScript validation handler outline**:

```ts
async function validateCoupon(userId: string, code: string) {
  const coupon = await redis.hgetall(`coupon:${code}`);
  if (!coupon.active) return reject('INACTIVE');

  const key = `use:${userId}:${code}`;
  const ok = await redis.eval(luaScript, 1, key, coupon.maxUses, coupon.ttl, coupon.mode);
  const result = ok === 1 ? 'VALID' : 'LIMIT_EXCEEDED';

  kafka.produce('coupon.validation.attempts', { userId, code, result, ts: Date.now() });
  return result;
}
```

#### Code walkthrough

1. **Cache coupon rules** in Redis hash — O(1) lookup among 5K coupons.
2. **Lua** ensures race-safe increment for concurrent requests.
3. **Kafka** decouples audit persistence from 100ms SLA.
4. **Postgres** updated by consumer for reporting and reconciliation.

#### Complexity

| | |
|-|-|
| Time | Validation O(1) Redis ops per request |
| Space | O(active coupons + hot user keys) |

#### Edge cases

- **Double-submit same ms** — idempotency key on client + Redis SETNX.
- **Clock skew on window coupons** — use server time; store window bounds in coupon metadata.
- **Expired mid-request** — check `expires_at` inside Lua atomically.

</details>

</article>

### Interview
<br>
<article>

The final interview was mostly informal, discussing about the company, work culture, internship
duration, and salary.

<details><summary>Theory and explanation</summary>

The **final informal interview** assesses **culture fit**, **expectations alignment**, and ** mutual interest** — not technical depth.

**Prepare to discuss**

- **Company** — ShopUp's B2B model, retailer/supplier impact, recent initiatives (read careers page/news).
- **Work culture** — team structure, mentorship, on-site vs hybrid, pace of launchpad.
- **Internship duration** — availability (3/6 months), academic constraints, full-time conversion interest.
- **Salary** — research BD intern ranges; express flexibility or anchor politely if asked; ask about benefits, transport, device policy.

**Questions to ask them**

- What does success look like for a launchpad intern in 90 days?
- How are interns paired with mentors?
- Typical stack for the team you might join?

**Tone**

- Conversational, curious, honest — match their informal style while staying professional.

#### Further reading

- [ShopUp career page](https://www.shopup.org/career) — roles and culture copy
- [Levels.fyi negotiation basics](https://www.levels.fyi/blog/guide-to-comp-negotiation.html) — general comp conversation tips (adapt for intern context)

</details>

<details><summary>Solution (JavaScript)</summary>

**Prep checklist** (non-code):

```js
const finalInterviewPrep = {
  companyTalkingPoints: [
    'B2B commerce for SMEs in Bangladesh',
    'Supply chain digitization impact',
  ],
  cultureQuestions: [
    'Team size for interns?',
    'Code review and deployment cadence?',
  ],
  logistics: ['Start date', 'Duration', 'University letter requirements'],
  compensation: ['Stipend range research', 'What is included ( lunch/transport )'],
};
```

#### Complexity

| | |
|-|-|
| Time | N/A (behavioral) |
| Space | N/A (behavioral) |

</details>

</article>
