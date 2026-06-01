---
description: Enosis, Enosis Solutions, Enosis Bangladesh, Enosis interview questions, Enosis interview stages, Enosis interview details, Enosis interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/enosis
---
# Enosis Solutions

|                   |                                  |
| :---------------- | :------------------------------- |
| Founding year     |                                  |
| Company Website   | https://www.enosisbd.com/        |
| Career Website    | https://enosisbd.pinpointhq.com/ |
| Technologies Used |                                  |

## Introduction

Enosis is a software development company based in Bangladesh, specializing in web and mobile application development. They focus on delivering high-quality software solutions to clients worldwide. 

## Interview Stages

1. **Online Screening**: This stage typically includes coding problems, algorithm questions. Candidates are expected to solve problems in a limited time frame. Usually the test is conducted on platforms like HackerRank.
2. **Technical Interview**: This interview focuses on assessing the candidate's technical skills, including programming languages, data structures, algorithms, and problem-solving abilities. Candidates may be asked to write code
3. **HR Interview**: The HR interview evaluates the candidate's fit within the company culture, communication skills, and overall personality. It may also cover salary expectations and job role details.

## Questions

<article>

Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified

[**💻 Submit Code**](https://leetcode.com/problems/text-justification/description/)

<details><summary>Theory and explanation</summary>

**Text justification** packs words greedily into lines of fixed width, then distributes extra spaces evenly between words. The **last line** is left-justified only (single spaces, no trailing padding).

**Greedy packing**

1. Accumulate words until the next word would exceed `maxWidth` (accounting for mandatory single spaces between words).
2. For a full line (not last): compute `totalSpaces = maxWidth - sum(word lengths)`; give each gap `totalSpaces // (wordCount-1)` spaces; distribute remainder to leftmost gaps.
3. Last line: join with single space, pad end with spaces to reach `maxWidth`.

**Interview talking points**

- Handle line with **one word** — pad trailing spaces only.
- Remainder spaces go to **left gaps first** (LeetCode rule).
- Time is linear in total characters across all words.

#### Further reading
- [LeetCode 68: Text Justification](https://leetcode.com/problems/text-justification/) — official problem
- [GfG: Text justification](https://www.geeksforgeeks.org/text-justification/) — step-by-step walkthrough

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function fullJustify(words, maxWidth) {
  const res = [];
  let i = 0;
  while (i < words.length) {
    let j = i, lineLen = 0;
    while (j < words.length && lineLen + words[j].length + (j - i) <= maxWidth) {
      lineLen += words[j].length;
      j++;
    }
    const count = j - i;
    const isLast = j === words.length;
    let line = '';
    if (count === 1 || isLast) {
      line = words.slice(i, j).join(' ');
      line += ' '.repeat(maxWidth - line.length);
    } else {
      const totalSpaces = maxWidth - lineLen;
      const gap = Math.floor(totalSpaces / (count - 1));
      let extra = totalSpaces % (count - 1);
      for (let k = i; k < j; k++) {
        line += words[k];
        if (k < j - 1) line += ' '.repeat(gap + (extra-- > 0 ? 1 : 0));
      }
    }
    res.push(line);
    i = j;
  }
  return res;
}
```

#### Code walkthrough
1. `j` scans how many words fit on the current line.
2. Single-word or last line: left justify and pad trailing spaces.
3. Otherwise distribute `totalSpaces` across `count-1` gaps with remainder to left gaps.

#### Complexity
| | |
|-|-|
| Time | O(N) where N is total characters in all words |
| Space | O(1) extra beyond output |

#### Edge cases
- **Single word per line** — pad trailing spaces only.
- **Last line** — never fully justify.
- **Empty words array** — return [].

</details>

</article>

<article>

You are given an `n x n` 2D `matrix` representing an image, rotate the image by 90 degrees (clockwise).

[**💻 Submit Code**](https://leetcode.com/problems/rotate-image/description/)

<details><summary>Theory and explanation</summary>

**In-place 90° clockwise rotation** can be done in two steps without extra matrix:

1. **Reverse rows** vertically (flip top-bottom).
2. **Transpose** — swap `matrix[i][j]` with `matrix[j][i]` for `i < j`.

Equivalently: transpose then reverse each row gives counter-clockwise.

**Why it works**

Cell `(i,j)` moves to `(j, n-1-i)` clockwise. Reverse-then-transpose achieves the same mapping in O(n²) time with O(1) extra space.

**Alternative:** rotate layer by layer from outside in — harder to implement under interview pressure.

#### Further reading
- [LeetCode 48: Rotate Image](https://leetcode.com/problems/rotate-image/) — problem statement
- [NeetCode: Rotate Image](https://neetcode.io/problems/rotate-image) — visual explanation

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function rotate(matrix) {
  const n = matrix.length;
  matrix.reverse();
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
    }
  }
}
```

#### Code walkthrough
1. `reverse()` flips rows vertically.
2. Nested loops transpose by swapping across the diagonal.
3. Mutates matrix in place.

#### Complexity
| | |
|-|-|
| Time | O(n²) |
| Space | O(1) |

#### Edge cases
- **1×1 matrix** — unchanged.
- **Non-square** — problem assumes n×n; general rotation needs different approach.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
void rotate(vector<vector<int>> &matrix)
    {
        reverse(matrix.begin(), matrix.end());
        for (int i = 0; i < matrix.size(); i++)
        {
            for (int j = i + 1; j < matrix.size(); j++)
            {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
    }
```

</details>

</article>

<article>

Given an array `nums`. Find the average of the array excluding the maximum and minimum values.

<details><summary>Theory and explanation</summary>

Find min and max in one pass (or use spread), sum all elements, subtract min and max, divide by `n-2`. If `n <= 2`, average is undefined — clarify with interviewer.

#### Further reading
- [GfG: Related problems](https://www.geeksforgeeks.org/) — algorithm reference

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function avgExcludingMinMax(nums) {
  if (nums.length <= 2) return null;
  let min = Infinity, max = -Infinity, sum = 0;
  for (const x of nums) {
    sum += x;
    if (x < min) min = x;
    if (x > max) max = x;
  }
  return (sum - min - max) / (nums.length - 2);
}
```

#### Code walkthrough
Single pass tracks min, max, and sum; subtract extremes and divide by remaining count.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases
Duplicate min/max values — only one instance of each extreme is excluded.
Array length ≤ 2 — return null or handle per spec.

</details>

</article>

<article>

Given n cars in a row with their speeds and a specific position, calculate the total number of collisions that occur.

<details><summary>Theory and explanation</summary>

Cars moving right collide with slower cars ahead; cars moving left collide with slower cars behind. Typical approach: for each car, count how many opposite-direction cars with higher speed will meet. Use stacks or prefix max/min per direction. Clarify direction/sign convention in interview.

#### Further reading
- [GfG: Related problems](https://www.geeksforgeeks.org/) — algorithm reference

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function countCollisions(speeds, directions) {
  // directions[i]: 1 = right, -1 = left
  let collisions = 0;
  for (let i = 0; i < speeds.length; i++) {
    if (directions[i] === 1) {
      for (let j = i + 1; j < speeds.length; j++) {
        if (directions[j] === -1 && speeds[i] > speeds[j]) collisions++;
      }
    }
  }
  return collisions;
}
```

#### Code walkthrough
Brute force: each right-moving car collides with left-moving slower cars to its right. Optimize with monotonic stacks for O(n).

#### Complexity
| | |
|-|-|
| Time | O(n²) brute; O(n) optimized |
| Space | O(1) |

#### Edge cases
All same direction — zero collisions.
Equal speeds — depends on problem rules.

</details>

</article>

<article>

Given an array of integers `nums` and queries in the form `l, r`. For each query, count the number of elements which are in range `[l,r]` in the array.

<details><summary>Theory and explanation</summary>

For each query, scan array counting elements in [l,r] — O(n) per query. With many queries, **sort + prefix counts** or **offline processing** helps. For static array, precompute frequency map if value range is small.

#### Further reading
- [GfG: Related problems](https://www.geeksforgeeks.org/) — algorithm reference

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function countInRange(nums, queries) {
  return queries.map(([l, r]) =>
    nums.filter(x => x >= l && x <= r).length
  );
}
```

#### Code walkthrough
Map each query to a filter count. For m queries over n elements: O(m·n).

#### Complexity
| | |
|-|-|
| Time | O(m·n) |
| Space | O(1) extra |

#### Edge cases
Empty array — all counts 0.
l > r — treat as empty range.

</details>

</article>

<article>

Given an array of integers `nums`. Find the second maximum element in an array using only one loop.

<details><summary>Theory and explanation</summary>

Track `first` and `second` while scanning. When updating max, push old max to second. Handle duplicates: second must be strictly less than first unless problem allows equality.

#### Further reading
- [GfG: Related problems](https://www.geeksforgeeks.org/) — algorithm reference

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function secondMax(nums) {
  let first = -Infinity, second = -Infinity;
  for (const x of nums) {
    if (x > first) {
      second = first;
      first = x;
    } else if (x > second && x < first) {
      second = x;
    }
  }
  return second === -Infinity ? null : second;
}
```

#### Code walkthrough
One pass updates first/second on each element; skip x equal to first for strict second max.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases
Fewer than 2 distinct values — no second max.
All equal — return null.

</details>

</article>

<article>

How do you center-align a right-angled triangle of numbers up to a given base limit?

<details><summary>Theory and explanation</summary>

For row `i` (0-indexed) with `i+1` numbers, pad `(base - i - 1)` leading spaces (or `(base-i-1)*2` if double-spacing digits). Print numbers separated by space. Centering = equal left padding per row.

#### Further reading
- [GfG: Related problems](https://www.geeksforgeeks.org/) — algorithm reference

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function printCenteredTriangle(base) {
  for (let i = 1; i <= base; i++) {
    const spaces = ' '.repeat(base - i);
    const row = Array.from({ length: i }, (_, j) => j + 1).join(' ');
    console.log(spaces + row);
  }
}
```

#### Code walkthrough
Row i has i numbers; leading spaces = base - i for center alignment in fixed-width rows.

#### Complexity
| | |
|-|-|
| Time | O(base²) |
| Space | O(base) |

#### Edge cases
base = 0 — print nothing.
Multi-digit numbers — adjust spacing width.

</details>

</article>

<article>

Convert a given string into a palindrome with the least number of changes.

<details><summary>Theory and explanation</summary>

Use two pointers from both ends. Mismatch → change one character (count++). Minimum changes = number of mismatched pairs. Greedy: always fix mismatch (either side works for count).

#### Further reading
- [GfG: Related problems](https://www.geeksforgeeks.org/) — algorithm reference

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function minChangesToPalindrome(s) {
  let changes = 0;
  let l = 0, r = s.length - 1;
  while (l < r) {
    if (s[l] !== s[r]) changes++;
    l++; r--;
  }
  return changes;
}
```

#### Code walkthrough
Compare mirrored pairs; increment changes on mismatch.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases
Empty string — 0 changes.
Already palindrome — 0.

</details>

</article>

<article>

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order. Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

[**💻 Submit Code**](https://leetcode.com/problems/merge-sorted-array/description/)

<details><summary>Theory and explanation</summary>

**Merge in-place** into `nums1` (length m+n with m valid elements): fill from the **end** to avoid overwriting unmerged elements in nums1.

Two pointers `i` (nums1), `j` (nums2), write index `k`. Compare tails, place larger at `k`, decrement pointers.

If nums2 remains when nums1 exhausted, copy rest.

#### Further reading
- [LeetCode 88: Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) — problem
- [NeetCode: Merge Sorted Array](https://neetcode.io/problems/merge-sorted-array) — walkthrough

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function merge(nums1, m, nums2, n) {
  let i = m - 1, j = n - 1, k = m + n - 1;
  while (j >= 0) {
    if (i >= 0 && nums1[i] > nums2[j]) nums1[k--] = nums1[i--];
    else nums1[k--] = nums2[j--];
  }
}
```

#### Code walkthrough
Fill from end; compare largest remaining from each array; decrement write pointer.

#### Complexity
| | |
|-|-|
| Time | O(m + n) |
| Space | O(1) |

#### Edge cases
nums2 empty — nums1 already sorted.
nums1 empty — copy nums2 to front.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
{
    int i = m - 1, j = n - 1, k = n + m - 1;
    while (j >= 0)
    {
        if (i>=0&&nums1[i] > nums2[j])
        {
            nums1[k] = nums1[i];
            i--;
        }
        else
        {
            nums1[k] = nums2[j];
            j--;
        }
        k--;
    }
}
```

</details>

</article>

<article>

Given an array of integers, calculate the absolute difference between the sum of odd-indexed and even-indexed elements.

<details><summary>Theory and explanation</summary>

Even indices: 0,2,4…; odd: 1,3,5…. Single pass: accumulate `evenSum` and `oddSum`, return `Math.abs(evenSum - oddSum)`.

#### Further reading
- [MDN: String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) — string ops

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function oddEvenDiff(nums) {
  let even = 0, odd = 0;
  nums.forEach((x, i) => (i % 2 === 0 ? even : odd) += x);
  return Math.abs(even - odd);
}
```

#### Code walkthrough
Simulate with two pointers or rule map as described.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases
Empty array — 0.

</details>

</article>

<article>

How would you encrypt a string based on a given set of encryption rules?

<details><summary>Theory and explanation</summary>

Clarify rules in interview (Caesar, substitution, XOR, etc.). General pattern: map each character through rule function. Discuss **reversibility**, **key management**, and never roll custom crypto for production.

#### Further reading
- [MDN: String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) — string ops

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function encrypt(s, rules) {
  return [...s].map(ch => rules[ch] ?? ch).join('');
}
```

#### Code walkthrough
Simulate with two pointers or rule map as described.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(n) |

#### Edge cases
Unknown characters — pass through or error per spec.

</details>

</article>

<article>

Given an array of integers `nums`. In each move pick two numbers from start and end of the array, store the smaller in output, then remove it. Repeat until empty. What will be the output array?

<details><summary>Theory and explanation</summary>

Always take smaller of front/back, append to result, remove that end. Equivalent to merging two sorted halves from outside-in producing ascending order if array sorted — for general array, simulate with two pointers.

#### Further reading
- [MDN: String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) — string ops

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function pickSmallerEnds(nums) {
  const out = [];
  let l = 0, r = nums.length - 1;
  while (l <= r) {
    if (nums[l] <= nums[r]) out.push(nums[l++]);
    else out.push(nums[r--]);
  }
  return out;
}
```

#### Code walkthrough
Simulate with two pointers or rule map as described.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(n) output |

#### Edge cases
Single element — one output.

</details>

</article>

<article>

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

[**💻 Submit Code**](https://leetcode.com/problems/palindrome-number/description/)

<details><summary>Theory and explanation</summary>

Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes. Reverse half the digits and compare, or build reversed number — watch **overflow** (use long). O(log₁₀ n) digits.

#### Further reading
- [LeetCode 9](https://leetcode.com/problems/palindrome-number/) — problem

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function isPalindrome(x) {
  if (x < 0 || (x !== 0 && x % 10 === 0)) return false;
  let rev = 0;
  while (x > rev) {
    rev = rev * 10 + x % 10;
    x = Math.floor(x / 10);
  }
  return x === rev || x === Math.floor(rev / 10);
}
```

#### Code walkthrough
Reverse second half only; compare when x <= rev.

#### Complexity
| | |
|-|-|
| Time | O(log n) |
| Space | O(1) |

#### Edge cases
Negative x — false.
x=0 — true.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
bool isPalindrome(int x)
{
    if (x < 0)
        return false;
    vector<int> v;
    long long n = x, ans = 0;
    while (x)
    {
        v.push_back(x % 10);
        x /= 10;
    }
    for (int i = 0; i < v.size(); i++)
    {
        ans += v[i] * pow(10, v.size() - 1 - i);
    }
    return n == ans;
}
```

</details>

</article>

<article>

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

[**💻 Submit Code**](https://leetcode.com/problems/rotate-array/description/)

<details><summary>Theory and explanation</summary>

Normalize `k %= n`. **Triple reverse**: reverse whole array, reverse first k, reverse rest — O(n) in-place. Or copy to new array at `(i+k)%n`.

#### Further reading
- [LeetCode 189](https://leetcode.com/problems/rotate-array/) — problem

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function rotate(nums, k) {
  const n = nums.length;
  k %= n;
  const copy = nums.slice();
  for (let i = 0; i < n; i++) nums[(i + k) % n] = copy[i];
}
```

#### Code walkthrough
Copy then place each element at rotated index.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(n) |

#### Edge cases
k=0 — unchanged.
k > n — use modulo.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
void rotate(vector<int> &nums, int k)
    {
        vector<int> cp = nums;
        int n = nums.size();
        k = k % n;
        for (int i = 0; i < n; i++)
        {
            cp[(i + k) % n] = nums[i];
        }
        nums = cp;
    }
```

</details>

</article>

<article>

Given an array and a number, construct a number from the array digits, subtract the given number, and return the result.

<details><summary>Theory and explanation</summary>

Concatenate digits to form big integer (string in JS to avoid overflow), subtract, return. For very large numbers use string arithmetic.

#### Further reading
- [GfG: Large number arithmetic](https://www.geeksforgeeks.org/difference-of-two-large-numbers/) — string subtraction

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function subtractFromDigits(digits, sub) {
  const num = BigInt(digits.join(''));
  return (num - BigInt(sub)).toString();
}
```

#### Code walkthrough
Join digits, use BigInt for arbitrary precision.

#### Complexity
| | |
|-|-|
| Time | O(d) |
| Space | O(d) |

#### Edge cases
Result negative — clarify return type.
Leading zeros in digits — normalize.

</details>

</article>

<article>

Given `n`, calculate the `nth` Fibonacci number F`(n)`.

[**💻 Submit Code**](https://leetcode.com/problems/fibonacci-number/description/)

<details><summary>Theory and explanation</summary>

F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2). **Iterative** O(n) O(1). **Matrix exponentiation** O(log n). Naive recursion O(2ⁿ).

#### Further reading
- [LeetCode 509](https://leetcode.com/problems/fibonacci-number/) — problem

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function fib(n) {
  if (n <= 1) return n;
  let a = 0, b = 1;
  for (let i = 2; i <= n; i++) [a, b] = [b, a + b];
  return b;
}
```

#### Code walkthrough
Rolling two variables; no recursion stack.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases
n=0 → 0.
Large n — use BigInt if needed.

</details>

</article>

<article>

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

[**💻 Submit Code**](https://leetcode.com/problems/valid-anagram/description/)

<details><summary>Theory and explanation</summary>

Same length and identical character counts. **Frequency array** size 26 (lowercase) or sort both strings and compare — O(n log n).

#### Further reading
- [LeetCode 242](https://leetcode.com/problems/valid-anagram/) — problem

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function isAnagram(s, t) {
  if (s.length !== t.length) return false;
  const cnt = new Map();
  for (const c of s) cnt.set(c, (cnt.get(c) || 0) + 1);
  for (const c of t) {
    if (!cnt.has(c)) return false;
    cnt.set(c, cnt.get(c) - 1);
    if (cnt.get(c) === 0) cnt.delete(c);
  }
  return cnt.size === 0;
}
```

#### Code walkthrough
Count s chars; decrement for t; empty map means match.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(1) alphabet |

#### Edge cases
Different lengths — false.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
bool isAnagram(string s, string t)
    {
        map<char, int> m1, m2;
        for (int i = 0; i < s.size(); i++)
        {
            m1[s[i]]++;
        }
        for (int i = 0; i < t.size(); i++)
        {
            m2[t[i]]++;
        }
        if (m1.size() != m2.size())
            return false;
        for (auto it : m1)
        {
            if (m2.count(it.first) == 0)
                return false;
            else if (m2[it.first] != it.second)
                return false;
        }
        return true;
    }
```

</details>

</article>

<article>

Print all repeating elements in an array.

<details><summary>Theory and explanation</summary>

Use **Set** or frequency map. Elements with count > 1 are repeating. Preserve order: track seen and duplicates sets.

#### Further reading
- [GfG: Find duplicates](https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/) — duplicate detection

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function repeatingElements(nums) {
  const seen = new Set(), dup = new Set(), res = [];
  for (const x of nums) {
    if (seen.has(x)) dup.add(x);
    else seen.add(x);
  }
  for (const x of nums) if (dup.has(x) && !res.includes(x)) res.push(x);
  return res;
}
```

#### Code walkthrough
Track seen; second occurrence marks duplicate; collect unique order.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(n) |

#### Edge cases
No repeats — empty array.

</details>

</article>

<article>

Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

[**💻 Submit Code**](https://leetcode.com/problems/validate-ip-address/description/)

<details><summary>Theory and explanation</summary>

**IPv4**: four dot-separated parts, each 0–255, no leading zeros (except '0'). **IPv6**: eight colon-separated hex groups (handle `::` compression carefully). Validate with split + rules.

#### Further reading
- [LeetCode 468](https://leetcode.com/problems/validate-ip-address/) — problem

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function validIPAddress(queryIP) {
  if (queryIP.includes('.')) {
    const parts = queryIP.split('.');
    if (parts.length !== 4) return 'Neither';
    for (const p of parts) {
      if (!/^(0|[1-9]\d{0,2})$/.test(p) || +p > 255) return 'Neither';
    }
    return 'IPv4';
  }
  if (queryIP.includes(':')) {
    const parts = queryIP.split(':');
    if (parts.length !== 8) return 'Neither';
    for (const p of parts) {
      if (!/^[0-9a-fA-F]{1,4}$/.test(p)) return 'Neither';
    }
    return 'IPv6';
  }
  return 'Neither';
}
```

#### Code walkthrough
Branch on delimiter; validate segment count and numeric/hex ranges.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(n) |

#### Edge cases
IPv6 compressed `::` — simplified version may need full parser.

</details>

</article>

<article>

You are given a string, `message`, and a positive integer, `limit`. Split the string into lines such that each line has a maximum of `limit` characters.
[**💻 Submit Code**](https://leetcode.com/problems/split-message-based-on-limit/description/)

<details><summary>Theory and explanation</summary>

Pack characters greedily into lines of at most `limit`. May need suffix `<i/n>` indicating part number — adjust available payload per line. Binary search or greedy simulation per LeetCode 2468.

#### Further reading
- [LeetCode 2468](https://leetcode.com/problems/split-message-based-on-limit/) — problem

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function splitMessage(message, limit) {
  const parts = [];
  let i = 0, part = 1;
  while (i < message.length) {
    const suffix = `<${part}/?>`;
    const maxLen = limit - suffix.length;
    if (maxLen <= 0) return [];
    parts.push(message.slice(i, i + maxLen) + suffix.replace('?', String(part)));
    i += maxLen;
    part++;
  }
  return parts;
}
```

#### Code walkthrough
Greedy slice with room for part suffix; refine total count in full solution.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(n) |

#### Edge cases
limit too small for suffix — impossible.

</details>

</article>

<article>

Build a linked-list-based tree structure with left and right children.

<details><summary>Theory and explanation</summary>

A **binary tree node** as linked list: each node has `val`, `left`, `right` pointers.

```js
class TreeNode {
  constructor(val, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}
```

Unlike arrays, no index arithmetic — traversal uses pointer chasing. Interview: discuss vs array-based heap representation.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [System Design Primer](https://github.com/donnemartin/system-design-primer) — architecture patterns

</details>

<details><summary>Solution (JavaScript)</summary>

```js
N/A — conceptual question.
```

#### Code walkthrough
Focus on verbal explanation and trade-offs.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases
Clarify scope with interviewer before deep-diving.

</details>

</article>

<article>

How would you build a tree structure from a list of given nodes?

<details><summary>Theory and explanation</summary>

Common inputs: **parent array** (`parent[i]` for node i), or **level-order with nulls**. Algorithm: create map id→node, second pass link children to parents. For `[val, leftIdx, rightIdx]` serialized form, recursive build.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [System Design Primer](https://github.com/donnemartin/system-design-primer) — architecture patterns

</details>

<details><summary>Solution (JavaScript)</summary>

```js
N/A — conceptual question.
```

#### Code walkthrough
Focus on verbal explanation and trade-offs.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases
Clarify scope with interviewer before deep-diving.

</details>

</article>

<article>

What are the key differences between a tree and a graph data structure?

<details><summary>Theory and explanation</summary>

| | Tree | Graph |
|-|------|-------|
| Cycles | No (acyclic) | May have cycles |
| Edges | n-1 for n nodes | Flexible |
| Root | Usually one root | No single root required |
| Connectivity | Connected | May be disconnected |

Trees are special graphs; DFS/BFS apply to both.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [System Design Primer](https://github.com/donnemartin/system-design-primer) — architecture patterns

</details>

<details><summary>Solution (JavaScript)</summary>

```js
N/A — conceptual question.
```

#### Code walkthrough
Focus on verbal explanation and trade-offs.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases
Clarify scope with interviewer before deep-diving.

</details>

</article>

<article>

What are the four pillars of Object-Oriented Programming (OOP)?

<details><summary>Theory and explanation</summary>

**Encapsulation** — hide state, expose methods. **Abstraction** — show essential behavior, hide complexity. **Inheritance** — reuse via IS-A hierarchy. **Polymorphism** — same interface, different implementations (overriding/overloading).

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [System Design Primer](https://github.com/donnemartin/system-design-primer) — architecture patterns

</details>

<details><summary>Solution (JavaScript)</summary>

```js
N/A — conceptual question.
```

#### Code walkthrough
Focus on verbal explanation and trade-offs.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases
Clarify scope with interviewer before deep-diving.

</details>

</article>

<article>

What is DFS? Implement Depth-First Search in any programming language.

<details><summary>Theory and explanation</summary>

**DFS** explores as deep as possible before backtracking. Uses **stack** (explicit or recursion). Time O(V+E) for graphs.

```js
function dfs(node, visit) {
  if (!node) return;
  visit(node);
  dfs(node.left, visit);
  dfs(node.right, visit);
}
```

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [System Design Primer](https://github.com/donnemartin/system-design-primer) — architecture patterns

</details>

<details><summary>Solution (JavaScript)</summary>

```js
N/A — conceptual question.
```

#### Code walkthrough
Focus on verbal explanation and trade-offs.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases
Clarify scope with interviewer before deep-diving.

</details>

</article>

<article>

Explain the internal working and implementation of a priority queue.

<details><summary>Theory and explanation</summary>

**Priority queue** always returns min (or max) element. Backed by **binary heap**: insert O(log n), extract-min O(log n), peek O(1). `bubbleUp` on insert, `sinkDown` on extract. JavaScript: `MinPriorityQueue` from `@datastructures-js` or simple heap array.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [System Design Primer](https://github.com/donnemartin/system-design-primer) — architecture patterns

</details>

<details><summary>Solution (JavaScript)</summary>

```js
N/A — conceptual question.
```

#### Code walkthrough
Focus on verbal explanation and trade-offs.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases
Clarify scope with interviewer before deep-diving.

</details>

</article>

<article>

What is the time complexity of operations in a Red-Black Tree?

<details><summary>Theory and explanation</summary>

| Operation | Average | Worst |
| Search | O(log n) | O(log n) |
| Insert | O(log n) | O(log n) |
| Delete | O(log n) | O(log n) |

RB-tree maintains balance via color rules + rotations; height ≤ 2log(n+1).

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [System Design Primer](https://github.com/donnemartin/system-design-primer) — architecture patterns

</details>

<details><summary>Solution (JavaScript)</summary>

```js
N/A — conceptual question.
```

#### Code walkthrough
Focus on verbal explanation and trade-offs.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases
Clarify scope with interviewer before deep-diving.

</details>

</article>

<article>

System design question: File management software. @@Senior@@

<details><summary>Theory and explanation</summary>

**Requirements**: upload/download, folders, permissions, versioning, search.

**High level**: Client → API Gateway → Metadata DB (PostgreSQL) + Object Storage (S3). Files stored by content hash; metadata holds path, owner, ACL.

**Key decisions**: chunk large files; CDN for downloads; event queue for virus scan/indexing; eventual consistency for search index.

**Scale**: shard metadata by tenant; multipart upload; deduplication via hash.

#### Further reading
- [MDN Web Docs](https://developer.mozilla.org/) — reference
- [System Design Primer](https://github.com/donnemartin/system-design-primer) — architecture patterns

</details>

<details><summary>Solution (JavaScript)</summary>

```js
N/A — conceptual question.
```

#### Code walkthrough
Focus on verbal explanation and trade-offs.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases
Clarify scope with interviewer before deep-diving.

</details>

</article>
