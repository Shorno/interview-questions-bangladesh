---
description: Optimizely interview questions, Optimizely interview stages, Optimizely interview details, Optimizely interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/optmizely
---
# Optimizely Bangladesh

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-| :- |
| Founding year | |
| Company Website | https://www.optimizely.com/ |
| Career Website | https://careers.optimizely.com/search/ |
| Technologies Used| Python, NodeJS, Angular2, Scala, MongoDB |

## Introduction

[Optimizely](https://www.optimizely.com/get-started/) has recently expanded its global operations with the establishment of a new office in Bangladesh. Optimizely is a leading software company specializing in digital experience platforms (DXP) that empower businesses to enhance their marketing and product strategies. Optimizely offers a comprehensive suite of tools, including a robust Content Management System (CMS) and an integrated Content Marketing Platform (CMP).

## Interview Stages

#### Software Engineer Intern

For the Software Engineer Intern position, the interview process consists of the following stages:

1. **Phone Screening**: The first stage of the interview process is a phone screening with a recruiter. The recruiter will ask you about your background, experience, and interest in the company. This is also an opportunity for you to ask questions about the role and the company.

2. **Take-Home Assignment**: If you pass the phone screening, you will be given a take-home assignment to complete. It's more of a practical problem-solving task that evaluates your coding skills and problem-solving abilities. You will need to come up with the solution, write a clean code, testcases(edge cases are important), and submit it in a google form. It will be judged based on correctness, efficiency, and code quality.

3. **On-Site Interview**: If you successfully complete the take-home assignment, you will be invited for an on-site interview. This will be a system design interview where you will be asked to design and code a system in 1 hour. Then you will be asked about your code, database design, sql queries, basic networking and OS, OOP concepts, design patterns and project related knowledge. There may be some in depth questions about the technologies in the projects that you have worked on. The whole interview may take around 2.5 hours. If you pass this stage, there may be a final interview with the hiring manager or a behavioral interview.

## Take-Home Assignment Questions

<article>

Build a tshirt distribution system

<details><summary>Theory and explanation</summary>

Imagine you manage orders at a T-shirt factory by packing a bulk number of shirts into a fixed number of bags. For every order you know **how many bags** to fill and **how many shirts** were actually produced (which may differ slightly from the planned count due to minor production errors).

The goal is to **distribute shirts as evenly as possible** across bags with one critical constraint: **at most one bag may contain a different count than the others**. All other bags must share the same size.

This is a classic **integer division with remainder** problem:

- Let `totalShirts` be the actual shirt count and `numBags` the number of bags.
- Each bag should ideally hold `floor(totalShirts / numBags)` shirts — call this the **base count**.
- The **remainder** `totalShirts % numBags` is the extra shirts that cannot be split evenly without breaking the “only one bag differs” rule.
- Put **all remainder shirts into a single bag**, so that bag holds `base + remainder` and every other bag holds `base`.

**Why this minimizes deviation**

The deviation is defined as the difference between the largest and smallest bag counts. When only one bag may differ:

- If `remainder = 0`, every bag has the same count and deviation is **0**.
- If `remainder > 0`, `numBags - 1` bags hold `base` and one bag holds `base + remainder`, so deviation is **`remainder`**.

Any attempt to spread the remainder across multiple bags would create **more than one bag with a different count**, violating the constraint. Spreading remainder across bags would also **not** reduce the max–min gap below `remainder` when one bag must absorb all extras.

**Example**

103 shirts, 10 bags → `base = 10`, `remainder = 3` → nine bags with 10 shirts, one bag with 13 → deviation `13 - 10 = 3`.

**Edge considerations for interviews**

- `numBags <= 0` or negative shirt counts are invalid inputs — validate and throw or return an error structure.
- `totalShirts < numBags` still works: `base = 0`, one bag gets all shirts, others empty (if zero shirts per bag is allowed — clarify with interviewer).
- Return type: array of bag sizes, or `{ bags, deviation }` — state your API clearly in the take-home.

#### Further reading

- [MDN: Remainder (%) operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder) — integer division remainder in JavaScript
- [GeeksforGeeks: Distribute N items among K people](https://www.geeksforgeeks.org/distribute-n-items-among-k-people-as-fairly-as-possible/) — fair distribution with remainder
- [Euclidean division (Wikipedia)](https://en.wikipedia.org/wiki/Euclidean_division) — formal definition of quotient and remainder
- [LeetCode 1282: Split a string in balanced strings](https://leetcode.com/problems/split-a-string-in-balanced-strings/) — related “balance across groups” thinking

</details>

<details><summary>Solution (JavaScript)</summary>

```js
/**
 * Distribute shirts into bags as evenly as possible.
 * At most one bag may differ from the others.
 *
 * @param {number} totalShirts - non-negative integer
 * @param {number} numBags - positive integer
 * @returns {{ bags: number[], deviation: number }}
 */
function distributeShirts(totalShirts, numBags) {
  if (!Number.isInteger(numBags) || numBags <= 0) {
    throw new RangeError('numBags must be a positive integer');
  }
  if (!Number.isInteger(totalShirts) || totalShirts < 0) {
    throw new RangeError('totalShirts must be a non-negative integer');
  }

  const base = Math.floor(totalShirts / numBags);
  const remainder = totalShirts % numBags;

  const bags = Array(numBags).fill(base);
  if (remainder > 0) {
    bags[numBags - 1] = base + remainder;
  }

  const deviation = remainder === 0 ? 0 : remainder;
  return { bags, deviation };
}

// Example: 103 shirts, 10 bags
distributeShirts(103, 10);
// { bags: [10,10,10,10,10,10,10,10,10,13], deviation: 3 }
```

#### Code walkthrough

1. **Validate inputs** — reject non-integers and invalid bag counts early; production take-homes should include tests for this.
2. **`base = floor(totalShirts / numBags)`** — the uniform count for all but one bag.
3. **`remainder = totalShirts % numBags`** — shirts that must go into the single “overflow” bag.
4. **Fill array** with `base`, then add all remainder to one bag (here the last bag; any single index works).
5. **`deviation`** equals `remainder` when remainder is non-zero, else `0`.

#### Complexity

| | |
|-|-|
| Time | O(n) where n = `numBags` to build the result array |
| Space | O(n) for the output array |

#### Edge cases

- **`totalShirts = 0`** — all bags contain 0; deviation 0.
- **`remainder = 0`** — perfectly even split (e.g. 100 shirts, 10 bags → all 10).
- **`totalShirts < numBags`** — e.g. 7 shirts, 10 bags → one bag gets 7, nine get 0 (if empty bags allowed).
- **Large inputs** — JavaScript numbers are safe up to `2^53 - 1`; use BigInt if the problem scales beyond that.

</details>

</article>

<article>

Task Management Software Reviewer Assignment

<details><summary>Theory and explanation</summary>

This problem models **reviewer assignment** in task tools like JIRA, Trello, or Asana. Each task has an assignee, optional reviewer, status, and estimated hours. You must **recommend reviewers** for tasks in `"in-review"` status that lack a reviewer, while balancing two objectives:

1. **Even distribution** — no team member should review far more tasks than others.
2. **Minimize total effort** — each person’s workload includes assignee hours plus review hours; reviewing costs **one-third** of the task’s `estimateInHours`.

**Data model recap**

| Field | Meaning |
|-------|---------|
| `taskId` | Unique identifier |
| `assigneeName` | Person doing the work |
| `reviewerName` | Code reviewer (`null` if unassigned) |
| `status` | `"todo"`, `"in-progress"`, `"in-review"`, `"done"` |
| `estimateInHours` | Assignee effort estimate |

**Constraints**

- Only suggest reviewers for `"in-review"` tasks **without** an existing reviewer.
- A person **cannot review their own task** (assignee ≠ reviewer).
- Everyone on the team has at least one assigned task — team roster = unique assignees.
- Some tasks already have reviewers; respect those when computing load.

**Algorithm strategy (greedy load balancing)**

This is a variant of **multi-dimensional load balancing**:

1. **Initialize load maps** from existing assignments:
   - **Effort** per person = sum of assignee `estimateInHours` for their tasks + sum of `estimateInHours / 3` for tasks they already review.
   - **Review count** per person = number of tasks they review.
2. Collect tasks needing a reviewer (`status === "in-review"` && `reviewerName == null`).
3. **Sort** those tasks by `estimateInHours` descending — assign heavy reviews first so large tasks go to the least-loaded reviewer early (greedy improvement).
4. For each task, pick the eligible team member with:
   - **Minimum total effort** (primary key),
   - then **minimum review count** (tie-break for even distribution),
   - excluding the assignee.
5. Assign reviewer, update effort and review count.

**Why greedy works here**

Exact optimality for multi-objective scheduling is NP-hard in general, but interview take-homes expect a **clear greedy heuristic** with O(tasks × team) complexity, readable code, and sensible tie-breaking. Mention in comments that weighted round-robin or min-cost flow are alternatives at scale.

**Interview talking points**

- Clarify whether assignee effort counts for `"done"` tasks or only active ones.
- Immutable vs in-place update of task list.
- Extensibility: skill-based reviewers, timezone overlap, max reviews per person.

#### Further reading

- [JIRA: Code reviewers and pull requests](https://support.atlassian.com/jira-software-cloud/docs/review-and-merge-code-in-jira/) — real-world reviewer workflows
- [Load balancing (Wikipedia)](https://en.wikipedia.org/wiki/Load_balancing_(computing)) — distributing work across workers
- [Greedy algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Greedy_algorithm) — heuristic assignment
- [MDN: Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) — tracking per-person effort in JS

</details>

<details><summary>Solution (JavaScript)</summary>

```js
/**
 * @typedef {Object} Task
 * @property {number} taskId
 * @property {string} assigneeName
 * @property {string|null} reviewerName
 * @property {'todo'|'in-progress'|'in-review'|'done'} status
 * @property {number} estimateInHours
 */

/** @param {Task[]} tasks */
function assignReviewers(tasks) {
  const effort = new Map();
  const reviewCount = new Map();

  const ensurePerson = (name) => {
    if (!effort.has(name)) {
      effort.set(name, 0);
      reviewCount.set(name, 0);
    }
  };

  for (const task of tasks) {
    ensurePerson(task.assigneeName);
    effort.set(
      task.assigneeName,
      effort.get(task.assigneeName) + task.estimateInHours
    );

    if (task.reviewerName) {
      ensurePerson(task.reviewerName);
      reviewCount.set(
        task.reviewerName,
        reviewCount.get(task.reviewerName) + 1
      );
      effort.set(
        task.reviewerName,
        effort.get(task.reviewerName) + task.estimateInHours / 3
      );
    }
  }

  const team = [...effort.keys()];

  const needsReviewer = tasks.filter(
    (t) => t.status === 'in-review' && t.reviewerName == null
  );
  needsReviewer.sort((a, b) => b.estimateInHours - a.estimateInHours);

  for (const task of needsReviewer) {
    let best = null;
    let bestEffort = Infinity;
    let bestReviews = Infinity;

    for (const name of team) {
      if (name === task.assigneeName) continue;
      const e = effort.get(name);
      const r = reviewCount.get(name);
      if (e < bestEffort || (e === bestEffort && r < bestReviews)) {
        best = name;
        bestEffort = e;
        bestReviews = r;
      }
    }

    if (best == null) {
      throw new Error(`No eligible reviewer for task ${task.taskId}`);
    }

    task.reviewerName = best;
    const reviewHours = task.estimateInHours / 3;
    effort.set(best, bestEffort + reviewHours);
    reviewCount.set(best, bestReviews + 1);
  }

  return tasks;
}
```

#### Code walkthrough

1. **`effort` / `reviewCount` maps** — seed from all tasks: every assignee accrues full estimate; existing reviewers accrue `estimate / 3` and increment review count.
2. **`needsReviewer`** — filter `"in-review"` tasks with null reviewer; sort descending by estimate so large reviews are placed first.
3. **Inner loop** — skip assignee; pick minimum effort, break ties with minimum review count.
4. **Update state** — mutate `reviewerName` and bump chosen reviewer’s effort and count before the next task.

#### Complexity

| | |
|-|-|
| Time | O(T log T + T × P) where T = tasks needing reviewer, P = team size |
| Space | O(P) for load maps |

#### Edge cases

- **Single-person team** — no eligible reviewer for their own `"in-review"` task; throw or leave null and document.
- **All reviewers pre-assigned** — function is a no-op on reviewer fields.
- **Floating effort** — `estimateInHours / 3` may be fractional; acceptable per problem statement.
- **Tie on effort and review count** — pick deterministically (first in `team` order) or alphabetically for reproducible tests.

</details>

</article>

## On-Site Interview Questions

<article>

Design a Backend for a Simplified Version of Internet Banking

<details><summary>Theory and explanation</summary>

This is a **system design** question for a simplified internet banking backend. You typically have ~1 hour to sketch APIs, data models, and core flows, then implement one function (often **Top N users by transactions**).

#### Acceptance criteria (functional)

| Feature | Description |
|---------|-------------|
| **View account balance** | Read current balance for authenticated user |
| **Transfer money** | Send funds to another registered user by phone number |
| **Pay utility bill** | Pay a provider chosen from a system provider list |
| **Top N users** | Given transactions, return top N users by transaction count (name, phone, count) descending |
| **Transaction history** | User’s history, newest first; transfers show recipient phone + amount; bills show provider name; all include payment date |

#### High-level architecture

```
Client (mobile/web)
    → API Gateway / Load Balancer
    → Auth service (JWT / session)
    → Banking API (REST or GraphQL)
    → PostgreSQL (accounts, transactions, providers)
    → Optional: Redis cache for hot balances
```

**Core entities**

- **User** — `id`, `name`, `phone` (unique), `password_hash`, `balance`
- **Transaction** — `id`, `type` (`transfer` \| `bill_payment`), `amount`, `user_id`, `created_at`, plus type-specific fields (`recipient_phone`, `provider_id`)
- **UtilityProvider** — `id`, `name`, `account_number`

#### Key design decisions

1. **ACID transfers** — debit sender and credit recipient in one **database transaction** with row-level locks (`SELECT … FOR UPDATE`) to prevent double-spend and race conditions.
2. **Idempotency** — clients may retry; accept `Idempotency-Key` header to avoid duplicate transfers.
3. **Validation** — sufficient balance, positive amount, registered recipient, known provider.
4. **Audit trail** — append-only transaction log; history is a query on `transactions` filtered by `user_id`, ordered by `created_at DESC`.
5. **Top N users** — aggregate `COUNT(*)` grouped by user; sort descending; limit N. Can be SQL or in-memory for the coding portion.

#### API sketch (REST)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/accounts/me/balance` | Current balance |
| POST | `/transfers` | `{ toPhone, amount }` |
| POST | `/bills/pay` | `{ providerId, amount }` |
| GET | `/accounts/me/transactions` | Paginated history |
| GET | `/admin/users/top?n=10` | Top N by volume (admin) |

#### Bonus: Promo codes

- **PromoCode** — `code`, `cashback_amount`, `max_uses_per_user`, `created_at`
- **PromoRedemption** — `promo_id`, `user_id`, `bill_transaction_id`
- Analytics: total uses, average uses per user, total cashback — SQL aggregations with `GROUP BY promo_id`, ordered by `created_at DESC`.

#### Security and non-functional

- HTTPS, hashed passwords (bcrypt/argon2), rate limiting on transfers.
- Decimal/money: store amounts as **integer minor units** (poisa) to avoid float errors.
- Mention monitoring, structured logging, and backup strategy briefly.

#### Further reading

- [Martin Fowler: Patterns of Enterprise Application Architecture](https://martinfowler.com/eaaCatalog/) — domain patterns for financial apps
- [Stripe: Idempotent requests](https://stripe.com/docs/api/idempotent_requests) — retry-safe payments
- [PostgreSQL: Transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — ACID guarantees
- [System Design Primer: Bank system discussions](https://github.com/donnemartin/system-design-primer) — scalable backend patterns
- [OWASP: Authentication cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) — securing user accounts

</details>

<details><summary>Solution (JavaScript)</summary>

Below are **data-structure sketches** and a reference implementation of **Top N users by transaction count** — the function most often implemented in the timed coding portion.

```js
// --- Schema sketches (TypeScript-style comments) ---

/**
 * User { id, name, phone, balanceCents }
 * Transaction {
 *   id, userId, type: 'transfer' | 'bill_payment',
 *   amountCents, createdAt,
 *   recipientPhone?, providerName?
 * }
 */

/** Top N users by number of transactions (descending). */
function topNUsersByTransactions(transactions, usersById, n) {
  const counts = new Map(); // userId -> count

  for (const tx of transactions) {
    counts.set(tx.userId, (counts.get(tx.userId) || 0) + 1);
  }

  const ranked = [...counts.entries()]
    .map(([userId, count]) => {
      const user = usersById.get(userId);
      return {
        name: user.name,
        phone: user.phone,
        transactionCount: count,
      };
    })
    .sort((a, b) => b.transactionCount - a.transactionCount)
    .slice(0, n);

  return ranked;
}

// --- Transfer sketch (pseudo-service layer) ---

async function transfer(db, { fromUserId, toPhone, amountCents, idempotencyKey }) {
  return db.transaction(async (trx) => {
    const sender = await trx.users.findByIdForUpdate(fromUserId);
    const recipient = await trx.users.findByPhoneForUpdate(toPhone);

    if (!recipient) throw new Error('Recipient not registered');
    if (sender.balanceCents < amountCents) throw new Error('Insufficient funds');

    await trx.users.updateBalance(fromUserId, sender.balanceCents - amountCents);
    await trx.users.updateBalance(recipient.id, recipient.balanceCents + amountCents);

    await trx.transactions.insert({
      userId: fromUserId,
      type: 'transfer',
      amountCents,
      recipientPhone: toPhone,
      createdAt: new Date(),
      idempotencyKey,
    });
  });
}
```

#### Code walkthrough

- **`topNUsersByTransactions`** — single pass to count per `userId`, join user metadata, sort by count descending, take first `n`.
- **`transfer` sketch** — wraps debit/credit in a DB transaction with row locks; validates recipient and balance before mutating.
- **History query** (not shown) — `SELECT * FROM transactions WHERE user_id = ? ORDER BY created_at DESC LIMIT ? OFFSET ?`.
- **Bill payment** — similar to transfer but credits a provider settlement account and stores `providerName`.

#### Complexity

| | |
|-|-|
| Time | Top N: O(T + U log U) for T transactions, U distinct users; transfer O(1) DB ops per request |
| Space | Top N: O(U) for count map |

#### Edge cases

- **Tie counts in Top N** — clarify sort order for equal counts (alphabetical by name, or by user id).
- **n larger than user count** — return all users with at least one transaction.
- **Concurrent transfers** — without `FOR UPDATE`, two threads can overdraw; always lock balance rows.
- **Self-transfer** — reject or no-op by policy.
- **Promo over-use** — enforce per-user redemption limit in a transaction when bonus scope is included.

</details>

<details><summary>Bonus Problem</summary>

- **Promo Codes Management**: Admin users can create promo codes in the system, which users can use while paying bills. Each promo code can be used a certain number of times per user, and each promo code has a certain amount of cashback.
- **Promo Codes Analytics**: Admin users can see a list of all promo codes, including the total number of uses, the average number of times utilized per user, and the total amount of cashback disbursed for each promo code. This list should be ordered by the most recent promo code first.
</details>

</article>

## Benefits, Perks and Things to Consider
Optimizely is a certified Great Place to Work. Here are some of the benefits and perks they offer:
- **Flexible Work Arrangements:** Optimizely supports flexible work from home or onsite work arrangements.
- **Parental leave:** Optimizely offers a supportive parental leave for both birthing and non-birthing parents. Duration of leave may vary by local regulations.
- **Meals and Snacks:** Free snacks and drinks are available in the office.

