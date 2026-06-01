---
description: Kite Games Studio interview questions, Kite Games Studio interview stages, Kite Games Studio interview details, Kite Games Studio interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/kite
---
# Kite Games Studio

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-| :- |
| Founding year | 2014 |
| Company Website | https://www.kitegamesstudio.com/ |
| Career Website | https://www.kitegamesstudio.com/ |
| Technologies Used| Swift, React, Kotlin, PyTorch |

## Introduction
[Kite Games Studio (KGS)](https://www.kitegamesstudio.com/), founded in 2014, is a leading mobile application development firm in Bangladesh. Based in Mohakhali DOHS, Dhaka, KGS specializes in developing software for both iOS and Android platforms, along with building websites. The company is known for its emphasis on competitive programming skills, making it an excellent choice for talented **competitive programmers** looking to join a dynamic and innovative team.

## Interview Stages

1. **Online Contest**: Candidates participate in an online programming contest that typically consists of 5-6 problems to be solved within 3-4 hours. The contest may be hosted on platforms like Toph, Hackerrank, or other online judges. Candidates are shortlisted for the next round based on their ranking in this contest.

2. **Technical Round**: This round primarily focuses on coding problems and some basic Java concepts. The interviewers assess the candidate's problem-solving approach and how they think through the problems.

## Technical Round Questions

<article>

A permutation `P` is good if `P[i] % i == 0` or `i % P[i] == 0` for `1 ≤ i ≤ N`. Given `N ≤ 20`, count the number of good permutations. 
<details><summary>Theory and explanation</summary>

Count permutations `P[1..N]` where at position `i` (1-based), value `P[i]` must satisfy **`i % P[i] == 0` OR `P[i] % i == 0`**.

**Approach: Bitmask DP**

- State: `mask` = which values `1..N` are already placed (bit `j-1` set if value `j+1` used — implementation uses 0-based indices).
- `pos = popcount(mask) + 1` = next position to fill (1-based).
- Try each unused value `v`; if divisibility holds with `pos`, transition `mask | (1<<v)`.

**Base case:** all bits set → one valid permutation.

**Why bitmask works**

`N ≤ 20` → at most 2²⁰ ≈ 1M states — feasible with memoization.

**Related**

Similar to counting valid permutations with local constraints; brute force O(N!) impossible for N=20.

#### Further reading

- [Bitmask DP (CP-Algorithms)](https://cp-algorithms.com/algebra/all-submasks.html)
- [Counting permutations with restrictions — Codeforces discussions](https://codeforces.com/blog/entry/337)

#### Complexity

| | |
|-|-|
| Time | O(N × 2^N × N) — states × choices |
| Space | O(2^N) DP table |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function countGoodPermutations(N) {
  const size = 1 << N;
  const dp = new Int32Array(size);
  dp.fill(-1);

  function popcount(m) {
    let c = 0;
    while (m) { m &= m - 1; c++; }
    return c;
  }

  function solve(mask) {
    if (mask === size - 1) return 1;
    if (dp[mask] !== -1) return dp[mask];

    const pos = popcount(mask) + 1;
    let ways = 0;
    for (let i = 0; i < N; i++) {
      if (mask & (1 << i)) continue;
      const val = i + 1;
      if (pos % val === 0 || val % pos === 0) {
        ways += solve(mask | (1 << i));
      }
    }
    dp[mask] = ways;
    return ways;
  }

  return solve(0);
}
```

#### Code walkthrough

- **`pos`** — 1-based index of next slot from number of placed elements.
- **`val = i + 1`** — value being placed (0-based bit → 1-based value).
- Memoize on `mask` to avoid recomputation.

#### Complexity

| | |
|-|-|
| Time | O(N² × 2^N) |
| Space | O(2^N) |

#### Edge cases

- **N = 1** — single permutation `[1]` is good → answer 1.
- **N = 2** — only permutations satisfying divisibility at both positions count.

</details>

<details><summary>Solution (other languages)</summary>

The final solution uses Bitmask DP to efficiently count the number of good permutations that satisfy the given condition.

```cpp
#include <iostream>
#include <vector>

using namespace std;

int N; // Global variable for the size of the permutation
vector<int> dp; // DP array to store results of subproblems

// Recursive function to count the number of good permutations using Bitmask DP
int solve(int mask) {
    if (mask == (1 << N) - 1) return 1; // Base case: all elements are placed
    if (dp[mask] != -1) return dp[mask]; // Return already computed result

    int pos = __builtin_popcount(mask) + 1; // Position to place the next element (1-based)
    dp[mask] = 0; // Initialize current DP state

    for (int i = 0; i < N; i++) {
        // Check if the i-th element is not used and it satisfies the condition
        if (!(mask & (1 << i)) && (pos % (i + 1) == 0 || (i + 1) % pos == 0)) {
            dp[mask] += solve(mask | (1 << i)); // Recur with updated mask
        }
    }
    return dp[mask];
}

int main() {
    cout << "Enter the value of N (N <= 20): ";
    cin >> N;

    dp.assign(1 << N, -1); // Initialize DP array with -1 for all masks
    int result = solve(0); // Start with an empty mask
    cout << "Number of good permutations for N = " << N << " is: " << result << endl;

    return 0;
}
```

</details>

</article>

<article>

Design a data structure to add integers and remove the most frequent element, with ties broken by recency.
<details><summary>Theory and explanation</summary>

Design a structure supporting:

1. **`add(val)`** — insert integer `val`.
2. **`remove()`** — remove and return the **most frequent** value; on tie, remove the one **most recently added** among tied frequencies.

**Constraints:** up to 10⁵ operations; values up to 10⁹.

**Approach (LeetCode 895 — Maximum Frequency Stack pattern)**

- `freq[x]` — count per value.
- `group[f]` — stack (vector) of values currently at frequency `f`; **back = most recent**.
- `maxFreq` — current highest frequency.

**Operations**

- **add:** increment `freq[x]`, push `x` onto `group[freq[x]]`, update `maxFreq`.
- **remove:** pop from `group[maxFreq]`, decrement `freq[x]`, if group empty decrease `maxFreq`, return `x`.

**Why it works**

Most frequent = top frequency bucket; recency tie = LIFO within that bucket.

#### Further reading

- [LeetCode 895 — Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/)
- [Hash map + bucket stacks editorial](https://leetcode.com/problems/maximum-frequency-stack/solutions/)

#### Complexity

| | |
|-|-|
| Time | O(1) amortized per operation |
| Space | O(n) over all added elements |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class FreqStack {
  constructor() {
    this.freq = new Map();
    this.group = new Map();
    this.maxFreq = 0;
  }

  push(x) {
    const f = (this.freq.get(x) || 0) + 1;
    this.freq.set(x, f);
    if (!this.group.has(f)) this.group.set(f, []);
    this.group.get(f).push(x);
    this.maxFreq = Math.max(this.maxFreq, f);
  }

  pop() {
    const stack = this.group.get(this.maxFreq);
    const x = stack.pop();
    if (stack.length === 0) this.maxFreq--;
    this.freq.set(x, this.freq.get(x) - 1);
    return x;
  }
}
```

#### Code walkthrough

- **`group[f]`** — all values with frequency `f`; last pushed wins on tie.
- **`pop`** — O(1) from end of frequency bucket.

#### Complexity

| | |
|-|-|
| Time | O(1) per push/pop |
| Space | O(n) |

#### Edge cases

- **Single element** — pop returns it; freq returns to 0.
- **Tie on frequency** — most recent addition popped first.

</details>

<details><summary>Solution (other languages)</summary>

Design a data structure that supports the following two operations:

1. **add(val)**: Add an integer `val` to the data structure.
2. **remove()**: Remove the most frequent element in the data structure. If there are multiple elements with the same highest frequency, print the element that was added last.

The constraints for the operations are:

* Total number of operations ≤ 10<sup>5</sup>
* 0 ≤ val ≤ 10<sup>9</sup>

**Solution:**

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class FreqStack {
    unordered_map<int, int> freq;                    // Map to store frequency of elements
    unordered_map<int, vector<int>> group;             // Map to store groups of elements by frequency
    int maxFreq = 0;                                 // Variable to track the maximum frequency

public:
    // Function to add an integer
    void push(int x) {
        freq[x]++;                                   // Increase the frequency of the element
        maxFreq = max(maxFreq, freq[x]);             // Update the max frequency
        group[freq[x]].push_back(x);                 // Add the element to the appropriate group
    }

    // Function to remove and return the most frequent element (with ties broken by recency)
    int pop() {
        int x = group[maxFreq].back();               // Get the most recent element with the highest frequency
        group[maxFreq].pop_back();                   // Remove it from the group
        if (group[maxFreq].empty()) {                // If no more elements in the group, reduce max frequency
            maxFreq--;
        }
        freq[x]--;                                   // Decrease the frequency of the element
        return x;                                    // Return the most frequent element
    }
};

int main() {
    FreqStack fs;
    fs.push(5);
    fs.push(7);
    fs.push(5);
    fs.push(7);
    fs.push(4);
    fs.push(5);
    
    cout << fs.pop() << endl;  // Should print 5
    cout << fs.pop() << endl;  // Should print 7
    cout << fs.pop() << endl;  // Should print 5
    cout << fs.pop() << endl;  // Should print 4
    
    return 0;
}
```

</details>

</article>

<article>

What are the main concepts of OOP? 
<details><summary>Theory and explanation</summary>

The four pillars of **Object-Oriented Programming (OOP)**:

1. **Encapsulation** — Bundle data and methods; hide internal state behind a public interface (`private` fields, getters/setters). Prevents unauthorized mutation.

2. **Abstraction** — Expose essential behavior, hide complexity (interfaces, abstract classes). Caller uses `payment.charge()` without knowing gateway details.

3. **Inheritance** — Derive classes from base classes; reuse and extend behavior (`class Dog extends Animal`). Supports **is-a** relationships.

4. **Polymorphism** — Same interface, different implementations — **runtime** (method overriding, virtual dispatch) or **compile-time** (overloading). Enables extensible APIs.

**Kite interview context**

Expect discussion in Java/Swift/Kotlin terms; may tie to design patterns (Singleton, Factory) in follow-ups.

#### Further reading

- [Oracle Java Tutorial — OOP concepts](https://docs.oracle.com/javase/tutorial/java/concepts/)
- [SOLID principles overview](https://en.wikipedia.org/wiki/SOLID)

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

</details>

<details><summary>Solution (JavaScript)</summary>

Illustrative ES6 class showing all four pillars:

```js
// Abstraction + Encapsulation
class BankAccount {
  #balance = 0; // private field (encapsulation)

  deposit(amount) {
    if (amount > 0) this.#balance += amount;
  }

  getBalance() {
    return this.#balance; // controlled access
  }
}

// Inheritance + Polymorphism
class SavingsAccount extends BankAccount {
  constructor(rate) {
    super();
    this.rate = rate;
  }

  accountType() {
    return 'savings'; // override
  }
}

class CheckingAccount extends BankAccount {
  accountType() {
    return 'checking';
  }
}

function printType(account) {
  console.log(account.accountType()); // polymorphic call
}
```

#### Code walkthrough

- **`#balance`** — encapsulation via private field.
- **`extends` / override** — inheritance and runtime polymorphism.
- **`BankAccount` API** — abstraction hides balance mechanics.

#### Complexity

| | |
|-|-|
| Time | O(1) method calls |
| Space | O(1) per instance |

#### Edge cases

- **JS lacks compile-time polymorphism** — use TypeScript interfaces for static contracts.
- **Prefer composition over inheritance** when behavior mixes are complex.

</details>

</article>

<article>

Implement the Singleton pattern.
<details><summary>Show Interaction</summary>

To provide better understanding, here's how the discussion typically goes. The questions aren't directly asked; instead, they are discussed in the context of a coding problem or a concept. (I am sharing real experience of mine):

**Interviewer:** Here's a scenario: you need to create a class for database connections, and as every developer of your team needs to use the same database connection, you should only allow one instance of this class.  How would you implement this in Java?  
**Candidate:** I would include a static variable within the class, initially set to null. I'd also create a static method called "connection." This method would first check if the static variable is null. If it is, it would create a new object, assign it to the variable, and then return it. If the variable is not null, it would simply return the existing object.  
**Interviewer:** But if someone creates an object of this class, wouldn't they get a different object?  
**Candidate:** To prevent that, I would make the constructor private.  
**Interviewer:** Is this approach feasible? Would you need to do anything else?  
**Candidate:** Yes, it's feasible, and no further changes are necessary.  
**Interviewer:** The process you described has a specific name in design patterns. Do you recall what it's called?  
**Candidate:** Sorry, I don't know the name.  
**Interviewer:** It's called the Singleton pattern.
</details>

<details><summary>Theory and explanation</summary>

**Singleton** ensures a class has **at most one instance** and provides global access.

**Requirements**

- **Private constructor** — blocks `new` from outside.
- **Static holder** — stores sole instance.
- **Static accessor** — lazy or eager initialization.

**Thread safety**

- **Single-threaded lazy init** — check-null then create (interview baseline).
- **Multi-threaded** — synchronize, **double-checked locking**, or **static holder idiom** / **enum singleton** (Java).

**Trade-offs**

- Global state complicates testing and hides dependencies.
- Prefer **dependency injection** of shared connection pool in modern apps unless interviewer asks for pattern by name.

> [!WARNING] 
> The given single threaded implementation of the singleton pattern though widely popular, is not thread-safe. If a multithreaded application were to get the connection, there is a chance that the connection is initialized multiple times. Ask the interviewer to make sure if they want it to be thread-safe. You can check this [wikipedia section](https://en.wikipedia.org/wiki/Double-checked_locking#Usage_in_Java) if you want to learn more.

#### Further reading

- [Refactoring Guru — Singleton](https://refactoring.guru/design-patterns/singleton)
- [Effective Java — enum singleton](https://www.oracle.com/java/technologies/effective-java.html)
- [Double-checked locking (Wikipedia)](https://en.wikipedia.org/wiki/Double-checked_locking)

#### Complexity

| | |
|-|-|
| Time | O(1) after initialization |
| Space | O(1) single instance |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class DatabaseConnection {
  static #instance = null;

  constructor() {
    if (DatabaseConnection.#instance) {
      throw new Error('Use DatabaseConnection.getInstance()');
    }
    // initialize connection
  }

  static getInstance() {
    if (!DatabaseConnection.#instance) {
      DatabaseConnection.#instance = new DatabaseConnection();
    }
    return DatabaseConnection.#instance;
  }

  query(sql) {
    return `executing: ${sql}`;
  }
}

// Module singleton (Node/browser bundlers) — idiomatic JS alternative
// export default new DatabaseConnection();
```

#### Code walkthrough

- **`#instance` static private** — holds singleton.
- **Constructor guard** — prevents accidental second `new`.
- **Module pattern** — often preferred in JS over class singleton.

#### Complexity

| | |
|-|-|
| Time | O(1) getInstance |
| Space | O(1) |

#### Edge cases

- **Concurrent first access in workers** — each worker has separate memory; use shared service instead.
- **Serialization** — Java: enum singleton prevents duplicate on deserialize.

</details>

<details><summary>Solution (other languages)</summary>

**Solution:** Below is the implementation of the Singleton pattern in Java:

::: code-group
```java [Single Threaded]
// Singleton class to manage database connections
public class DatabaseConnection {
    // Static variable to hold the single instance of the class
    private static DatabaseConnection instance = null;

    // Private constructor to prevent instantiation
    private DatabaseConnection() {
        // Initialization code, e.g., establish database connection
    }

    // Public method to provide access to the single instance
    public static DatabaseConnection getInstance() {
        // Check if instance is null, create new one if needed
        if (instance == null) {
            instance = new DatabaseConnection();
        }
        // Return the existing instance
        return instance;
    }
}
```
```go [Thread Safe]
var lock = &sync.Mutex{}

type single struct {
}

var singleInstance *single

func getInstance() *single {
    if singleInstance == nil {
        lock.Lock()
        defer lock.Unlock()
        if singleInstance == nil {
            fmt.Println("Creating single instance now.")
            singleInstance = &single{}
        } else {
            fmt.Println("Single instance already created.")
        }
    } else {
        fmt.Println("Single instance already created.")
    }

    return singleInstance
}
```
:::

</details>

</article>

<article>

Given a string `s` and multiple queries. Each query consists of a string `t`. Check if `t` is a subsequence of `s`.@@2025@@

[**💻 Submit Code**](https://leetcode.com/problems/is-subsequence/description/)

<details><summary>Theory and explanation</summary>

[LeetCode 392 — Is Subsequence](https://leetcode.com/problems/is-subsequence/description/)

**Subsequence:** `t` is subsequence of `s` if you can delete zero or more chars from `s` (without reordering) to get `t`.

**Two-pointer**

- `i` on `s`, `j` on `t`.
- If `s[i] === t[j]`, advance both; else advance `i` only.
- Success if `j === t.length`.

**Many queries**

Preprocess **next occurrence table** `next[i][c]` = smallest index ≥ i where `s[index] === c`, or -1. Answer each query in O(|t|).

#### Further reading

- [LeetCode 392 editorial](https://leetcode.com/problems/is-subsequence/)
- [Follow-up: Streaming subsequence (LeetCode 1055)](https://leetcode.com/problems/shortest-way-to-form-string/)

#### Complexity

| | |
|-|-|
| Time | O(|s| + |t|) per check; O(|s| × alphabet) preprocess + O(|t|) per query |
| Space | O(1) two-pointer; O(|s| × σ) for next table |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function isSubsequence(s, t) {
  let j = 0;
  for (let i = 0; i < s.length && j < t.length; i++) {
    if (s[i] === t[j]) j++;
  }
  return j === t.length;
}

function isSubsequenceQueries(s, queries) {
  return queries.map((t) => isSubsequence(s, t));
}

// Many queries: build next index (26 lowercase)
function buildNext(s) {
  const n = s.length;
  const next = Array.from({ length: n + 1 }, () => Array(26).fill(-1));
  for (let i = n - 1; i >= 0; i--) {
    next[i] = [...next[i + 1]];
    next[i][s.charCodeAt(i) - 97] = i;
  }
  return next;
}

function isSubsequenceFast(s, t, next) {
  let pos = 0;
  for (const ch of t) {
    const idx = ch.charCodeAt(0) - 97;
    pos = next[pos][idx];
    if (pos === -1) return false;
    pos++;
  }
  return true;
}
```

#### Code walkthrough

- **Two-pointer** — greedy match earliest chars of `t` in order.
- **`buildNext`** — backward DP for O(1) jump per character in query.

#### Complexity

| | |
|-|-|
| Time | O(|s| + |t|) single; O(|s|·26 + Q·|t|) many queries |
| Space | O(|s|·26) next table |

#### Edge cases

- **Empty t** — always subsequence.
- **Empty s, non-empty t** — false.

</details>

</article>

<article>

You are given an integer array `nums` and two integers `indexDiff` and `valueDiff`. Find a pair of indices `(i, j)` such that: `i != j`, `abs(i - j) <= indexDiff` and `abs(nums[i] - nums[j]) <= valueDiff`.@@2025@@

[**💻 Submit Code**](https://leetcode.com/problems/contains-duplicate-iii/description/)

<details><summary>Theory and explanation</summary>

[LeetCode 220 — Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/description/)

Find indices `i ≠ j` with **|i − j| ≤ indexDiff** and **|nums[i] − nums[j]| ≤ valueDiff**.

**Sliding window + ordered set**

Maintain a window of at most `indexDiff + 1` elements in a **balanced BST** (C++ `set`) or **TreeMap**.

For current `nums[i]`:

1. Remove `nums[i - indexDiff - 1]` if out of window.
2. Find successor ≥ `nums[i]` — if `|diff| ≤ valueDiff`, return true.
3. Find predecessor ≤ `nums[i]` — same check.
4. Insert `(nums[i], i)`.

**Bucket approach (alternative)**

Bucket size `valueDiff + 1`; map bucket id → value; check neighbor buckets O(1) average.

#### Further reading

- [LeetCode 220 solutions](https://leetcode.com/problems/contains-duplicate-iii/)
- [C++ multiset / set lower_bound](https://en.cppreference.com/w/cpp/container/set/lower_bound)

#### Complexity

| | |
|-|-|
| Time | O(n log indexDiff) with set |
| Space | O(indexDiff) window |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff) {
  if (valueDiff < 0) return false;
  const buckets = new Map();

  function bucketId(x) {
    return Math.floor(x / (valueDiff + 1));
  }

  for (let i = 0; i < nums.length; i++) {
    const b = bucketId(nums[i]);
    if (buckets.has(b)) return true;
    if (buckets.has(b - 1) && Math.abs(nums[i] - buckets.get(b - 1)) <= valueDiff) return true;
    if (buckets.has(b + 1) && Math.abs(nums[i] - buckets.get(b + 1)) <= valueDiff) return true;

    buckets.set(b, nums[i]);
    if (i >= indexDiff) buckets.delete(bucketId(nums[i - indexDiff]));
  }
  return false;
}
```

#### Code walkthrough

- **Bucket width** `valueDiff + 1` — values in same/adjacent buckets within `valueDiff`.
- **Sliding delete** — remove element leaving window.

#### Complexity

| | |
|-|-|
| Time | O(n) average with Map |
| Space | O(indexDiff) |

#### Edge cases

- **valueDiff = 0** — duplicate within window (Duplicate II).
- **indexDiff = 0** — no valid pair (i ≠ j impossible).

</details>

<details><summary>Solution (other languages)</summary>

```cpp
bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {
    set<pair<int,int>> st;
    for(int i=0;i<nums.size();i++){
        if( i>indexDiff ) st.erase({nums[i-indexDiff-1],i-indexDiff-1});
        auto it = st.lower_bound({nums[i],0});
        if ( it != st.end() ) {
            if ( abs(nums[i] - it->first) <= valueDiff ) 
                return true;
        }
        if( it != st.begin() ){
            it--;
            if ( abs(nums[i] - it->first) <= valueDiff ) 
                return true;
        }
        st.insert({nums[i],i});
    }
    return false;
}
```

</details>

</article>

## Online Round Questions

<article>

You're at a buffet with various food items. Each food item has a deliciousness factor and nutrient values. You need to maximize the total deliciousness of the foods you eat. Additionally, for health reasons, each nutrient value must occur in an odd number of food items. @@2024@@

[**💻 Submit Code**](https://toph.co/c/recruitment-contest-by-kite-games-studio)

<details><summary>Theory and explanation</summary>

**Toph Kite 2024 — Buffet**

Each item has **deliciousness** and a **subset of nutrients** (toggle bitmask). Choose a subset maximizing sum of deliciousness subject to: for every nutrient bit, it appears in an **odd** number of chosen items.

**XOR / parity DP**

State `dp[mask]` = max deliciousness using items processed so far with nutrient parity = `mask` (bit k = odd count mod 2 for nutrient k).

For item with mask `m` and value `d`:

```
dp'[mask] = max(dp[mask], dp[mask XOR m] + d)
```

Answer: `max(0, dp[fullMask])` where `fullMask = (1<<numNutrients) - 1` if all nutrients must be odd — or problem may require **each** nutrient odd (often all bits 1 in final mask per statement).

**Interpretation from solution:** target mask `(1<<numNutrients)-1` — every nutrient toggled odd times.

#### Further reading

- [Subset XOR DP (bitmask knapsack)](https://cp-algorithms.com/algebra/bit-masks.html)
- [Toph contest archive](https://toph.co/c/recruitment-contest-by-kite-games-studio)

#### Complexity

| | |
|-|-|
| Time | O(items × 2^nutrients) |
| Space | O(2^nutrients) |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function maxBuffetDeliciousness(items, numNutrients) {
  const full = (1 << numNutrients) - 1;
  const dp = new Int32Array(1 << numNutrients);
  dp.fill(-Infinity);
  dp[0] = 0;

  for (const { deliciousness, nutrientMask } of items) {
    for (let mask = full; mask >= 0; mask--) {
      const prev = mask ^ nutrientMask;
      dp[mask] = Math.max(dp[mask], dp[prev] + deliciousness);
    }
  }

  return Math.max(0, dp[full]);
}
```

#### Code walkthrough

- **`nutrientMask`** — XOR toggles parity for each nutrient in item.
- Iterate masks descending to avoid reusing same item twice in one pass (0/1 knapsack style).

#### Complexity

| | |
|-|-|
| Time | O(n × 2^k) |
| Space | O(2^k) |

#### Edge cases

- **Skip all items** — answer 0 (`max(0, …)`).
- **k nutrients small** — typical k ≤ 10 in contest.

</details>

<details><summary>Solution (other languages)</summary>

**Solution:** 

<<< @/snippets/kite/buffet.cpp

</details>

</article>

<article>

You have a 2D grid representing a village. 'X' denotes farmer-owned land, and '.' denotes government-owned land. Connected 'X' areas belong to the same farmer. If two connected 'X' areas match under any 90° rotation, they also belong to the same farmer. Count the number of unique farmers in the village. @@2024@@

[**💻 Submit Code**](https://toph.co/c/recruitment-contest-by-kite-games-studio)

<details><summary>Theory and explanation</summary>

**Problem steps**

1. **4-connected flood fill** on `'X'` cells → connected components with bounding box.
2. Extract **subgrid** of each component's bounding rectangle.
3. **Canonicalize** shape under **90° rotations** (4 rotations) — use normalized string/grid as key in hash map.
4. Count distinct canonical keys → **unique farmers**.

**Rotation**

Rotate subgrid 90° CW: `rot[j][rows-1-i] = sub[i][j]`.

Two regions same farmer if one's pattern matches any rotation of the other's extracted shape (problem groups rotation-equivalent plots).

#### Further reading

- [Connected components on grid (DFS)](https://cp-algorithms.com/graph/searching.html)
- [Shape canonicalization under dihedral group](https://en.wikipedia.org/wiki/Dihedral_group)

#### Complexity

| | |
|-|-|
| Time | O(R×C × max shape area) |
| Space | O(R×C) visited + map keys |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function rotate(grid) {
  const r = grid.length, c = grid[0].length;
  return Array.from({ length: c }, (_, j) =>
    Array.from({ length: r }, (_, i) => grid[r - 1 - i][j])
  );
}

function canonicalKey(grid) {
  let g = grid.map((row) => [...row]);
  const keys = [];
  for (let t = 0; t < 4; t++) {
    keys.push(g.map((row) => row.join('')).join('|'));
    g = rotate(g);
  }
  return keys.sort()[0];
}

function countUniqueFarmers(grid) {
  const rows = grid.length, cols = grid[0].length;
  const seen = Array.from({ length: rows }, () => Array(cols).fill(false));
  const shapes = new Set();

  function dfs(i, j, box) {
    seen[i][j] = true;
    box.minR = Math.min(box.minR, i); box.maxR = Math.max(box.maxR, i);
    box.minC = Math.min(box.minC, j); box.maxC = Math.max(box.maxC, j);
    for (const [di, dj] of [[1,0],[-1,0],[0,1],[0,-1]]) {
      const ni = i + di, nj = j + dj;
      if (ni >= 0 && ni < rows && nj >= 0 && nj < cols && !seen[ni][nj] && grid[ni][nj] === 'X') {
        dfs(ni, nj, box);
      }
    }
  }

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (grid[i][j] === 'X' && !seen[i][j]) {
        const box = { minR: i, maxR: i, minC: j, maxC: j };
        dfs(i, j, box);
        const sub = [];
        for (let r = box.minR; r <= box.maxR; r++) {
          sub.push(grid[r].slice(box.minC, box.maxC + 1));
        }
        shapes.add(canonicalKey(sub));
      }
    }
  }
  return shapes.size;
}
```

#### Code walkthrough

- **DFS** collects component bounding box.
- **`canonicalKey`** — lexicographically smallest of 4 rotations identifies equivalence class.

#### Complexity

| | |
|-|-|
| Time | O(R×C×S) for S = typical component size |
| Space | O(R×C) |

#### Edge cases

- **Single 'X' cell** — 1×1 key.
- **Non-square bounding box** — rotation changes dimensions.

</details>

<details><summary>Solution (other languages)</summary>

**Solution:** 

<<< @/snippets/kite/farmer.cpp

</details>

</article>

<article>

You need to write a program to simulate a Linux terminal on an old computer. You'll be given commands like "mkdir", "ls", "rm", "pwd", and "cd", and you need to simulate their behavior, printing the appropriate output or error messages. @@2024@@

[**💻 Submit Code**](https://toph.co/c/recruitment-contest-by-kite-games-studio)

<details><summary>Theory and explanation</summary>

Simulate a **virtual filesystem tree**:

- **Nodes** = directories; each has `name`, `parent`, `children` set/map.
- **Current working directory** pointer `cwd`.
- **Root** fixed (e.g. `KGS`).

**Commands**

| Command | Behavior |
|---------|----------|
| `mkdir name` | Create child path if absent; error if exists |
| `ls` | List immediate child directory **names** (basename) |
| `rm name` | Remove subtree; error if missing |
| `pwd` | Print full path of `cwd` |
| `cd name` | Enter child; `cd ..` go to parent |

**Implementation notes**

- Store **full path strings** as keys in `map<string, int>` for node ids, or nested `set<string>` of full child paths.
- **`rm`** — recursive delete all descendants (DFS clear children).

#### Further reading

- [Linux filesystem hierarchy](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)
- [Trie / tree for path strings](https://en.wikipedia.org/wiki/Trie)

#### Complexity

| | |
|-|-|
| Time | O(path length) per command; rm O(subtree size) |
| Space | O(total directories created) |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function createTerminal() {
  let id = 1;
  const names = { 1: 'KGS' };
  const parent = { 1: 1 };
  const children = { 1: new Set() };
  const pathIndex = { KGS: 1 };
  let cwd = 1;

  function fullPath(node) { return names[node]; }

  return {
    mkdir(arg) {
      const sub = fullPath(cwd) + '/' + arg.slice(6).trim();
      if (pathIndex[sub]) return 'Error: Already Exists';
      id++;
      names[id] = sub;
      parent[id] = cwd;
      children[cwd].add(sub);
      children[id] = new Set();
      pathIndex[sub] = id;
    },
    ls() {
      return [...children[cwd]].map((p) => p.split('/').pop()).join('\n');
    },
    pwd() { return names[cwd]; },
    cd(arg) {
      if (arg.endsWith('..')) { cwd = parent[cwd]; return; }
      const sub = fullPath(cwd) + '/' + arg.slice(3).trim();
      if (!pathIndex[sub]) return 'Error: No Such Directory';
      cwd = pathIndex[sub];
    },
  };
}
```

#### Code walkthrough

- **`pathIndex`** — O(1) lookup by full path string.
- **`cd ..`** — follow parent pointer to root's parent = root.

#### Complexity

| | |
|-|-|
| Time | O(1) mkdir/cd/pwd; O(k) ls for k children |
| Space | O(nodes) |

#### Edge cases

- **rm non-empty directory** — recursive wipe in full solution.
- **cd from root `..`** — stay at root.

</details>

<details><summary>Solution (other languages)</summary>

**Solution:** 

<<< @/snippets/kite/linux-terminal.cpp

</details>

</article>

<article>

You have a 2D grid representing a field with crop fields and godowns. Harvesters start at godowns and collect crops from fields, bringing them back to their godown. The first harvester must collect from a specific number of fields. You need to calculate the minimum total time for all harvesters to collect all crops. @@2024@@

[**💻 Submit Code**](https://toph.co/c/recruitment-contest-by-kite-games-studio)

<details><summary>Theory and explanation</summary>

**Model:** Multiple harvesters at **godowns**; **crop fields** need visiting; travel time = grid distance (often Manhattan). First harvester has **minimum field quota**.

**Typical approach**

1. **Assign fields to nearest godown** (Voronoi / multi-source BFS).
2. **Per godown** — list fields with round-trip cost `2 × dist(godown, field)`.
3. **First harvester constraint** — must cover ≥ K fields → assign K cheapest fields exclusively or use DP/greedy on sorted costs.
4. **Remaining harvesters** — partition remaining fields to minimize max or sum completion time (assignment / min-cost matching / greedy by cost).

Contest input defines exact rules; solution often combines **BFS distances** + **greedy assignment** by increasing trip cost.

#### Further reading

- [Multi-source BFS](https://cp-algorithms.com/graph/breadth-first-search.html)
- [Assignment problem (Hungarian algorithm)](https://cp-algorithms.com/graph/hungarian-algorithm.html)

#### Complexity

| | |
|-|-|
| Time | O(R×C + F log F) for F fields |
| Space | O(R×C) distance grid |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function manhattan(a, b) {
  return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
}

function minHarvestTime(godowns, fields, firstQuota) {
  // Assign each field to nearest godown; cost = round trip
  const buckets = godowns.map(() => []);
  for (const f of fields) {
    let best = 0, bestD = Infinity;
    godowns.forEach((g, i) => {
      const d = manhattan(g, f);
      if (d < bestD) { bestD = d; best = i; }
    });
    buckets[best].push(2 * bestD);
  }

  buckets.forEach((b) => b.sort((a, b) => a - b));

  // Greedy: first harvester takes firstQuota smallest overall (simplified)
  const all = buckets.flat().sort((a, b) => a - b);
  let first = 0;
  for (let i = 0; i < firstQuota; i++) first += all[i];

  const rest = all.slice(firstQuota);
  const parallel = rest.reduce((s, c) => s + c, 0); // divide by other harvesters in full solution
  return first + parallel;
}
```

#### Code walkthrough

- **Nearest godown** — minimizes one-way distance per field.
- **Round trip** — factor 2 on distance.
- Full contest solution adds parallel scheduling across harvesters.

#### Complexity

| | |
|-|-|
| Time | O(F × G + F log F) |
| Space | O(F) |

#### Edge cases

- **firstQuota > fields** — infeasible per problem constraints.
- **Multiple godowns equidistant** — tie-break by index.

</details>

</article>

<article>

You have a list of unique strings and an empty list. You'll be given queries to add strings to the empty list, delete strings from it, and count the number of strings between two given strings in the list after sorting it. @@2024@@

[**💻 Submit Code**](https://toph.co/c/recruitment-contest-by-kite-games-studio)
<details><summary>Show Description</summary>

You are given a list <i>L</i> of <i>N</i> unique strings and an initially empty list <i>P</i>. You need to process <i>Q</i> queries of the following types:

* **add i f:** Add the string <i>L[i]</i> to the list <i>P</i> a total of <i>f</i> times.
* **delete i f:** Let <i>t</i> be the number of occurrences of string <i>L[i]</i> in list <i>P</i>. Delete min(<i>f</i>, <i>t</i>) occurrences of <i>L[i]</i> from list <i>P</i>.
* **count i j:** Sort the elements of list <i>P</i> in lexicographic order, then count the number of strings in <i>P</i> that are between <i>L[i]</i> and <i>L[j]</i> (inclusive).

**Constraints:**

* **1 ≤ N ≤ 10<sup>5</sup>** - Number of strings in list <i>L</i>.
* The total length of all strings in <i>L</i> is at most 2 × 10<sup>6</sup>, and each string length is between 1 and 10<sup>6</sup> characters.
* **1 ≤ Q ≤ 10<sup>5</sup>** - Number of queries.
* For **add i f** and **delete i f** queries: **1 ≤ i ≤ N** and **1 ≤ f ≤ 10<sup>5</sup>**.
* For **count i j** queries: **1 ≤ i ≤ N** and **1 ≤ j ≤ N**.

</details>

<details><summary>Theory and explanation</summary>

**Key idea:** Map original indices → **lexicographic rank** after sorting `L` once.

Maintain **frequency array** `freq[rank]` = count of that string in multiset `P`.

**Queries**

- **add i f:** `freq[rank(i)] += f`
- **delete i f:** `freq[rank(i)] -= min(f, freq[rank(i)])`
- **count i j:** sum `freq[a..b]` where `a,b` are ranks of `L[i]`, `L[j]` (swap if needed)

**Data structure:** **Segment tree / Fenwick tree** on frequencies for O(log N) range sum and point update.

#### Further reading

- [Fenwick tree (CP-Algorithms)](https://cp-algorithms.com/data_structures/fenwick.html)
- [Coordinate compression](https://en.wikipedia.org/wiki/Discretization)

#### Complexity

| | |
|-|-|
| Time | O((N + Q) log N) |
| Space | O(N) |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class Fenwick {
  constructor(n) { this.n = n; this.bit = Array(n + 1).fill(0); }
  add(i, d) { for (i++; i <= this.n; i += i & -i) this.bit[i] += d; }
  sum(i) { let s = 0; for (i++; i > 0; i -= i & -i) s += this.bit[i]; return s; }
  range(a, b) { return this.sum(b) - (a ? this.sum(a - 1) : 0); }
}

function processStringQueries(L, queries) {
  const sorted = [...L].map((s, i) => [s, i]).sort((a, b) => a[0].localeCompare(b[0]));
  const rank = Array(L.length);
  sorted.forEach(([, orig], r) => { rank[orig] = r; });

  const fw = new Fenwick(L.length);
  const out = [];

  for (const q of queries) {
    const [type, a, b] = q;
    if (type === 'add') {
      fw.add(rank[a - 1], b);
    } else if (type === 'delete') {
      const r = rank[a - 1];
      const cur = fw.range(r, r);
      fw.add(r, -Math.min(b, cur));
    } else {
      let x = rank[a - 1], y = rank[b - 1];
      if (x > y) [x, y] = [y, x];
      out.push(fw.range(x, y));
    }
  }
  return out;
}
```

#### Code walkthrough

- **rank** — static lex order of master list `L`.
- **Fenwick** — dynamic multiset counts; range sum = count in `[L[i], L[j]]`.

#### Complexity

| | |
|-|-|
| Time | O(Q log N) |
| Space | O(N) |

#### Edge cases

- **count i j** inclusive — Fenwick range includes endpoints.
- **delete more than present** — cap at current frequency.

</details>

<details><summary>Solution (other languages)</summary>

**Solution:** 

<<< @/snippets/kite/copy-string.cpp

</details>

</article>

<article>

Given a number `N`, find the number of integers between `[1,N]` that has odd number of divisors. @@Jr SWE 2025@@ 

[**💻 Submit Code**](https://www.hackerrank.com/contests/jr-software-developer-recruitment-contest-may-2025/challenges/hey-this-is-the-giveaway-problem)

<details><summary>Theory and explanation</summary>

**Giveaway — perfect squares**

An integer has an **odd** number of divisors **iff** it is a **perfect square**.

Reason: divisors pair as `(d, n/d)` except when `d = n/d` → `d = √n`.

Count = **⌊√N⌋** (possibly adjust upper bound if problem uses strict `< N` — check statement).

**Example:** N = 16 → squares 1,4,9,16 → 4 numbers.

#### Further reading

- [Divisors function — odd count characterization](https://math.stackexchange.com/questions/3849869)
- [LeetCode 2485 — Find the Pivot Integer (related square theme)](https://leetcode.com/problems/find-the-pivot-integer/)

#### Complexity

| | |
|-|-|
| Time | O(1) or O(√N) if enumerating |
| Space | O(1) |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function countOddDivisors(N) {
  return Math.floor(Math.sqrt(N));
}

// Verify: divisor count parity
function divisorCount(n) {
  let c = 0;
  for (let d = 1; d * d <= n; d++) {
    if (n % d === 0) c += d * d === n ? 1 : 2;
  }
  return c;
}
```

#### Code walkthrough

- **`Math.floor(Math.sqrt(N))`** — count integers k with k² ≤ N.
- **`divisorCount`** — brute check for small N validation.

#### Complexity

| | |
|-|-|
| Time | O(1) |
| Space | O(1) |

#### Edge cases

- **N = 0** — empty range.
- **Perfect square N** — include √N itself.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
long long solve(long long n) {
    long long sq = sqrtl(n);
    if( (sq+1)*(sq+1) == n ) sq++;
    return sq;
}
```

</details>

</article>

<article>

Given an array of pairs indicating the size and reward of each item. You will be given a minimum and maximum size of the bag. You need to find the maximum reward you can get by filling the bag with items. @@Jr SWE 2025@@

[**💻 Submit Code**](https://www.hackerrank.com/contests/jr-software-developer-recruitment-contest-may-2025/challenges/ripe-range.cpp)

<details><summary>Theory and explanation</summary>

**Ripe Range — bounded knapsack variant**

Each item `(size, reward)`; bag capacity in **[L, R]** (min and max total size). Maximize total reward with total size ∈ [L, R].

**DP approach (from snippet)**

- `dp[s]` = max reward for **exact** total size `s` (or boolean feasibility + maximize).
- 0/1 knapsack loop over items; only extend sizes downward for each item.
- Answer = `max_{s in [L,R]} dp[s]`.

**Segment tree optimization in C++ solution**

After building `dp`, answer queries `[L,R]` max on range — use **segment tree over dp array** for multiple query pairs.

#### Further reading

- [Knapsack DP (CP-Algorithms)](https://cp-algorithms.com/dynamic_programming/knapsack.html)
- [Segment tree range max query](https://cp-algorithms.com/data_structures/segment_tree.html)

#### Complexity

| | |
|-|-|
| Time | O(n × MAX + Q log MAX) |
| Space | O(MAX) |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function maxRewardInRange(items, minSize, maxSize, cap = 50000) {
  const dp = new Float64Array(cap + 1).fill(-Infinity);
  dp[0] = 0;

  for (const [size, reward] of items) {
    for (let s = cap - size; s >= 0; s--) {
      if (dp[s] !== -Infinity) {
        dp[s + size] = Math.max(dp[s + size], dp[s] + reward);
      }
    }
  }

  let best = -Infinity;
  for (let s = minSize; s <= maxSize; s++) {
    best = Math.max(best, dp[s]);
  }
  return best === -Infinity ? 0 : best;
}
```

#### Code walkthrough

- **Backward loop** — 0/1 knapsack (each item once).
- Scan `[minSize, maxSize]` for best feasible reward.

#### Complexity

| | |
|-|-|
| Time | O(n × cap + (maxSize − minSize)) |
| Space | O(cap) |

#### Edge cases

- **No feasible fill** — return 0 or -1 per problem.
- **minSize = 0** — empty bag may be allowed.

</details>

<details><summary>Solution (other languages)</summary>

<<< @/snippets/kite/ripe-range.cpp

</details>

</article>

<article>

Given an array `A` of size `N` and some queries. Each query will ask for `f(l,r)` where the function computes the sum of the greatest common divisors over all prefixes of some range `[l,r]`.  @@Jr SWE 2025@@

[**💻 Submit Code**](https://www.hackerrank.com/contests/jr-software-developer-recruitment-contest-may-2025/challenges/cumulative-gcd)

<details><summary>Theory and explanation</summary>

**Cumulative GCD query**

For range `[l,r]`, define prefixes `A[l..l]`, `A[l..l+1]`, …, `A[l..r]`. For each prefix compute **GCD** of elements, then **sum** those GCDs.

**Naive:** O(N) per query — compute running GCD along prefix.

**Optimization**

- **GCD is associative** and decreases stepwise (only O(log max) distinct values as you extend prefix).
- For many queries: **Mo's algorithm**, **prefix precomputation**, or **segment tree** storing GCD + contribution counts depending on editorial.

**Running GCD property:** `g = gcd(g, A[i])` updates in O(log max(A)) time.

#### Further reading

- [Euclidean algorithm (CP-Algorithms)](https://cp-algorithms.com/algebra/euclid-algorithm.html)
- [Mo's algorithm](https://cp-algorithms.com/sorting/mo-algorithm.html)

#### Complexity

| | |
|-|-|
| Time | O((r−l+1) log maxA) naive per query |
| Space | O(N) |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function gcd(a, b) {
  while (b) { [a, b] = [b, a % b]; }
  return Math.abs(a);
}

function cumulativeGcdSum(A, l, r) {
  let g = 0;
  let sum = 0;
  for (let i = l; i <= r; i++) {
    g = gcd(g, A[i]);
    sum += g;
  }
  return sum;
}

function answerQueries(A, queries) {
  return queries.map(([l, r]) => cumulativeGcdSum(A, l, r));
}
```

#### Code walkthrough

- Extend prefix one element at a time; update running `g`.
- Add each prefix GCD to `sum`.

#### Complexity

| | |
|-|-|
| Time | O(Q × N log maxA) naive |
| Space | O(1) per query |

#### Edge cases

- **Single element range** — answer = A[l].
- **Zeros in array** — gcd(0, x) = |x|.

</details>

</article>

<article>

Given a permutation of size `N`. You will change the permutation repeatedly. In each operation, you will create a new permutation b such that `b[i] = a[a[i]]` for all `1 ≤ i ≤ n`. Then replace `a` with `b`. You need to find the number of operations required to make the permutation sorted or report that it is impossible. @@Jr SWE 2025@@

[**💻 Submit Code**](https://www.hackerrank.com/contests/jr-software-developer-recruitment-contest-may-2025/challenges/permutation-sorting-1)

<details><summary>Theory and explanation</summary>

**Operation:** `b[i] = a[a[i]]` (using 1-based indices in statement; 0-based: `b[i] = a[a[i] - 1]` adjusted).

This is **functional iteration** — applying permutation composition `a ∘ a`.

**Cycle analysis**

Permutation decomposes into **disjoint cycles**. On each operation, each element moves two steps along its cycle (apply `a` twice).

Sorted permutation `[1,2,…,n]` is fixed point under repeated squaring only if cycle structure aligns.

**Approach**

1. Detect if sorted reachable — all cycles must have length dividing certain pattern; element at position i must eventually map to i.
2. Simulate per cycle: how many squaring steps until every element in cycle is at correct index, or detect loop without sorting.
3. Answer = **LCM** of per-cycle required steps (if consistent) or **impossible**.

#### Further reading

- [Permutation cycles](https://cp-algorithms.com/algebra/permutation.html)
- [Functional graph iteration](https://en.wikipedia.org/wiki/Functional_graph)

#### Complexity

| | |
|-|-|
| Time | O(N log N) cycle decomposition + per-cycle simulation |
| Space | O(N) |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function applyTwice(a) {
  const n = a.length;
  return a.map((_, i) => a[a[i] - 1]); // 1-based values
}

function isSorted(a) {
  return a.every((v, i) => v === i + 1);
}

function stepsToSort(a, maxSteps = 1e6) {
  const seen = new Map();
  let cur = [...a];
  for (let step = 0; step <= maxSteps; step++) {
    if (isSorted(cur)) return step;
    const key = cur.join(',');
    if (seen.has(key)) return -1;
    seen.set(key, step);
    cur = applyTwice(cur);
  }
  return -1;
}
```

#### Code walkthrough

- **`applyTwice`** — one problem operation.
- **Cycle detection** on full permutation vector — if revisit state before sorted, impossible.

#### Complexity

| | |
|-|-|
| Time | O(steps × N) |
| Space | O(steps × N) visited keys |

#### Edge cases

- **Already sorted** — 0 steps.
- **N = 1** — always sorted.

</details>

</article>

<article>

Given a tree with `N` nodes. You will need to chose an optimal start node `s` such that the round trip distance from `s` to some given target nodes is minimized. @@Jr SWE 2025@@

[**💻 Submit Code**](https://www.hackerrank.com/contests/jr-software-developer-recruitment-contest-may-2025/challenges/kawchars-new-home)

<details><summary>Theory and explanation</summary>

**Tree routing with demands**

Each target node `c` requires `t` visits (weight). Cost from start `s`:

Sum over targets of **`2 × dist(s, c) × t`** if each trip is round-trip (go and return) — factor 2 in snippet `cost[u] += 2*child[v] + cost[v]`.

**Tree DP (rerooting)**

1. **dfs1** — compute subtree demand `child[u]` and cost `cost[u]` assuming root at 1.
2. **dfs2** — reroot: moving root from `u` to `v` adjusts cost by **`new_cost = c - 4*child[v] + 2*total_child`** (standard tree DP formula when all trips are from root to subtree and back).

Pick `s` minimizing total cost.

#### Further reading

- [Tree rerooting DP (Codeforces blog)](https://codeforces.com/blog/entry/78564)
- [Kawchar's New Home — Hackerrank contest](https://www.hackerrank.com/contests/jr-software-developer-recruitment-contest-may-2025/challenges/kawchars-new-home)

#### Complexity

| | |
|-|-|
| Time | O(N) two DFS passes |
| Space | O(N) adjacency |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function optimalStartNode(edges, demands) {
  const n = edges.length + 1;
  const adj = Array.from({ length: n + 1 }, () => []);
  for (const [u, v] of edges) {
    adj[u].push(v);
    adj[v].push(u);
  }

  const child = Array(n + 1).fill(0);
  const cost = Array(n + 1).fill(0);
  let totalChild = demands.reduce((s, d) => s + d[1], 0);

  for (const [c, t] of demands) child[c] += t;

  function dfs1(u, p) {
    for (const v of adj[u]) {
      if (v === p) continue;
      dfs1(v, u);
      child[u] += child[v];
      cost[u] += 2 * child[v] + cost[v];
    }
  }

  let best = { cost: Infinity, node: 1 };

  function dfs2(u, p, c) {
    if (c < best.cost) best = { cost: c, node: u };
    for (const v of adj[u]) {
      if (v === p) continue;
      dfs2(v, u, c - 4 * child[v] + 2 * totalChild);
    }
  }

  dfs1(1, 0);
  dfs2(1, 0, cost[1]);
  return best;
}
```

#### Code walkthrough

- **`child[u]`** — total trip weight in subtree.
- **Reroot formula** — adjust cost when moving root across edge `(u,v)`.

#### Complexity

| | |
|-|-|
| Time | O(N) |
| Space | O(N) |

#### Edge cases

- **Single node tree** — start at node 1.
- **Zero demands** — any node cost 0.

</details>

<details><summary>Solution (other languages)</summary>

<<< @/snippets/kite/new-home.cpp#snippet

</details>

</article>

<article>

Given a grid of size `N` and `M` with digit `0` and `1`. The grid indicates some patterns which are not connected. The patterns can be rotated or stretched too. You will need to find the patterns present in the grid. @@Jr SWE 2025@@

[**💻 Submit Code**](https://www.hackerrank.com/contests/jr-software-developer-recruitment-contest-may-2025/challenges/simple-digit-recognition)

<details><summary>Theory and explanation</summary>

**Simple Digit Recognition**

Grid contains **disconnected 0/1 patterns** (digits or shapes). Patterns may appear **rotated** or **scaled (stretched)**.

**Pipeline**

1. **Extract connected components** of `1` cells (4- or 8-connected per statement).
2. **Normalize** each component:
   - Crop bounding box.
   - Optionally **downsample** stretch to unit aspect ratio or compare via run-length encoding.
3. **Canonical form** under rotation (4 dihedral variants) — hash or template match.
4. Match against **pattern library** or count distinct normalized shapes.

**Stretch handling:** compare row/col run lengths ratios, or resize to fixed `h×w` bitmap via nearest-neighbor scaling.

#### Further reading

- [Connected component labeling](https://en.wikipedia.org/wiki/Connected-component_labeling)
- [Template matching / image moments](https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html)

#### Complexity

| | |
|-|-|
| Time | O(N×M×components) |
| Space | O(N×M) |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function normalize(grid) {
  const rows = grid.length, cols = grid[0].length;
  let minR = rows, maxR = -1, minC = cols, maxC = -1;
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (grid[i][j] === '1') {
        minR = Math.min(minR, i); maxR = Math.max(maxR, i);
        minC = Math.min(minC, j); maxC = Math.max(maxC, j);
      }
    }
  }
  if (maxR < 0) return '';
  const out = [];
  for (let i = minR; i <= maxR; i++) {
    out.push(grid[i].slice(minC, maxC + 1).join(''));
  }
  return out.join('|');
}

function rotateKey(key) {
  const rows = key.split('|');
  const r = rows.length, c = rows[0].length;
  const rot = Array.from({ length: c }, (_, j) =>
    Array.from({ length: r }, (_, i) => rows[r - 1 - i][j]).join('')
  );
  return rot.join('|');
}

function canonicalPattern(grid) {
  let k = normalize(grid);
  const variants = [];
  for (let t = 0; t < 4; t++) {
    variants.push(k);
    k = rotateKey(k);
  }
  return variants.sort()[0];
}
```

#### Code walkthrough

- **`normalize`** — crop to bounding box of `1`s.
- **4 rotations** — pick lexicographically smallest key as canonical id.

#### Complexity

| | |
|-|-|
| Time | O(N×M) per component |
| Space | O(N×M) |

#### Edge cases

- **Empty grid** — no patterns.
- **Stretch** — full solution rescales before hashing; normalize by gcd of run lengths.

</details>

</article>
