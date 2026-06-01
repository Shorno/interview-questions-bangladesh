---
description: Chaldal interview questions, Chaldal interview stages, Chaldal interview details, Chaldal interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/chaldal
---
# Chaldal

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-| :- |
| Founding year | 2013 |
| Company Website | https://chaldal.com/ |
| Career Website | https://chaldal.tech/ |
| Technologies Used| .NET, F#, C#, SQL Server, TypeScript, JavaScript, Xamarin, Android, React, React Native, Microsoft Orleans |

## Introduction

Chaldal.com, founded in 2013, is a grocery e-commerce platform in Bangladesh. They maintain the whole system by themselves. So, they are a tech company too and arguably one the most prestigious tech company in bangaldesh

## Interview Stages

Chaldal interview process has 3 stage

1. **Apltitude Test:** Basic reasoning, vocabulary, maths etc
2. **First round Interview:** There will be 2 seperate interview. The questions asked depend on the interviewer. They may be coding or technical or both. Two yes will lead to next round. 1 yes and 1 no gives you a third chance.
3. **CTO round:** It is kind of a behavioural round. But the questions can be coding or technical.

## First round Interview Questions

<article>

Tell me about yourself? Why do you want to join chaldal

<details><summary>Theory and explanation</summary>

**Behavioral opener** — Chaldal uses this to assess communication and motivation for a **product + engineering** company (grocery logistics, not generic outsourcing).

**Structure (60–90 seconds)**

1. **Who you are** — education, core skills (.NET, mobile, algorithms — match their stack).
2. **Highlight** — one project with impact (scale, users, performance).
3. **Why Chaldal** — full-stack ownership, F#/Orleans, real operations (warehouse, delivery), prestige in BD tech.
4. **Close** — what you want to contribute in year one.

**Avoid**

- Generic "I want to learn" without specifics.
- Ignoring the logistics/e-commerce domain.

#### Further reading

- [Chaldal Tech](https://chaldal.tech/) — engineering blog and culture
- [Harvard Business Review: Self-intro in interviews](https://hbr.org/2014/10/how-to-succeed-at-the-interview) — concise pitch
- [The Muse: Why this company answers](https://www.themuse.com/advice/why-do-you-want-to-work-here-interview-question-answer-examples) — tailoring motivation

</details>

<details><summary>Solution (JavaScript)</summary>

N/A — spoken answer outline:

```
Background → relevant project → why Chaldal (tech ownership + impact on millions of orders) → growth goal
```

#### Complexity

N/A (behavioral)

</details>
</article>

<article>

You have been provided a spiral matrix of size NXN along with a coordinate (x, y) as follows. Find the element at the position (x, y) of the matrix.
N = 4, x = 2, y =1

<table >
<tbody>
  <tr><td>1</td><td>2</td><td>3</td><td>4</td></tr>
  <tr><td>12</td><td>13</td><td>14</td> <td>5</td></tr>
  <tr> <td>11</td> <td>16</td><td>15</td><td>6</td></tr>
  <tr><td>10</td> <td>9</td><td>8</td><td>7</td></tr>
</tbody>
</table>

<details><summary>Theory and explanation</summary>

**Spiral matrix** fills 1…N² clockwise from top-left. Given **1-based** `(x, y)` from problem (row 2, col 1 → value **12**), find element without building full matrix.

**Approaches**

1. **Simulate layers** — peel onion rings; determine which layer `(x,y)` belongs to and position on that ring's perimeter.
2. **Generate until coordinate** — O(n²) unacceptable for large n.
3. **Math on layer** — compute side lengths and offset along spiral path.

**Layer idea**

- Outer layer side = n; next n−2, etc.
- Map (row,col) to segment: top, right, bottom, left of current layer.

**Interview talking points**

- Clarify 0-based vs 1-based indexing — hint says (2,1) → 12 with 1-based rows/cols.
- Chaldal may ask O(1) or O(n) without full matrix allocation.

#### Further reading

- [LeetCode 54: Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) — generation
- [LeetCode 885: Spiral Matrix III](https://leetcode.com/problems/spiral-matrix-iii/) — coordinate walk
- [GeeksforGeeks: Spiral matrix](https://www.geeksforgeeks.org/spiral-matrix/) — layer simulation

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function spiralValue(n, row, col) {
  // 1-based row, col → convert to 0-based
  let r = row - 1, c = col - 1;
  let top = 0, left = 0, bottom = n - 1, right = n - 1;
  let val = 1;

  while (top <= bottom && left <= right) {
    for (let j = left; j <= right; j++) if (top === r && j === c) return val; else val++;
    top++;
    for (let i = top; i <= bottom; i++) if (i === r && right === c) return val; else val++;
    right--;
    if (top <= bottom) {
      for (let j = right; j >= left; j--) if (bottom === r && j === c) return val; else val++;
      bottom--;
    }
    if (left <= right) {
      for (let i = bottom; i >= top; i--) if (i === r && left === c) return val; else val++;
      left++;
    }
  }
  return -1;
}

spiralValue(4, 2, 1); // 12
```

#### Code walkthrough

1. Walk spiral same as generation; increment counter.
2. When current cell matches target coordinates, return counter.

#### Complexity

| | |
|-|-|
| Time | O(n²) worst case; O(n) if direct layer formula used |
| Space | O(1) |

#### Edge cases

- **n = 1** — only cell value 1.
- **Corner cells** — belong to correct segment of layer.

</details>
</article>

<article>

Given a number in roman format. Convert it to arabic numeral.

<details><summary>Theory and explanation</summary>

**Roman to integer** — read left to right; if current value < next, subtract current (e.g. IV = 4), else add.

**Mapping**: I=1, V=5, X=10, L=50, C=100, D=500, M=1000.

**Subtract pairs**: IV, IX, XL, XC, CD, CM.

**Interview talking points**

- Validate input or assume well-formed per problem.
- Reverse problem (int to Roman) uses greedy buckets.

#### Further reading

- [LeetCode 13: Roman to Integer](https://leetcode.com/problems/roman-to-integer/) — exact problem
- [LeetCode 12: Integer to Roman](https://leetcode.com/problems/integer-to-roman/) — inverse
- [GeeksforGeeks: Roman to decimal](https://www.geeksforgeeks.org/roman-numerals-to-decimal/) — walkthrough

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function romanToInt(s) {
  const map = { I:1, V:5, X:10, L:50, C:100, D:500, M:1000 };
  let val = 0;
  for (let i = 0; i < s.length; i++) {
    const cur = map[s[i]], next = map[s[i + 1]] || 0;
    val += cur < next ? -cur : cur;
  }
  return val;
}
```

#### Code walkthrough

- Compare each symbol with next; subtract if smaller (subtractive notation).

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases

- **Single char** — direct map.
- **Invalid roman** — problem may guarantee validity.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
map<char,int>RtoA;
void preprocess(){
    // Map of romans to Arabic
    RtoA['I'] = 1;      RtoA['V'] = 5;
    RtoA['X'] = 10;     RtoA['L'] = 50;
    RtoA['C'] = 100;    RtoA['D'] = 500;
    RtoA['M'] = 1000;
}

// Roman numerals to Arabic
int RomanToArabic(string R){
    int value = 0;
    int n = R.size();
    for(int i=0;i<n;i++){
        if( R[i+1] && RtoA[ R[i] ] < RtoA[ R[i+1] ] ){
            value+= RtoA[ R[i+1] ] - RtoA[ R[i] ];
            i++;
        } else{
            value+=RtoA[ R[i] ];
        }
    }
    return value;
}
```

</details>
</article>

<article>

Given a string of characters. Reverse the string without using any library function.

<details><summary>Theory and explanation</summary>

Reverse in-place by swapping symmetric pairs `(i, n−1−i)` for `i` from `0` to `⌊n/2⌋−1`.

No built-in `reverse()` — manual swap only.

#### Further reading

- [LeetCode 344: Reverse String](https://leetcode.com/problems/reverse-string/) — two-pointer
- [GeeksforGeeks: Reverse a string](https://www.geeksforgeeks.org/reverse-string-in-java/) — iterative swap

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function reverseInPlace(s) {
  const arr = [...s]; // strings immutable in JS — use array of chars
  let i = 0, j = arr.length - 1;
  while (i < j) {
    [arr[i], arr[j]] = [arr[j], arr[i]];
    i++; j--;
  }
  return arr.join('');
}
```

#### Code walkthrough

- Two pointers swap from both ends toward center.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(n) for char array in JS |

#### Edge cases

- **Empty / single char** — unchanged.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
void solve(string &s){

    int n = s.size();

    for(int i=0;i<n/2;i++){

        char temp = s[i];
        s[i] = s[n-i-1];
        s[n-i-1] = temp;
    }
}
```

</details>
</article>

<article>

Given a string of characters. Check if the given string is a palindrome.

<details><summary>Theory and explanation</summary>

**Palindrome** — reads same forward and backward. Compare mirrored indices or reverse half and compare.

Ignore case/spaces only if problem says so — default is exact match.

#### Further reading

- [LeetCode 125: Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) — alphanumeric filter variant
- [GeeksforGeeks: Check palindrome string](https://www.geeksforgeeks.org/check-string-palindrome-string/) — two-pointer

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function isPalindrome(s) {
  let i = 0, j = s.length - 1;
  while (i < j) {
    if (s[i] !== s[j]) return false;
    i++; j--;
  }
  return true;
}
```

#### Code walkthrough

- Compare symmetric chars until pointers meet.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases

- **Empty string** — palindrome.
- **Odd length** — middle char ignored by loop.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
bool solve(string s){
    int n = s.size();
    for(int i=0;i<n/2;i++){
        if(s[i] != s[n-i-1]) return false;
    }
    return true;
}
```

</details>
</article>

<article>

Given an positive integer n. Find the sum of even fibonacchi number upto nth term.

[**💻 Submit Code**](https://supecoder.dev/questions/Sum%20of%20Even%20Fibonacci%20Numbers?questionId=66a6015c5cbe5326054ebf70)

<details><summary>Theory and explanation</summary>

Fibonacci with F(1)=1, F(2)=1. Sum **even** Fibonacci terms among first **n** terms (not F(n) itself unless even).

Every 3rd Fibonacci is even: F(3k) even. Can also iterate and accumulate when term % 2 === 0.

**Interview talking points**

- Clarify "nth term" means count of terms, not index value.
- F(1), F(2) are odd → sum may start at 0 for n < 3.

#### Further reading

- [LeetCode 509: Fibonacci](https://leetcode.com/problems/fibonacci-number/) — base sequence
- [Project Euler 2: Even Fibonacci sum](https://projecteuler.net/problem=2) — classic variant
- [GeeksforGeeks: Sum of even Fibonacci](https://www.geeksforgeeks.org/sum-of-even-fibonacci-numbers/) — approaches

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function sumEvenFib(n) {
  if (n < 3) return 0;
  let sum = 0, a = 1, b = 1;
  for (let i = 3; i <= n; i++) {
    const c = a + b;
    a = b;
    b = c;
    if (b % 2 === 0) sum += b;
  }
  return sum;
}
```

#### Code walkthrough

1. Generate terms from 3 to n.
2. Add to sum when current term is even.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases

- **n = 1 or 2** — no even terms in first two → 0.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
long long solve(int n){
    if(n == 1 or n == 2) return 0;
    long long sum = 0, first = 1, second = 1;
    for(int fib=2;fib<n;fib++){
        long long temp = first;
        first = second;
        second = temp + second;
        if(second % 2 == 0) sum += second;
    }
    return sum;
}
```

</details>
</article>

<article>

Given a string of characters [0-9]. Convert it to integer.

[**💻 Submit Code**](https://supecoder.dev/questions/Convert%20String%20to%20Integer?questionId=66a8cba05cbe532605568a68)

<details><summary>Theory and explanation</summary>

**String to integer** — horner-style: `res = res * 10 + (s[i] - '0')`.

Handle sign, overflow, leading zeros per problem constraints — Chaldal version often assumes non-negative digits only.

#### Further reading

- [LeetCode 8: String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) — full atoi rules
- [MDN: parseInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt) — built-in (may be disallowed in interview)

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function stringToInteger(s) {
  let res = 0;
  for (const ch of s) {
    res = res * 10 + (ch.charCodeAt(0) - 48);
  }
  return res;
}
```

#### Code walkthrough

- Shift accumulated value left decimal place; add digit value.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases

- **Empty string** — 0 or error.
- **Overflow** — use BigInt or clamp for LeetCode atoi.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
long long stringToInteger(string &s) {
    int n = s.size();
    long long res = 0;
    for(int i=0;i<n;i++){
        res = (res*10) + (s[i] - '0');
    }
    return res;
}
```

</details>
</article>

<article>

Given an array of integers. Generate all possible permutation of the given array.

[**💻 Submit Code**](https://leetcode.com/problems/permutations/)

<details><summary>Theory and explanation</summary>

**Permutations** — all orderings; backtracking with used-mark or swap-based in-place.

**Backtrack template**

1. Choose unused element, append to path.
2. Recurse with remaining count − 1.
3. Undo choice.

**Complexity** — n! permutations; O(n · n!) output size.

#### Further reading

- [LeetCode 46: Permutations](https://leetcode.com/problems/permutations/) — problem
- [CP-Algorithms: Generating permutations](https://cp-algorithms.com/combinatorics/generating_combinations.html) — methods
- [NeetCode: Permutations](https://neetcode.io/problems/permutations) — video

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function permute(nums) {
  const res = [];
  const path = [];
  const used = new Array(nums.length).fill(false);

  function backtrack() {
    if (path.length === nums.length) {
      res.push([...path]);
      return;
    }
    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;
      used[i] = true;
      path.push(nums[i]);
      backtrack();
      path.pop();
      used[i] = false;
    }
  }
  backtrack();
  return res;
}
```

#### Code walkthrough

1. Track `used` to avoid reusing same index.
2. Complete path → copy to result.
3. Backtrack by unmarking and popping.

#### Complexity

| | |
|-|-|
| Time | O(n · n!) |
| Space | O(n) recursion + output |

#### Edge cases

- **Duplicates** — use LeetCode 47 approach (sort + skip same level).
- **Single element** — one permutation.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
class Solution {
public:
    vector<vector<int>> perms;
    
    void backtrack(vector<int>& nums, vector<int> &perm, int rem){
        if( rem == 0 ){
            perms.push_back(perm);
            return;
        }
        for(int i=0;i<nums.size();i++){
            if( nums[i] == 69 ) continue;
            perm.push_back(nums[i]);
            nums[i] = 69;
            backtrack(nums,perm,rem-1);
            nums[i] = perm.back();
            perm.pop_back();
        }
    }

    vector<vector<int>> permute(vector<int>& nums){
        vector<int> perm;
        backtrack(nums,perm,nums.size());
        return perms;
    }
};
```

</details>
</article>

<article>

Given an array of integers. Generate all possible subset of the given array.

[**💻 Submit Code**](https://leetcode.com/problems/subsets/)

<details><summary>Theory and explanation</summary>

**Power set** — 2^n subsets. **Backtracking**: at each index, include element or skip.

Alternatively bitmask 0…2^n−1.

#### Further reading

- [LeetCode 78: Subsets](https://leetcode.com/problems/subsets/) — problem
- [LeetCode 90: Subsets II](https://leetcode.com/problems/subsets-ii/) — with duplicates
- [GeeksforGeeks: Power set](https://www.geeksforgeeks.org/power-set/) — bitmask method

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function subsets(nums) {
  const res = [];
  const path = [];
  function dfs(i) {
    if (i === nums.length) {
      res.push([...path]);
      return;
    }
    path.push(nums[i]);
    dfs(i + 1);
    path.pop();
    dfs(i + 1);
  }
  dfs(0);
  return res;
}
```

#### Code walkthrough

- At index i: branch take nums[i] or skip; leaf records subset.

#### Complexity

| | |
|-|-|
| Time | O(n · 2^n) |
| Space | O(n) stack |

#### Edge cases

- **Empty array** — `[[]]`.
- **Duplicates** — sort and skip duplicates at same depth.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
class Solution {
public:
    vector<vector<int>> subs;
    vector<int> sub;

    void backtrack(vector<int>& nums, int index){
        if( index == nums.size() ){
            subs.push_back(sub);
            return;
        }
        // take the current value
        sub.push_back(nums[index]);
        backtrack(nums,index+1);
        sub.pop_back();
        // don't take the current value
        backtrack(nums,index+1);
    }

    vector<vector<int>> subsets(vector<int>& nums){
        backtrack(nums,0);
        return subs;
    }
};
```

</details>
</article>

<article>

Given a regex expression and a string. Check if the regex expression matches with the string.

<details><summary>Theory and explanation</summary>

General **regex matching** is complex (NFA/DFA). Interview may mean simplified patterns: `.`, `*`, `?`, or full LeetCode 10 (`.` and `*` only).

**LeetCode 10 DP**

`dp[i][j]` — does `s[0..i)` match `p[0..j)`.

- `*` — zero or more of preceding element.
- `.` — any single char.

**Interview talking points**

- Clarify which regex flavor (PCRE vs simplified).
- For production, use engine library; interview tests DP understanding.

#### Further reading

- [LeetCode 10: Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) — `.` and `*`
- [LeetCode 44: Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) — `?` and `*`
- [Russ Cox: Regex NFA](https://swtch.com/~rsc/regexp/regexp1.html) — how engines work

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function isMatch(s, p) {
  const m = p.length, n = s.length;
  const dp = Array.from({ length: n + 1 }, () => Array(m + 1).fill(false));
  dp[0][0] = true;

  for (let j = 2; j <= m; j += 2) {
    if (p[j - 1] === '*') dp[0][j] = dp[0][j - 2];
  }

  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= m; j++) {
      if (p[j - 1] === '*') {
        dp[i][j] = dp[i][j - 2];
        if (p[j - 2] === '.' || p[j - 2] === s[i - 1])
          dp[i][j] ||= dp[i - 1][j];
      } else if (p[j - 1] === '.' || p[j - 1] === s[i - 1]) {
        dp[i][j] = dp[i - 1][j - 1];
      }
    }
  }
  return dp[n][m];
}
```

#### Code walkthrough

1. Base: empty matches empty; handle leading `a*`, `.*` patterns.
2. `*` branch: skip pair or use star if char matches.

#### Complexity

| | |
|-|-|
| Time | O(n · m) |
| Space | O(n · m) |

#### Edge cases

- **Empty pattern** — only matches empty string.
- **`a*`** matches zero a's.

</details>
</article>

<article>

Each student is assigned to an assignment at a particular location at a specific time. Are there any inconsistencies in the assignments ? Find at least one of them by looking into the input. Then write a code to print all inconsistencies in the assignments. 

<details><summary>Theory and explanation</summary>

**Scheduling conflict detection** — same student assigned to **multiple locations at the same time** is inconsistent.

**Model**

- Key: `(studentId, timeSlot)`.
- Value: list of areas/locations.
- If any key maps to >1 distinct assignment → conflict.

**Chaldal angle** — resembles warehouse shift or delivery slot double-booking validation.

#### Further reading

- [GeeksforGeeks: Hashing](https://www.geeksforgeeks.org/hashing-data-structure/) — grouping by composite key
- [LeetCode 219: Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) — overlap detection pattern

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function findConflicts(assignments) {
  const map = new Map();
  for (const { Area, Time, StudentIds } of assignments) {
    for (const id of StudentIds) {
      const key = `${id}|${Time}`;
      if (!map.has(key)) map.set(key, []);
      map.get(key).push(Area);
    }
  }
  const conflicts = [];
  for (const [key, areas] of map) {
    if (areas.length > 1) {
      const [studentId, time] = key.split('|');
      conflicts.push({ studentId: Number(studentId), time, areas });
    }
  }
  return conflicts;
}
```

#### Code walkthrough

1. Group areas by `(studentId, time)`.
2. Emit entries with more than one area.

#### Complexity

| | |
|-|-|
| Time | O(S) where S = total student slots across assignments |
| Space | O(S) |

#### Edge cases

- **Same area listed twice** — may or may not be conflict; dedupe if needed.
- **No conflicts** — empty output.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Assignment {
    string Area, Time;
    vector<int> StudentIds;
};

vector<Assignment> getInput() {
    vector<Assignment> res = {
        {"Garden", "A", {2, 9, 1}},
        {"Pond", "M", {2, 8, 5}},
        {"FoodCourt", "A", {4, 8, 7}},
        {"Playground", "M", {1, 7, 2}},
        {"PicnicArea", "M", {7, 3, 9}},
        {"Zoo", "A", {6, 3, 2}},
    };
    return res;
}

int main() {
    vector<Assignment> inputs = getInput();

    map< pair<int, string>, vector<string> > mapping;
    for (Assignment a : inputs) {
        for (auto studentId : a.StudentIds)
            mapping[{studentId, a.Time}].push_back(a.Area);
    }

    for (auto k: mapping) {
        if (k.second.size() > 1) {
            cout << "Student " << k.first.first << " has conflicts at time " << k.first.second << " at : " << endl;

            for (string area : k.second) {
                cout << area << " ";
            }
            cout << endl;
        }
    }
}
```

</details>
</article>

<article>

Implement Game of Life

<details><summary>Show Description</summary>

```
__________________

|██ 
|  ██ ██
|██ ██ 
|
|
|
|
|
```
In the game of life, you have a 2D matrix of small squares that can be either alive or dead. The matrix goes through iterations, and on every iteration the squares can die or be revived. This is based on the previous iteration and the below rules
- A living square with 1 or less neighbors in the previous iteration will die, as if from loneliness
- A living square with 2 or 3 neighbors in the previous iteration will survive, as if from contentment
- A living square with 4 or more neighbors in the previous iteration will die, as if from overpopulation
- A dead square with exactly 3 neighbors in the previous iteration will be revived, as if by unfulfilled desires

Implement a square matrix of size 20 and set up the initial five (given) living squares. Then run 10 iterations on it, then print the final matrix. 0,0 should be the top left of the matrix, where the first is the row and the second is the column.
```
matrix size = 20
iterations = 10
initial squares =
[0][0]
[1][1]
```
</details>

<details><summary>Theory and explanation</summary>

**Conway's Game of Life** — cellular automaton on 2D grid.

**Rules (8 neighbors)**

| Current | Neighbors | Next |
|---------|-----------|------|
| Alive | < 2 | Dead (underpopulation) |
| Alive | 2 or 3 | Alive |
| Alive | > 3 | Dead (overpopulation) |
| Dead | 3 | Alive (reproduction) |

**Implementation**

- Count neighbors with 8 directions; apply rules simultaneously.
- Use **double buffer** (`next` grid) to avoid in-place race.

#### Further reading

- [LeetCode 289: Game of Life](https://leetcode.com/problems/game-of-life/) — in-place tricks
- [ConwayLife.com](https://conwaylife.com/) — patterns and rules
- [Wikipedia: Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) — history

</details>

<details><summary>Solution (JavaScript)</summary>

```js
const MSZ = 20;
const DX = [-1,-1,-1,0,0,1,1,1];
const DY = [-1,0,1,-1,1,-1,0,1];

function gameOfLife(initial, generations = 10) {
  let grid = Array.from({ length: MSZ }, () => Array(MSZ).fill(false));
  for (const [r, c] of initial) grid[r][c] = true;

  for (let gen = 0; gen < generations; gen++) {
    const next = Array.from({ length: MSZ }, () => Array(MSZ).fill(false));
    for (let i = 0; i < MSZ; i++) {
      for (let j = 0; j < MSZ; j++) {
        let n = 0;
        for (let k = 0; k < 8; k++) {
          const ni = i + DX[k], nj = j + DY[k];
          if (ni >= 0 && ni < MSZ && nj >= 0 && nj < MSZ && grid[ni][nj]) n++;
        }
        if (grid[i][j]) next[i][j] = n === 2 || n === 3;
        else next[i][j] = n === 3;
      }
    }
    grid = next;
  }
  return grid;
}
```

#### Code walkthrough

1. Initialize grid from seed cells.
2. Each generation: count 8-neighbors, apply rules into `next`.
3. Swap grids.

#### Complexity

| | |
|-|-|
| Time | O(generations · rows · cols · 8) |
| Space | O(rows · cols) |

#### Edge cases

- **Border cells** — fewer neighbors; bounds check required.
- **Stable patterns** — may converge early.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
#include <bits/stdc++.h>

using namespace std;

vector<vector<bool>> matrix(msz, vector<bool>(msz, false));

vector<int> dx = {-1, -1, -1, 0, 0, 1, 1, 1};
vector<int> dy = {-1, 0, 1, -1, 1, -1, 0, 1};

signed main() {
    matrix[0][0] = true;
    matrix[1][1] = true;
    matrix[1][2] = true;
    matrix[2][0] = true;
    matrix[2][1] = true;

    for (int gen = 1; gen <= max_iters; gen++) {
        vector<vector<bool>> next_gen_mat(msz, vector<bool>(msz, false));

        for (int i=0; i<msz; i++) {
            for (int j=0; j<msz; j++) {
                int alive_neighbors = 0;

                for (int k=0; k<8; k++)  {
                    int ni = i + dx[k], nj = j + dy[k];
                    if (ni >= 0 and ni < msz and nj >=0 and nj < msz) {
                        if (matrix[ni][nj]) alive_neighbors++;
                    }
                }

                if (matrix[i][j]) {
                    if (alive_neighbors <= 1) next_gen_mat[i][j] = false;
                    else if (alive_neighbors <= 3) next_gen_mat[i][j] = true;
                    else next_gen_mat[i][j] = false;
                } else {
                    if (alive_neighbors == 3) next_gen_mat[i][j] = true;
                }

            }
        }

        matrix = next_gen_mat;

        cout << "Gen : " << gen << endl;
        for (int i=0; i<msz; i++) {
            for (int j=0; j<msz; j++) {
                if (matrix[i][j]) cout << "██";
                else cout << "  ";
            }
            cout << endl;
        }
        cout << endl;

    }
}
```

</details>
</article>

<article>

Find digits from a string( Leading zeroes doesn't get counted)

<details><summary>Theory and explanation</summary>

Extract **numeric tokens** from mixed string; convert to integer so **leading zeros drop** (`"007"` → 7).

Use regex `\d+` or manual scan building digit runs.

#### Further reading

- [MDN: RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp) — `\d+` patterns
- [LeetCode 8: atoi](https://leetcode.com/problems/string-to-integer-atoi/) — digit parsing

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function extractNumbers(input) {
  const matches = input.match(/\d+/g) || [];
  return matches.map(s => parseInt(s, 10));
}
```

#### Code walkthrough

- `\d+` finds contiguous digit runs.
- `parseInt` strips leading zeros.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(k) for k numbers |

#### Edge cases

- **No digits** — empty array.
- **Very long numbers** — use BigInt if needed.

</details>

<details><summary>Solution (other languages)</summary>

```
vector<int> extractNumbers(const string& input) {
    vector<int> numbers;
    regex re("\\d+"); // match one or more digits
    sregex_iterator begin(input.begin(), input.end(), re);
    sregex_iterator end;

    for (auto it = begin; it != end; ++it) {
        string numStr = it->str();
        int num = stoi(numStr); // converts string to int (removes leading zeros)
        numbers.push_back(num);
    }

    return numbers;
}
```

</details>
</article>

<article>

Given a string s containing lowercase lattin letters and another string p containing lowercase lattin letters and * and ?. * means any substring possibly empty. ? means any character but single.

Print yes or no if both strings matches. [RegEx Matching]

[**💻 Submit Code**](https://leetcode.com/problems/regular-expression-matching/)

<details><summary>Theory and explanation</summary>

**Wildcard matching** (this variant): `?` = one any char; `*` = any sequence (including empty). Different from LeetCode 10 (only `.` and `*` on preceding element).

Use **DP** or recursive memo: `match(i, j)` for `s[i:]` and `p[j:]`.

For `*`, either skip `*` or consume char and stay on `*`.

See also LeetCode 44 Wildcard Matching.

#### Further reading

- [LeetCode 44: Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) — `?` and `*`
- [LeetCode 10: Regex Matching](https://leetcode.com/problems/regular-expression-matching/) — `.` and `*`
- [GeeksforGeeks: Wildcard pattern matching](https://www.geeksforgeeks.org/wildcard-character-matching/) — DP

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function wildcardMatch(s, p) {
  const dp = Array.from({ length: s.length + 1 }, () =>
    Array(p.length + 1).fill(false)
  );
  dp[0][0] = true;

  for (let j = 1; j <= p.length; j++) {
    if (p[j - 1] === '*') dp[0][j] = dp[0][j - 1];
  }

  for (let i = 1; i <= s.length; i++) {
    for (let j = 1; j <= p.length; j++) {
      if (p[j - 1] === '*') {
        dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
      } else if (p[j - 1] === '?' || p[j - 1] === s[i - 1]) {
        dp[i][j] = dp[i - 1][j - 1];
      }
    }
  }
  return dp[s.length][p.length];
}
```

#### Code walkthrough

1. `*` — match empty (skip) or extend match with same star.
2. `?` — match any single char if prior state valid.

#### Complexity

| | |
|-|-|
| Time | O(n · m) |
| Space | O(n · m) |

#### Edge cases

- **Pattern only stars** — matches empty.
- **Multiple consecutive `*`** — collapse in preprocessing.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
int dp[25][25];
    bool Down(string &p,string &s, int i,int j){
    if( p[j] == '*' and p[j-1] == s[i] and dp[i-1][j] == 1 ) return true;
    if( p[j] == '*' and p[j-1] == '.' and dp[i-1][j] == 1 ) return true;
    return false;
}
bool Corner(string &p,string &s, int i,int j){
    if( p[j] == '.' and dp[i-1][j-1] == 1 ) return true;
    if( p[j] == s[i] and dp[i-1][j-1] == 1 ) return true;
    return false;
}
bool Right(string &p,string &s, int i,int j){
    if( p[j] == '*' and dp[i-1][j-2] == 1 ) {
        dp[i-1][j] = 1;
    }
    if( p[j] == '*' and dp[i][j-2] == 1 ) {
        return true;
    }
    return false;
}
bool isMatch(string s, string p) {
    for(int i=0;i<25;i++) for(int j=0;j<25;j++) dp[i][j] = 0;
    dp[0][0] = 1;
    s = "#"+s;
    p = "#"+p;
    int n = s.size(); int m = p.size();

    dp[0][0] = 1;
    for(int i=1;i<n;i++){
        for(int j=1;j<m;j++){
            Right(p,s,i,j);
            if( Down(p,s,i,j) or Corner(p,s,i,j) or Right(p,s,i,j)  ) dp[i][j] = 1;
        }
    }
   
    return dp[n-1][m-1];
}
```

</details>
</article>

<article>

About project: What have you done in the authentication part in your project? Also how did you specify roles for different users.

<details><summary>Theory and explanation</summary>

**System design / experience question** — Chaldal expects concrete auth stories from your projects.

**Cover in answer**

1. **Authentication** — how users prove identity (email/password, OAuth, JWT, session cookies).
2. **Authorization** — role-based access control (RBAC): roles like `admin`, `customer`, `warehouse_staff`.
3. **Implementation** — middleware checking claims; password hashing (bcrypt/Argon2); HTTPS only.
4. **Role assignment** — DB `users.role_id` or JWT claims; admin panel to assign roles.

**Chaldal stack alignment**

- Mention .NET Identity, JWT bearer, policy-based authorization, or similar if used.

#### Further reading

- [OWASP: Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) — best practices
- [Microsoft: ASP.NET Core RBAC](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/roles) — role authorization
- [JWT.io](https://jwt.io/introduction) — token structure

</details>

<details><summary>Solution (JavaScript)</summary>

Illustrative RBAC sketch:

```js
const ROLES = { ADMIN: 'admin', USER: 'user', PICKER: 'picker' };

function authMiddleware(requiredRole) {
  return (req, res, next) => {
    const user = verifyJwt(req.headers.authorization);
    if (!user) return res.status(401).end();
    if (requiredRole && !user.roles.includes(requiredRole))
      return res.status(403).end();
    req.user = user;
    next();
  };
}
```

#### Complexity

N/A (architecture)

</details>
</article>

<article>

Write a function which converts decimal number to hexadecimal

[**💻 Submit Code**](https://supecoder.dev/questions/Convert%20a%20Number%20to%20Hexadecimal?questionId=66acbdc29e71a163cdcece36)

<details><summary>Theory and explanation</summary>

**Decimal to hex** — repeated divide by 16; remainder maps to digit 0–9 or A–F (10–15).

Read remainders **bottom-up** (prepend to result string).

#### Further reading

- [LeetCode 405: Convert Number to Hexadecimal](https://leetcode.com/problems/convert-a-number-to-hexadecimal/) — problem
- [GeeksforGeeks: Decimal to hex](https://www.geeksforgeeks.org/program-decimal-hexadecimal-conversion/) — iterative method

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function decimalToHex(n) {
  if (n === 0) return '0';
  const digits = '0123456789ABCDEF';
  let hex = '';
  while (n > 0) {
    hex = digits[n % 16] + hex;
    n = Math.floor(n / 16);
  }
  return hex;
}
```

#### Code walkthrough

- Mod 16 for remainder; divide by 16; prepend digit char.

#### Complexity

| | |
|-|-|
| Time | O(log₁₆ n) |
| Space | O(log₁₆ n) |

#### Edge cases

- **0** — `'0'`.
- **Negative** — two's complement if required (LeetCode variant).

</details>

<details><summary>Solution (other languages)</summary>

```cpp
string decimalToHexa(int decimal){
    string hexa = "";
    while(decimal > 0){
        int remainder = decimal % 16;
        if(remainder < 10){
            hexa = to_string(remainder) + hexa;
        }else{
            hexa = char(remainder + 55) + hexa;
        }
        decimal /= 16;
    }
    return hexa;
}
```

</details>
</article>

<article>

Write a function which finds all the subset of a given set.

[**💻 Submit Code**](https://leetcode.com/problems/subsets/description/)

<details><summary>Theory and explanation</summary>

Same as **power set** / subsets of array — see subsets article above. Set can be represented as array of unique elements.

2^n subsets via backtracking or bitmasks.

#### Further reading

- [LeetCode 78: Subsets](https://leetcode.com/problems/subsets/) — problem
- [GeeksforGeeks: Power set](https://www.geeksforgeeks.org/power-set/) — bitmask

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function allSubsets(set) {
  const res = [];
  const path = [];
  function dfs(i) {
    if (i === set.length) { res.push([...path]); return; }
    path.push(set[i]);
    dfs(i + 1);
    path.pop();
    dfs(i + 1);
  }
  dfs(0);
  return res;
}
```

#### Code walkthrough

- Include/exclude each element at index i.

#### Complexity

| | |
|-|-|
| Time | O(n · 2^n) |
| Space | O(n) |

#### Edge cases

- **Empty set** — `[[]]`.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
vector<vector<int>> ans;
void allsubset(vector<int>&nums,int i,vector<int>&subset){
    if(i>=nums.size()){
        ans.push_back(subset);
        return;
    }
    subset.push_back(nums[i]);
    allsubset(nums,i+1,subset);
    subset.pop_back();
    allsubset(nums,i+1,subset);
}
vector<vector<int>> subsets(vector<int>& nums) {
    vector<int>subset;
    allsubset(nums,0,subset);
    return ans;
}
```

</details>
</article>

<article>

Given a set of orderings of letters, determine their topological sorting order. The orderings are provided as strings. 
For example, given the input ["A>B", "B>C", "C>D"], the expected output is "ABCD".

<details><summary>Theory and explanation</summary>

**Alien dictionary / topological sort** — constraints `A > B` mean **A comes before B** in custom order (parse `"A>B"` as edge A → B).

**Algorithm (Kahn's BFS)**

1. Build graph and indegree from all pairs in rules.
2. Queue nodes with indegree 0.
3. Append to order, reduce neighbor indegrees.
4. If order length ≠ unique letters → cycle (invalid).

**Interview talking points**

- Collect all unique characters first.
- Chaldal may use this for dependency ordering (tasks, SKU bundles).

#### Further reading

- [LeetCode 269: Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) — classic hard problem
- [CP-Algorithms: Topological sort](https://cp-algorithms.com/graph/topological-sort.html) — Kahn & DFS
- [GeeksforGeeks: Topological sorting](https://www.geeksforgeeks.org/topological-sorting/) — introduction

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function topoFromRules(rules) {
  const edges = rules.map(r => {
    const [a, , b] = r.replace(/\s/g, '').split('');
    return [a, b]; // "A>B" → A before B
  });
  const nodes = new Set();
  edges.forEach(([u, v]) => { nodes.add(u); nodes.add(v); });
  const indeg = Object.fromEntries([...nodes].map(c => [c, 0]));
  const adj = Object.fromEntries([...nodes].map(c => [c, []]));
  for (const [u, v] of edges) {
    adj[u].push(v);
    indeg[v]++;
  }
  const q = [...nodes].filter(c => indeg[c] === 0);
  const order = [];
  while (q.length) {
    const u = q.shift();
    order.push(u);
    for (const v of adj[u]) {
      if (--indeg[v] === 0) q.push(v);
    }
  }
  if (order.length !== nodes.size) throw new Error('cycle');
  return order.join('');
}

topoFromRules(['A>B', 'B>C', 'C>D']); // ABCD
```

#### Code walkthrough

1. Parse each rule into directed edge.
2. Kahn's algorithm produces linear extension.
3. Cycle detection via incomplete sort.

#### Complexity

| | |
|-|-|
| Time | O(V + E) |
| Space | O(V + E) |

#### Edge cases

- **Contradictory rules** — cycle, no valid order.
- **Disconnected letters** — all still appear in order.

</details>
</article>

<article>

Given two numbers represented as arrays of characters in decimal format, add them and return the result in the same format.
For example, Input: ['1', '2', '3'] and ['4', '5', '6']
Output: Output: ['5', '7', '9']

[**💻 Submit Code**](https://supecoder.dev/questions/Add%20Two%20Numbers%20Represented%20as%20Character%20Arrays?questionId=66acc37d9e71a163cdcee583)

<details><summary>Theory and explanation</summary>

**Big number addition** — add from least significant digit with carry.

Reverse arrays or add from end indices; push digits to result; reverse output.

Same as elementary school addition — O(max(n,m)).

#### Further reading

- [LeetCode 415: Add Strings](https://leetcode.com/problems/add-strings/) — string variant
- [GeeksforGeeks: Sum of large numbers](https://www.geeksforgeeks.org/sum-two-large-numbers/) — digit arrays

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function addCharArrays(A, B) {
  let i = A.length - 1, j = B.length - 1, carry = 0;
  const out = [];
  while (i >= 0 || j >= 0 || carry) {
    const a = i >= 0 ? A[i--].charCodeAt(0) - 48 : 0;
    const b = j >= 0 ? B[j--].charCodeAt(0) - 48 : 0;
    const s = a + b + carry;
    out.push(String(s % 10));
    carry = Math.floor(s / 10);
  }
  return out.reverse();
}
```

#### Code walkthrough

1. Process from right (ones place).
2. Sum digits + carry; push remainder digit.
3. Reverse result array.

#### Complexity

| | |
|-|-|
| Time | O(max(n,m)) |
| Space | O(max(n,m)) |

#### Edge cases

- **Different lengths** — treat missing as 0.
- **Final carry** — adds extra digit.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
vector<char> sum(vector<char> &A, vector<char> &B){
    reverse(A.begin(),A.end());
    reverse(B.begin(),B.end());
    vector<char> sum;
    int c = 0;
    int i=0,j=0;
    while(true){
        int a=0,b=0;
        if( i<A.size() ) a = A[i++]-'0';
        if( j<B.size() ) b = B[j++]-'0';

        int s = (a+b+c)%10;
        c = (a+b+c)/10;
        sum.push_back(s+'0');
        if( i>=A.size() and j>=B.size() and c == 0 ) break;
    }
    reverse(sum.begin(),sum.end());
    return sum;
}
```

</details>
</article>

<article>

Given the root of a binary tree, return its maximum depth.

[**💻 Submit Code**](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)

<details><summary>Theory and explanation</summary>

**Max depth** = longest path from root to any leaf (number of nodes or edges — clarify; LeetCode counts nodes).

**Recursive**: `1 + max(depth(left), depth(right))`.

**Iterative**: BFS level count or DFS stack tracking depth.

#### Further reading

- [LeetCode 104: Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) — problem
- [GeeksforGeeks: Height of binary tree](https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/) — DFS/BFS

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function TreeNode(val, left = null, right = null) {
  this.val = val; this.left = left; this.right = right;
}

function maxDepth(root) {
  if (!root) return 0;
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}

function maxDepthBFS(root) {
  if (!root) return 0;
  let depth = 0, q = [root];
  while (q.length) {
    depth++;
    const level = q.length;
    for (let i = 0; i < level; i++) {
      const node = q.shift();
      if (node.left) q.push(node.left);
      if (node.right) q.push(node.right);
    }
  }
  return depth;
}
```

#### Code walkthrough

- **DFS** — base null → 0; else 1 + max subtrees.
- **BFS** — count levels processed.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(h) DFS stack or O(w) BFS queue |

#### Edge cases

- **Empty tree** — 0.
- **Skewed tree** — recursion depth O(n).

</details>

<details><summary>Solution (other languages)</summary>

```cpp
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if( root == nullptr ) return 0;
        return max( maxDepth(root->left), maxDepth(root->right) ) + 1;
    }
};
```

</details>
</article>

<article>

You are to create a data structure that will support the following operations with the mentioned time complexity

- Insert a number in `O(1)`
- Search for a number in `O(1)`
- Delete a number in `O(1)`
- Return a number from the container with equal probability in `O(1)`

You can use existing containers of your favourite language.

<details><summary>Theory and explanation</summary>

This is **LeetCode 380: Insert Delete GetRandom O(1)**.

**Key idea**

- **Array** stores values for O(1) random index access.
- **Hash map** stores `value → index` in array for O(1) lookup.
- **Delete**: swap target with last element, pop, update map — O(1).

Without map, search is O(n); without array, random is O(n).

#### Further reading

- [LeetCode 380: Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) — exact problem
- [LeetCode 381: With duplicates](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/) — harder variant
- [GeeksforGeeks: RandomizedSet design](https://www.geeksforgeeks.org/design-a-data-structure-that-supports-insert-delete-search-and-getrandom-in-constant-time/) — walkthrough

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class RandomizedSet {
  constructor() {
    this.arr = [];
    this.idx = new Map();
  }
  insert(val) {
    if (this.idx.has(val)) return false;
    this.idx.set(val, this.arr.length);
    this.arr.push(val);
    return true;
  }
  remove(val) {
    if (!this.idx.has(val)) return false;
    const i = this.idx.get(val);
    const last = this.arr[this.arr.length - 1];
    this.arr[i] = last;
    this.idx.set(last, i);
    this.arr.pop();
    this.idx.delete(val);
    return true;
  }
  getRandom() {
    const i = Math.floor(Math.random() * this.arr.length);
    return this.arr[i];
  }
}
```

#### Code walkthrough

1. **Insert** — append to array; record index in map.
2. **Remove** — swap with last, fix map indices, pop.
3. **Random** — uniform index into array.

#### Complexity

| Operation | Time |
|-----------|------|
| insert | O(1) avg |
| search/has | O(1) avg |
| remove | O(1) avg |
| getRandom | O(1) |

#### Edge cases

- **getRandom on empty** — undefined; guard in production.
- **Duplicates** — use multiset variant (LC 381).

</details>
</article>

<article>

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it. (It is called the digital root of the number)

[**💻 Submit Code**](https://leetcode.com/problems/add-digits/description/)

<details><summary>Theory and explanation</summary>

**Digital root** — repeat digit sum until single digit.

**Math trick**: answer is `1 + (num - 1) % 9` for num > 0 (base 9 digital root).

**Recursive/loop**: sum digits, recurse until < 10.

#### Further reading

- [LeetCode 258: Add Digits](https://leetcode.com/problems/add-digits/) — problem
- [Wikipedia: Digital root](https://en.wikipedia.org/wiki/Digital_root) — mathematical property
- [GeeksforGeeks: Digital root](https://www.geeksforgeeks.org/digital-rootrepeated-digital-sum-given-integer/) — O(1) formula

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function addDigits(num) {
  if (num === 0) return 0;
  return 1 + ((num - 1) % 9);
}

function addDigitsLoop(num) {
  while (num >= 10) {
    let sum = 0;
    while (num) {
      sum += num % 10;
      num = Math.floor(num / 10);
    }
    num = sum;
  }
  return num;
}
```

#### Code walkthrough

- **O(1)** formula from congruence mod 9.
- **Loop** — sum digits until one digit remains.

#### Complexity

| Approach | Time |
|----------|------|
| Formula | O(1) |
| Loop | O(log num) per round |

#### Edge cases

- **0** — return 0.
- **Negative** — problem usually assumes positive.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
class Solution {
public:
    int addDigits(int num) {
        if( num < 10 ) return num;
        int root = 0;
        while(num){
            root += num%10;
            num /= 10;
        }
        return addDigits(root);
    }
};
```

</details>
</article>

<article>

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 

[**💻 Submit Code**](https://leetcode.com/problems/decode-string/description/)

<details><summary>Theory and explanation</summary>

**Decode string** — nested `k[abc]` means repeat inner decode `k` times.

**Stack approach**

- Push current string and multiplier when seeing `[`.
- On `]`, pop and append repeated segment.
- Digits build `k`; letters append to current segment.

**Recursion** also works with index pointer.

#### Further reading

- [LeetCode 394: Decode String](https://leetcode.com/problems/decode-string/) — problem
- [NeetCode: Decode String](https://neetcode.io/problems/decode-string) — stack walkthrough
- [GeeksforGeeks: Decode string](https://www.geeksforgeeks.org/decode-string-recursively-encoded-count-number/) — recursive

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function decodeString(s) {
  const stack = [];
  let cur = '', k = 0;
  for (const ch of s) {
    if (ch >= '0' && ch <= '9') {
      k = k * 10 + Number(ch);
    } else if (ch === '[') {
      stack.push([cur, k]);
      cur = '';
      k = 0;
    } else if (ch === ']') {
      const [prev, mult] = stack.pop();
      cur = prev + cur.repeat(mult);
    } else {
      cur += ch;
    }
  }
  return cur;
}

decodeString('3[a2[c]]'); // accaccacc
```

#### Code walkthrough

1. Build integer k from digit chars.
2. `[` saves state (current string, k) on stack.
3. `]` pops and repeats current segment k times onto previous.

#### Complexity

| | |
|-|-|
| Time | O(output length) |
| Space | O(n) stack |

#### Edge cases

- **Nested brackets** — stack handles naturally.
- **Multi-digit k** — accumulate before `[`.

</details>
</article>

<article>

You are given `row x col` grid representing a map where `grid[i][j] = 1` represents land and `grid[i][j] = 0` represents water.

Grid cells are connected horizontally/vertically (not diagonally). The `grid` is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The `grid` is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

[**💻 Submit Code**](https://leetcode.com/problems/island-perimeter/description/)

<details><summary>Theory and explanation</summary>

**Island perimeter** — each land cell contributes 4 edges minus shared borders with adjacent land.

**Methods**

1. **Cell scan** — for each land cell, +4 minus 1 per land neighbor (each shared edge counted twice → subtract 2 per internal edge or 1 per neighbor in implementation).
2. **Formula per cell**: `4 - neighbors` for each land cell (neighbor count 0–4).

No full DFS needed — single pass O(rows·cols).

#### Further reading

- [LeetCode 463: Island Perimeter](https://leetcode.com/problems/island-perimeter/) — problem
- [LeetCode 200: Number of Islands](https://leetcode.com/problems/number-of-islands/) — related DFS
- [GeeksforGeeks: Island perimeter](https://www.geeksforgeeks.org/find-perimeter-of-island/) — grid walkthrough

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function islandPerimeter(grid) {
  const rows = grid.length, cols = grid[0].length;
  const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
  let p = 0;
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (!grid[r][c]) continue;
      p += 4;
      for (const [dr, dc] of dirs) {
        const nr = r + dr, nc = c + dc;
        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc])
          p -= 2; // shared edge removes 2 from total perimeter count
      }
    }
  }
  return p;
}

// Alternative: add 1 for each land-water boundary
function islandPerimeterAlt(grid) {
  let p = 0;
  for (let r = 0; r < grid.length; r++) {
    for (let c = 0; c < grid[0].length; c++) {
      if (!grid[r][c]) continue;
      for (const [dr, dc] of [[1,0],[-1,0],[0,1],[0,-1]]) {
        const nr = r + dr, nc = c + dc;
        if (nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length || !grid[nr][nc])
          p++;
      }
    }
  }
  return p;
}
```

#### Code walkthrough

- **Alt method** (clearer): each land cell checks 4 sides; increment if neighbor is water or out of bounds.

#### Complexity

| | |
|-|-|
| Time | O(rows · cols) |
| Space | O(1) |

#### Edge cases

- **Single land cell** — perimeter 4.
- **All land** — outer border only.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
class Solution {
public:
    bool isLand(vector<vector<int>>& grid, int x, int y){
        if( x < 0 or x >= grid.size() or y < 0 or y >= grid[0].size()  ) return false;
        return grid[x][y] == 1;
    }
    int islandPerimeter(vector<vector<int>>& grid) {
        int dx[] = {1,-1,0,0};
        int dy[] = {0,0,1,-1};
        int perimeter = 0;
        for(int ux = 0; ux < grid.size(); ux ++){
            for(int uy = 0; uy < grid[ux].size(); uy ++){
                if( !isLand(grid, ux, uy) ) continue;
                for(int i = 0; i < 4; i ++) {
                    int vx = ux + dx[i];
                    int vy = uy + dy[i];
                    if( !isLand(grid, vx, vy) ) perimeter ++;
                }
            }
        }
        return perimeter;
    }
};
```

</details>
</article>
