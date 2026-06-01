---
description: Pathao interview questions, Pathao interview stages, Pathao frontend interview details, Pathao interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/pathao
---
# Pathao

|                   |                                     |
| :---------------- | :---------------------------------- |
| Founding year     | 2015                                |
| Company Website   | https://pathao.com                  |
| Career Website    | https://career.pathao.com/#position |
| Technologies Used | JavaScript, React, Vue, Nuxt        |

## Introduction

Pathao started as an app-based courier service and has grown into a **super-app** covering ride sharing, rentals, food delivery, groceries, and more. They also operate **Pathao Pay** (digital wallet) and products like Pathao Maps. Frontend hiring for roles such as **Associate Software Engineer (Frontend)** emphasizes **JavaScript**, **React**, and practical UI building.

## Interview Stages

Recent **Associate Software Engineer (Frontend)** hiring follows four stages:

1. **Initial Interview** — In-person; resume, projects, and React/JavaScript fundamentals.
2. **Take Home Assessment** — Trello-like kanban board with drag-and-drop; submit on GitHub (~1 week).
3. **On-site Assessment** — 5–6 hours; e-commerce dashboard CRUD built with **Nuxt.js** (Vue stack).
4. **Final Interview** — With CTO and HR; discussion of on-site work, graph/DSA topics, and behavioral questions.

## Initial Interview Questions

<article>

What is the difference between React **Context** and component **state**?

<details><summary>Theory and explanation</summary>

**Component state** (`useState`, `useReducer`) is **local or lifted** to a parent that owns it. Updating state re-renders that component (and children receiving changed props). State is ideal for UI that belongs to one subtree (form inputs, toggles, modal open/close).

**Context** (`createContext`, `Provider`, `useContext`) is a **dependency-injection channel** for values that many distant components need without prop drilling — theme, locale, authenticated user, feature flags.

| | State | Context |
|-|-------|---------|
| Scope | Component subtree via props | Any consumer under `Provider` |
| Updates | `setState` / dispatch in owner | Update value at Provider (often paired with state/reducer) |
| Re-renders | Owner + affected children | **All consumers** re-render when context value changes (unless split contexts or memoized) |
| Best for | Local UI, lifted shared state in one branch | Cross-cutting read-mostly or global app data |

**Common mistake in interviews**

Saying Context "replaces Redux." Context solves **prop drilling**, not necessarily **complex async updates**, middleware, devtools, or fine-grained subscriptions — that is where **Zustand/Redux** fit.

**Pathao angle**

Kanban boards need **local state** per card/column drag and **lifted or global state** for board data — explain when you would use Context (current user, theme) vs colocated state (drag preview).

#### Further reading

- [React: Passing data deeply with Context](https://react.dev/learn/passing-data-deeply-with-context) — official mental model
- [React: Sharing state between components](https://react.dev/learn/sharing-state-between-components) — lifting state up
- [React: useState](https://react.dev/reference/react/useState) — local state API
- [Kent C. Dodds: How to use React Context effectively](https://kentcdodds.com/blog/how-to-use-react-context-effectively) — avoid overusing Context

</details>

<details><summary>Solution (JavaScript)</summary>

```jsx
import { createContext, useContext, useState } from 'react';

const ThemeContext = createContext('light');

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

function Toolbar() {
  const { theme, setTheme } = useContext(ThemeContext);
  return (
    <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
      Toggle theme ({theme})
    </button>
  );
}

function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount((c) => c + 1)}>{count}</button>;
}
```

#### Code walkthrough

1. **Counter** uses **local state** — only Counter re-renders on click.
2. **ThemeProvider** holds theme **state** and exposes it via **Context**.
3. **Toolbar** reads context — no props from App needed.
4. Splitting Context (theme vs auth) avoids unrelated re-renders.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases

- **Default context value** used when no Provider — document fallbacks.
- **New object every render** as Provider value → all consumers re-render; memoize with `useMemo`.
- **High-frequency updates** (drag position) — prefer local state or external store, not Context.

</details>

</article>

<article>

What is the difference between **Zustand** and **Redux**?

<details><summary>Theory and explanation</summary>

Both are **client-side state containers** for React (and beyond). They centralize state outside the component tree and offer predictable updates.

| | Redux (Toolkit) | Zustand |
|-|---------------|---------|
| Boilerplate | Store, slices, actions, reducers (RTK reduces this) | Minimal — `create(set => ({ ... }))` |
| Update model | Dispatch actions → reducers → new state | Call `set` or imperative methods on store |
| DevTools | Excellent time-travel | Supported via middleware |
| Middleware | Thunks, sagas, listeners | Middleware optional, simpler |
| Selectors | `useSelector` + memoization | Subscribe to slices of state |
| Learning curve | Steeper (conventions, immutability) | Gentle for small/medium apps |
| Bundle | Larger (especially with ecosystem) | ~1 KB scale |

**When Redux shines**

Large teams, complex async flows, strict action logs, many cross-slice dependencies, existing Redux codebase (Pathao-scale super-apps may use formal patterns).

**When Zustand shines**

Medium apps, quick prototypes, kanban/trello UIs, when you want global state without ceremony.

**Interview talking points**

- Both encourage **single source of truth** vs scattered `useState`.
- Redux enforces **unidirectional data flow** explicitly; Zustand is flexible but can become messy without discipline.
- Neither replaces **server state** — pair with React Query/SWR for API cache.

#### Further reading

- [Redux Toolkit: Quick start](https://redux-toolkit.js.org/tutorials/quick-start) — modern Redux setup
- [Zustand docs](https://docs.pmnd.rs/zustand/getting-started/introduction) — API and patterns
- [Redux: Immutable update patterns](https://redux.js.org/usage/structuring-reducers/ImmutableUpdatePatterns) — why reducers return new state
- [React Query docs](https://tanstack.com/query/latest) — server vs client state split

</details>

<details><summary>Solution (JavaScript)</summary>

Redux Toolkit slice vs Zustand store for a kanban **board list**:

```js
// --- Zustand ---
import { create } from 'zustand';

export const useBoardStore = create((set) => ({
  boards: [],
  addBoard: (title) =>
    set((s) => ({ boards: [...s.boards, { id: crypto.randomUUID(), title }] })),
  removeBoard: (id) =>
    set((s) => ({ boards: s.boards.filter((b) => b.id !== id) })),
}));
```

```js
// --- Redux Toolkit ---
import { createSlice } from '@reduxjs/toolkit';

const boardsSlice = createSlice({
  name: 'boards',
  initialState: { items: [] },
  reducers: {
    addBoard(state, action) {
      state.items.push({ id: crypto.randomUUID(), title: action.payload });
    },
    removeBoard(state, action) {
      state.items = state.items.filter((b) => b.id !== action.payload);
    },
  },
});

export const { addBoard, removeBoard } = boardsSlice.actions;
export default boardsSlice.reducer;
```

#### Code walkthrough

1. **Zustand** — one function, direct `set`, hook `useBoardStore()` in components.
2. **Redux** — actions describe *what happened*; reducer produces next state (Immer makes mutation syntax safe in RTK).
3. Same domain logic; different ceremony and DevTools integration.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases

- **Persist to localStorage** — both support middleware/persist plugins.
- **SSR (Nuxt vs Next)** — Redux often needs per-request store; Zustand needs hydration care too.

</details>

</article>

<article>

What is a **reducer** function in React state management?

<details><summary>Theory and explanation</summary>

A **reducer** is a pure function `(state, action) => newState` that describes **how state transitions** in response to **actions** (events with a `type` and optional payload).

```js
function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    default:
      return state;
  }
}
```

**Rules**

1. **Pure** — no side effects, same inputs → same output.
2. **Immutable updates** — return new objects/arrays; do not mutate `state` (except RTK + Immer internally).
3. **Centralized transitions** — all valid state changes go through the reducer.

**Where it appears**

- `useReducer(reducer, initialState)` — React built-in for complex local state.
- **Redux** — single app reducer (or combined slices).
- **React Context + useReducer** — lightweight global store pattern.

**Why reducers help**

- Easier to test (`expect(reducer(s, a)).toEqual(...)`).
- Predictable logs (action → state diff).
- Good for **many related fields** updated together (forms, wizards, undo stacks).

**Pathao / kanban example**

Actions: `ADD_TASK`, `MOVE_TASK`, `DELETE_TASK` — reducer updates columns immutably.

#### Further reading

- [React: useReducer](https://react.dev/reference/react/useReducer) — hook API
- [React: Extracting state logic into a reducer](https://react.dev/learn/extracting-state-logic-into-a-reducer) — tutorial
- [Redux: Reducers](https://redux.js.org/fundamentals/part-3-state-actions-reducers) — fundamentals
- [Reducer pattern (Martin Fowler)](https://martinfowler.com/eaaDev/Reducer.html) — general CS pattern

</details>

<details><summary>Solution (JavaScript)</summary>

Kanban column reducer with `useReducer`:

```js
const initial = { columns: { todo: [], done: [] } };

function kanbanReducer(state, action) {
  switch (action.type) {
    case 'ADD_TASK': {
      const { columnId, task } = action.payload;
      return {
        columns: {
          ...state.columns,
          [columnId]: [...state.columns[columnId], task],
        },
      };
    }
    case 'MOVE_TASK': {
      const { from, to, taskId } = action.payload;
      const task = state.columns[from].find((t) => t.id === taskId);
      return {
        columns: {
          ...state.columns,
          [from]: state.columns[from].filter((t) => t.id !== taskId),
          [to]: [...state.columns[to], task],
        },
      };
    }
    default:
      return state;
  }
}

// usage: const [state, dispatch] = useReducer(kanbanReducer, initial);
// dispatch({ type: 'ADD_TASK', payload: { columnId: 'todo', task: { id: '1', title: 'Fix bug' } } });
```

#### Code walkthrough

1. **ADD_TASK** — copy `columns`, append to one column array.
2. **MOVE_TASK** — find task, remove from `from`, append to `to`.
3. **default** — return same state reference (no re-render if nothing changed — React still compares by reference from dispatch result).

#### Complexity

| | |
|-|-|
| Time | O(n) per move if finding task in column of length n |
| Space | O(n) new column arrays per update |

#### Edge cases

- **Unknown action type** — return current state.
- **Missing task id** — handle gracefully or no-op.
- **Same column reorder** — separate action or include index in payload.

</details>

</article>

<article>

How is the **`useEffect`** hook used, and how does it work?

<details><summary>Theory and explanation</summary>

`useEffect(setup, dependencies?)` runs **side effects** after React commits DOM updates — data fetching, subscriptions, timers, syncing with non-React systems.

**Execution timing**

1. Component renders.
2. React updates DOM.
3. **Effect runs** (after paint for most cases).
4. Before next effect run (or unmount), React calls the **cleanup** function from the previous effect (if any).

**Dependency array**

| Deps | Behavior |
|------|----------|
| Omitted | Runs after **every** render (rarely intended) |
| `[]` | Runs once after mount (+ cleanup on unmount) |
| `[a, b]` | Runs when `a` or `b` change (shallow compare) |

**Strict Mode (development)**

React may **mount → unmount → remount** to surface missing cleanups — effects run twice in dev; production runs once per dependency change.

**Common patterns**

- **Fetch on id change**: `useEffect(() => { fetch(id) }, [id])`.
- **Event listener**: add in effect, remove in cleanup.
- **Avoid**: setting state unconditionally every render without deps control → infinite loop.

**Interview talking points**

- `useEffect` is **not** for derived state — use direct computation or `useMemo`.
- Prefer **React Query** / server components for data where applicable.
- **useLayoutEffect** runs before paint — measure DOM, avoid flicker.

#### Further reading

- [React: Synchronizing with Effects](https://react.dev/learn/synchronizing-with-effects) — mental model
- [React: useEffect reference](https://react.dev/reference/react/useEffect) — API details
- [React: You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect) — avoid unnecessary effects
- [MDN: AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController) — cancel fetch in cleanup

</details>

<details><summary>Solution (JavaScript)</summary>

Fetch boards on mount, subscribe to window resize, cleanup correctly:

```jsx
import { useEffect, useState } from 'react';

function BoardList({ userId }) {
  const [boards, setBoards] = useState([]);
  const [width, setWidth] = useState(window.innerWidth);

  useEffect(() => {
    const controller = new AbortController();
    async function load() {
      const res = await fetch(`/api/users/${userId}/boards`, {
        signal: controller.signal,
      });
      if (!res.ok) throw new Error('Failed');
      setBoards(await res.json());
    }
    load().catch((e) => {
      if (e.name !== 'AbortError') console.error(e);
    });
    return () => controller.abort();
  }, [userId]);

  useEffect(() => {
    const onResize = () => setWidth(window.innerWidth);
    window.addEventListener('resize', onResize);
    return () => window.removeEventListener('resize', onResize);
  }, []);

  return <div style={{ width }}>{boards.length} boards</div>;
}
```

#### Code walkthrough

1. **First effect** — re-runs when `userId` changes; aborts in-flight fetch on cleanup.
2. **Second effect** — empty deps: subscribe once, cleanup on unmount.
3. Cleanup prevents **memory leaks** and **stale setState** after unmount.

#### Complexity

| | |
|-|-|
| Time | N/A (I/O bound for fetch) |
| Space | O(1) for listeners if cleaned up |

#### Edge cases

- **Missing cleanup** on subscriptions → leaks and duplicate handlers.
- **Object/array deps** recreated each render → effect loops; stabilize with `useMemo` or primitives.
- **Race conditions** — abort or ignore stale responses (compare request id).

</details>

</article>

## Take Home Assessment

<article>

Build a **Trello-like kanban dashboard** with boards, columns, and drag-and-drop — tasks can be added, moved, edited, and deleted.

[**💻 Example Submission**](https://github.com/RadifTajwar/Pathao)

<details><summary>Show Description</summary>

Pathao sends instructions ~1 week after the initial interview. Requirements typically include:

- Multiple **boards**, each with **columns** (lists).
- **Tasks/cards** with add, edit, delete, and **move between columns**.
- **Drag-and-drop** support (within and across columns).
- **Bonus**: reorder within same column, **persist state across reload** (localStorage/API), OAuth login, unit tests.

</details>

<details><summary>Theory and explanation</summary>

**Architecture**

- **State model**: `boards[] → columns[] → tasks[]` or normalized `{ boardsById, columnsById, tasksById }` for O(1) updates.
- **Drag-and-drop**: HTML5 DnD, **@dnd-kit/core**, or **react-beautiful-dnd** — handle `onDragEnd` to update state immutably.
- **Persistence**: `localStorage.setItem` on debounced state change, or REST API with auth.

**Key design decisions**

1. **Optimistic UI** — update UI before server confirms; rollback on error.
2. **IDs** — `crypto.randomUUID()` for client-generated ids before sync.
3. **Accessibility** — keyboard DnD alternatives (@dnd-kit supports sensors).

**Interview talking points**

- Explain reducer vs Zustand for board moves.
- How you tested drag edge cases (empty column, same position).
- Trade-offs of localStorage vs backend for take-home scope.

#### Further reading

- [@dnd-kit documentation](https://docs.dndkit.com/) — accessible drag-and-drop
- [React: Preserving and resetting state](https://react.dev/learn/preserving-and-resetting-state) — list keys and drag
- [MDN: Drag and Drop API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API) — native browser DnD
- [Testing Library: user-event](https://testing-library.com/docs/user-event/intro) — unit test interactions

</details>

<details><summary>Solution (JavaScript)</summary>

Minimal move-task handler (works with any DnD library's `onDragEnd`):

```js
function moveTask(state, { taskId, fromColumnId, toColumnId, toIndex }) {
  const fromTasks = [...state.columns[fromColumnId].taskIds];
  const toTasks =
    fromColumnId === toColumnId
      ? fromTasks
      : [...state.columns[toColumnId].taskIds];

  const fromIndex = fromTasks.indexOf(taskId);
  if (fromIndex === -1) return state;

  fromTasks.splice(fromIndex, 1);
  if (fromColumnId !== toColumnId) {
    toTasks.splice(toIndex, 0, taskId);
  } else {
    fromTasks.splice(toIndex, 0, taskId);
  }

  return {
    ...state,
    columns: {
      ...state.columns,
      [fromColumnId]: { ...state.columns[fromColumnId], taskIds: fromTasks },
      ...(fromColumnId !== toColumnId && {
        [toColumnId]: { ...state.columns[toColumnId], taskIds: toTasks },
      }),
    },
  };
}

function persistState(key, state) {
  localStorage.setItem(key, JSON.stringify(state));
}
```

#### Code walkthrough

1. Copy task id arrays before mutating.
2. Remove from source; insert at `toIndex` in target (same or different column).
3. Return new state tree for React re-render.
4. **persistState** for reload survival bonus.

#### Complexity

| | |
|-|-|
| Time | O(n) per move (indexOf + splice in column length n) |
| Space | O(n) copied arrays |

#### Edge cases

- **Invalid taskId** — no-op return previous state.
- **Same index after remove** — adjust index when reordering within column.
- **Concurrent tabs** — localStorage `storage` event or use backend.

</details>

</article>

## On-site Assessment

<article>

Build an **e-commerce admin dashboard** with basic **CRUD** using **Nuxt.js** (Vue ecosystem).

[**💻 Example Submission**](https://github.com/RadifTajwar/pathaoFinal)

<details><summary>Show Description</summary>

After the take-home, Pathao schedules a **5–6 hour on-site** build. Candidates implement an e-commerce dashboard (products/orders/inventory — exact spec in session) with **Create, Read, Update, Delete** flows. Stack requirement: **Nuxt.js**, reflecting Pathao's existing **Vue** systems, even if your background is React/Next.js.

</details>

<details><summary>Theory and explanation</summary>

**Nuxt 3 building blocks**

- **File-based routing** — `pages/products/index.vue`, `pages/products/[id].vue`.
- **`useFetch` / `$fetch`** — data loading with SSR/hydration awareness.
- **Composables** — `composables/useProducts.js` for reusable CRUD logic.
- **Pinia** — Vue store (analogous to Zustand/Redux) for shared cart/admin state.

**CRUD API shape**

| Op | HTTP | Route example |
|----|------|---------------|
| List | GET | `/api/products` |
| Read | GET | `/api/products/:id` |
| Create | POST | `/api/products` |
| Update | PUT/PATCH | `/api/products/:id` |
| Delete | DELETE | `/api/products/:id` |

**React → Vue mental map**

| React | Vue/Nuxt |
|-------|----------|
| `useState` | `ref` / `reactive` |
| `useEffect` | `watch`, `onMounted` |
| JSX | Vue SFC template + script setup |
| Context | `provide/inject` or Pinia |
| Next.js pages | Nuxt `pages/` |

**Interview talking points**

- How you learned Nuxt quickly (docs, parallels to Next).
- Form validation and error states on create/edit.
- Loading and empty states in tables.

#### Further reading

- [Nuxt 3 documentation](https://nuxt.com/docs) — routing, data fetching
- [Vue 3 Composition API](https://vuejs.org/guide/extras/composition-api-faq.html) — `ref`, `computed`, `watch`
- [Pinia](https://pinia.vuejs.org/) — state management
- [MDN: Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) — CRUD HTTP calls

</details>

<details><summary>Solution (JavaScript)</summary>

Composable + page sketch for product CRUD:

```js
// composables/useProducts.js
export function useProducts() {
  const products = ref([]);
  const pending = ref(false);
  const error = ref(null);

  async function fetchProducts() {
    pending.value = true;
    error.value = null;
    try {
      products.value = await $fetch('/api/products');
    } catch (e) {
      error.value = e.message;
    } finally {
      pending.value = false;
    }
  }

  async function createProduct(payload) {
    const created = await $fetch('/api/products', { method: 'POST', body: payload });
    products.value.push(created);
    return created;
  }

  async function updateProduct(id, payload) {
    const updated = await $fetch(`/api/products/${id}`, { method: 'PATCH', body: payload });
    const i = products.value.findIndex((p) => p.id === id);
    if (i !== -1) products.value[i] = updated;
  }

  async function deleteProduct(id) {
    await $fetch(`/api/products/${id}`, { method: 'DELETE' });
    products.value = products.value.filter((p) => p.id !== id);
  }

  return { products, pending, error, fetchProducts, createProduct, updateProduct, deleteProduct };
}
```

#### Code walkthrough

1. **ref** holds reactive list and UI flags.
2. **$fetch** is Nuxt's wrapper for API calls (works SSR/client).
3. Mutations update local list after successful server response (optimistic optional).
4. Wire `fetchProducts` in `onMounted` on dashboard page.

#### Complexity

| | |
|-|-|
| Time | O(n) list render; O(1) per CRUD API call |
| Space | O(n) products in memory |

#### Edge cases

- **Network failure** — show error, do not drop row silently.
- **Stale list after edit** — replace by id or refetch.
- **Validation** — disable submit until required fields valid.

</details>

</article>

## Final Interview Questions

<article>

Explain **graph** data structures and core **graph algorithms** (BFS, DFS, shortest path).

<details><summary>Theory and explanation</summary>

A **graph** `G = (V, E)` has **vertices** (nodes) and **edges** (connections). Can be **directed** or **undirected**, **weighted** or unweighted.

**Representations**

1. **Adjacency list** — `Map<node, neighbors[]>` — sparse graphs, O(V + E) traversal space.
2. **Adjacency matrix** — `n × n` boolean/weight — O(1) edge lookup, O(n²) space.

**BFS (Breadth-First Search)**

- Queue; explores **level by level**.
- Finds **shortest path** in unweighted graphs.
- Time **O(V + E)**, space **O(V)**.

**DFS (Depth-First Search)**

- Stack/recursion; goes **deep** then backtracks.
- Used for **cycle detection**, **topological sort**, **connected components**.
- Time **O(V + E)**, space **O(V)** (recursion depth).

**Other common topics**

- **Dijkstra** — weighted shortest path (non-negative weights).
- **Union-Find** — connectivity, Kruskal's MST.

**Pathao context**

Routing, delivery networks, and maps products involve graph models — even frontend roles may get conceptual DSA questions in the final round.

#### Further reading

- [Visualgo: BFS](https://visualgo.net/en/bfs) — interactive traversal
- [Visualgo: DFS](https://visualgo.net/en/dfs) — stack visualization
- [CP-Algorithms: BFS](https://cp-algorithms.com/graph/breadth-first-search.html) — shortest paths
- [CP-Algorithms: DFS](https://cp-algorithms.com/graph/depth-first-search.html) — applications

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function buildAdj(n, edges, directed = false) {
  const adj = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) {
    adj[u].push(v);
    if (!directed) adj[v].push(u);
  }
  return adj;
}

function bfs(adj, start) {
  const visited = new Set([start]);
  const dist = Array(adj.length).fill(-1);
  const q = [start];
  dist[start] = 0;
  while (q.length) {
    const u = q.shift();
    for (const v of adj[u]) {
      if (!visited.has(v)) {
        visited.add(v);
        dist[v] = dist[u] + 1;
        q.push(v);
      }
    }
  }
  return dist;
}

function dfs(adj, start, visit = () => {}) {
  const seen = new Set();
  function go(u) {
    seen.add(u);
    visit(u);
    for (const v of adj[u]) if (!seen.has(v)) go(v);
  }
  go(start);
}
```

#### Code walkthrough

1. **buildAdj** — adjacency list from edge list.
2. **bfs** — queue + distance array for unweighted shortest hops.
3. **dfs** — recursive depth-first with visited set.

#### Complexity

| | |
|-|-|
| Time | O(V + E) per traversal |
| Space | O(V) queue/stack + visited |

#### Edge cases

- **Disconnected graph** — BFS/DFS from one start misses nodes; loop all vertices or track components.
- **Self-loops / multi-edges** — dedupe or handle in problem spec.
- **Weighted graph** — BFS dist wrong; use Dijkstra.

</details>

</article>

<article>

As a **React/Next.js** developer, how did you approach learning **Nuxt/Vue** for the on-site assessment?

<details><summary>Theory and explanation</summary>

Pathao's final round often asks **how the on-site build went** and how hard it was to switch frameworks. Structure a **behavioral + technical** answer:

**1. Acknowledge overlap**

- Component-based UI, reactive state, file-based routing, SSR data loading — concepts transfer.
- Map React hooks to Vue Composition API before writing code.

**2. Concrete learning steps**

- Skim **Nuxt docs** (routing, `useFetch`, layouts).
- Build smallest CRUD slice first (list + create) before polish.
- Use **Pinia** only if prop drilling hurts — do not over-engineer under time pressure.

**3. Challenges to mention honestly**

- Template syntax vs JSX (`v-for`, `v-model`).
- Reactivity rules (`ref` vs `reactive`, `.value` in script).
- SSR hydration mismatches if client-only APIs used in setup.

**4. What you delivered**

- Working CRUD, clear folder structure, basic error/loading UX.
- What you would refactor with more time (tests, auth, design system).

**5. Growth mindset**

- Willingness to match team stack (Vue at Pathao) while leveraging JS fundamentals.

#### Further reading

- [Vue.js: Comparison with React](https://vuejs.org/guide/extras/comparison.html) — official comparison
- [Nuxt migration guides](https://nuxt.com/docs/migration/overview) — if coming from Next mental model
- [React to Vue cheat sheet (community)](https://vuejs.org/guide/extras/comparison.html#mental-model) — hook mapping

</details>

<details><summary>Solution (JavaScript)</summary>

Side-by-side: same "fetch products on mount" in React vs Nuxt:

```jsx
// React (Next.js client component)
useEffect(() => {
  let cancelled = false;
  fetch('/api/products')
    .then((r) => r.json())
    .then((data) => { if (!cancelled) setProducts(data); });
  return () => { cancelled = true; };
}, []);
```

```js
// Nuxt 3 script setup — data fetching on server and client
const { data: products, pending, error } = await useFetch('/api/products');
// template binds to products, pending, error
```

#### Code walkthrough

1. React uses effect + manual cancel flag.
2. Nuxt **`useFetch`** handles SSR, caching, and pending/error refs.
3. Cite this mapping in the interview to show deliberate learning.

#### Complexity

| | |
|-|-|
| Time | N/A (behavioral) |
| Space | N/A (behavioral) |

#### Edge cases

- Do not blame the stack — focus on adaptability.
- If you ran out of time, explain prioritization (CRUD before styling).

</details>

</article>

## Contributors

- [Radif Tajwar](https://bd.linkedin.com/in/radiftajwar)
