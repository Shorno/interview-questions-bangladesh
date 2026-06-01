# Appscode Limited

|                   |                       |
| :---------------- | :-------------------- |
| Founding year     | 2016                  |
| Company Website   | https://appscode.com/ |
| Career Website    |                       |
| Technologies Used |                       |

## Introduction
AppsCode is a Kubernetes solution provider. They have several products including production grade database, backup and recovery solution, authentication webhook etc.

## Interview Stages:

Appscode generally gives a google form for the applicants. Based on the application form they call for the written exam.
1. **Written Exam**:	In-person 
2. **Technical Interview**:   1 technical round with CEO
3. **HR Interview**:	1 HR round

## Topics:

- Programming Fundamentals
- Data Structures and Algorithms
- API design
- SQL
- Regular expressions
- Encryption
- Basic HTML and CSS

## Questions
Questions from the written exam took place on May 1, 2025 

<article>

Given a array of numbers. You have to perform a number of queries. Each queries ask for the average of numbers from a range.

<details><summary>Theory and explanation</summary>

This is **range average query** on a static array. Average on `[L, R]` = `(sum(L, R)) / (R - L + 1)`.

**Approaches**

| Method | Preprocess | Query |
|--------|------------|-------|
| **Brute force** | O(1) | O(n) per query |
| **Prefix sum** | O(n) | O(1) per query |

Build `prefix[i] = sum(arr[0..i-1])` with `prefix[0] = 0`. Then:

`sum(L, R) = prefix[R+1] - prefix[L]`

Average = that sum divided by count.

**Follow-ups interviewers may ask**

- **Updates** to array → Fenwick tree or segment tree O(log n) per update/query.
- **Floating output** — precision/format requirements.

#### Further reading

- [CP-Algorithms: Prefix sums](https://cp-algorithms.com/algebra/prefix-sums.html) — range sum in O(1)
- [LeetCode 303: Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) — same prefix technique
- [GeeksforGeeks: Prefix sum array](https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/) — applications

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class RangeAverageQuery {
  constructor(nums) {
    this.prefix = [0];
    for (const x of nums) {
      this.prefix.push(this.prefix.at(-1) + x);
    }
  }

  average(left, right) {
    const sum = this.prefix[right + 1] - this.prefix[left];
    const count = right - left + 1;
    return sum / count;
  }
}

const raq = new RangeAverageQuery([1, 2, 3, 4, 5]);
raq.average(1, 3); // (2+3+4)/3 = 3
```

#### Code walkthrough

1. Build prefix sums once in constructor.
2. Range sum via difference of prefix at `right+1` and `left`.
3. Divide by element count for average.

#### Complexity

| | |
|-|-|
| Time | O(n) preprocess; O(1) per query |
| Space | O(n) prefix array |

#### Edge cases

- **Empty range** — invalid if `left > right`.
- **Integer overflow** — use 64-bit or BigInt for large sums in other languages.
- **Single element range** — average equals that element.

</details>

</article>

<article>

A dynamic programming problem.(Similar to 0/1 knapsack)

<details><summary>Theory and explanation</summary>

The **0/1 knapsack** problem: given item weights `w[i]`, values `v[i]`, and capacity `W`, maximize total value choosing each item **at most once**.

**Recurrence**

Let `dp[i][c]` = max value using first `i` items with capacity `c`.

`dp[i][c] = max(dp[i-1][c], v[i] + dp[i-1][c - w[i]])` if `w[i] <= c`

**Space optimization**

Use 1D array `dp[c]` iterated **backwards** over capacity to avoid reusing item i twice:

```text
for each item i:
  for c from W down to w[i]:
    dp[c] = max(dp[c], dp[c - w[i]] + v[i])
```

**Similar AppsCode variants**

- Subset sum (can we reach target?)
- Partition equal subset sum
- Count knapsack combinations

Always clarify whether items are **0/1**, **unbounded**, or **bounded** count.

#### Further reading

- [LeetCode 416: Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) — 0/1 knapsack disguised
- [CP-Algorithms: Knapsack problem](https://cp-algorithms.com/dynamic_programming/knapsack.html) — full treatment
- [Visualgo: DP knapsack](https://visualgo.net/en/recursion) — recursion tree intuition

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function knapsack01(weights, values, capacity) {
  const dp = new Array(capacity + 1).fill(0);

  for (let i = 0; i < weights.length; i++) {
    const w = weights[i];
    const v = values[i];
    for (let c = capacity; c >= w; c--) {
      dp[c] = Math.max(dp[c], dp[c - w] + v);
    }
  }
  return dp[capacity];
}

knapsack01([1, 3, 4, 5], [1, 4, 5, 7], 7); // 9 (items 3+4)
```

#### Code walkthrough

1. `dp[c]` stores best value achievable at capacity `c` so far.
2. Process each item once; inner loop **descending** enforces 0/1 constraint.
3. Answer is `dp[capacity]`.

#### Complexity

| | |
|-|-|
| Time | O(n × W) |
| Space | O(W) |

#### Edge cases

- **Zero capacity** — return 0.
- **Item heavier than capacity** — skipped naturally.
- **All zero weight** — clarify if items can be taken together unboundedly (different problem).

</details>

</article>

<article>

How does trie works. Implementation of trie.

<details><summary>Theory and explanation</summary>

A **trie** (prefix tree) stores strings character-by-character in a tree. Each node represents a prefix; edges labeled with characters; nodes mark **end of word**.

**Operations**

- **Insert** — walk/create nodes per character; mark terminal at end.
- **Search** — follow edges; check terminal flag for full word.
- **StartsWith** — same walk; no terminal required.

**Complexity**

- Insert/search: **O(L)** where L = key length.
- Space: O(total characters stored) — can be heavy for long alphabets; compress with **radix tree**.

**Use cases**

- Autocomplete, spell check, IP routing tables, word games.

**AppsCode relevance**

- Kubernetes/etcd paths, DNS-like prefix matching, configuration key namespaces.

#### Further reading

- [LeetCode 208: Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) — standard interview problem
- [GeeksforGeeks: Trie insert and search](https://www.geeksforgeeks.org/trie-insert-and-search/) — step-by-step
- [Wikipedia: Radix tree](https://en.wikipedia.org/wiki/Radix_tree) — compressed trie variant

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class TrieNode {
  constructor() {
    this.children = new Map();
    this.isEnd = false;
  }
}

class Trie {
  constructor() {
    this.root = new TrieNode();
  }

  insert(word) {
    let node = this.root;
    for (const ch of word) {
      if (!node.children.has(ch)) node.children.set(ch, new TrieNode());
      node = node.children.get(ch);
    }
    node.isEnd = true;
  }

  search(word) {
    const node = this._walk(word);
    return Boolean(node && node.isEnd);
  }

  startsWith(prefix) {
    return this._walk(prefix) !== null;
  }

  _walk(str) {
    let node = this.root;
    for (const ch of str) {
      if (!node.children.has(ch)) return null;
      node = node.children.get(ch);
    }
    return node;
  }
}
```

#### Code walkthrough

1. **`insert`** — create child map entries per character; set `isEnd` on last node.
2. **`search`** — `_walk` entire word; require `isEnd`.
3. **`startsWith`** — `_walk` prefix; any complete path suffices.

#### Complexity

| | |
|-|-|
| Time | O(L) per operation |
| Space | O(N × L_avg) nodes in worst case |

#### Edge cases

- **Empty string** — define if allowed as word.
- **Duplicate inserts** — idempotent if `isEnd` already set.
- **Case sensitivity** — normalize or store separate branches.

</details>

</article>

<article>

What is hashing? How does it work? What is hash collision?

<details><summary>Theory and explanation</summary>

**Hashing** maps data of arbitrary size to a fixed-size **hash code** via a **hash function** `h(key)`.

**Hash table** uses hash codes to index into buckets storing key-value pairs:

1. Compute `index = h(key) mod bucket_count`.
2. Store/lookup in bucket `index`.

**Properties of good hash functions**

- **Deterministic** — same key → same hash.
- **Uniform distribution** — reduces collisions.
- **Avalanche** — small input change → large hash change (cryptographic hashes).
- Fast to compute for hash tables; slow OK for password hashing (bcrypt, argon2).

**Hash collision**

Two distinct keys `k1 ≠ k2` with `h(k1) = h(k2)` (or same bucket index).

**Collision resolution**

| Strategy | Idea |
|----------|------|
| **Chaining** | Bucket holds linked list / tree of entries |
| **Open addressing** | Probe next slots (linear, quadratic, double hashing) |

**Security note**

- Cryptographic hashing (SHA-256) ≠ hash table hashing (Murmur, FNV).
- Passwords need **salt + slow hash** — never plain SHA alone.

#### Further reading

- [MDN: Map object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) — JS hash map semantics
- [Wikipedia: Hash table](https://en.wikipedia.org/wiki/Hash_table) — collision strategies
- [OWASP: Password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) — bcrypt/argon2 vs fast hashes

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class SimpleHashMap {
  constructor(size = 16) {
    this.buckets = Array.from({ length: size }, () => []);
  }

  _hash(key) {
    let h = 0;
    const s = String(key);
    for (let i = 0; i < s.length; i++) {
      h = (h * 31 + s.charCodeAt(i)) >>> 0;
    }
    return h % this.buckets.length;
  }

  set(key, value) {
    const idx = this._hash(key);
    const bucket = this.buckets[idx];
    const existing = bucket.find(([k]) => k === key);
    if (existing) existing[1] = value;
    else bucket.push([key, value]);
  }

  get(key) {
    const bucket = this.buckets[this._hash(key)];
    const pair = bucket.find(([k]) => k === key);
    return pair ? pair[1] : undefined;
  }
}
```

#### Code walkthrough

1. **`_hash`** — polynomial rolling hash mod bucket count.
2. **`set/get`** — **chaining** via arrays in each bucket; update if key exists.
3. Collisions handled by scanning small chain in bucket.

#### Complexity

| | |
|-|-|
| Time | Average O(1) insert/lookup; worst O(n) if all keys collide |
| Space | O(n + buckets) |

#### Edge cases

- **Load factor high** — rehash to larger bucket array.
- **Mutable keys** — if key object changes hash, lookup breaks (use immutable keys).
- **Negative mod in other languages** — normalize index to `[0, size)`.

</details>

</article>

<article>

Design an API for a music streaming platform like Spotify

<details><summary>Theory and explanation</summary>

Design **RESTful (or GraphQL) APIs** for core Spotify-like flows: catalog browse, search, playlists, playback metadata, user library.

**Core resources**

| Resource | Endpoints (examples) |
|----------|---------------------|
| **Tracks** | `GET /v1/tracks/{id}`, `GET /v1/albums/{id}/tracks` |
| **Artists** | `GET /v1/artists/{id}`, `GET /v1/artists/{id}/albums` |
| **Search** | `GET /v1/search?q=&type=track,artist,album&limit=&offset=` |
| **Playlists** | `POST /v1/playlists`, `PUT /v1/playlists/{id}/tracks` |
| **User library** | `POST /v1/me/tracks`, `GET /v1/me/playlists` |
| **Playback** | `GET /v1/me/player`, `PUT /v1/me/player/play` (device model) |

**Design principles**

- **Versioning** — `/v1/` prefix.
- **Pagination** — `limit`, `offset` or cursor `next`.
- **Auth** — OAuth2 Bearer tokens; scopes (`user-read-private`, `playlist-modify`).
- **Rate limiting** — `429` + `Retry-After`.
- **Consistent errors** — `{ error: { code, message } }`.
- **HATEOAS optional** — `_links` for related resources.

**Non-functional**

- CDN for static artwork; cache hot catalog in Redis.
- Search via Elasticsearch.
- Idempotent `PUT` for playlist edits with `If-Match` etag.

#### Further reading

- [Spotify Web API reference](https://developer.spotify.com/documentation/web-api) — real-world model
- [Microsoft REST API guidelines](https://github.com/microsoft/api-guidelines/blob/vNext/azure/Guidelines.md) — naming and pagination
- [OAuth 2.0 RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749) — authorization for user resources

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// Illustrative OpenAPI-style route map
const routes = {
  'GET /v1/search': 'SearchController.search',
  'GET /v1/tracks/:id': 'TrackController.get',
  'GET /v1/albums/:id/tracks': 'AlbumController.listTracks',
  'POST /v1/users/:userId/playlists': 'PlaylistController.create',
  'PUT /v1/playlists/:id/tracks': 'PlaylistController.addTracks',
  'GET /v1/me/player': 'PlayerController.getState',
  'PUT /v1/me/player/play': 'PlayerController.startPlayback',
};

// Example JSON: POST /v1/users/{id}/playlists
const createPlaylistBody = {
  name: 'Interview Mix',
  description: 'AppsCode exam prep',
  public: false,
};
```

#### Code walkthrough

- Separate **catalog** (public read) from **user** (`/me`) resources.
- **Search** unified endpoint with `type` filter reduces client round trips.
- **Playback** endpoints coordinate devices — stateful resource requiring active device id.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases

- **Region licensing** — track availability varies by country header.
- **Explicit content** — filter flag on search/playlists.
- **Offline downloads** — separate mobile sync API (mention if asked).

</details>

</article>

<article>

Design the schema and write queries like fetching the top 10 songs of the previous month.

<details><summary>Theory and explanation</summary>

**Relational schema (minimal streaming analytics)**

```text
artists(id, name)
albums(id, artist_id, title, released_at)
tracks(id, album_id, title, duration_ms)
users(id, username)
plays(id, user_id, track_id, played_at)  -- event log
```

**Top 10 songs previous month**

- Filter `plays.played_at` to `[first_day_last_month, first_day_this_month)`.
- `GROUP BY track_id`, `COUNT(*)` as play_count.
- Join `tracks` for title; order desc; `LIMIT 10`.

**Indexes**

- `(played_at)` or `(played_at, track_id)` on `plays` for time-range aggregates.
- Consider **monthly rollup table** `track_plays_monthly(track_id, year, month, play_count)` for faster dashboards.

**Follow-ups**

- Top by **unique listeners** → `COUNT(DISTINCT user_id)`.
- Exclude bots / short plays → `WHERE listened_seconds > 30`.

#### Further reading

- [PostgreSQL: GROUP BY and aggregates](https://www.postgresql.org/docs/current/queries-table-expressions.html#QUERIES-GROUP) — top-N queries
- [Spotify Wrapped engineering posts](https://engineering.atspotify.com/) — scale inspiration for play counts
- [Use The Index, Luke: Indexing for sorting/grouping](https://use-the-index-luke.com/) — performance tuning

</details>

<details><summary>Solution (JavaScript)</summary>

```sql
-- Schema (PostgreSQL)
CREATE TABLE tracks (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL
);

CREATE TABLE plays (
  id BIGSERIAL PRIMARY KEY,
  track_id INT REFERENCES tracks(id),
  user_id INT NOT NULL,
  played_at TIMESTAMPTZ NOT NULL
);

CREATE INDEX idx_plays_played_at ON plays (played_at);

-- Top 10 tracks by play count in the previous calendar month
SELECT
  t.id,
  t.title,
  COUNT(*) AS play_count
FROM plays p
JOIN tracks t ON t.id = p.track_id
WHERE p.played_at >= date_trunc('month', CURRENT_DATE - INTERVAL '1 month')
  AND p.played_at < date_trunc('month', CURRENT_DATE)
GROUP BY t.id, t.title
ORDER BY play_count DESC
LIMIT 10;
```

#### Code walkthrough

1. **`date_trunc('month', ...)`** bounds the previous calendar month cleanly.
2. **Join** plays to tracks for human-readable titles.
3. **Aggregate** with `COUNT(*)`, sort, limit 10.

#### Complexity

| | |
|-|-|
| Time | O(rows in month) with index on `played_at` |
| Space | O(tracks) for aggregation hash |

#### Edge cases

- **Ties at rank 10** — use `DENSE_RANK()` if all tied songs should appear.
- **Timezone** — use UTC or user locale consistently.
- **No plays** — empty result set.

</details>

</article>

<article>

Write a regex validator for email.

<details><summary>Theory and explanation</summary>

**Email validation** in production has two layers:

1. **Syntax** — reasonable regex or parser for local@domain structure.
2. **Deliverability** — DNS MX lookup, confirmation email (regex alone is never sufficient).

**RFC 5322** full grammar is too complex for most interviews; exam expects a **practical pattern**:

- Local part: letters, digits, `.`, `_`, `%`, `+`, `-`
- `@` separator
- Domain: labels separated by `.`, TLD at least 2 chars

**JavaScript note**

- Use `RegExp` or `pattern` attribute; avoid catastrophic backtracking on long strings.
- **HTML5** `<input type="email">` uses built-in validation for forms.

**Security**

- Validate length limits (local ≤ 64, domain ≤ 255 typical guidance).
- Do not use regex alone for auth identifiers without normalization (lowercase domain).

#### Further reading

- [MDN: Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions) — JS regex syntax
- [RFC 5322 (email format)](https://datatracker.ietf.org/doc/html/rfc5322) — formal grammar
- [OWASP: Input validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) — defense in depth beyond regex

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function isValidEmail(email) {
  if (typeof email !== 'string' || email.length > 320) return false;
  const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return re.test(email.trim());
}

isValidEmail('user.name+tag@appscode.com'); // true
isValidEmail('bad@domain');               // false
```

#### Code walkthrough

1. Length guard prevents absurd input and ReDoS on huge strings.
2. Pattern checks local@domain.tld structure with common allowed characters.
3. `trim()` handles accidental whitespace.

#### Complexity

| | |
|-|-|
| Time | O(n) on email length |
| Space | O(1) |

#### Edge cases

- **Plus addressing** (`user+tag@domain`) — allowed by pattern.
- **Internationalized domain (IDN)** — punycode `xn--` not covered by simple ASCII regex.
- **Quoted local parts** (`"weird"@example.com`) — rare; usually rejected in practical validators.

</details>

</article>

<article>

What is the difference between `div` and `span` 

<details><summary>Theory and explanation</summary>

Both are generic HTML containers, but they differ in **default display** and **semantic usage**.

| | `<div>` | `<span>` |
|---|---------|----------|
| **Display** | Block-level (starts new line, takes full width available) | Inline (flows with text, no line break) |
| **Typical use** | Page sections, layout groups, cards, wrappers for block content | Inline styling, highlight word/phrase inside paragraph |
| **Nesting** | Often contains other blocks | Usually inside phrasing content |
| **Semantics** | Neutral; prefer semantic tags (`section`, `article`, `nav`) when applicable | Neutral inline grouping |

**CSS can change display** — `display: inline-block` on `div` or `display: block` on `span` blurs visual difference; HTML default still matters for accessibility tree and reset styles.

**Interview talking points**

- Neither adds inherent meaning — choose semantic elements when possible.
- `span` for applying class to part of sentence; `div` for layout flex/grid children.
- AppsCode exam includes **basic HTML/CSS** alongside backend topics.

#### Further reading

- [MDN: div element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div) — block container
- [MDN: span element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/span) — inline container
- [MDN: Block and inline layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_display/Block_and_inline_layout) — display types

</details>

<details><summary>Solution (JavaScript)</summary>

```html
<!-- div: block-level layout sections -->
<div class="card">
  <h2>AppsCode Products</h2>
  <p>Kubernetes tools for production clusters.</p>
</div>

<!-- span: inline phrase styling -->
<p>
  Contact us at
  <span class="highlight">support@appscode.com</span>
  for help.
</p>
```

```css
.card {
  display: block;
  margin-bottom: 1rem;
  padding: 1rem;
  border: 1px solid #ccc;
}
.highlight {
  color: #0066cc;
  font-weight: 600;
}
```

#### Code walkthrough

- **`div.card`** stacks as block — occupies row, wraps heading and paragraph.
- **`span.highlight`** styles only the email inside the sentence without breaking line flow.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases

- **Accessibility** — neither is focusable; use `<button>` or `<a>` for interactive inline controls.
- **Over-nesting divs** — "div soup"; refactor with semantic HTML5 elements.

</details>

</article>

## Contributors
- Interview applicant [Pulok Saha](https://bd.linkedin.com/in/pulok-saha-23b765212)
