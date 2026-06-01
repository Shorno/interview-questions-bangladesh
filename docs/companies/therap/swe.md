---
description: Therap Software Engineer interview questions, Therap Software Engineer interview stages, Therap Software Engineer interview details, Therap Software Engineer interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/therap/swe
---
# Therap Software Engineer

## Interview Stages

The selection process has 3 stages,

1. **Initial screening:** This round is taken in written format
1. **1st technical round** The first round is taken by the BD team
1. **HR Round:** This is the final stage before onboarding and typically deals with salary negotiation. 

## Software Engineering Questions

<article>

Given an array of numbers indicating stock price of n consecutive days. If you buy stock at one day and sell at any later day what is the maximum profit that you can get?

[**💻 Submit Code**](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

<details><summary>Theory and explanation</summary>

**Best time to buy and sell stock I** — one transaction max profit. Track **minimum price seen**; at each day update `profit = max(profit, price - minPrice)` and `minPrice = min(minPrice, price)`.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function maxProfit(prices) {
  let min = prices[0], best = 0;
  for (let i = 1; i < prices.length; i++) {
    best = Math.max(best, prices[i] - min);
    min = Math.min(min, prices[i]);
  }
  return best;
}
```

#### Code walkthrough
Single forward scan; never need to sell before buying.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases
Monotonic decreasing prices — profit 0.

</details>

<details><summary>Solution (other languages)</summary>

```C++
int maxProfit(vector<int>& prices) {
    int buy = prices[0];
    int profit = 0;
    for(int i=1;i<prices.size();i++){
        if( prices[i]-buy > profit ) profit = prices[i] - buy;
        if( prices[i] < buy ) buy = prices[i];
    }
    return profit;
}
```

</details>

</article>


<article>

Given an array of n integers. You need to take all zeroes in array to the end without changing the relative order of remaining element.
eg: `[2,0,0,3,1,0,5]` => `[2,3,1,5,0,0,0]`

[**💻 Submit Code**](https://leetcode.com/problems/move-zeroes/description/)

<details><summary>Theory and explanation</summary>

**Move zeroes** — in-place stable partition: pointer `i` marks next non-zero slot; scan `j`, swap when non-zero found then increment `i`.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function moveZeroes(nums) {
  let i = 0;
  for (let j = 0; j < nums.length; j++) {
    if (nums[j] !== 0) {
      [nums[i], nums[j]] = [nums[j], nums[i]];
      i++;
    }
  }
}
```

#### Code walkthrough
Two-pointer swap preserves non-zero order.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases
All zeros — no swaps needed.

</details>

<details><summary>Solution (other languages)</summary>

```C++
void moveZeroes(vector<int>& nums) {
    int i = 0;
    for(int j=0;j<nums.size();j++){
        swap(nums[i], nums[j]);
        if( nums[i] != 0 ) i++;
    }
}
```

</details>

</article>


<article>

Given an array of n integers. Reorder the elements such that all odd numbers occur after even numbers.

<details><summary>Theory and explanation</summary>

Stable partition by **value parity** while keeping relative order within evens and odds. Two-pointer or two output lists merged.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function reorderOddAfterEven(nums) {
  const evens = [], odds = [];
  for (const x of nums) (x % 2 === 0 ? evens : odds).push(x);
  return [...evens, ...odds];
}
```

#### Code walkthrough
Split then concatenate; stable within each group.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(n) |

#### Edge cases
Single parity — entire array one side.

</details>

</article>


<article>

Given an array of strings. Print the sets of strings which are anagram.
eg: ["cat","tab","act","bat","taco"] => [{"cat","act"},{"tab","bat"},{"taco"}] 

[**💻 Submit Code**](https://leetcode.com/problems/group-anagrams/)

<details><summary>Theory and explanation</summary>

**Group anagrams** — canonical key = sorted chars (or 26-letter frequency). Hash map key → list of words.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function groupAnagrams(strs) {
  const map = new Map();
  for (const s of strs) {
    const key = [...s].sort().join('');
    if (!map.has(key)) map.set(key, []);
    map.get(key).push(s);
  }
  return [...map.values()];
}
```

#### Code walkthrough
Sort each word as O(k log k) key.

#### Complexity
| | |
|-|-|
| Time | O(n·k log k) |
| Space | O(nk) |

#### Edge cases
Empty string group.

</details>

<details><summary>Solution (other languages)</summary>

```C++
vector<vector<string>> groupAnagrams(vector<string>& strs) {
    map<string,int> index;
    vector<vector<string>> vs;
    for(auto str:strs){
        string str2 = str;
        if( str2.size()>1 ) sort(str2.begin(),str2.end());
        if( index.find(str2) == index.end() ){
            vs.push_back(vector<string>());
            index[str2] = vs.size()-1;
        }
        vs[ index[str2] ].push_back(str);
    }
    return vs;
}
```

</details>

</article>


<article>

Given an array of n integers. Find the kth largest element in the array.

[**💻 Submit Code**](https://leetcode.com/problems/kth-largest-element-in-an-array/)

<details><summary>Theory and explanation</summary>

**Kth largest** — min-heap size k (O(n log k)) or quickselect O(n) average. `partial_sort` in C++ picks top k.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function findKthLargest(nums, k) {
  return nums.sort((a, b) => b - a)[k - 1];
}
```

#### Code walkthrough
Sort descending; index k-1.

#### Complexity
| | |
|-|-|
| Time | O(n log n) |
| Space | O(1) |

#### Edge cases
k > n invalid.

</details>

<details><summary>Solution (other languages)</summary>

```C++
int findKthLargest(vector<int>& nums, int k) {
    partial_sort(nums.begin(), nums.begin() + k, nums.end(), greater<int>());
    return nums[k-1];
}
```

</details>

</article>


<article>

Given two very large number in string format. Find the sum of the two number

<details><summary>Theory and explanation</summary>

Grade-school addition from **least significant digit** with carry; reverse strings or index from end.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function addBig(A, B) {
  let i = A.length - 1, j = B.length - 1, carry = 0, res = '';
  while (i >= 0 || j >= 0 || carry) {
    const a = i >= 0 ? +A[i--] : 0;
    const b = j >= 0 ? +B[j--] : 0;
    const s = a + b + carry;
    res = (s % 10) + res;
    carry = Math.floor(s / 10);
  }
  return res;
}
```

#### Code walkthrough
Digit-by-digit with carry from right.

#### Complexity
| | |
|-|-|
| Time | O(max(m,n)) |
| Space | O(1) |

#### Edge cases
Different lengths — pad implicitly with 0.

</details>

<details><summary>Solution (other languages)</summary>

```C++
string sum(string &A, string &B){
    reverse(A.begin(),A.end());
    reverse(B.begin(),B.end());
    string sum;
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

Given two binary tree. Check if they are identical [not isomorphism]

[**💻 Submit Code**](https://leetcode.com/problems/same-tree/)

<details><summary>Theory and explanation</summary>

Same structure and values at every node. **Recursive DFS**: both null → true; one null or val mismatch → false; else recurse left & right.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function isSameTree(p, q) {
  if (!p && !q) return true;
  if (!p || !q || p.val !== q.val) return false;
  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}
```

#### Code walkthrough
Base cases for null and value mismatch.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(h) stack |

#### Edge cases
Empty trees — true.

</details>

<details><summary>Solution (other languages)</summary>

::: code-group

```C++ [Normal Solution]
bool isSameTree(TreeNode* p, TreeNode* q) {
    if( p == nullptr and q != nullptr ) return false;
    if( p != nullptr and q == nullptr ) return false;
    if( p == nullptr and q == nullptr ) return true;

    if( p->val != q->val ) return false;

    return isSameTree(p->left,q->left) &&
            isSameTree(p->right,q->right);
}
```

```go [Weird Solution]
// ref: https://go.dev/tour/concurrency/7
package main

import (
	"fmt"

	"golang.org/x/tour/tree"
)

// Walk walks the tree t sending all values
// from the tree to the channel ch.
func WalkRecursive(t *tree.Tree, ch chan int) {
	if t.Left != nil {
		WalkRecursive(t.Left, ch)
	}
	ch <- t.Value
	if t.Right != nil {
		WalkRecursive(t.Right, ch)
	}
}

func Walk(t *tree.Tree, ch chan int) {
    WalkRecursive(t, ch)
    close(ch)
}

// Same determines whether the trees
// t1 and t2 contain the same values.
func Same(t1, t2 *tree.Tree) bool {
	ch1 := make(chan int)
	ch2 := make(chan int)
	go Walk(t1, ch1)
	go Walk(t2, ch2)
	for {
		x, ok1 := <-ch1
		y, ok2 := <-ch2

		if ok1 != ok2 || x != y {
			return false
		}
		if !ok1 {
			break
		}
	}
	return true
}

func main() {
	fmt.Println(Same(tree.New(1), tree.New(2)))
}
```

:::

</details>

</article>


<article>

Given two array of integers. Find the common elements between them.

Unique : [**💻 Submit Code**](https://leetcode.com/problems/intersection-of-two-arrays/) Repeats: [**💻 Submit Code**](https://leetcode.com/problems/intersection-of-two-arrays-ii/)

<details><summary>Theory and explanation</summary>

**Unique intersection** — hash set of nums1, filter nums2. **With repetition** — sort both, merge two pointers like merge step in merge sort.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function intersectionUnique(a, b) {
  const s = new Set(a);
  return [...new Set(b.filter(x => s.has(x)))];
}
```

#### Code walkthrough
Set for unique variant.

#### Complexity
| | |
|-|-|
| Time | O(n+m) |
| Space | O(n) |

#### Edge cases
Empty input — [].

</details>

<details><summary>Solution (other languages)</summary>

::: code-group

```C++ [Return uniques]
vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
    set<int> st;
    for(auto num:nums1) st.insert(num);
    set<int> res;
    for(auto num:nums2) if( st.count(num) == 1 ) res.insert(num);
    vector<int> ret;
    for(auto num:res) ret.push_back(num);
    return ret;
}
```

```C++ [With repeatation]
vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
    sort(nums1.begin(),nums1.end());
    sort(nums2.begin(),nums2.end());

    vector<int> merged;
    int i=0,j=0;
    while(i<nums1.size() and j<nums2.size()){
        if( nums1[i] == nums2[j] ){
            merged.push_back(nums1[i]);
            i++;j++;
        }else if( nums1[i]<nums2[j] ) i++;
        else j++;
    }
    return merged;
}
```

:::

</details>

</article>


<article>

Find pairs with given target sum in a doubly linked list. 
```
Input: 
1 <> 2 <> 4 <> 5 <> 6 <> 8 <> 9
target = 7
Output: 
(1,6), (2,5)
```

[**💻 Submit Code**](https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1)

<details><summary>Theory and explanation</summary>

**Two pointers** from head and tail (DLL allows O(1) prev). If sum < target move left forward; if sum > target move right back; equal record pair.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function pairsDLL(head, target) {
  if (!head) return [];
  let left = head, right = head;
  while (right.next) right = right.next;
  const ans = [];
  while (left !== right && left.prev !== right) {
    const s = left.val + right.val;
    if (s === target) { ans.push([left.val, right.val]); left = left.next; right = right.prev; }
    else if (s < target) left = left.next;
    else right = right.prev;
  }
  return ans;
}
```

#### Code walkthrough
Opposite ends converge.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases
Unsorted list — hash set alternative.

</details>

<details><summary>Solution (other languages)</summary>

```C++
class Solution
{
public:
    vector<pair<int, int>> findPairsWithGivenSum(Node *head, int target)
    {
        vector<pair<int,int>> ans;
        
        Node* left = head;
        
        /// traverse to the end of the list
        while(head!= nullptr && head->next!=nullptr){
            head = head->next;
        }
        Node* right = head;
        
        while(left!= right && left->prev != right){
            if(left->data + right->data == target){
                ans.push_back(make_pair(left->data, right->data));
                left = left->next;
                right = right->prev;
            }
            else if(left->data + right->data > target){
                right = right->prev;
            }else{
                left = left->next;
            }
        }
        
        return ans;    
        
    }
};
```

</details>

</article>


<article>

Solve the problem using Object Oriented Programming

``` C++
int main(){
    int square1width = 50;
    int square2width = 80;
    int rectangle1width = 30, rectangle1height = 40;
    int rectangle2width = 20, rectangle2height = 40;

    int square1area = square1width* square1width;
    int square2area = square2width* square2width;
    int rectangle1area = rectangle1height*rectangle1width;
    int rectangle2area = rectangle2width* rectangle2height;
}
```

<details><summary>Theory and explanation</summary>

Replace duplicated area math with **polymorphic `Shape.area()`**. Abstract base class; Square/Rectangle override. Open/closed principle — add Circle without changing client.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class Shape { area() { throw new Error('implement'); } }
class Square extends Shape {
  constructor(w) { super(); this.w = w; }
  area() { return this.w * this.w; }
}
class Rectangle extends Shape {
  constructor(w, h) { super(); this.w = w; this.h = h; }
  area() { return this.w * this.h; }
}
```

#### Code walkthrough
Inheritance + override eliminates copy-paste formulas.

#### Complexity
| | |
|-|-|
| Time | O(1) per area |
| Space | O(1) |

#### Edge cases
Invalid dimensions — validate in constructor.

</details>

<details><summary>Solution (other languages)</summary>

``` C++
#include <iostream>
using namespace std;

// Abstract base class
class Shape {
public:
    virtual int area() const = 0;  // Pure virtual function for area
};

class Square : public Shape {
private:
    int width;
public:
    Square(int w) : width(w) {}  // Constructor to initialize width

    int area() const override {
        return width * width;  // Area of square
    }
};

class Rectangle : public Shape {
private:
    int width;
    int height;
public:
    Rectangle(int w, int h) : width(w), height(h) {}  // Constructor to initialize width and height

    int area() const override {
        return width * height;  // Area of rectangle
    }
};

int main() {
    
    Square square1(50);
    Square square2(80);
    Rectangle rectangle1(30, 40);
    Rectangle rectangle2(20, 40);

    cout << "Square 1 area: " << square1.area() << endl;
    cout << "Square 2 area: " << square2.area() << endl;
    cout << "Rectangle 1 area: " << rectangle1.area() << endl;
    cout << "Rectangle 2 area: " << rectangle2.area() << endl;
    return 0;
}

```

</details>

</article>


<article>

Given an array of sides of triangles, return an array of strings. The strings would be either “yes” or “no”, corresponding to whether the same indexed triangle is a right triangle or not.

Input: `[[3,4,5], [5,9,12], [6,8,10]]`
Output: `["yes","no","yes"]`

<details><summary>Theory and explanation</summary>

Sort three sides a≤b≤c. **Pythagorean theorem**: right iff a²+b²=c². Map boolean to yes/no strings.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function rightTriangles(triangles) {
  return triangles.map(([a,b,c]) => {
    const s = [a,b,c].sort((x,y)=>x-y);
    return s[0]**2 + s[1]**2 === s[2]**2 ? 'yes' : 'no';
  });
}
```

#### Code walkthrough
Sort sides; check hypotenuse.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases
Degenerate triangle — not right.

</details>

<details><summary>Solution (other languages)</summary>

```python
def areRightTriangles(triangles):
    res = []
    
    for sides in triangles:
        sides.sort()
        a,b,c = sides
        if a**2 + b**2 == c**2:
            res.append(True)
        else:
            res.append(False)
    
    return res
```

</details>

</article>


<article>

A dictionary of sorted words was like this: [a, above, bad, broke, cat,..., yes, yolk, zoo]. After a malfunction it became this: [..., yes, yolk, zoo, a, above, bad, broke, cat,....]. Write a program so that given a word, one can find the word in the dictionary, with the same time complexity as when the dictionary was sorted.

[**💻 Submit Code**](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)

<details><summary>Theory and explanation</summary>

**Search in rotated sorted array** — one half always sorted; compare `target` with bounds to pick half. O(log n).

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function searchRotated(words, target) {
  let l = 0, r = words.length - 1;
  while (l <= r) {
    const m = (l + r >> 1);
    if (words[m] === target) return m;
    if (words[l] <= words[m]) {
      if (target >= words[l] && target < words[m]) r = m - 1; else l = m + 1;
    } else {
      if (target > words[m] && target <= words[r]) l = m + 1; else r = m - 1;
    }
  }
  return -1;
}
```

#### Code walkthrough
Modified binary search on rotated array.

#### Complexity
| | |
|-|-|
| Time | O(log n) |
| Space | O(1) |

#### Edge cases
Duplicates — may degrade to O(n).

</details>

<details><summary>Solution (other languages)</summary>

```python
def search(words, target):
        l, r = 0, len(words) - 1

        while l <= r:
            m = (l + r) // 2
            if words[m] == target:
                return m
            
            if words[l] <= words[m]:
                if target < words[l] or target > words[m]:
                    l = m + 1
                else :
                    r = m - 1
            
            else:
                if target > words[r] or target < words[m] :
                    r = m - 1
                else :
                    l = m + 1

        return -1
```

</details>

</article>


<article>

Given two strings s1, s2, return whether a substring of s1 is an anagram of s2

Input: `s1 = "hello", s2 = "lol"` Output: `True`\
Input: `s1 = "hello", s2 = "loa"` Output: `False`

<details><summary>Theory and explanation</summary>

Fixed window size |s2| on s1. Compare **26-char frequency** arrays; slide by decrementing leaving char, incrementing entering char.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function containsAnagram(s1, s2) {
  if (s2.length > s1.length) return false;
  const count = (s) => {
    const a = Array(26).fill(0);
    for (const c of s) a[c.charCodeAt(0) - 97]++;
    return a;
  };
  let a = count(s1.slice(0, s2.length)), b = count(s2);
  const eq = (x,y) => x.every((v,i)=>v===y[i]);
  if (eq(a,b)) return true;
  for (let i = s2.length; i < s1.length; i++) {
    a[s1.charCodeAt(i - s2.length) - 97]--;
    a[s1.charCodeAt(i) - 97]++;
    if (eq(a,b)) return true;
  }
  return false;
}
```

#### Code walkthrough
Sliding window frequency match.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases
s2 longer than s1 — false.

</details>

<details><summary>Solution (other languages)</summary>

```python
def containsAnagram(s1, s2):
    ara1 = [0]*26
    ara2 = [0]*26

    for i in range(len(s2)):
        ara1[ord(s1[i])-ord(('a'))] += 1
        ara2[ord(s2[i])-ord(('a'))] += 1

    l, r = 0, len(s2)
    while r < len(s1):
        if ara1 == ara2:
            return True
        ara1[ord(s1[l])-ord(('a'))] -= 1
        ara1[ord(s1[r])-ord(('a'))] += 1
        l += 1
        r += 1

    return ara1 == ara2
```

</details>

</article>


<article>

Given two large numbers as strings, num1 and num2 with num1 larger than num2, return their difference in string format, using no direct string to int conversion or libraries.

<details><summary>Theory and explanation</summary>

Subtract LSD to MSD with **borrow**; pad shorter num2 with leading zeros implicitly.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function subtractStrings(num1, num2) {
  num1 = num1.split('').reverse();
  num2 = num2.split('').reverse();
  let res = '', borrow = 0;
  for (let i = 0; i < num1.length; i++) {
    let d = +num1[i] - (+num2[i] || 0) - borrow;
    if (d < 0) { d += 10; borrow = 1; } else borrow = 0;
    res += d;
  }
  return res.replace(/0+$/, '').split('').reverse().join('') || '0';
}
```

#### Code walkthrough
Reverse, subtract digit-wise, strip zeros.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(n) |

#### Edge cases
num1 < num2 — handle sign per spec.

</details>

<details><summary>Solution (other languages)</summary>

```python
def subtract(num1, num2):
    num1, num2 = num1[::-1], num2[::-1]   
    res = ""
    carry = 0

    for i in range(len(num1)):
        digit1 = int(num1[i])
        digit2 = int(num2[i]) if i < len(num2) else 0
        diff = digit1 - digit2 - carry

        if diff < 0:
            diff += 10
            carry = 1

        else:
            carry = 0

        res += str(diff)

    # Remove leading zeros
    res = res.rstrip("0")

    return res[::-1]
```

</details>

</article>


<article>

Given an array containing 0,1,2 sort it.

Input: `[2,0,1,1,0,2]` Output: `[0,0,1,1,2,2]`

<details><summary>Theory and explanation</summary>

**Dutch national flag** — three pointers low/mid/high; swap 0 to front, 2 to back. O(n) one pass.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function sortColors(nums) {
  let lo = 0, mid = 0, hi = nums.length - 1;
  while (mid <= hi) {
    if (nums[mid] === 0) [nums[lo++], nums[mid++]] = [nums[mid], nums[lo]];
    else if (nums[mid] === 2) [nums[mid], nums[hi--]] = [nums[hi], nums[mid]];
    else mid++;
  }
  return nums;
}
```

#### Code walkthrough
Three-way partition in one pass.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases
Already sorted — still O(n).

</details>

<details><summary>Solution (other languages)</summary>

```python
def bring2Front(ara,start,target):
    target_index = start
    for i in range(start,len(ara)):
        ara[i],ara[target_index] = ara[target_index],ara[i]
        if ara[target_index] == target:
            target_index += 1
    return target_index

def sortNums(ara):
    target_index = bring2Front(ara,0,0)
    bring2Front(ara,target_index,1)
    return ara
```

</details>

</article>


<article>

Using no loops, print this pattern for a given number n: 

`n, n-5, n-10,....0,....,n-10,n-5,n`.
Example: `7, 2, -3, 2, 7`

<details><summary>Theory and explanation</summary>

**Recursion** replaces loop: descend by 5 until ≤0, then unwind appending same values. Produces symmetric sequence.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function pattern(n) {
  const out = [];
  function rec(v) {
    out.push(v);
    if (v > 0) { rec(v - 5); out.push(v); }
  }
  rec(n);
  return out;
}
```

#### Code walkthrough
Recursive descent and return builds palindrome-like sequence.

#### Complexity
| | |
|-|-|
| Time | O(n/5) |
| Space | O(n/5) stack |

#### Edge cases
Negative n — base case behavior.

</details>

<details><summary>Solution (other languages)</summary>

```python
def recursiveAdd(ara, n):
    ara.append(n)
    if n > 0:
        recursiveAdd(ara, n-5)
        ara.append(n)

def solution(n):
    ara = []
    recursiveAdd(ara, n)
    return ara
```

</details>

</article>


<article>

Design this legacy table for using in a relational database.

| ID 	| Name  	| Email           	| Subject 	| Courses                              	|
|----	|-------	|-----------------	|---------	|--------------------------------------	|
| 1  	| Rahim 	| rahim@gmail.com 	| CSE     	| CSE101, CSE102, EEE101, CIVIL104     	|
| 2  	| karim 	| karim@gmail.com 	| EEE     	| EEE101, EEE102, CSE102, CIVIL104     	|
| 3  	| Josim 	| josim@gmail.com 	| BME     	| EEE101, CSE101, BME101               	|
| 4  	| Belal 	| belal@gmail.com 	| CIVIL   	| CIVIL101, CIVIL102, MECHA101, EEE101 	|
| 5  	| Rakib 	| rakib@gmail.com 	| MECHA   	| CSE101, BME101, MECHA101, MECHA101   	|

<details><summary>Theory and explanation</summary>

Violates **1NF** (multi-valued Courses column). Normalize: **Student**, **Course**, **Subject**, **Enrollment(student_id, course_id)**. Email unique on Student.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```sql
CREATE TABLE student (id PK, name, email UNIQUE, subject_id FK);
CREATE TABLE course (code PK, title);
CREATE TABLE enrollment (student_id FK, course_id FK, PRIMARY KEY (student_id, course_id));
```

#### Code walkthrough
Split repeating groups into junction table.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Same course code different departments — clarify PK.

</details>

</article>


## April 2026

<article>

You are given a list of orders, where each order takes a certain amount of time to process (e.g., brewing a coffee). There are `k` identical machines available to process these orders. Orders are processed on a first-come, first-served basis, and each order must be assigned to exactly one machine. Orders will be placed sequentially. Find the total time required to complete all orders.

```
Input: k = 2, orders = [3,2,5,4]
Output: 7
```

<details><summary>Theory and explanation</summary>

**Minimum time to finish with k machines** — min-heap of machine finish times; assign job to earliest-free machine; answer = max heap value.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function minCompletionTime(k, orders) {
  const heap = [];
  const push = (x) => { heap.push(x); heap.sort((a,b)=>a-b); };
  const pop = () => heap.shift();
  for (const t of orders) {
    if (heap.length < k) push(t);
    else push(pop() + t);
  }
  return Math.max(...heap);
}
```

#### Code walkthrough
Simulate k parallel workers with min-heap.

#### Complexity
| | |
|-|-|
| Time | O(n log k) |
| Space | O(k) |

#### Edge cases
k >= n — sum of all orders.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int getMinTime(int k, vector<int> &orders) {
    // Min-heap to keep track of the earliest available machine
    priority_queue<int, vector<int>, greater<int>> pq;

    for (int curr : orders) {
      if (!pq.empty() || pq.size() < k) {
        // If there are still empty machines, just push the task time
        pq.push(curr);
      } else {
        // If pq.size() == k, get the earliest available machine
        int x = pq.top();
        pq.pop();
        // Add the current task time to that machine and push back
        pq.push(x + curr);
      }
    }

    // At the end, return the max element in the pq while pq is not empty
    int max_time = 0;
    while (!pq.empty()) {
      max_time =
          pq.top(); // Since it's a min-heap, the last element popped is the max
      pq.pop();
    }

    return max_time;
  }
};
```

</details>

</article>


<article>

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer. There can be nested encoding. You may assume that the input string is always valid; digits are only used as repeat numbers.

```
Input: s = "3[a2[bc]]"
Output: "abcbcabcbcabcbc"
```

[**💻 Submit Code**](https://leetcode.com/problems/decode-string/description/?envType=problem-list-v2&envId=recursion)

<details><summary>Theory and explanation</summary>

**Decode string** — stack of (string, repeat count) or char stack; on `]` pop and repeat substring.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function decodeString(s) {
  const st = [], counts = [], strs = [''];
  for (const c of s) {
    if (c >= '0' && c <= '9') {
      counts[counts.length-1] = (counts[counts.length-1]||0)*10 + +c;
    } else if (c === '[') { st.push(strs[strs.length-1]); strs[strs.length-1]=''; counts.push(0); }
    else if (c === ']') {
      const rep = counts.pop(), prev = st.pop();
      strs[strs.length-1] = prev + strs.pop().repeat(rep);
    } else strs[strs.length-1] += c;
  }
  return strs[0];
}
```

#### Code walkthrough
Stack tracks nested repeats.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(n) |

#### Edge cases
Nested encoding — stack depth.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
class Solution {
public:
  string decodeString(string s) {
    stack<char> st;

    for (int i = 0; i < s.size(); i++) {
      if (s[i] == ']') {
        string substr = "";
        while (st.top() != '[') {
          substr += st.top();
          st.pop();
        }
        st.pop();

        reverse(substr.begin(), substr.end());
        string num = "";

        while (!st.empty() && isdigit(st.top())) {
          num += st.top();
          st.pop();
        }
        reverse(num.begin(), num.end());
        int n = stoi(num);

        string temp = substr;
        for (int j = 1; j < n; j++) {
          substr += temp;
        }

        for (int j = 0; j < substr.size(); j++) {
          st.push(substr[j]);
        }

      } else {
        st.push(s[i]);
      }
    }

    string ans = "";
    while (!st.empty()) {
      ans += st.top();
      st.pop();
    }

    reverse(ans.begin(), ans.end());
    return ans;
  }
};
```

</details>

</article>


<article>

Given two strings `s` and `t`, return the shortest substring of `s` such that every character in `t`, including duplicates, is present in the substring. If such a substring does not exist, return an empty string `""`.

```
Input: s = "OUZODYXAZV", t = "XYZ"
Output: "YXAZ"
```

[**💻 Submit Code**](https://neetcode.io/problems/minimum-window-with-characters/question?list=neetcode150)

<details><summary>Theory and explanation</summary>

**Minimum window substring** — expand until window covers all chars of t; shrink from left while valid; track minimum.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function minWindow(s, t) {
  const need = {};
  for (const c of t) need[c] = (need[c]||0)+1;
  let missing = t.length, l = 0, best = '';
  for (let r = 0; r < s.length; r++) {
    if (need[s[r]]-- > 0) missing--;
    while (!missing) {
      const win = s.slice(l, r+1);
      if (!best || win.length < best.length) best = win;
      if (++need[s[l]] > 0) missing++;
      l++;
    }
  }
  return best;
}
```

#### Code walkthrough
Sliding window with missing counter.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(1) alphabet |

#### Edge cases
No valid window — ''.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
class Solution {
public:
  string minWindow(string s, string t) {
    map<char, int> pattern, mp;

    for (auto &x : t)
      pattern[x]++;

    int i = 0, j = 0, cnt = 0, n = t.size();
    string ans = "";

    while (i < s.size()) {
      mp[s[i]]++;

      if (mp[s[i]] <= pattern[s[i]])
        cnt++;

      while (j <= i && mp[s[j]] > pattern[s[j]]) {
        mp[s[j]]--;
        j++;
      }

      if (cnt == n && (ans.empty() || i - j + 1 < ans.length()))
        ans = s.substr(j, i - j + 1);

      i++;
    }

    return ans;
  }
};
```

</details>

</article>


<article>

Given an integer array `nums`, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

```
Input: nums = [2,2,3,4]
Output: 3
```

[**💻 Submit Code**](https://leetcode.com/problems/valid-triangle-number/description/)

<details><summary>Theory and explanation</summary>

Sort array. Fix largest side `i`, two-pointer `l,r` on smaller sides; if sum > nums[i], all pairs in [l..r-1] work with r.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function triangleNumber(nums) {
  nums.sort((a,b)=>a-b);
  let count = 0;
  for (let i = nums.length-1; i >= 2; i--) {
    let l = 0, r = i-1;
    while (l < r) {
      if (nums[l]+nums[r] > nums[i]) { count += r-l; r--; }
      else l++;
    }
  }
  return count;
}
```

#### Code walkthrough
Sort + two-pointer per fixed longest side.

#### Complexity
| | |
|-|-|
| Time | O(n²) |
| Space | O(1) |

#### Edge cases
nums[i]===0 — skip.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int count = 0;
        for (int i = nums.size() - 1; i >= 2; i--) {
            int l = 0, r = i - 1;
            while (l < r) {
                if (nums[l] + nums[r] > nums[i]) {
                    count += r - l;
                    r--;
                } else {
                    l++;
                }
            }
        }
        return count;
    }
};
```

</details>

</article>


<article>

You are given a singly linked list. Traverse the list and reverse every block of 3 consecutive nodes. If the number of nodes is not a multiple of 3, the remaining nodes at the end should be left as is.

```
Input:  a > b > c > d > e > f > g > h
Output: c > b > a > f > e > d > g > h
```

[**💻 Submit Code**](https://leetcode.com/problems/reverse-nodes-in-k-group/)

<details><summary>Theory and explanation</summary>

**Reverse nodes in k-group** — reverse first k nodes iteratively/recursively, connect tail to result of rest.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function reverseKGroup(head, k) {
  let cur = head, n = 0;
  while (cur && n < k) { cur = cur.next; n++; }
  if (n < k) return head;
  cur = head; let prev = null;
  for (let i = 0; i < k; i++) { const next = cur.next; cur.next = prev; prev = cur; cur = next; }
  head.next = reverseKGroup(cur, k);
  return prev;
}
```

#### Code walkthrough
Reverse k then recurse on remainder.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(n/k) stack |

#### Edge cases
Tail < k nodes — leave unchanged.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
ListNode* reverseKGroup(ListNode* head, int k) {
    ListNode* curr = head;
    int count = 0;
    while (curr && count < k) {
        curr = curr->next;
        count++;
    }
    if (count < k) return head;

    curr = head;
    ListNode* prev = nullptr;
    for (int i = 0; i < k; i++) {
        ListNode* next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    head->next = reverseKGroup(curr, k);
    return prev;
}
```

</details>

</article>


<article>

Given a database table, normalize it. Show the primary key, foreign key, and the relationships among the tables.

| code | bus_name | type    | from  | to         | departure | arrival | days          |
|------|----------|---------|-------|------------|-----------|---------|---------------|
| 101  | Khanika  | express | dhaka | rajshahi   | 9 am      | 9 pm    | sat, mon, thu |
| 102  | Taranga  | local   | dhaka | khulna     | 10 pm     | 11 am   | everyday      |
| 103  | Ulka     | express | dhaka | chittagong | 10 pm     | 11 am   | sat, sun      |

<details><summary>Theory and explanation</summary>

Split **Bus**, **Route**(from, to), **Schedule**(code PK, route_id FK, departure, arrival), **ScheduleDay**(schedule_id, day). Remove repeating `days` CSV.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```sql
-- Bus(code PK, name, type)
-- Route(id PK, from_city, to_city)
-- Schedule(code PK, bus_code FK, route_id FK, departure, arrival)
-- ScheduleDay(schedule_code FK, day_of_week)
```

#### Code walkthrough
Entity per noun; M:N days via junction.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
'everyday' — expand to 7 rows or enum.

</details>

</article>


<article>

Given an integer `n`, find the first `n` rows of Pascal's triangle.

```
Input: n = 4
Output: [[1], [1,1], [1,2,1], [1,3,3,1]]
```

[**💻 Submit Code**](https://leetcode.com/problems/pascals-triangle/)

<details><summary>Theory and explanation</summary>

Each row starts/ends with 1; interior `row[j] = prev[j-1] + prev[j]`.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function pascalsTriangle(n) {
  const res = [];
  for (let i = 0; i < n; i++) {
    const row = Array(i+1).fill(1);
    for (let j = 1; j < i; j++) row[j] = res[i-1][j-1] + res[i-1][j];
    res.push(row);
  }
  return res;
}
```

#### Code walkthrough
Build row from previous.

#### Complexity
| | |
|-|-|
| Time | O(n²) |
| Space | O(n²) |

#### Edge cases
n=0 — [].

</details>

<details><summary>Solution (other languages)</summary>

```cpp
vector<vector<int>> generate(int numRows) {
    vector<vector<int>> result;
    for (int i = 0; i < numRows; i++) {
        vector<int> row(i + 1, 1);
        for (int j = 1; j < i; j++) {
            row[j] = result[i-1][j-1] + result[i-1][j];
        }
        result.push_back(row);
    }
    return result;
}
```

</details>

</article>


<article>

An alien's warship has a large amount of fuel and needs to distribute it across multiple vessels. As the amount is very large, the fuel amount is given in string format and a divisor is given. Output the quotient.

```
Input:  total amount = "44444444444666666667777777777", divisor = 2
Output: quotient = "22222222222333333333888888888"
```

[**💻 Submit Code**](https://www.geeksforgeeks.org/dsa/divide-large-number-represented-string/)

<details><summary>Theory and explanation</summary>

**Long division** on string: accumulate remainder digit-by-digit, append quotient digit.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function divideString(dividend, divisor) {
  let cur = 0, res = '';
  for (const c of dividend) {
    cur = cur * 10 + (c - '0');
    res += Math.floor(cur / divisor);
    cur %= divisor;
  }
  return res.replace(/^0+/, '') || '0';
}
```

#### Code walkthrough
Schoolbook long division.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(n) |

#### Edge cases
Leading zeros in quotient.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
string divideString(string dividend, int divisor) {
    string result = "";
    long long current = 0;
    for (char c : dividend) {
        current = current * 10 + (c - '0');
        result += to_string(current / divisor);
        current %= divisor;
    }
    size_t start = result.find_first_not_of('0');
    return start == string::npos ? "0" : result.substr(start);
}
```

</details>

</article>


<article>

Given a list of software versions in chronological order and a current version, output the following.

```
Input:
versions = ["1.0", "1.5", "2.0"]
current_version = "1.0"

Output:
{
  "isLatest": false,
  "latestVersion": "2.0",
  "versionBehind": 2
}
```

<details><summary>Theory and explanation</summary>

Find index of current in ordered list; `latest = versions.at(-1)`; `versionBehind = len - 1 - idx`.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function checkVersion(versions, current) {
  if (!versions.length) return { isLatest: false, latestVersion: '', versionBehind: -1 };
  const idx = versions.indexOf(current);
  const latest = versions[versions.length - 1];
  if (idx === -1) return { isLatest: false, latestVersion: latest, versionBehind: -1 };
  return { isLatest: current === latest, latestVersion: latest, versionBehind: versions.length - 1 - idx };
}
```

#### Code walkthrough
Index lookup on chronological array.

#### Complexity
| | |
|-|-|
| Time | O(n) |
| Space | O(1) |

#### Edge cases
Unknown current version — versionBehind -1.

</details>

<details><summary>Solution (other languages)</summary>

```cpp
tuple<bool, string, int> checkVersion(const vector<string>& versions, const string& current_version) {
    if (versions.empty()) {
        return {false, "", -1};
    }

    string latest = versions.back();
    auto it = find(versions.begin(), versions.end(), current_version);
    if (it == versions.end()) {
        return {false, latest, -1};
    }

    bool isLatest = current_version == latest;
    int idx = static_cast<int>(distance(versions.begin(), it));
    int versionBehind = static_cast<int>(versions.size()) - 1 - idx;
    return {isLatest, latest, versionBehind};
}
```

</details>

</article>


<article>

Design an object-oriented programming solution for a parking management system. The system should model `ParkingLot`, `ParkingSpace`, and `Ticket`, and support different types of vehicles using a `Vehicle` superclass with subclasses such as `Car` and `Motorbike`.

<details><summary>Theory and explanation</summary>

**ParkingLot** owns **ParkingSpace** list; **Vehicle** hierarchy (Car, Motorbike); **Ticket** issued on park linking vehicle+space+timestamp.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class ParkingLot {
  constructor(n) { this.spaces = Array.from({length:n}, (_,i)=>({id:i+1, free:true})); }
  park(vehicle) {
    const s = this.spaces.find(x => x.free);
    if (!s) return null;
    s.free = false;
    return { vehicle, space: s.id, at: Date.now() };
  }
  leave(ticket) { this.spaces.find(s=>s.id===ticket.space).free = true; }
}
```

#### Code walkthrough
Find first free space; ticket on entry.

#### Complexity
| | |
|-|-|
| Time | O(n) park |
| Space | O(n) |

#### Edge cases
Full lot — null ticket.

</details>

<details><summary>Solution (other languages)</summary>

```java
abstract class Vehicle {
    protected String licensePlate;
    public Vehicle(String licensePlate) {
        this.licensePlate = licensePlate;
    }
    public String getLicensePlate() { return licensePlate; }
}

class Car extends Vehicle {
    public Car(String licensePlate) { super(licensePlate); }
}

class Motorbike extends Vehicle {
    public Motorbike(String licensePlate) { super(licensePlate); }
}

class Ticket {
    private Vehicle vehicle;
    private ParkingSpace space;
    private long entryTime;

    public Ticket(Vehicle vehicle, ParkingSpace space) {
        this.vehicle = vehicle;
        this.space = space;
        this.entryTime = System.currentTimeMillis();
    }
    public Vehicle getVehicle() { return vehicle; }
    public ParkingSpace getSpace() { return space; }
}

class ParkingSpace {
    private int id;
    private boolean isOccupied;

    public ParkingSpace(int id) {
        this.id = id;
        this.isOccupied = false;
    }
    public boolean isAvailable() { return !isOccupied; }
    public void occupy() { isOccupied = true; }
    public void vacate() { isOccupied = false; }
    public int getId() { return id; }
}

class ParkingLot {
    private List<ParkingSpace> spaces;

    public ParkingLot(int totalSpaces) {
        spaces = new ArrayList<>();
        for (int i = 1; i <= totalSpaces; i++) {
            spaces.add(new ParkingSpace(i));
        }
    }

    public Ticket park(Vehicle vehicle) {
        for (ParkingSpace space : spaces) {
            if (space.isAvailable()) {
                space.occupy();
                return new Ticket(vehicle, space);
            }
        }
        return null; // No space available
    }

    public void leave(Ticket ticket) {
        ticket.getSpace().vacate();
    }
}
```

</details>

</article>


<article>

Write about a project you have implemented. Discuss the use of AI, the challenges faced, and how you overcame those challenges.

<details><summary>Theory and explanation</summary>

Behavioral — use **STAR**: project scope, your role, AI tools (testing, codegen), challenges (deadline, integration), measurable outcome. Be honest about AI assist limits.

#### Further reading
- [LeetCode](https://leetcode.com/) — practice problems

</details>

<details><summary>Solution (JavaScript)</summary>

```js
Prepare 3–5 minute narrative covering: problem, stack, AI usage, hardest bug, result metric.
```

#### Code walkthrough
No code — communication assessed.

#### Complexity
| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A |

#### Edge cases
Avoid vague claims — cite specifics.

</details>

</article>

