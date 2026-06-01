---
description: Fringecore interview questions, Fringecore interview stages, Fringecore interview details, Fringecore interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/fringecore
---
# Fringecore

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-| :- |
| Founding year | |
| Company Website | https://fringecore.sh/ |
| Career Website | https://work-pool.notion.site/FringeCore_-Careers-cd5106060028424383fcbbb7fc885e38 |
| Technologies Used| React, Node.js, GPU.js, streams |

## Introduction
[Fringecore](https://fringecore.sh/) is a team of engineers and designers, who build software, hack hardware and apply design thinking in-order to tame the chaos in business processes.

Fringecore interviews often use **public take-home repositories** for frontend UI challenges and backend Node.js systems tasks. Complete the linked repo and be ready to explain architecture, edge cases, and performance.

## Frontend Questions

<article>

Build a recursive partitioner

[**💻 Problem Repository**](https://github.com/fringecore/fringecore-frontend-challenge-recursive-partitioning)

<details><summary>Show Description</summary>

![](../resource/fringecore-images/recursive-partitioner.webp)

Your task is to create a recursive partitioner. Upon opening the project, users should be greeted with a random background color and two buttons labeled "v" and "h." The "v" button allows the screen to be split vertically, while the "h" button splits it horizontally. When a split occurs, one partition should retain its original color, and the newly created partition should adopt a new random color. Each partition should remain interactive and allow further splits. Additionally, if multiple partitions exist, users should have the option to remove any partition. All partitions should be resizable by clicking and dragging their edges.
</details>

<details><summary>Theory and explanation</summary>

Model the UI as a **binary partition tree**:

- **Leaf node** — one colored pane with controls (`v`, `h`, remove).
- **Internal node** — split direction (`vertical` | `horizontal`), two children, and a **split ratio** (e.g. 0.5).

**Layout**

- Use **percentage/flex** or absolute positioning from tree: parent size × ratio for first child, remainder for second.
- **Resize drag** updates only the split ratio on that internal node; children reflow recursively.

**State updates**

- **Split:** replace leaf with internal node; one child keeps color, sibling gets `randomColor()`.
- **Remove:** delete node; promote sibling to fill parent (or collapse tree to single leaf if one pane left).

**React structure**

- `PartitionNode` component recurses on `node.children`.
- Lift tree state to root; immutable updates (`structuredClone` or immer) for predictable renders.

**Interview talking points**

- Why a **tree** beats a flat list of rectangles (splits are hierarchical).
- Hit-testing on **divider handles** (mouse down → mouse move → mouse up).
- Minimum pane size clamp so splits do not collapse to zero.

#### Further reading

- [React docs: Lifting state up](https://react.dev/learn/sharing-state-between-components) — tree state at root
- [MDN: Pointer events](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events) — drag handles
- [CSS flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout) — split layouts

</details>

<details><summary>Solution (JavaScript)</summary>

Core tree helpers (UI wiring in repo):

```js
function randomColor() {
  return `hsl(${Math.floor(Math.random() * 360)}, 70%, 60%)`;
}

function splitLeaf(leaf, direction) {
  return {
    type: 'split',
    direction, // 'vertical' | 'horizontal'
    ratio: 0.5,
    children: [
      { ...leaf, color: leaf.color },
      { type: 'leaf', id: crypto.randomUUID(), color: randomColor() },
    ],
  };
}

function removeNode(root, targetId) {
  if (!root || root.type === 'leaf') return root;
  const [a, b] = root.children;
  if (a.id === targetId) return b.type === 'leaf' ? b : b;
  if (b.id === targetId) return a.type === 'leaf' ? a : a;
  return {
    ...root,
    children: [removeNode(a, targetId), removeNode(b, targetId)],
  };
}
```

#### Code walkthrough

1. **Leaf** stores `id` + `color` for remove targeting.
2. **splitLeaf** replaces one leaf with two-pane internal node.
3. **removeNode** splices out pane and collapses sibling upward (simplify per spec).
4. Render: if `split`, flex-direction `row` or `column` with `flex: ratio` on first child.

#### Complexity

| | |
|-|-|
| Time | O(depth) per split/remove; render O(leaves) |
| Space | O(leaves) tree nodes |

#### Edge cases

- **Remove last split** — restore single full-screen leaf.
- **Drag below min width** — clamp ratio (e.g. 0.1–0.9).
- **Deep nesting** — very small panes; optional max depth.

</details>

</article>

<article>

Build a GPU-accelerated color picker

[**💻 Problem Repository**](https://github.com/fringecore/fringecore-frontend-challenge-colorpicker-pentagon)

<details><summary>Show Description</summary>

Develop a GPU-accelerated color picker with a unique pentagon shape, focusing on implementing the core color computation logic using GPU.js, while utilizing the provided React wrapper and UI components. The color picker should generate smooth gradients, handling hue transitions across the color spectrum. Horizontal gradients should transition from white to the primary color, while vertical gradients should range from white to black. 

The implementation must include precise RGB channel calculations based on the current hue, ensure smooth transitions between primary colors, handle the alpha channel correctly, and deliver pixel-perfect gradient rendering. 

Your primary task is to implement the kernelFunction in kernel.js, which will take three parameters—canvas width, canvas height, and the current hue value (0–1)—to compute appropriate RGB values for each pixel, manage color transitions, and return the correct channel value based on the thread position.
</details>

<details><summary>Theory and explanation</summary>

**HSV / HSL to RGB** drives the pentagon picker:

- Fix **hue** `h ∈ [0,1]` from UI slider.
- For pixel `(x, y)` in kernel:
  - **Horizontal:** interpolate **white → pure hue color** as `t = x / width`.
  - **Vertical:** interpolate result toward **black** as `s = y / height` (value/saturation semantics per spec).

**GPU.js kernel**

- Each thread maps to `(this.thread.x, this.thread.y)`.
- Return one channel per call or RGB triple depending on repo API — match `kernel.js` signature in challenge.

**RGB from hue (6-sector HSV)**

- `h' = h * 6`, sector `i = floor(h')`, fractional part `f = h' - i`.
- Standard switch on `i` for `(r,g,b)` before mixing with white/black.

**Interview talking points**

- Why GPU: parallel per-pixel work; CPU loop on large canvas is slow.
- **Premultiplied alpha** if compositing on UI.
- Match reference screenshots pixel-perfect — floating rounding matters.

#### Further reading

- [GPU.js documentation](https://gpu.rocks/) — kernel API
- [Wikipedia: HSL and HSV](https://en.wikipedia.org/wiki/HSL_and_HSV) — conversion formulas
- [MDN: Canvas pixel manipulation](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Pixel_manipulation) — CPU fallback intuition

</details>

<details><summary>Solution (JavaScript)</summary>

HSV to RGB helper + kernel outline:

```js
function hsvToRgb(h, s, v) {
  const i = Math.floor(h * 6);
  const f = h * 6 - i;
  const p = v * (1 - s);
  const q = v * (1 - f * s);
  const t = v * (1 - (1 - f) * s);
  switch (i % 6) {
    case 0: return [v, t, p];
    case 1: return [q, v, p];
    case 2: return [p, v, t];
    case 3: return [p, q, v];
    case 4: return [t, p, v];
    default: return [v, p, q];
  }
}

// kernel.js conceptual: for thread (x,y), width, height, hue
// t = x/width, s = y/height
// base = lerp(white, hsvToRgb(hue,1,1), t)
// rgb = lerp(base, [0,0,0], s)
// return channel by thread.z or separate kernels per channel
```

#### Code walkthrough

1. Compute **pure hue color** at full saturation/value.
2. **Horizontal lerp** with white using `t`.
3. **Vertical lerp** toward black using `s`.
4. GPU kernel writes each pixel in parallel.

#### Complexity

| | |
|-|-|
| Time | O(width × height) work, O(1) per pixel parallelized on GPU |
| Space | O(width × height) framebuffer |

#### Edge cases

- **hue = 0 vs 1** — wrap continuity at red.
- **width/height = 0** — guard in kernel launch.
- **alpha channel** — return 255 or 1.0 per spec when opaque.

</details>

</article>

<article>

Build a block graph

[**💻 Problem Repository**](https://github.com/fringecore/fringecore-frontend-challenge-block-graph)

<details><summary>Show Description</summary>

![](../resource/fringecore-images/block-graph.webp)

Build an interactive page where, upon loading, a block appears at a random position on the screen. Each block should feature a "+" button, which, when pressed, spawns a new block at another random position. All blocks should be draggable using mouse clicks, allowing users to reposition them freely. A dashed line should visually connect each new block to its parent, i.e., the block on which the "+" button was pressed. These connecting lines must dynamically adjust their position to reflect any movement of the parent or child blocks, maintaining their connection at all times.
</details>

<details><summary>Theory and explanation</summary>

**Data model:** forest of **trees** (or directed graph) stored as:

```js
{ id, x, y, parentId: null | string }
```

**Rendering**

- Blocks: absolutely positioned `div`s at `(x, y)`.
- Edges: **SVG `<line>`** or canvas stroke from `(parent.x, parent.y)` to `(child.x, child.y)` center — update on every drag frame.

**Interactions**

- **Drag:** `pointerdown` on block → track delta → update `x,y` in state.
- **Add child:** push new node with `parentId = clickedBlock.id`, random position avoiding overlap if possible.

**Interview talking points**

- Store **edges implicitly** via `parentId` vs separate edge list.
- Use `requestAnimationFrame` or React state batching for smooth drag.
- Z-index: dragged node on top.

#### Further reading

- [SVG line element](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/line) — dynamic connectors
- [React DnD patterns](https://react.dev/learn/escape-hatches) — pointer drag without heavy library
- [Graph visualization basics](https://observablehq.com/@d3/force-directed-graph) — if extending layout

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function addChild(blocks, parentId, w, h) {
  const size = 80;
  return [
    ...blocks,
    {
      id: crypto.randomUUID(),
      parentId,
      x: Math.random() * (w - size),
      y: Math.random() * (h - size),
    },
  ];
}

function edgeLines(blocks) {
  const byId = Object.fromEntries(blocks.map((b) => [b.id, b]));
  return blocks
    .filter((b) => b.parentId && byId[b.parentId])
    .map((b) => {
      const p = byId[b.parentId];
      return { x1: p.x, y1: p.y, x2: b.x, y2: b.y, key: b.id };
    });
}
```

#### Code walkthrough

1. **blocks** array is single source of truth.
2. **edgeLines** derives SVG line coords from parent/child positions.
3. On drag, update only dragged block coords; lines recompute on render.

#### Complexity

| | |
|-|-|
| Time | O(n) edges per frame, n = block count |
| Space | O(n) |

#### Edge cases

- **Orphan parentId** — skip line if parent missing.
- **Drag off-screen** — clamp coordinates.
- **Many children** — lines overlap; acceptable per spec.

</details>

</article>

<article>

Build a interactive bouncing ball

[**💻 Problem Repository**](https://github.com/fringecore/fringecore-frontend-challenge-bouncing-ball)

<details><summary>Show Description</summary>

Create an interactive bouncing ball simulation featuring a ball centered on a blank canvas at the start. 

Display instructions prompting the user to "Click to launch the ball!" Upon clicking, the ball should launch toward the clicked position, bouncing off the canvas boundaries with realistic elastic collisions. Its speed should gradually decrease due to friction, eventually stopping when the speed becomes negligible. At this point, the instructions should reappear, inviting the user to relaunch the ball. Implement core physics features, including constant initial velocity, angle-based directional movement, elastic boundary collisions, and friction-based speed reduction. 

Avoid using any physics or animation libraries, but you may use build tools like Vite or Create React App, and basic styling libraries such as Tailwind.
</details>

<details><summary>Theory and explanation</summary>

**2D kinematics** on canvas:

- State: position `(x, y)`, velocity `(vx, vy)`.
- On click at `(tx, ty)` from center: direction unit vector `d = normalize((tx-x, ty-y))`, set `(vx, vy) = d * v0` (constant initial speed).

**Wall collision (elastic)**

- If `x - r < 0` → `x = r`, `vx = -vx * restitution`
- If `x + r > width` → flip `vx` similarly for `y`.

**Friction**

- Each frame: `vx *= (1 - friction)`, `vy *= (1 - friction)` or subtract constant deceleration aligned with velocity.
- When `|v| < epsilon` → stop animation, show prompt again.

**Loop**

- `requestAnimationFrame` + `dt` (delta time) for frame-independent motion: `x += vx * dt`.

**Interview talking points**

- No libraries = you own integrator and collision tests.
- **Separate axes** collision is valid for axis-aligned box.
- Normalize delta time for consistent speed across monitors.

#### Further reading

- [MDN: Canvas tutorial](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial) — drawing loop
- [MDN: requestAnimationFrame](https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame) — animation timing
- [Elastic collision (Wikipedia)](https://en.wikipedia.org/wiki/Elastic_collision) — restitution coefficient

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function stepBall(state, canvas, dt) {
  let { x, y, vx, vy, r } = state;
  const friction = 0.02;
  const eps = 0.5;

  x += vx * dt;
  y += vy * dt;

  if (x - r < 0) { x = r; vx = -vx; }
  if (x + r > canvas.width) { x = canvas.width - r; vx = -vx; }
  if (y - r < 0) { y = r; vy = -vy; }
  if (y + r > canvas.height) { y = canvas.height - r; vy = -vy; }

  vx *= 1 - friction;
  vy *= 1 - friction;

  const speed = Math.hypot(vx, vy);
  if (speed < eps) return { ...state, x, y, vx: 0, vy: 0, stopped: true };
  return { ...state, x, y, vx, vy, stopped: false };
}

function launchToward(ball, target, v0 = 400) {
  const dx = target.x - ball.x;
  const dy = target.y - ball.y;
  const len = Math.hypot(dx, dy) || 1;
  return { ...ball, vx: (dx / len) * v0, vy: (dy / len) * v0, stopped: false };
}
```

#### Code walkthrough

1. **launchToward** sets constant speed along click direction.
2. **stepBall** integrates position, reflects velocity at walls, applies friction.
3. **stopped** flag re-shows UI prompt.

#### Complexity

| | |
|-|-|
| Time | O(1) per frame |
| Space | O(1) |

#### Edge cases

- **Click on ball center** — `len === 0`; ignore or default direction.
- **Corner tunneling** — small `r` + large `dt`; cap `dt` or sub-step.
- **Tab background** — pause loop with Page Visibility API (bonus).

</details>

</article>

<article>

Build an interactive polygon drawing tool

[**💻 Problem Repository**](https://github.com/fringecore/fringecore-frontend-challenge-draw-polygon)

<details><summary>Show Description</summary>

Build an interactive polygon drawing tool that features a blank canvas upon project initialization, allowing users to create and edit polygons. Users can define a polygon by clicking points to create vertices and closing the shape by clicking near the starting point. Multiple polygons can be drawn on the same canvas, each created by sequential clicks, with a dashed line previewing the next edge before the polygon is closed. Closed polygons are automatically filled with a semi-transparent color.

The tool should also support editing: vertices are displayed as draggable points, enabling users to modify the shape of the polygons. Multiple polygons can be edited independently without interfering with each other. Smooth dragging functionality must be implemented for seamless vertex adjustments, and overlapping polygons should be handled correctly.

The implementation should use React and SVG for rendering, with React's built-in state management to manage multiple polygons effectively. Focus on writing clean, maintainable code, and use any preferred build tool such as Vite or Create React App. Styling can be enhanced with libraries like Tailwind if needed.
</details>

<details><summary>Theory and explanation</summary>

**State shape**

```js
polygons: [
  { id, closed: boolean, points: [{x,y}, ...], fill }
]
activePolygonId, draftPoint (cursor preview)
```

**Create flow**

1. Click adds vertex to active polygon.
2. **Close** when click within threshold ε of first vertex → `closed = true`, assign fill.
3. While open, render **dashed** segment from last vertex to cursor.

**Edit flow**

- Hit-test vertices (distance < radius); drag updates one point in one polygon.
- **Hit priority:** topmost polygon / selected polygon first for overlaps.

**SVG**

- `<polygon points="...">` or `<path>` for fill; `<circle>` handles for vertices.

**Interview talking points**

- Point-in-polygon not required for drag but useful for selection.
- Immutable updates per polygon id for React performance.

#### Further reading

- [SVG polygon](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/polygon) — rendering
- [GeeksforGeeks: Point in polygon](https://www.geeksforgeeks.org/check-if-a-point-is-inside-outside-and-on-a-polygon/) — overlap selection
- [React SVG events](https://react.dev/reference/react-dom/components/common#svg-elements) — click/drag on SVG

</details>

<details><summary>Solution (JavaScript)</summary>

```js
const CLOSE_EPS = 12;

function isNear(a, b) {
  return Math.hypot(a.x - b.x, a.y - b.y) <= CLOSE_EPS;
}

function addClick(poly, p) {
  if (!poly.closed && poly.points.length >= 3 && isNear(p, poly.points[0])) {
    return { ...poly, closed: true, fill: poly.fill || 'rgba(66,135,245,0.35)' };
  }
  return { ...poly, points: [...poly.points, p] };
}

function moveVertex(poly, index, p) {
  const points = poly.points.map((pt, i) => (i === index ? p : pt));
  return { ...poly, points };
}
```

#### Code walkthrough

1. **addClick** appends vertex or closes when near start.
2. **moveVertex** updates single index during drag.
3. Render: map polygons to `<polygon>`; open polylines use dashed `<line>` to cursor.

#### Complexity

| | |
|-|-|
| Time | O(v) per polygon per render; hit-test O(total vertices) |
| Space | O(total vertices) |

#### Edge cases

- **< 3 points** — cannot close meaningfully.
- **Self-intersecting polygon** — fill may look odd; acceptable unless spec forbids.
- **Dragging first vertex** of closed polygon — update closure threshold behavior.

</details>

</article>

<article>

Build an interactive art-board

[**💻 Problem Repository**](https://github.com/fringecore/fringecore-frontend-challenge-art-board)

<details><summary>Show Description</summary>

Build an interactive art-board featuring a clean white canvas and two tools— a pen tool and an eraser tool—accessible from the top toolbar. When the pen tool is selected, users can draw on the canvas by pressing and holding the mouse button while moving the cursor, creating continuous lines. Releasing the mouse button stops the drawing action.

When the eraser tool is selected, users can erase any drawn lines by pressing and holding the mouse button while moving the cursor over the lines. The eraser should visibly indicate its area of effect, ensuring users can clearly see what will be erased.

The implementation should be lightweight and not rely on external drawing or canvas libraries. You may structure the code in any way you prefer, using build tools like Vite or Create React App, with optional basic styling enhancements via libraries like Tailwind. Focus on creating intuitive functionality for seamless drawing and erasing experiences.
</details>

<details><summary>Theory and explanation</summary>

**Stroke model**

- Store strokes as polylines: `{ tool: 'pen'|'eraser', points: [{x,y,t}], width }`.
- Pen strokes append points while mouse down.
- Eraser: either **destination-out** composite on canvas or remove/intersect strokes geometrically.

**Canvas 2D approach (no libraries)**

- Keep offscreen or persistent layer; redraw all pen strokes each frame.
- Eraser with `globalCompositeOperation = 'destination-out'` and circular brush preview circle following cursor.

**Eraser preview**

- Draw semi-transparent circle at pointer when eraser active (not committed to art layer).

**Interview talking points**

- Vector strokes vs raster: vector easier to undo; raster simpler with eraser composite.
- **Pointer events** for pen tablet compatibility.
- Performance: batch points; simplify polyline if noisy.

#### Further reading

- [MDN: globalCompositeOperation](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/globalCompositeOperation) — eraser mode
- [Perfect freehand (concept)](https://github.com/steveruizok/perfect-freehand) — smooth strokes (optional enhancement)
- [Pointer Events API](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events) — unified mouse/touch

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function drawStrokes(ctx, strokes) {
  for (const s of strokes) {
    if (s.tool !== 'pen' || s.points.length < 2) continue;
    ctx.strokeStyle = '#111';
    ctx.lineWidth = s.width ?? 2;
    ctx.lineCap = 'round';
    ctx.beginPath();
    ctx.moveTo(s.points[0].x, s.points[0].y);
    for (let i = 1; i < s.points.length; i++) {
      ctx.lineTo(s.points[i].x, s.points[i].y);
    }
    ctx.stroke();
  }
}

function eraseAt(ctx, x, y, radius = 12) {
  ctx.save();
  ctx.globalCompositeOperation = 'destination-out';
  ctx.beginPath();
  ctx.arc(x, y, radius, 0, Math.PI * 2);
  ctx.fill();
  ctx.restore();
}
```

#### Code walkthrough

1. Accumulate **points** while `pointerdown` + move.
2. On `pointerup`, push stroke to array and commit to bitmap or keep vector list.
3. **eraseAt** punches transparent holes; preview eraser circle in separate pass.

#### Complexity

| | |
|-|-|
| Time | O(strokes × points) full redraw; eraser O(1) per dab |
| Space | O(total points) |

#### Edge cases

- **Empty stroke** (click without move) — discard.
- **Tool switch mid-drag** — cancel current stroke.
- **High-DPI canvas** — scale by `devicePixelRatio`.

</details>

</article>



## Backend Questions

<article>

Stream Transform

[**💻 Problem Repository**](https://github.com/Abir66/fringecore-backend-challenges/tree/main/stream-transform)

<details><summary>Show Description</summary>
There is a TCP server that gives out top secret information mixed with random data. You need to make another server that will connects to this server, reads the streams of text and outputs the same data but with the top-secret data hidden and replaced with dashes.

We don’t really know when the data will end, hence it is absolutely critical that our proxy server that hides secret information does not wait for the entire data before giving output.
</details>

<details><summary>Theory and explanation</summary>

This challenge tests **Node.js streams** and **backpressure** — you must transform data **incrementally**, not buffer the full TCP session.

**Architecture**

- TCP client connects to upstream secret server.
- Pipe: `upstreamSocket` → **Transform stream** → `downstreamSocket` (or stdout).
- Transform replaces detected secret tokens with `-` **as chunks arrive**.

**Why not buffer**

- Unknown stream length; memory blowup and latency violate requirements.
- Use `socket.pipe(transform).pipe(out)` or async iteration on `'data'` events.

**Secret detection**

- Follow challenge rules (fixed marker, regex, length-prefix — read repo README).
- Handle **chunk boundaries** — secret may straddle two `'data'` events; keep **carry buffer** for partial matches.

**Interview talking points**

- `Transform` class `_transform(chunk, enc, cb)`.
- Error propagation and `destroy()` on failure.
- TCP `setNoDelay` optional latency note.

#### Further reading

- [Node.js Stream documentation](https://nodejs.org/api/stream.html) — Transform, pipe, backpressure
- [Node.js Net module](https://nodejs.org/api/net.html) — TCP client/server
- [Substack: Stream handbook](https://github.com/substack/stream-handbook) — mental model

</details>

<details><summary>Solution (JavaScript)</summary>

```js
import net from 'net';
import { Transform } from 'stream';

const SECRET = 'TOPSECRET'; // replace per challenge spec

function createRedactTransform() {
  let carry = '';
  return new Transform({
    transform(chunk, _enc, cb) {
      let data = carry + chunk.toString();
      carry = '';
      if (data.length >= SECRET.length - 1) {
        carry = data.slice(-(SECRET.length - 1));
        data = data.slice(0, -(SECRET.length - 1));
      }
      cb(null, data.replaceAll(SECRET, '-'.repeat(SECRET.length)));
    },
    flush(cb) {
      cb(null, carry.replaceAll(SECRET, '-'.repeat(SECRET.length)));
    },
  });
}

const upstream = net.connect({ port: 9000, host: '127.0.0.1' });
const redact = createRedactTransform();
upstream.pipe(redact).pipe(process.stdout);
```

#### Code walkthrough

1. **carry** retains tail characters so secrets split across chunks still match.
2. **replaceAll** emits output immediately per chunk.
3. **flush** handles trailing carry at stream end.

#### Complexity

| | |
|-|-|
| Time | O(bytes in) per chunk |
| Space | O(secret length) carry buffer |

#### Edge cases

- **Overlapping secret patterns** — clarify spec (e.g. `AAA` in `AAAA`).
- **Upstream closes abruptly** — end transform cleanly.
- **Binary vs text** — challenge uses text; use `String` carefully with multi-byte UTF-8.

</details>

</article>



<article>

Custom Serializer

[**💻 Problem Repository**](https://github.com/Abir66/fringecore-backend-challenges/tree/main/custom-serializer)

<details><summary>Show Description</summary>
You are given a complex object. You need to write a function that will convert this object into a string with some specific rules.

Sample Input
![](../resource/fringecore-images/custom-serializer-input.png)

Sample Output
![](../resource/fringecore-images/custom-serializer-output.png)
</details>

<details><summary>Theory and explanation</summary>

Follow the **exact formatting rules** in the challenge images (type prefixes, nesting, array/object delimiters, null/undefined handling).

**General approach**

- **Recursive walk** over values.
- Dispatch by `typeof` / `Array.isArray` / `null`.
- Objects: serialize keys in **stable order** (often sorted keys) if required.
- Escape strings per spec (quotes, backslashes, unicode).

**Interview talking points**

- Contrast with `JSON.stringify` — custom format is usually **not JSON-compatible**.
- Cycle detection: `WeakSet` for visited objects if references can loop.
- `BigInt`, `Date`, `undefined` — explicit rules from README.

#### Further reading

- [MDN: JSON.stringify](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) — comparison baseline
- [Challenge README](https://github.com/Abir66/fringecore-backend-challenges/tree/main/custom-serializer) — authoritative rules
- [Visitor pattern](https://refactoring.guru/design-patterns/visitor) — recursive type dispatch

</details>

<details><summary>Solution (JavaScript)</summary>

Template recursive serializer (adapt keys/format to repo tests):

```js
function serialize(value) {
  if (value === null) return 'N|null;';
  if (Array.isArray(value)) {
    return `A[${value.map(serialize).join('')}];`;
  }
  if (typeof value === 'object') {
    const keys = Object.keys(value).sort();
    const body = keys.map((k) => `K${serialize(k)}${serialize(value[k])}`).join('');
    return `O{${body}};`;
  }
  if (typeof value === 'string') return `S${value.length}:${value};`;
  if (typeof value === 'number') return `D${value};`;
  if (typeof value === 'boolean') return `B${value ? 1 : 0};`;
  return 'U;';
}
```

@@warning:Replace prefix letters and delimiters with the exact format shown in custom-serializer-input/output images before submitting.@@

#### Code walkthrough

1. Type tag prefixes each encoded value for parser symmetry.
2. Objects sort keys for deterministic output.
3. Strings length-prefixed to allow `;` inside content.

#### Complexity

| | |
|-|-|
| Time | O(nodes) in object graph |
| Space | O(depth) recursion stack |

#### Edge cases

- **Circular references** — throw or replace with sentinel.
- **Empty object/array** — still need correct wrappers.
- **Sparse arrays** — holes vs `undefined` per spec.

</details>

</article>



<article>

Man in the middle

[**💻 Problem Repository**](https://github.com/Abir66/fringecore-backend-challenges/tree/main/man-in-the-middle)

<details><summary>Show Description</summary>
Secure messages exchanged between two individuals, faisal and monjur, were intercepted, but the encryption and protocol used are custom and complex.

***Encryption Details:***

- The encryption keys are `8` bytes long.
- Each message is encrypted with a different key using just `XOR`.
- Messages include the sender's username in lowercase, appended as a prefix with a colon, e.g., `faisal:hello`.
- Messages are padded with newlines (`\n`) to ensure the total length is a multiple of `7` bytes.
- After padding, the message is split into groups of `7` bytes, and an index byte is prepended to each group, turning them into `8-byte` blocks.
- All groups, except the first, are shuffled randomly.
- Each group is then encrypted and `Base64` encoded.
- `faisal` initiates the dialogue.

***What To Build***

1. Write a Node.js program to decrypt and reconstruct the original messages to uncover the content of their communication.
2. Your program should write a file named `decrypted.json` with all the messages in an array.

</details>

<details><summary>Theory and explanation</summary>

**Decryption pipeline (reverse order)**

1. **Base64 decode** each intercepted payload.
2. **XOR decrypt** with 8-byte key (same operation as encrypt).
3. Split into **8-byte blocks**; read **index byte** + 7 payload bytes.
4. **Unshuffle** blocks: first block stays; reorder others by index byte.
5. Concatenate 7-byte groups, **strip padding** newlines until multiple of 7 constraint satisfied.
6. Parse `username:message` prefix.

**XOR properties**

- `cipher[i] ^ key[i % 8] = plain[i]` — key reuse pattern critical.

**Shuffle recovery**

- Block 0 fixed; for remaining blocks, place block `k` at position indicated by index byte (read repo tests for exact indexing).

**Output**

- Ordered dialogue starting with **faisal** → array of `{ from, text }` in `decrypted.json`.

**Interview talking points**

- Treat as **protocol reverse engineering** — write decoder functions unit-tested per sample.
- Buffer lengths — off-by-one in block index breaks message.

#### Further reading

- [Node.js Buffer](https://nodejs.org/api/buffer.html) — byte manipulation
- [RFC 4648 Base64](https://datatracker.ietf.org/doc/html/rfc4648) — decoding
- [XOR cipher (Wikipedia)](https://en.wikipedia.org/wiki/XOR_cipher) — symmetric decrypt

</details>

<details><summary>Solution (JavaScript)</summary>

```js
import fs from 'fs';

function xor(buf, key) {
  const out = Buffer.alloc(buf.length);
  for (let i = 0; i < buf.length; i++) out[i] = buf[i] ^ key[i % key.length];
  return out;
}

function decodeMessage(b64, key) {
  const raw = xor(Buffer.from(b64, 'base64'), key);
  const blocks = [];
  for (let i = 0; i < raw.length; i += 8) {
    blocks.push(raw.subarray(i, i + 8));
  }
  const first = blocks[0];
  const rest = blocks.slice(1);
  const ordered = [first];
  const slots = Array(rest.length).fill(null);
  for (const b of rest) {
    const idx = b[0];
    slots[idx] = b;
  }
  for (const b of slots) ordered.push(b);
  const bytes = Buffer.concat(ordered.map((b) => b.subarray(1, 8)));
  const text = bytes.toString('utf8').replace(/\n+$/g, '');
  const colon = text.indexOf(':');
  return { from: text.slice(0, colon), text: text.slice(colon + 1) };
}

// fs.writeFileSync('decrypted.json', JSON.stringify(messages, null, 2));
```

#### Code walkthrough

1. **xor** reverses encryption on full buffer.
2. Split 8-byte blocks; block 0 anchor; index byte routes other blocks.
3. Strip index bytes, join 7-byte payloads, remove padding newlines, split sender/body.

#### Complexity

| | |
|-|-|
| Time | O(blocks) per message |
| Space | O(message length) |

#### Edge cases

- **Invalid base64** — skip or fail per harness.
- **Index collisions** — protocol assumes valid permutation.
- **UTF-8 multi-byte** — operate on bytes before converting to string.

</details>

</article>



<article>

Color Picker Pentagon

[**💻 Problem Repository**](https://github.com/Abir66/fringecore-backend-challenges/tree/main/colorpicker-pentagon)

<details><summary>Show Description</summary>

![color-picker](../resource/fringecore-images/color-picker-pentagon.png)

Create a GPU-accelerated color picker with a unique pentagon shape. You'll be implementing the core color computation logic using GPU.js, while we provide the React wrapper and UI components.

1. Core Requirements:
    - Implement a kernel function that generates a color picker gradient
    - Handle hue transitions across the color spectrum
    - Create horizontal gradients from white to the primary color
    - Apply vertical gradients from white to black
2. Color Computation Features:
    - RGB channel calculations based on hue value
    - Smooth transitions between primary colors
    - Proper alpha channel handling
    - Pixel-perfect gradient rendering

**Your Task**

Implement the `kernelFunction` in `kernel.js` that:

1. Takes three parameters:
    - `width`: Canvas width
    - `height`: Canvas height
    - `hue`: Current hue value (0-1)
2. Computes appropriate RGB values for each pixel
3. Handles color transitions and gradients
4. Returns the correct channel value based on the thread position

</details>

<details><summary>Theory and explanation</summary>

Backend repo mirrors the **frontend color picker** task — same **GPU.js kernel** and HSV gradient logic. Implement `kernelFunction` in `kernel.js` per repository tests.

See **Build a GPU-accelerated color picker** (frontend section) for full color math. Backend evaluation may run kernel in Node via `gpu.js` without React.

**Interview talking points**

- Match thread coordinates to width/height parameters.
- Return correct **channel** slice if kernel is split per RGBA.
- Pentagon **mask** may be applied outside kernel — only pixels inside pentagon get color; clarify in README.

#### Further reading

- [GPU.js](https://gpu.rocks/) — kernel functions
- [Fringecore backend colorpicker-pentagon](https://github.com/Abir66/fringecore-backend-challenges/tree/main/colorpicker-pentagon) — test harness
- [HSV color model](https://en.wikipedia.org/wiki/HSL_and_HSV) — hue to RGB

</details>

<details><summary>Solution (JavaScript)</summary>

Same HSV gradient kernel as frontend challenge — implement in repo `kernel.js`:

```js
// Pseudocode inside GPU.js kernel — API names from challenge stub
// const x = this.thread.x, y = this.thread.y;
// const t = x / width, s = y / height;
// rgb = mix(mix([1,1,1], hsv(hue,1,1), t), [0,0,0], s);
// return rgb[channelIndex];
```

Refer to frontend **Solution (JavaScript)** `hsvToRgb` for CPU-validated reference values.

#### Complexity

| | |
|-|-|
| Time | O(width × height) parallel |
| Space | O(width × height) output buffer |

#### Edge cases

- **hue** outside [0,1] — clamp.
- **Channel index** out of range — assert in dev.

</details>

</article>



<article>

Event Syncer

[**💻 Problem Repository**](https://github.com/Abir66/fringecore-backend-challenges/tree/main/event-syncer)

<details><summary>Show Description</summary>

We want to build an awkward mix between a real-time long-polling server and a queue system.

[Video explanation from team Fringecore_](https://www.tella.tv/video/event-syncer-1-416j)

***Event Life-cycle***

1. Events are automatically cleared after 2 minutes
2. Each event is associated with a specific key

***Consumption Mechanism***

1. Each unique combination of `key` and `groupId` represents a distinct consumer group
2. When a consumer group requests events, it will receive ALL unconsumed events for that specific key
3. Once events are consumed by a group, they are marked as consumed and won't be returned again
4. If multiple consumers in the same group request events, only one will receive the available events

***Endpoint Behaviors***

1. `GET /blocking-get?key=meow&groupId=3`:
    - Waits up to 30 seconds for event to be pushed with the key `meow`
    - If there are already unconsumed events for  key `meow` and groupId `3`, return all unconsumed events for that specific key and group
    - Returns an empty array `[]` if no events arrive within 30 seconds
2. `POST /push?key=meow`:
    - Adds new event to the `meow` event queue
    - Does not specify which consumer group will receive the event
    - Multiple events can be pushed under a single key.
</details>

<details><summary>Theory and explanation</summary>

**In-memory model**

```js
// events[key] = [{ id, payload, createdAt, consumedBy: Set<groupId> }]
// waiters[key][groupId] = array of pending HTTP responses / resolvers
```

**POST /push**

- Append event to `events[key]`.
- Notify any **blocking** `GET` waiters for that `key` (wake one consumer per group rules).

**GET /blocking-get**

- If unconsumed events exist for `(key, groupId)` → return immediately, mark consumed for that group.
- Else hold connection up to **30s** (long poll); on push or timeout return payload or `[]`.
- **Same group competition:** only one waiter gets batch when events arrive — use mutex/queue per `(key, groupId)`.

**TTL 2 minutes**

- `setInterval` or lazy purge on access removing stale events.

**Interview talking points**

- Do not block event loop — use `Promise` + timers, not busy wait.
- Race: push arrives while GET waiting — resolve waiter with new events.
- Express/Fastify raw `res` held open for long poll.

#### Further reading

- [Tella: Event syncer explanation](https://www.tella.tv/video/event-syncer-1-416j) — Fringecore team walkthrough
- [MDN: Long polling](https://developer.mozilla.org/en-US/docs/Web/HTTP/Connection_management_in_HTTP_1.x) — HTTP hold patterns
- [Kafka consumer groups (concept)](https://kafka.apache.org/documentation/#consumerconfigs) — analogy for groupId

</details>

<details><summary>Solution (JavaScript)</summary>

```js
const events = new Map(); // key -> Event[]
const waiters = new Map(); // key -> Map<groupId, resolver[]>

function getUnconsumed(key, groupId) {
  const list = events.get(key) || [];
  return list.filter((e) => !e.consumedBy.has(groupId));
}

function blockingGet(key, groupId) {
  const ready = getUnconsumed(key, groupId);
  if (ready.length) {
    ready.forEach((e) => e.consumedBy.add(groupId));
    return Promise.resolve(ready);
  }
  return new Promise((resolve) => {
    const keyWaiters = waiters.get(key) ?? new Map();
    const g = keyWaiters.get(groupId) ?? [];
    g.push(resolve);
    keyWaiters.set(groupId, g);
    waiters.set(key, keyWaiters);
    setTimeout(() => resolve([]), 30_000);
  });
}

function push(key, payload) {
  const e = { id: crypto.randomUUID(), payload, createdAt: Date.now(), consumedBy: new Set() };
  if (!events.has(key)) events.set(key, []);
  events.get(key).push(e);
  // wake one waiter per group per spec...
}
```

#### Code walkthrough

1. **consumedBy** set tracks per-group consumption.
2. Long poll registers resolver; **push** resolves with pending events.
3. **TTL** sweeper removes `Date.now() - createdAt > 120_000`.

#### Complexity

| | |
|-|-|
| Time | O(events per key) scan; push O(1) append |
| Space | O(total events + open waiters) |

#### Edge cases

- **Duplicate group waiters** — only first receives batch.
- **Timeout vs push race** — clear timer when resolving early.
- **Memory leak** — always purge TTL and completed waiters.

</details>

</article>



<article>

Priority Task Scheduler

[**💻 Problem Repository**](https://github.com/Abir66/fringecore-backend-challenges/tree/main/priority-task-scheduler)

<details><summary>Show Description</summary>

***What To Build***

Modify the function `processTask()` in `challenge.mjs` in such way that:

- **Single Task Processing:** Ensure the program processes only one task at a time.
- **Task Duration:** Each task should be processed for exactly `5` seconds.
- **Priority Handling:**
    - If a new task with **higher priority** arrives while a task is being processed, the program should:
        - Pause the current task.
        - Process the **higher priority** task immediately.
    - Once the higher priority task is completed, the paused task should **resume processing** from where it left off.
- **Task Management:** Maintain a smooth workflow for handling task interruptions and resumptions to ensure no task is lost or delayed indefinitely.

[Video explanation from team Fringecore_](https://www.tella.tv/video/priority-task-scheduler-6lao)
</details>

<details><summary>Theory and explanation</summary>

**Preemptive priority scheduling** with **resume**:

- One worker executes tasks sequentially in real time.
- Each task needs **5 seconds total CPU time** (not necessarily wall-clock if paused).
- Higher **priority number = more important** (confirm in repo).

**State per task**

- `remainingMs` — how much of the 5s slice left.
- `status`: `running` | `paused` | `done`.

**On new higher-priority task while running**

1. Pause current: store `remainingMs`, push to **paused stack/queue**.
2. Run high-priority task to completion (5s).
3. Pop paused task and continue until its `remainingMs` hits 0.

**Data structures**

- **Max-heap** or sorted queue for pending tasks by priority.
- Current running task pointer + stack of paused tasks (LIFO resume matches nested preemption).

**Interview talking points**

- Use `setTimeout` / `async` sleep chunks (e.g. 100ms ticks) to allow preemption checks between ticks.
- [Video explanation](https://www.tella.tv/video/priority-task-scheduler-6lao) shows expected ordering — watch before coding.

#### Further reading

- [Tella: Priority task scheduler](https://www.tella.tv/video/priority-task-scheduler-6lao) — Fringecore walkthrough
- [Operating Systems: preemptive scheduling](https://en.wikipedia.org/wiki/Scheduling_(computing)#Preemptive) — concept
- [JavaScript async patterns](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous) — timers and queues

</details>

<details><summary>Solution (JavaScript)</summary>

```js
const TICK = 100;

async function runSlice(task, ms) {
  const end = Date.now() + ms;
  while (Date.now() < end) {
    await new Promise((r) => setTimeout(r, TICK));
    if (pendingHigherPriority(task)) {
      const spent = Date.now() - (end - ms);
      task.remaining -= spent;
      return 'paused';
    }
  }
  task.remaining = 0;
  return 'done';
}

async function processTask(queue) {
  const paused = [];
  while (queue.length || paused.length) {
    const next = pickHighest(queue);
    let current = next ?? paused.pop();
    while (current && current.remaining > 0) {
      const status = await runSlice(current, current.remaining);
      if (status === 'done') break;
      const preempt = pickHighest(queue);
      if (preempt) {
        paused.push(current);
        current = preempt;
      }
    }
  }
}
```

#### Code walkthrough

1. Track **remaining** milliseconds per 5s task budget.
2. Run in slices; between slices check for higher-priority arrivals.
3. On preemption, push current to **paused** stack; after urgent task completes, resume.

#### Complexity

| | |
|-|-|
| Time | O(total processed time) wall clock |
| Space | O(paused tasks + queue) |

#### Edge cases

- **Equal priority** — FCFS among equals.
- **Nested preemption** — stack ordering must resume inner paused task first (LIFO).
- **Empty queue** — exit cleanly.

</details>

</article>

