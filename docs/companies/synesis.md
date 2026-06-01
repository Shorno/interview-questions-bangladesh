---
description: Synesis IT interview questions, Synesis IT interview stages, Synesis IT interview details, Synesis IT interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/synesis
---
# Synesis IT

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-| :- |
| Founding year | |
| Company Website | https://synesisit.com.bd/ |
| Career Website | https://synesisit.com.bd/career/ |
| Technologies Used|  |

## Introduction
Synesis takes a on campus written test first. The questions contain some coding problem, Database, writting sql, OOP etc
The second stage is face to face interview

## On Campus Written Test

<article>

Given a list of courses you have to take and a list of prerequisites, return the order in which you have to take the courses. If it is not possible to take all the courses return an empty list.

[**💻 Submit Code**](https://leetcode.com/problems/course-schedule-ii)

<details><summary>Theory and explanation</summary>

[Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) is a **topological ordering** problem. Courses are nodes; each prerequisite `[a, b]` means you must take `b` before `a`, so draw a directed edge `b → a`.

**Goal**

Produce any valid linear order of all `numCourses` nodes, or `[]` if a **cycle** exists (impossible schedule).

**Approach 1: Kahn's algorithm (BFS)**

1. Build adjacency list and **in-degree** count per node.
2. Enqueue all nodes with in-degree 0 (no prerequisites).
3. Repeatedly dequeue a course, append to order, decrement in-degree of neighbors; enqueue neighbors that reach 0.
4. If final order length `< numCourses`, a cycle exists → return `[]`.

**Approach 2: DFS with three colors**

- `0` unvisited, `1` visiting (on recursion stack), `2` finished.
- On DFS, if you reach a `1` node, cycle detected.
- Append node to order **after** visiting all descendants, then reverse (post-order).

**Interview talking points**

- Same graph as [Course Schedule I](https://leetcode.com/problems/course-schedule/) but you must output the order, not just feasibility.
- Multiple valid orderings may exist; any one is accepted.
- Time is O(V + E) for V courses and E prerequisites.

#### Further reading

- [LeetCode: Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) — problem statement and examples
- [GeeksforGeeks: Topological sorting](https://www.geeksforgeeks.org/topological-sorting/) — Kahn's and DFS methods
- [CP-Algorithms: Topological sort](https://cp-algorithms.com/graph/topological-sort.html) — cycle detection details
- [Khan Academy: Topological ordering](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/topological-sorting) — intuitive introduction

#### Complexity

| | |
|-|-|
| Time | O(V + E) |
| Space | O(V + E) for graph storage; O(V) for queue/stack |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
function findOrder(numCourses, prerequisites) {
  const graph = Array.from({ length: numCourses }, () => []);
  const indegree = Array(numCourses).fill(0);

  for (const [course, prereq] of prerequisites) {
    graph[prereq].push(course);
    indegree[course]++;
  }

  const queue = [];
  for (let i = 0; i < numCourses; i++) {
    if (indegree[i] === 0) queue.push(i);
  }

  const order = [];
  while (queue.length) {
    const u = queue.shift();
    order.push(u);
    for (const v of graph[u]) {
      indegree[v]--;
      if (indegree[v] === 0) queue.push(v);
    }
  }

  return order.length === numCourses ? order : [];
}
```

#### Code walkthrough

- **Build graph** — For `[a, b]`, add edge `b → a` and increment `indegree[a]`.
- **Seed queue** — Courses with no prerequisites start the order.
- **Process** — Each removal frees dependents; when a node's in-degree hits 0, it becomes available.
- **Cycle check** — If not all courses were processed, some nodes sit in a cycle → return `[]`.

#### Complexity

| | |
|-|-|
| Time | O(V + E) |
| Space | O(V + E) |

#### Edge cases

- **No prerequisites** — any order of `0..numCourses-1` works; Kahn's order depends on queue order.
- **Single course** — return `[0]`.
- **Cycle** — e.g. `0→1→0` → return `[]`.
- **Duplicate prerequisite entries** — build graph carefully or dedupe to avoid inflating in-degree.

</details>

<details><summary>Solution (other languages)</summary>

```C++
class Solution {
public:
    vector<int> order;
    vector<int> graph[2005];
    int color[2005] = {0};

    bool dfs(int u){
        color[u] = 1;
        for(auto v : graph[u]){
            if( color[v] == 1 ) return false;
            if( color[v] == 2 ) continue;
            bool possible = dfs(v);
            if( !possible ) return false;
        }
        color[u] = 2;
        order.push_back(u);
        return true;
    }

    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        for(auto prerequisite : prerequisites){
            graph[prerequisite[1]].push_back(prerequisite[0]);
        }
        for(int i = 0; i < numCourses; i++){
            if( color[i] == 0 ) {
                bool possible = dfs(i);
                if( !possible ) return vector<int>{};
            }
        }
        reverse(order.begin(), order.end());
        return order;
    }
};
```

</details>
</article>

<article>

Given an integer array of size n, find all elements that appear more than `⌊n/3⌋` times.

[**💻 Submit Code**](https://leetcode.com/problems/majority-element-ii)

<details><summary>Theory and explanation</summary>

[Majority Element II](https://leetcode.com/problems/majority-element-ii/) asks for every value that appears **strictly more than** `⌊n/3⌋` times. At most **two** such elements can exist in any array (pigeonhole principle: if three values each exceeded n/3, counts would sum to more than n).

**Approach 1: Boyer–Moore voting (O(n) time, O(1) space)**

Generalized from the n/2 majority problem:

1. Maintain up to two **candidate** values and their vote counts.
2. Scan the array: if current value matches a candidate, increment; else if an empty candidate slot exists, assign; else decrement both counts (cancel triple).
3. **Verification pass** — Count occurrences of each candidate; keep those with count `> n/3`.

**Approach 2: Sort (O(n log n))**

Sort and sweep to count runs of equal values; push run leader if run length `> n/3`. Simple but slower.

**Approach 3: Hash map (O(n) time, O(n) space)**

Count frequencies; filter keys above threshold.

**Interview talking points**

- Explain why at most two answers exist before coding.
- Boyer–Moore for n/3 requires a **second verification pass** (unlike n/2 where one candidate is guaranteed if majority exists).
- Synesis onsite tests often accept sort-based solutions; mention optimal O(n) voting for bonus points.

#### Further reading

- [LeetCode: Majority Element II](https://leetcode.com/problems/majority-element-ii/) — official problem
- [LeetCode: Majority Element](https://leetcode.com/problems/majority-element/) — simpler n/2 variant
- [GeeksforGeeks: Boyer-Moore Majority Vote](https://www.geeksforgeeks.org/boyer-moore-majority-voting-algorithm/) — voting intuition
- [Wikipedia: Boyer–Moore majority vote algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm) — proof sketch

#### Complexity

| | |
|-|-|
| Time | O(n) with Boyer–Moore + verification; O(n log n) with sort |
| Space | O(1) extra with voting; O(n) with hash map |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
/**
 * @param {number[]} nums
 * @return {number[]}
 */
function majorityElement(nums) {
  let cand1 = null;
  let cand2 = null;
  let count1 = 0;
  let count2 = 0;

  for (const x of nums) {
    if (x === cand1) {
      count1++;
    } else if (x === cand2) {
      count2++;
    } else if (count1 === 0) {
      cand1 = x;
      count1 = 1;
    } else if (count2 === 0) {
      cand2 = x;
      count2 = 1;
    } else {
      count1--;
      count2--;
    }
  }

  count1 = 0;
  count2 = 0;
  for (const x of nums) {
    if (x === cand1) count1++;
    else if (x === cand2) count2++;
  }

  const threshold = Math.floor(nums.length / 3);
  const result = [];
  if (count1 > threshold) result.push(cand1);
  if (count2 > threshold && cand2 !== cand1) result.push(cand2);
  return result;
}
```

#### Code walkthrough

- **Phase 1** — Track two candidates; unmatched elements "cancel" one vote from each candidate (generalized pairing for n/3).
- **Phase 2** — Re-count frequencies of candidates only; strict inequality `> ⌊n/3⌋` decides inclusion.
- **Duplicate candidates** — Guard with `cand2 !== cand1` when both slots collapse to the same value.

#### Complexity

| | |
|-|-|
| Time | O(n) — two linear passes |
| Space | O(1) — only candidate counters |

#### Edge cases

- **Empty array** — return `[]`.
- **Length 1 or 2** — single element always exceeds n/3 when n ≤ 2? For n=1, threshold 0, any element qualifies.
- **No element exceeds n/3** — verification pass returns `[]`.
- **Negative numbers** — algorithm works unchanged.

</details>

<details><summary>Solution (other languages)</summary>

```C++
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<int> majors;
        int count = 1;

        for(int i = 1; i < nums.size(); i++){
            if( nums[i] != nums[i-1] ){
                if( count > nums.size()/3 ) majors.push_back(nums[i-1]);
                count = 0;
            }
            count++;
        }

        if( count > nums.size()/3 ) majors.push_back(nums.back());
        return majors;
    }
};
```

</details>
</article>

<article>

Given string num representing a non-negative integer `num`, and an integer `k`, return the smallest possible integer after removing `k` digits from num.

[**💻 Submit Code**](https://leetcode.com/problems/remove-k-digits)

<details><summary>Theory and explanation</summary>

[Remove K Digits](https://leetcode.com/problems/remove-k-digits/) asks for the **lexicographically smallest** number obtainable after deleting exactly `k` digits without reordering remaining digits.

**Greedy + monotonic stack**

To minimize the result, build the answer left to right and prefer **smaller leading digits**:

1. Use a stack (or string builder) representing the chosen digits so far.
2. For each new digit `d`, while `k > 0`, the stack is non-empty, and **top > d**, pop the top (remove a larger earlier digit) and decrement `k`.
3. Push `d`.
4. If `k` remains after the scan, remove `k` digits from the **end** (they are the largest remaining in a non-decreasing tail).
5. Strip **leading zeros**; if empty, return `"0"`.

**Why it works**

Removing a digit at position `i` is only beneficial if a smaller digit appears later — popping while `top > current` implements that exchange. The stack stays **non-decreasing**, giving the smallest possible prefix at each step.

**Interview talking points**

- Same pattern as [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) and [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/) — monotonic stack family.
- String can be long; O(n) single pass is expected.
- Leading-zero handling is a common implementation bug.

#### Further reading

- [LeetCode: Remove K Digits](https://leetcode.com/problems/remove-k-digits/) — examples and constraints
- [GeeksforGeeks: Build lowest number by removing n digits](https://www.geeksforgeeks.org/build-lowest-number-by-removing-n-digits-from-a-given-number/) — stack explanation
- [Monotonic stack guide (LeetCode Discuss)](https://leetcode.com/discuss/general-discussion/1062398/Monotonic-Stack-Summary-and-Questions) — pattern collection
- [Stack Overflow: Greedy digit removal](https://stackoverflow.com/questions/16269623/greedy-algorithm-for-building-smallest-number) — intuition threads

#### Complexity

| | |
|-|-|
| Time | O(n) — each digit pushed and popped at most once |
| Space | O(n) — stack stores up to n digits |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
/**
 * @param {string} num
 * @param {number} k
 * @return {string}
 */
function removeKdigits(num, k) {
  const stack = [];

  for (const ch of num) {
    while (k > 0 && stack.length && stack[stack.length - 1] > ch) {
      stack.pop();
      k--;
    }
    stack.push(ch);
  }

  while (k > 0 && stack.length) {
    stack.pop();
    k--;
  }

  let result = stack.join('').replace(/^0+/, '');
  return result.length ? result : '0';
}
```

#### Code walkthrough

- **Main loop** — Before appending `ch`, drop stack tops that are larger while removals remain — each pop makes the prefix smaller.
- **Tail trim** — Remaining `k` deletes the rightmost digits (largest in the monotone suffix).
- **Normalize** — Remove leading zeros; empty string becomes `"0"`.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(n) |

#### Edge cases

- **`k = 0`** — return `num` without leading-zero strip unless input has them (problem usually allows strip).
- **`k >= num.length`** — result is `"0"`.
- **All identical digits** `"1111", k=2` — remove from end → `"11"`.
- **Leading zeros after removal** — `"10200", k=1` → `"200"` not `"0200"`.

</details>

<details><summary>Solution (other languages)</summary>

```C++
class Solution {
public:
    string removeKdigits(string num, int k) {
       
        string newNum = "";
        // remove digits that are greater than the next digit
        for(int i=0;i<num.size();i++){
            while( k and newNum.size() and newNum.back() > num[i] ){
                k--;
                newNum.pop_back();
            }
            newNum += num[i];
        }
        // remove leading zeros
        reverse(newNum.begin(),newNum.end());
        while( newNum.size() and newNum.back() == '0' ) newNum.pop_back();
        reverse(newNum.begin(),newNum.end());
        // remove remaining k digits if any
        while(k and newNum.size()) {
            newNum.pop_back();
            k--;
        }
        // if newNum is empty, return 0
        if( newNum.size() == 0 ) newNum = "0";
        return newNum;
    }
};

```

</details>
</article>

## Behavioral Questions
<article>

How would you manage your team if some teammate doesn't cooperate or doesn't contribute?

<details><summary>Theory and explanation</summary>

This is a **behavioral leadership** question. Interviewers want evidence you can handle conflict, accountability, and team outcomes without escalating unnecessarily or ignoring the problem.

**Framework: STAR method**

Structure your answer with **Situation**, **Task**, **Action**, **Result**:

1. **Situation** — Brief context: team size, deadline pressure, what "not cooperating" looked like (missed standups, blocked PRs, silent in planning).
2. **Task** — Your responsibility as peer lead, scrum master, or senior engineer: deliver the sprint, keep morale, unblock dependencies.
3. **Action** — Concrete steps you took (see below).
4. **Result** — Measurable outcome: feature shipped, conflict reduced, person improved or escalated appropriately.

**Recommended actions (pick 2–3 you actually used)**

1. **Private 1:1 first** — Assume good intent; ask about blockers (personal, technical, unclear requirements). Many "uncooperative" behaviors come from confusion or overload.
2. **Clarify expectations** — Restate goals, Definition of Done, and how their work ties to team success. Document agreements in writing (ticket, email summary).
3. **Adjust workload or pairing** — Offer pairing, smaller scoped tasks, or mentorship if skill gap is the issue.
4. **Make impact visible** — Use standups and boards so contribution (or lack thereof) is transparent to the team without public shaming.
5. **Escalate when needed** — If behavior persists after direct feedback, involve manager/HR with facts (dates, missed deliverables), not personality labels.
6. **Protect the team** — Reassign critical path work if deadlines are at risk; do not let one member block everyone silently.

**What to avoid**

- Badmouthing the teammate in the interview.
- Saying you would "just do their work" indefinitely without addressing root cause.
- Jumping to HR on day one without a direct conversation.

**Synesis context**

Onsite and face-to-face rounds often probe **soft skills** alongside DSA. Tie your answer to Bangladesh workplace norms: respect hierarchy when escalating, but lead with empathy and clarity first.

#### Further reading

- [MIT Career Advising: STAR method](https://capd.mit.edu/resources/the-star-method-for-behavioral-interviews/) — structuring behavioral answers
- [Harvard Business Review: Difficult conversations](https://hbr.org/2016/06/difficult-conversations-9-common-mistakes) — common escalation mistakes
- [Atlassian: Team health checks](https://www.atlassian.com/team-playbook/health-monitor) — spotting collaboration issues early
- [Google re:Work — Managers](https://rework.withgoogle.com/subjects/managers/) — research-backed people leadership practices

#### Complexity

| | |
|-|-|
| Time | N/A (behavioral) |
| Space | N/A (behavioral) |

</details>

<details><summary>Solution (JavaScript)</summary>

Use this as a **response outline** (not executable code). Fill in your real example before the interview.

```js
const starResponse = {
  situation:
    'Our four-person squad had a release in two weeks; one member stopped joining standups and missed two API integrations.',
  task:
    'As the senior on the feature, I needed the endpoints merged without burning out the rest of the team.',
  action: [
    'Scheduled a private 30-minute 1:1 to ask about blockers — learned they were stuck on an unclear schema from another team.',
    'Paired for one afternoon, split their ticket into two smaller PRs, and posted a written summary of ownership in Slack.',
    'Set a check-in two days later; when the first PR still slipped, I reassigned the critical path item and informed our manager with dates and impact.',
  ],
  result:
    'We shipped on time; the teammate delivered the smaller PRs the following sprint and later thanked me for the direct conversation instead of public call-outs.',
};

// Interview tip: keep total spoken answer to ~90 seconds unless asked to elaborate.
function summarize({ situation, task, action, result }) {
  return [situation, task, action.join(' '), result].join(' ');
}
```

#### Code walkthrough

- **`starResponse`** — Template fields interviewers expect; replace every line with your authentic story.
- **`action` array** — Shows a progression: empathy → clarity → escalation, which demonstrates maturity.
- **`summarize`** — Practice compressing the story so you do not ramble under time pressure.

#### Complexity

| | |
|-|-|
| Time | N/A (communication skill) |
| Space | N/A |

#### Edge cases

- **Teammate had a personal emergency** — Explain how you covered short term and involved manager for support, not punishment.
- **You were not the lead** — Describe how you raised concern to the lead with specific examples.
- **Behavior was toxic (harassment)** — Skip extended 1:1; document and escalate immediately through proper channels.

</details>

</article>
