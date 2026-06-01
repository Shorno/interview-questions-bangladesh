---
description: Bevy Commerce interview questions, Bevy Commerce interview stages, Bevy Commerce interview details, Bevy Commerce interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/bevycommerce
---
# Bevy Commerce

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-| :- |
| Founding year | |
| Company Website | https://bevycommerce.com/landing |
| Career Website | |
| Technologies Used| Node.js, React, GraphQL |

## Introduction
[Bevy Commerce](https://bevycommerce.com/landing) is a software development studio specializing in cutting-edge eCommerce solutions. They build tailored, innovative products that drive sales and elevate the customer experience for industry giants such as Canadian Tire, Alo Yoga, Authentic Brands Group, and Shopify corporate. 

## Interview Stages
The interview process was based on two stages

1. Technical Round: Half an hour of quick-fire questions online. For the 1st assessment interview, focus on the node, react and graphQL basics
2. Coding Round: Based on problem-solving

## Coding Round Questions

<article>

How does error handling differ in synchronous and asynchronous code in Node.js, and what are the best practices for error handling in asynchronous code?

<details><summary>Theory and explanation</summary>

In **synchronous** Node.js code, execution proceeds line by line on the call stack. Errors surface as **exceptions** that propagate up the stack until something catches them with `try/catch` or until they become an **uncaught exception** and crash the process (unless you listen for `process.on('uncaughtException')`, which is generally discouraged for recovery).

In **asynchronous** code, work is scheduled and the current stack unwinds before the async work finishes. That means:

1. **`try/catch` around an async call does not catch errors inside the async callback** unless you `await` the promise inside the `try` block or wrap the callback yourself.
2. **Errors can appear in different places**: callback as first argument (`err`), rejected `Promise`, `async` function throw, or event emitters (`error` event on streams).
3. **Multiple concurrent operations** mean you must decide whether to fail fast, collect partial results, or use patterns like `Promise.allSettled`.

**Synchronous patterns**

- Wrap risky sync code in `try/catch`.
- Validate inputs early and throw `TypeError` / custom errors with clear messages.
- Let errors bubble to a boundary (route handler, CLI main) when appropriate.

**Asynchronous best practices**

1. **Prefer `async/await` with `try/catch`** for linear flow; map low-level APIs to promises with `util.promisify` or `new Promise`.
2. **Always handle promise rejections**: `await` inside `try/catch`, or `.catch()` on chains. Never fire-and-forget without a handler.
3. **Use `process.on('unhandledRejection')` in development** to log stray rejections; fix the root cause rather than swallowing in production.
4. **Callbacks (legacy)**: check `if (err) return next(err)` (Express) or call the callback with `err` first.
5. **Express**: pass errors to `next(err)`; define a **four-argument** error middleware `(err, req, res, next)`.
6. **Operational vs programmer errors** (Node.js design): operational errors (network timeout, 404) can be handled and reported; programmer errors (null reference) may warrant crashing after logging so a process manager restarts a clean state.
7. **Do not mix styles** in one function without discipline (callback + promise without wrapping causes double-callback or lost errors).

**Interview talking points**

- Explain why `try { setTimeout(() => { throw new Error() }, 0) } catch` does not catch.
- Mention that `async` functions always return a Promise; thrown errors become rejections.
- For Bevy’s stack (Node + React), note that frontend async errors also need error boundaries and promise handling in effects.

#### Further reading

- [Node.js: Error handling](https://nodejs.org/api/errors.html) — official error types and propagation
- [Node.js: Process 'unhandledRejection' event](https://nodejs.org/api/process.html#event-unhandledrejection) — monitoring stray rejections
- [Express: Error handling](https://expressjs.com/en/guide/error-handling.html) — middleware pattern used in many Node APIs
- [MDN: Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) — rejection and chaining
- [Joyent: Error handling in Node.js](https://www.joyent.com/node-js/production/design/errors) — operational vs programmer errors (classic reference)

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// Sync: try/catch works on the same tick
function readConfigSync(path) {
  try {
    const fs = require('fs');
    return JSON.parse(fs.readFileSync(path, 'utf8'));
  } catch (err) {
    err.message = `Config load failed: ${err.message}`;
    throw err;
  }
}

// Async: await inside try/catch
async function fetchUser(id) {
  try {
    const res = await fetch(`https://api.example.com/users/${id}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.error('fetchUser failed', err);
    throw err; // rethrow or return a Result type
  }
}

// Express-style boundary
function asyncHandler(fn) {
  return (req, res, next) => Promise.resolve(fn(req, res, next)).catch(next);
}
```

#### Code walkthrough

- **Sync example**: `readFileSync` throws on missing file or invalid JSON; `try/catch` runs in the same call stack turn.
- **Async example**: `fetch` returns a Promise; `await` suspends the async function until settlement; rejections (network, `throw`, non-OK response) jump to `catch`.
- **`asyncHandler`**: wraps route handlers so rejected promises reach Express `next(err)` instead of becoming unhandled rejections.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases

- Errors thrown **after** `await` in `try` are caught; errors in `.then` without `.catch` are not unless chained.
- **`throw` in `.then`** on a floating promise → unhandled rejection.
- **Multiple `await` in one `try`**: first failure skips rest; use `Promise.allSettled` if you need all outcomes.

</details>

</article>

<article>

Write a function that takes an array and a number as an argument. if the number is greater than 0, you must pop the number of elements from the array. if the number is not provided then pop once.

<details><summary>Theory and explanation</summary>

`Array.prototype.pop()` removes and returns the **last** element, mutating the array in place. The interview asks you to generalize: pop **once** by default, or pop **`n` times** when a positive number is given.

Key ideas:

- **Mutation**: `pop` changes the original array; callers who need immutability should copy first (`[...arr]` or `arr.slice()`).
- **`n` not provided**: treat as `1` (one pop). In JavaScript, `undefined` is falsy; use `n ?? 1` or explicit checks—not `n || 1` if `0` should mean “pop zero times” (here the spec says only pop when `n > 0`, else default once).
- **`n <= 0`**: clarify in interview: typically pop **once** when omitted, and **zero** pops when `n` is 0 or negative (no-op), unless they say otherwise.
- **Empty array**: `pop` on empty returns `undefined`; looping `n` times is safe but returns `undefined` each time.

Returning **popped values** vs only mutating: interview may want an array of removed elements or the final array—state your contract.

#### Further reading

- [MDN: Array.prototype.pop()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop) — behavior and return value
- [MDN: Nullish coalescing (??)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing) — default when `n` is `undefined`
- [MDN: Spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) — copying before mutate

</details>

<details><summary>Solution (JavaScript)</summary>

```js
/**
 * Pop elements from the end of arr.
 * @param {unknown[]} arr - mutated in place
 * @param {number} [n] - if omitted, pop once; if > 0, pop n times
 * @returns {unknown[]} removed elements (last popped first in array order)
 */
function popMany(arr, n) {
  const times = n === undefined ? 1 : n > 0 ? Math.floor(n) : 0;
  const removed = [];
  for (let i = 0; i < times; i++) {
    removed.push(arr.pop());
  }
  return removed;
}

// Example
const data = [1, 2, 3, 4, 5];
popMany(data, 2); // data -> [1, 2, 3], returns [5, 4]
popMany(data);    // data -> [1, 2], returns [3]
```

#### Code walkthrough

1. **`times`**: `undefined` → 1 pop; positive `n` → `Math.floor(n)` pops; zero or negative → 0 pops (no-op per “only if greater than 0” for the multiplier; default handles missing arg).
2. **Loop**: each `pop()` removes from the end; collected in `removed`.
3. **Return**: `removed` lists popped values with most recently popped last in `removed` (order of push).

#### Complexity

| | |
|-|-|
| Time | O(k) where k is the number of pops (each pop is O(1) amortized) |
| Space | O(k) for the `removed` array if you return popped values; O(1) extra if you only mutate |

#### Edge cases

- **Empty array**: `pop()` returns `undefined`; still O(k) iterations.
- **n larger than length**: array becomes `[]`; extra pops yield `undefined`.
- **Non-integer n**: `Math.floor` avoids fractional loop counts.
- **Not an array**: validate with `Array.isArray(arr)` in production code.

</details>

</article>

<article>

What is event driven programming? How event driven programming works in JavaScript?

<details><summary>Theory and explanation</summary>

**Event-driven programming (EDP)** is a paradigm where program flow is determined by **events** (user input, I/O completion, timers, messages) and **handlers** (callbacks, listeners) registered to react to those events, rather than a single linear script that polls for changes.

**Core pieces**

1. **Event producer** — button click, HTTP request, `setTimeout`, file read completion.
2. **Event channel / dispatcher** — browser DOM, Node.js `EventEmitter`, WebSocket, message queue.
3. **Event handler** — function invoked when the event fires; may enqueue more async work.

**How it works in JavaScript**

- **Browser**: DOM events (`click`, `submit`), `fetch` + promises, `message` from Web Workers. The **event loop** takes tasks from the macrotask queue (timers, I/O) and microtask queue (promise reactions) and runs them when the call stack is empty.
- **Node.js**: Built on libuv; I/O is non-blocking. `EventEmitter` (`emitter.on('data', handler)`) is the canonical pattern; many streams and servers extend it.
- **React** (relevant to Bevy interviews): Synthetic events wrap DOM events; state updates schedule re-renders—still event-driven at the UI layer.

**Contrast with synchronous batch processing**

- EDP scales to many concurrent connections without one thread per request (on the server).
- Downsides: harder debugging, callback/promise discipline, risk of unhandled async errors.

**Interview talking points**

- Draw the loop: run script → complete sync code → process microtasks → next macrotask.
- Mention **debouncing** / **throttling** as event-driven UX patterns.
- Node: `process.nextTick` vs `setImmediate` ordering (advanced).

#### Further reading

- [MDN: Introduction to web events](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events) — browser event model
- [Node.js: Events](https://nodejs.org/api/events.html) — `EventEmitter` API
- [MDN: Event loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Event_loop) — how JS schedules work
- [What the heck is the event loop anyway? (Philip Roberts)](https://www.youtube.com/watch?v=8aGhZQkoFbQ) — visual explanation of call stack and queues
- [Node.js: Timers](https://nodejs.org/api/timers.html) — `setTimeout` / `setImmediate` in the loop

</details>

<details><summary>Solution (JavaScript)</summary>

```js
const { EventEmitter } = require('events');

// Node-style EventEmitter
const bus = new EventEmitter();

bus.on('order:placed', (order) => {
  console.log('Notify warehouse', order.id);
});

bus.on('order:placed', (order) => {
  console.log('Send receipt email', order.id);
});

bus.emit('order:placed', { id: 'ORD-42' });

// Browser-style (if running in DOM environment)
// document.getElementById('buy').addEventListener('click', () => {
//   console.log('User clicked buy');
// });
```

#### Code walkthrough

- **`EventEmitter`**: register multiple listeners with `.on(event, fn)`; `.emit(event, payload)` invokes all synchronously in registration order (unless using `once` or removing listeners).
- **Decoupling**: producers do not call warehouse/email directly—they emit one event; subscribers handle side effects (open/closed for extension).
- **DOM**: same idea with `addEventListener` and user gestures driving handlers.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual); emitting to `k` listeners is O(k) |
| Space | N/A (conceptual); listeners stored until removed |

#### Edge cases

- **Listener throws**: other listeners may not run unless error is isolated; use `try/catch` in emit wrappers in production.
- **Memory leaks**: remove listeners (`off`) when components unmount (React `useEffect` cleanup).
- **Sync emit stack**: long sync handlers block the event loop.

</details>

</article>

<article>

Given an array of integers, find the second max of the array

<details><summary>Theory and explanation</summary>

The **second maximum** is the largest value that is strictly less than the maximum, or—if duplicates exist—the second distinct largest value. Clarify with the interviewer:

- **Distinct second max**: `[5, 5, 3]` → max `5`, second max `3`.
- **Second largest element by sorting**: might be `5` again if duplicates count.

The efficient approach tracks **`max`** and **`secondMax`** in one pass:

- Initialize both to `-Infinity` (or use first two elements after validation).
- For each `x`: if `x > max`, shift old `max` to `secondMax`, set `max = x`; else if `x > secondMax && x < max`, update `secondMax`; else if duplicates allowed and `x === max`, second max may still be below `max` from earlier distinct values.

If fewer than two distinct values exist, return `null` or throw.

**Alternative**: sort descending O(n log n) and scan for first value `< max`—simpler but slower.

#### Further reading

- [MDN: Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) — iteration methods
- [LeetCode discussion: Second Largest Element](https://leetcode.com/discuss/) — many variations tagged array-scan
- [GeeksforGeeks: Second largest element in an array](https://www.geeksforgeeks.org/find-second-largest-element-array/) — single-pass approach walkthrough

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function secondMax(nums) {
  if (!Array.isArray(nums) || nums.length < 2) return null;

  let max = -Infinity;
  let second = -Infinity;

  for (const x of nums) {
    if (x > max) {
      second = max;
      max = x;
    } else if (x < max && x > second) {
      second = x;
    }
  }

  return second === -Infinity ? null : second;
}

// Examples
secondMax([10, 3, 8, 10, 1]); // 8
secondMax([5, 5, 5]);         // null (no distinct second)
```

#### Code walkthrough

1. Reject arrays with fewer than two elements (or no distinct second).
2. **`x > max`**: previous max becomes candidate for second; update max.
3. **`x < max && x > second`**: `x` is strictly between second and max.
4. **`x === max`**: does not update second (distinct second max definition).
5. If `second` never moved from `-Infinity`, no valid second exists.

#### Complexity

| | |
|-|-|
| Time | O(n) — single pass |
| Space | O(1) — only two scalars |

#### Edge cases

- **All equal**: return `null`.
- **Single element**: return `null`.
- **Negative numbers**: `-Infinity` initialization works.
- **Two elements**: `[1, 2]` → `1`.

</details>

</article>

<article>

Given an array of integers and a sorting criteria[asc/desc], sort the array based on the sorting criteria in either ascending or descending order

<details><summary>Theory and explanation</summary>

Sorting rearranges elements into non-decreasing (**asc**) or non-increasing (**desc**) order by a comparison function.

In JavaScript, **`Array.prototype.sort(compareFn)`** sorts **in place** (mutates the array) and uses a stable sort in modern engines (V8). If `compareFn` is omitted, elements are converted to strings and sorted lexicographically—which is wrong for numeric arrays—so always pass a comparator for numbers.

**Comparator contract**

- Return **negative** if `a` should come before `b`
- Return **positive** if `a` should come after `b`
- Return **0** if order does not matter

For ascending numeric: `(a, b) => a - b`. For descending: `(a, b) => b - a`.

**Complexity**: comparison sorts are typically **O(n log n)** time; extra space depends on engine (often O(log n) for stack).

**Interview extras**

- Do not mutate input if forbidden—copy with `slice()` first.
- For large data or nearly sorted input, mention **Timsort** (used by V8) or specialized sorts.
- **Stability** matters when sorting objects by one key.

#### Further reading

- [MDN: Array.prototype.sort()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort) — comparator and mutation warning
- [MDN: Sorting with a comparator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#sorting_with_a_comparator) — examples
- [Visualgo: Sorting](https://visualgo.net/en/sorting) — algorithm intuition
- [V8 blog: Stable sort](https://v8.dev/blog/array-sort) — modern JS sort behavior

</details>

<details><summary>Solution (JavaScript)</summary>

```js
/**
 * @param {number[]} arr - will be copied unless mutate=true
 * @param {'asc' | 'desc'} criteria
 * @param {boolean} [mutate=false]
 * @returns {number[]}
 */
function sortByCriteria(arr, criteria, mutate = false) {
  const out = mutate ? arr : arr.slice();
  const factor = criteria === 'desc' ? -1 : 1;
  out.sort((a, b) => (a - b) * factor);
  return out;
}

sortByCriteria([3, 1, 4, 1, 5], 'asc');  // [1, 1, 3, 4, 5]
sortByCriteria([3, 1, 4, 1, 5], 'desc'); // [5, 4, 3, 1, 1]
```

#### Code walkthrough

1. **`slice()`** avoids mutating the caller’s array unless `mutate` is true.
2. **`factor`**: multiplying `(a - b)` by `-1 reverses order for descending.
3. **`sort`** uses numeric subtraction; safe for integers in JS; for floats or large integers consider `Intl.Collator` or BigInt-specific compare.

#### Complexity

| | |
|-|-|
| Time | O(n log n) average for comparison sort |
| Space | O(n) if copying input; O(log n) typical auxiliary for sort stack |

#### Edge cases

- **Invalid criteria**: validate `asc` / `desc`; throw or default.
- **Empty array**: returns `[]`.
- **Already sorted**: still O(n log n) unless engine optimizes nearly sorted runs.
- **Lexicographic pitfall**: `[10, 2].sort()` without comparator → `[10, 2]` string order.

</details>

</article>
