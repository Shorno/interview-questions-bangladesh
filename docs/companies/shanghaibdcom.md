---
description: Shanghai BDCOM interview questions, Shanghai BDCOM interview stages, Shanghai BDCOM written test, Shanghai BDCOM R&D intern questions
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/shanghaibdcom
---
# Shanghai Baud Data Communication Co. Ltd.

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-------------- | :------------------- |
| Founding year   | 1994                 |
| Company Website | https://www.bdcom.cn |

## Introduction
[BDCOM](https://www.bdcom.cn/about/) is a Chinese company specializing in networking and communication solutions. It has established its Research & Development (R&D) department in Bangladesh and recruits intern R&D engineers through a 6-month program leading to a Junior R&D Engineer role.

## Interview Stages
- **Written test**: The total time is 2 hours.
- **On site contest and Interview**

## Written Test Questions

### C Programming

- pointer, memory, sizeof, struct, define, enum, string, unsigned char/int, short int, array output tracing type problems (search on google, you may find tons of output tracing problems), 1's/2's complement, sign magnitude, arithmetic/logical shift
- Size of a struct.
- Pointer to a struct, incrementing the pointer
- Output tracing with various conditional operators

### Operating System

<article>

Discuss what led to the need for process scheduling in modern operating systems.  
Explain how multitasking and limited CPU resources made it necessary to manage processes efficiently, and describe the objectives of a process scheduler (e.g., fairness, responsiveness, throughput, CPU utilization).

<details><summary>Theory and explanation</summary>

**Why scheduling exists**

Early systems ran one program at a time. Modern OSes run **many processes/threads** on **few CPUs**. The CPU can execute only one runnable task per core at an instant, so the kernel must **choose who runs next** — that is **process scheduling**.

**Forces that created the need**

1. **Multitasking** — users expect browser, IDE, and music player concurrently; I/O-bound tasks must not block the whole machine.
2. **Limited CPU** — cores are scarce relative to runnable work; without scheduling, one long CPU-bound job starves others.
3. **I/O waiting** — processes block on disk/network; CPU should switch to ready work instead of idling.
4. **Interactive vs batch** — mixed workloads need policies that balance latency and throughput.
5. **Priorities & fairness** — real-time, background, and user-facing tasks need different treatment.

**Scheduler objectives**

| Objective | Meaning |
|-----------|---------|
| **CPU utilization** | Keep CPU busy; minimize idle time when work is ready |
| **Throughput** | Maximize jobs completed per unit time |
| **Turnaround time** | Minimize finish − arrival for batch jobs |
| **Waiting time** | Minimize time spent in ready queue |
| **Response time** | Minimize time until first output (interactive) |
| **Fairness** | No process waits indefinitely (starvation avoidance) |

**Common policies (names to mention)**

- **FCFS**, **SJF/SRTF**, **Round Robin** (time quantum), **Priority**, **Multilevel feedback queues**.
- Preemptive vs non-preemptive scheduling.

**Interview tip**

Connect scheduling to **context switch** cost, **ready queue** data structure, and **preemption** on timer interrupt or higher-priority wake-up.

#### Further reading

- [Operating System Concepts — CPU Scheduling](https://www.os-book.com/OS10/) — textbook chapter
- [GeeksforGeeks: CPU Scheduling Algorithms](https://www.geeksforgeeks.org/cpu-scheduling-in-operating-systems/) — algorithm comparison
- [Linux CFS scheduler overview](https://docs.kernel.org/scheduler/sched-design-CFS.html) — real-world policy

#### Complexity

| | |
|-|-|
| Time | O(1) or O(log n) per scheduling decision depending on queue structure |
| Space | O(n) for ready queues with n runnable processes |

</details>

<details><summary>Solution (JavaScript)</summary>

Illustrative **Round Robin** simulator (educational — not a real OS scheduler):

```js
function roundRobin(processes, quantum) {
  const queue = processes.map((p) => ({ ...p, remaining: p.burst }));
  const results = [];
  let time = 0;

  while (queue.length) {
    const p = queue.shift();
    const run = Math.min(quantum, p.remaining);
    time += run;
    p.remaining -= run;
    if (p.remaining === 0) {
      results.push({ id: p.id, turnaround: time - p.arrival, finish: time });
    } else {
      queue.push(p);
    }
  }
  return results;
}

// Example: [{ id: 'A', burst: 5, arrival: 0 }, { id: 'B', burst: 3, arrival: 1 }]
```

#### Code walkthrough

- Processes enter a FIFO **ready queue**; each gets at most `quantum` CPU time per turn.
- Finished processes record **turnaround time** = finish − arrival.
- Real schedulers add priorities, I/O blocking, and preemption hooks.

#### Complexity

| | |
|-|-|
| Time | O(total burst / quantum × n) naive simulation |
| Space | O(n) queue |

#### Edge cases

- **Quantum too large** — behaves like FCFS.
- **Quantum = 1** — high context-switch overhead in theory.
- **All I/O-bound** — scheduler should not block on one process (use separate wait queues).

</details>

</article>

<article>

When a high-level program file (e.g., C or C++) is turned into an executable file, several steps occur in sequence. Explain each stage and how they work together to create a runnable program.

<details><summary>Theory and explanation</summary>

![](https://d8it4huxumps7.cloudfront.net/uploads/images/655df16819a37_compilation_in_c_01.jpg?d=2000x2000)

Turning `program.c` into `./a.out` follows the **compilation pipeline**:

1. **Preprocessing** — The **preprocessor** handles directives (`#include`, `#define`, `#ifdef`, `#pragma`). Textual substitution and header inclusion produce **translation unit** source (`.i` if saved).

2. **Compilation** — The compiler front-end parses C/C++, checks types, and lowers to **assembly** (`.s`) for the target ISA. Optimizations may apply here.

3. **Assembling** — The **assembler** converts mnemonics to **machine code** → **object file** (`.o` / `.obj`) with relocatable symbols and debug sections.

4. **Linking** — The **linker** merges object files and libraries, resolves **external symbols** (`printf`, `main`), applies **relocation**, and emits the final **executable** or shared library.

**How they fit together**

Each `.c` file compiles to `.o`; the linker combines all `.o` plus `libc` into one loadable binary the loader maps into memory (`execve` on Linux).

**Interview extras**

- **Static vs dynamic linking** — `.so` / `.dll` resolved at load or run time.
- **Cross-compilation** — same pipeline, different target triple.
- C++ adds **name mangling** and may require linking `libstdc++`.

#### Further reading

- [GCC compilation stages](https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html) — `-E`, `-S`, `-c`
- [How linkers work (Ian Lance Taylor)](https://www.airs.com/blog/archives/38) — relocation deep dive
- [ELF executable format](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format) — Linux binary layout

#### Complexity

| | |
|-|-|
| Time | O(source size); dominated by optimization in compile step |
| Space | O(source + symbol table) intermediate files |

</details>

<details><summary>Solution (JavaScript)</summary>

Pipeline mental model as a pure function chain (illustrative):

```js
function preprocess(source, macros = {}) {
  let out = source;
  for (const [name, val] of Object.entries(macros)) {
    out = out.replaceAll(name, val);
  }
  return out.replace(/^#include\s+"(\w+)"/gm, (_, h) => `/* header ${h} */`);
}

function compileToAsm(source) {
  return `; pseudo-asm for: ${source.split('\n')[0]}`;
}

function assemble(asm) {
  return { machineCode: Buffer.from(asm), symbols: ['main'] };
}

function link(objects) {
  return { executable: objects.flatMap((o) => [...o.machineCode]), entry: 'main' };
}

function build(source) {
  return link([assemble(compileToAsm(preprocess(source)))]);
}
```

#### Code walkthrough

- Each stage consumes output of the previous — mirrors `#include` → parse → object → executable.
- Real toolchains invoke `cpp`, `cc1`, `as`, `ld` as separate programs.

#### Complexity

| | |
|-|-|
| Time | O(n) per stage on input size n (simplified) |
| Space | O(n) intermediate representations |

#### Edge cases

- **Undefined reference at link** — symbol declared but no definition in any `.o`.
- **Multiple definition** — same global in two `.c` files without `static`.
- **Header-only libraries** — compiled into every TU that includes them.

</details>

</article>

<article>

Define the following fundamental computer science terms: DMA, Byte Order, coroutine, RISC, PCB.

<details><summary>Theory and explanation</summary>

- **DMA (Direct Memory Access):** Lets **peripherals** (disk, NIC, GPU) read/write **main memory** without the CPU copying every byte. The CPU programs a **DMA controller** with source, destination, and length, then continues other work; an **interrupt** signals completion. Reduces CPU overhead for bulk transfers.

- **Byte Order (Endianness):** Order of bytes in multi-byte integers. **Little-endian** — least significant byte at lowest address (x86, ARM default). **Big-endian** — most significant byte first (network byte order in protocols). Matters for serialization, file formats, and network code.

- **Coroutine:** A **cooperative** control-flow construct: execution can **yield** and **resume** while keeping local state (stack frame). Unlike threads, coroutines typically **voluntarily** transfer control (async/await, generators). Used in asyncio, Lua, Kotlin coroutines, and user-space schedulers.

- **RISC (Reduced Instruction Set Computer):** CPU design with a **small, fixed set** of simple instructions executed in few cycles; complexity moved to compilers. Contrasts with **CISC** (x86 historically). ARM, RISC-V are RISC-flavored; modern x86 decodes to internal RISC-like μops.

- **PCB (Process Control Block):** Kernel **data structure** per process storing **PID**, **state** (ready/running/blocked), **CPU registers** snapshot, **memory map** (page tables), **open files**, **priority**, **parent/children**, scheduling stats. Context switch = swap PCB/register image.

#### Further reading

- [OSDev: DMA](https://wiki.osdev.org/DMA) — controller programming
- [RFC 1700 — byte order](https://www.rfc-editor.org/rfc/rfc1700) — network endianness
- [Python generators / coroutines](https://docs.python.org/3/howto/functional.html#generators) — cooperative multitasking
- [RISC vs CISC (GeeksforGeeks)](https://www.geeksforgeeks.org/difference-between-risc-and-cisc-processor/)

#### Complexity

| | |
|-|-|
| Time | N/A (definitions) |
| Space | PCB typically O(1) fixed size per process in kernel |

</details>

<details><summary>Solution (JavaScript)</summary>

Illustrative **coroutine** with generator (maps to "pause/resume" concept):

```js
function* coroutineExample() {
  const a = yield 1;
  const b = yield a + 2;
  return b * 2;
}

const gen = coroutineExample();
gen.next();      // { value: 1, done: false }
gen.next(10);    // { value: 12, done: false } — a = 10
gen.next(5);     // { value: 10, done: true }  — b = 5, return 10

// Endianness check (platform byte order)
function isLittleEndian() {
  const buf = new ArrayBuffer(2);
  new DataView(buf).setUint16(0, 0x0102, true);
  return new Uint8Array(buf)[0] === 0x02;
}
```

#### Code walkthrough

- **Generator** `yield` pauses without losing locals — coroutine behavior in JS.
- **`isLittleEndian`** — writes 0x0102 and inspects first byte.

#### Complexity

| | |
|-|-|
| Time | O(1) per coroutine step |
| Space | O(depth) saved stack frames for generator state |

#### Edge cases

- **DMA cache coherency** — CPU cache vs device-visible memory may need flush/invalidate.
- **Mixed-endian** — rare bi-endian CPUs; know your target.
- **PCB on fork** — child gets copy of parent's address space description.

</details>

</article>

<article>

List and briefly describe the major parts of a CPU (Central Processing Unit):

<details><summary>Theory and explanation</summary>

- **ALU (Arithmetic Logic Unit):** Executes **integer/floating** arithmetic (`+`, `-`, `×`, `/`) and **bitwise/logical** ops (`AND`, `OR`, `XOR`, shifts, comparisons). Feeds results to registers or memory write path.

- **CU (Control Unit):** **Decodes instructions**, generates **control signals** for ALU, registers, and buses, and orchestrates the **fetch–decode–execute** cycle. In modern CPUs, decoders map ISA instructions to internal micro-operations.

- **Registers:** **Small, fast** storage inside the CPU — **PC** (program counter), **SP** (stack pointer), **general-purpose** (AX/RAX, etc.), **status/flags** (zero, carry, overflow). Access in one cycle vs cache/memory latency.

- **Cache (L1/L2/L3):** **SRAM** hierarchy hiding memory latency. **L1** split I/D per core; **L2/L3** shared. Holds hot instructions and data; **cache lines** (typically 64 B) moved on miss from RAM.

- **Clock / timing:** **Clock signal** synchronizes pipeline stages; **frequency** (GHz) bounds cycles per second. Pipelining and superscalar execution issue multiple ops per cycle subject to hazards.

**Bonus for interviews:** mention **MMU** (virtual memory), **branch predictor**, and **bus interface** to chipset/DMA.

#### Further reading

- [Hennessy & Patterson — computer architecture](https://www.elsevier.com/books/computer-architecture/patterson/978-0-12-811905-7)
- [Intel 64 and IA-32 manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html) — register set
- [GeeksforGeeks: CPU components](https://www.geeksforgeeks.org/computer-organization-and-architecture/)

#### Complexity

| | |
|-|-|
| Time | N/A (hardware components) |
| Space | Register file O(1); cache sizes fixed per chip |

</details>

<details><summary>Solution (JavaScript)</summary>

Educational **fetch-decode-execute** trace (not cycle-accurate):

```js
function simulateCpu(program, registers = { pc: 0, acc: 0 }) {
  const alu = (op, a, b) => ({ add: a + b, sub: a - b, and: a & b }[op]);
  const mem = [...program];

  while (registers.pc < mem.length) {
    const [op, arg] = mem[registers.pc];
    if (op === 'load') registers.acc = arg;
    else if (op === 'add') registers.acc = alu('add', registers.acc, arg);
    else if (op === 'halt') break;
    registers.pc++;
  }
  return registers;
}

// program: [['load', 5], ['add', 3], ['halt']]
```

#### Code walkthrough

- **CU** loop reads `mem[pc]`, dispatches op; **ALU** handles `add`.
- **Registers** hold `pc` and `acc`; real CPUs have dozens of named registers.

#### Complexity

| | |
|-|-|
| Time | O(instructions executed) |
| Space | O(program length) |

#### Edge cases

- **Pipeline hazards** — real CPUs stall on data dependencies; toy model ignores this.
- **Cache miss** — access to RAM orders of magnitude slower than L1 hit.

</details>

</article>


### Networking

<article>

What happens when you type google.com and press enter in your search bar

<details><summary>Theory and explanation</summary>

This classic question tests **end-to-end networking** literacy. A structured answer walks through layers:

1. **URL parsing** — Browser parses scheme (`https`), host (`google.com`), path. May upgrade HTTP→HTTPS via HSTS.

2. **DNS resolution** — Cache check (browser → OS → resolver). If miss: recursive query to DNS (root → TLD `.com` → authoritative) → **A/AAAA record** → IP address(es).

3. **TCP connection** — **Three-way handshake** (SYN, SYN-ACK, ACK) to server IP:443. May try **IPv6** or **IPv4**; **Happy Eyeballs** races connections.

4. **TLS handshake** — ClientHello, certificate chain validation, key exchange, **session keys** for encrypted HTTP.

5. **HTTP request** — `GET / HTTP/1.1`, headers (`Host`, `User-Agent`, cookies). HTTP/2 may multiplex if negotiated.

6. **Server processing** — Load balancer → application servers → possibly DB/cache. Response status, headers, body (HTML).

7. **Rendering** — HTML parse → DOM; CSS → CSSOM; layout/paint; JS download/execute; subresource requests (images, fonts, XHR/fetch).

8. **Caching** — `Cache-Control`, CDN edge caches, service worker if installed.

**Bangladesh / BDCOM angle:** mention **latency**, **DNS TTL**, **NAT**, and **ISP routing** as factors affecting perceived speed.

#### Further reading

- [What Happens When (alex/what-happens-when)](https://github.com/alex/what-happens-when) — canonical deep dive
- [MDN: How the Web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
- [Cloudflare: DNS explained](https://www.cloudflare.com/learning/dns/what-is-dns/)

#### Complexity

| | |
|-|-|
| Time | Dominated by RTT × round trips (DNS, TCP, TLS, HTTP) — often 100ms–1s+ |
| Space | Browser buffers, connection pools — O(response size) |

</details>

<details><summary>Solution (JavaScript)</summary>

High-level **DNS-then-fetch** outline (browser APIs):

```js
async function fetchPage(host, path = '/') {
  // DNS is implicit in fetch/connect — no direct DNS API in browsers
  const url = `https://${host}${path}`;
  const res = await fetch(url, { method: 'GET', redirect: 'follow' });
  const html = await res.text();
  return { status: res.status, headers: Object.fromEntries(res.headers), length: html.length };
}

// Node.js: explicit DNS lookup before connect
// const dns = require('dns').promises;
// const addrs = await dns.lookup('google.com', { all: true });
```

#### Code walkthrough

- Browsers hide DNS/TCP/TLS behind `fetch`; Node `dns.lookup` exposes resolution step.
- Real page load adds parsing, asset discovery, and parallel connections.

#### Complexity

| | |
|-|-|
| Time | O(1) API calls; network latency dominates |
| Space | O(response body) |

#### Edge cases

- **DNS failure** — NXDOMAIN, captive portal, wrong resolver.
- **Certificate error** — MITM or expired cert blocks page.
- **Redirect chain** — 301/302 multiple hops before final HTML.

</details>

</article>

### Analytical

<article>

There are `N` train coaches numbered from `1` to `N` placed in sequence on a left track. The coaches can be moved either directly to the right track or temporarily to a spur track (which behaves like a stack). Once a coach moves from the left track to either the spur or the right, it cannot return to the left.  
Print all possible valid output sequences (permutations) in which the coaches can arrive at the right track using the spur as intermediate storage.

<details><summary>Theory and explanation</summary>

This is the **train shunting / stack permutation** problem.

**Model**

- Input sequence: `1, 2, …, N` (left track, front = 1).
- Operations: push to **stack** (spur) or pop from stack to **output** (right track); may also move directly left→right when allowed (variant — classic version uses stack only via push/pop of next input).
- Output: all permutations of `1..N` achievable with one stack.

**Characterization**

Not all `N!` permutations are valid. A permutation is a **valid stack permutation** iff for every pair `i < j`, if `j` appears before `i` in the output, then all numbers in `(i, j)` must have been output before `j` was pushed (equivalently: no `(k)` with `i < k < j` where `j` before `k` before `i` in output).

**Count**

Valid stack permutations = **Catalan number** `C_N = (1/(N+1)) × C(2N, N)`.

**Generation**

DFS/backtracking: at each step, if next input not exhausted, **push**; if stack non-empty, **pop** to output. Enumerate all outputs when input consumed and stack empty.

#### Further reading

- [GeeksforGeeks: Stack permutations](https://www.geeksforgeeks.org/stack-permutations-check-if-an-array-is-stack-permutation-of-other/)
- [Catalan numbers (CP-Algorithms)](https://cp-algorithms.com/combinatorics/catalan-numbers.html)
- [LeetCode 946 — Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/)

#### Complexity

| | |
|-|-|
| Time | O(N × C_N) to enumerate all outputs; validation O(N) per permutation |
| Space | O(N) stack + recursion |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function stackPermutations(n) {
  const results = [];
  const input = Array.from({ length: n }, (_, i) => i + 1);

  function generate(inIdx, stack, out) {
    if (out.length === n) {
      results.push([...out]);
      return;
    }
    if (inIdx < n) {
      stack.push(input[inIdx]);
      generate(inIdx + 1, stack, out);
      stack.pop();
    }
    if (stack.length) {
      out.push(stack.pop());
      generate(inIdx, stack, out);
      stack.push(out.pop());
    }
  }

  generate(0, [], []);
  return results;
}

#### Code walkthrough

- **`generate`** tries **push next coach** or **pop to output** when stack non-empty.
- Base case: output length `N` — record permutation.
- Backtrack by undoing push/pop.

#### Complexity

| | |
|-|-|
| Time | O(N × C_N) — Catalan many outputs |
| Space | O(N) recursion depth |

#### Edge cases

- **N = 1** — single output `[1]`.
- **N = 3** — outputs include `[1,2,3]`, `[1,3,2]`, `[2,3,1]` but not `[3,2,1]`.

</details>

</article>

<article>

There are `1000` liquid bottles. One of the bottles contains poisoned liquid. A rat dies after one hour of drinking the poisoned wine. How many minimum rats are needed to figure out which bottle contains poison in hour? [Also called the Poison and Rat problem]

<details><summary>Theory and explanation</summary>

Each rat can represent one **bit of information** (alive = 0, dead = 1) after one hour.

**Encoding**

- Label bottles `0..999` in **binary** with **⌈log₂ 1000⌉ = 10** bits.
- Rat `i` drinks from all bottles whose bit `i` is `1`.
- After one hour, dead rats form a binary number = **poisoned bottle index**.

**Why 10 is enough**

- 2¹⁰ = 1024 ≥ 1000 distinct labels.
- 9 rats only give 512 combinations — insufficient.

**General formula**

Minimum rats = **⌈log₂ B⌉** for `B` bottles (one trial, one hour).

#### Further reading

- [Classic poison bottle puzzle](https://brilliant.org/wiki/poisoned-wine-bottles/) — binary encoding
- [Information theory intuition](https://en.wikipedia.org/wiki/Information_theory) — bits as distinguishable states

#### Complexity

| | |
|-|-|
| Time | O(B × rats) to assign drinks; O(1) to read outcome |
| Space | O(rats) outcome bits |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function minRats(bottles) {
  return Math.ceil(Math.log2(bottles));
}

function poisonedBottleIndex(bottles, deadRats) {
  // deadRats: array of rat indices (0-based) that died
  let index = 0;
  for (const r of deadRats) index |= 1 << r;
  return index; // 0-based bottle number
}

// Assign which bottles rat r drinks (for planning)
function bottlesForRat(bottles, rat) {
  const list = [];
  for (let b = 0; b < bottles; b++) {
    if (b & (1 << rat)) list.push(b);
  }
  return list;
}

// minRats(1000) === 10
```

#### Code walkthrough

- **`minRats`** — ceiling of log₂(1000) = 10.
- **`poisonedBottleIndex`** — OR bit for each dead rat → bottle id.
- **`bottlesForRat`** — precompute feeding schedule.

#### Complexity

| | |
|-|-|
| Time | O(B × log B) to build schedule; O(log B) decode |
| Space | O(log B) |

#### Edge cases

- **B = 1** — 0 rats needed (already know which bottle).
- **Multiple hours** — if rats can be retested across hours, fewer rats possible (advanced variant).

</details>

</article>

<article>

Four people need to cross a bridge at night. They have one torch and the bridge can only hold two people at a time. Each person walks at a different speed: `1`, `2`, `5`, and `10` minutes. If two people cross together, they must go at the slower person's pace. What is the minimum total time required for all four people to cross the bridge?

<details><summary>Theory and explanation</summary>

Classic **bridge and torch** puzzle (1, 2, 5, 10).

**Optimal strategy (17 minutes)**

1. **1 and 2** cross → 2 min (right side: 1,2; left: 5,10).
2. **1** returns with torch → 1 min.
3. **5 and 10** cross → 10 min (right: 1,2,5,10).
4. **2** returns with torch → 2 min.
5. **1 and 2** cross again → 2 min.

**Total = 2 + 1 + 10 + 2 + 2 = 17** minutes.

**Why not send 10+5 first?** Slow pair crossing early wastes time; fast people **shuttle the torch** so the 10-minute person crosses only once with the 5-minute person.

**Pattern**

For times `{a ≤ b ≤ c ≤ d}` with small `a`, often optimal: `(a,b)` over, `a` back, `(c,d)` over, `b` back, `(a,b)` over — compare with alternative `(a,b)`, `b` back, `(a,c)`, `a` back, `(a,d)`.

#### Further reading

- [Bridge crossing puzzle (Math StackExchange)](https://math.stackexchange.com/questions/tagged-bridge-crossing)
- [GeeksforGeeks: Bridge and torch](https://www.geeksforgeeks.org/puzzle-1-a-person-can-cross-a-bridge-in-x-minutes/)

#### Complexity

| | |
|-|-|
| Time | O(1) for four fixed speeds; O(n!) brute force for general n |
| Space | O(1) |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function bridgeTorchFour() {
  const steps = [
    { cross: [1, 2], time: 2 },
    { cross: [1], time: 1, return: true },
    { cross: [5, 10], time: 10 },
    { cross: [2], time: 2, return: true },
    { cross: [1, 2], time: 2 },
  ];
  return steps.reduce((sum, s) => sum + s.time, 0); // 17
}

function minBridgeTime(times) {
  times.sort((a, b) => a - b);
  const [a, b, c, d] = times;
  const plan1 = b + a + d + c + b; // classic shuttle
  const plan2 = b + c + a + a + d; // alternative
  return Math.min(plan1, plan2);
}

// minBridgeTime([1, 2, 5, 10]) === 17
```

#### Code walkthrough

- **`bridgeTorchFour`** — encodes optimal 5-step plan; sum = 17.
- **`minBridgeTime`** — compares two standard strategies for 4 people.

#### Complexity

| | |
|-|-|
| Time | O(1) for n = 4 |
| Space | O(1) |

#### Edge cases

- **Two people only** — time = slower person's time.
- **Three people** — send two fastest, return fastest, send remaining two.

</details>

</article>

<article>

You are given two candles of equal length. Each candle takes exactly 60 minutes to burn, but they burn at inconsistent rates (i.e., half the candle may not burn in 30 minutes). How can you measure exactly 45 minutes using these two candles? [Also called the The Burning Candles problem]

<details><summary>Theory and explanation</summary>

**Key insight:** Non-uniform burn rate means you **cannot** assume half length = half time — but you **can** use **extinction events** as known timestamps.

**Standard 45-minute solution**

1. Light **candle A** at both ends and **candle B** at one end simultaneously.
2. When **A** burns out → **30 minutes** elapsed (two ends burning halves total burn time to 30 min regardless of non-uniformity — both halves of A finish together in 30 min).
3. Immediately light the **other end** of **B** (still has 30 min of wax left in "time-to-burn-from-one-end" terms).
4. When **B** goes out → **15 more minutes** (half of remaining 30-min-equivalent wax by double-end burn).
5. **Total = 30 + 15 = 45 minutes.**

**Why double-end burning works**

If one end takes 60 min alone, burning both ends consumes length at **2× relative rate** → finishes in exactly **30 min** wall time, independent of varying linear density.

#### Further reading

- [Burning rope / candle puzzles](https://brilliant.org/wiki/burning-ropes/) — non-uniform timing
- [Interview puzzle: two candles](https://www.geeksforgeeks.org/puzzle-12-candle-burning-problem/)

#### Complexity

| | |
|-|-|
| Time | O(1) steps (physical process) |
| Space | O(1) |

</details>

<details><summary>Solution (JavaScript)</summary>

State-machine simulation of **events** (not burn physics):

```js
function measure45Minutes() {
  const timeline = [];
  let t = 0;

  // t=0: light A both ends, B one end
  timeline.push({ t: 0, action: 'light A (both ends), B (one end)' });

  t += 30;
  timeline.push({ t, action: 'A extinguished — 30 min elapsed' });

  timeline.push({ t, action: 'light B other end' });

  t += 15;
  timeline.push({ t, action: 'B extinguished — 45 min total' });

  return { totalMinutes: t, timeline };
}
```

#### Code walkthrough

- First interval fixed at **30** by double-ended A.
- Second interval **15** by double-ended remaining B.
- No need to model wax density — only event times matter.

#### Complexity

| | |
|-|-|
| Time | O(1) |
| Space | O(1) |

#### Edge cases

- **Cannot relight** — problem assumes you can light unlit end while burning.
- **Unequal length candles** — problem states equal initial length.

</details>

</article>

<article>

There are `10` jars of pills. One jar contains pills that weigh `9` grams each, while the others contain pills weighing `10` grams each. Using a weighing scale only once, how can you determine which jar contains the lighter pills?

<details><summary>Theory and explanation</summary>

**One-weighing encoding**

Take from jar `i` exactly **`i` pills** (1 from jar 1, 2 from jar 2, …, 10 from jar 10) — total **55 pills**.

**Expected weight if all 10g:** `55 × 10 = 550` grams.

If jar `k` has 9g pills, total is **`550 − k`** grams (each pill in jar k weighs 1g less, and you took `k` pills from it).

**Read scale once:** `missing = 550 − measured` → **`k = missing`**.

**Why it works**

Difference in count per jar creates a **unique fingerprint** for which jar contributed lighter pills.

#### Further reading

- [Classic 9g/10g pill puzzle](https://brilliant.org/wiki/identifying-the-poisoned-pill/) — similar encoding
- [Information in single measurement](https://en.wikipedia.org/wiki/Balance_puzzle)

#### Complexity

| | |
|-|-|
| Time | O(J) to collect pills; O(1) weighing |
| Space | O(1) |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function lighterJarFromWeight(measuredGrams, jars = 10, heavy = 10, light = 9) {
  const totalPills = (jars * (jars + 1)) / 2;
  const expected = totalPills * heavy;
  const missing = expected - measuredGrams;
  return missing; // jar index (1-based if missing grams equals pills taken)
}

function expectedWeight(jars = 10, heavy = 10) {
  return ((jars * (jars + 1)) / 2) * heavy;
}

// Example: jar 3 light → take 55 pills, weight = 550 - 3 = 547
// lighterJarFromWeight(547) === 3
```

#### Code walkthrough

- **`expectedWeight`** — 55 × 10 = 550.
- **`missing`** grams → jar number (1-based index).

#### Complexity

| | |
|-|-|
| Time | O(1) |
| Space | O(1) |

#### Edge cases

- **J jars generalization** — take `i` pills from jar `i`; expected = `10 × J(J+1)/2`.
- **Digital scale precision** — must resolve 1g difference.

</details>

</article>

### Data Structure and Algorithm

<article>

You are given an arithmetic expression in either infix or postfix notation. Write a program to convert it to prefix notation, maintaining correct operator precedence and associativity.

<details><summary>Theory and explanation</summary>

**Notations**

- **Infix:** `A + B` — operators between operands.
- **Prefix (Polish):** `+ A B` — operator before operands.
- **Postfix (RPN):** `A B +` — operator after operands.

**Precedence & associativity**

Standard: `^` (right-assoc) > `* /` > `+ -` (left-assoc). Parentheses override.

**Infix → prefix (high level)**

1. Reverse infix string (swap operands around operators, reverse parentheses).
2. Convert reversed infix to postfix using shunting-yard.
3. Reverse postfix → prefix.

**Or direct algorithm:** scan infix **right-to-left**, use stack — push operands to output front; pop higher-precedence ops from stack.

**Postfix → prefix:** scan postfix **right-to-left**; operands to stack; on operator, pop two, push `(op + right + left)`.

#### Further reading

- [Shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm)
- [GeeksforGeeks: Infix to Prefix](https://www.geeksforgeeks.org/infix-to-prefix-conversion/)
- [CP-Algorithms: Expression parsing](https://cp-algorithms.com/string/expression_parsing.html)

#### Complexity

| | |
|-|-|
| Time | O(n) for n tokens |
| Space | O(n) stack |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
const prec = { '+': 1, '-': 1, '*': 2, '/': 2, '^': 3 };
const rightAssoc = new Set(['^']);

function infixToPrefix(tokens) {
  const rev = [...tokens].reverse().map((t) => (t === '(' ? ')' : t === ')' ? '(' : t));
  const out = [];
  const stack = [];

  for (const t of rev) {
    if (/^[A-Za-z0-9]+$/.test(t)) out.push(t);
    else if (t === '(') stack.push(t);
    else if (t === ')') {
      while (stack.length && stack[stack.length - 1] !== '(') out.push(stack.pop());
      stack.pop();
    } else {
      while (
        stack.length &&
        stack[stack.length - 1] !== '(' &&
        (prec[stack[stack.length - 1]] > prec[t] ||
          (prec[stack[stack.length - 1]] === prec[t] && !rightAssoc.has(t)))
      ) {
        out.push(stack.pop());
      }
      stack.push(t);
    }
  }
  while (stack.length) out.push(stack.pop());
  return out.reverse();
}

// infixToPrefix(['(','A','+','B',')','*','C']) → ['*', '+', 'A', 'B', 'C'] style tokens
```

#### Code walkthrough

- Reverse + parenthesis swap → apply shunting-yard → reverse output = prefix.
- Handles precedence and right-associativity of `^`.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(n) |

#### Edge cases

- **Unary minus** — treat as separate token or parenthesize.
- **Invalid expression** — mismatched parentheses → error.

</details>

</article>

<article>

You are given `1000` unsorted numbers and need to find the `10` smallest elements efficiently. Which sorting or selection algorithm would be most optimal to solve this problem and why?

<details><summary>Theory and explanation</summary>

**Goal:** 10 smallest out of `n = 1000` — **partial selection**, not full sort.

**Best choices**

1. **Min-heap of size 10 (recommended)** — O(n log k) = O(1000 × log 10) ≈ O(1000 × 3.3). Scan array; if `x` < heap max, replace. Extract 10 mins.

2. **Quickselect** — average O(n) to partition around 10th order statistic; worst O(n²) without careful pivot. Good in practice for single k.

3. **Full sort** — O(n log n) ≈ 1000 × 10 — overkill when k ≪ n.

4. **Bubble/select repeated** — O(k × n) = O(10 × 1000) — acceptable but worse than heap for general k.

**Why heap wins here**

- k = 10 fixed and small; heap memory **O(k)**; predictable O(n log k).
- **Partial quicksort** (priority queue in C++ `partial_sort`) same complexity class.

**Interview answer**

Use a **size-10 max-heap**; after one pass, heap holds 10 smallest. Do **not** full-sort 1000 elements.

#### Further reading

- [LeetCode 215 — Kth Largest Element](https://leetcode.com/problems/kth-largest-element-in-an-array/) — heap/select
- [Quickselect (CP-Algorithms)](https://cp-algorithms.com/sequences/k-th.html)
- [C++ partial_sort](https://en.cppreference.com/w/cpp/algorithm/partial_sort)

#### Complexity

| Approach | Time | Space |
|----------|------|-------|
| Max-heap size k | O(n log k) | O(k) |
| Quickselect | O(n) avg | O(1) |
| Full sort | O(n log n) | O(1) or O(n) |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class MaxHeap {
  constructor() { this.a = []; }
  size() { return this.a.length; }
  peek() { return this.a[0]; }
  push(v) {
    this.a.push(v);
    let i = this.a.length - 1;
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (this.a[p] >= this.a[i]) break;
      [this.a[p], this.a[i]] = [this.a[i], this.a[p]];
      i = p;
    }
  }
  pop() {
    const top = this.a[0];
    const last = this.a.pop();
    if (this.a.length) {
      this.a[0] = last;
      let i = 0;
      for (;;) {
        let l = i * 2 + 1, r = l + 1, big = i;
        if (l < this.a.length && this.a[l] > this.a[big]) big = l;
        if (r < this.a.length && this.a[r] > this.a[big]) big = r;
        if (big === i) break;
        [this.a[i], this.a[big]] = [this.a[big], this.a[i]];
        i = big;
      }
    }
    return top;
  }
}

function tenSmallest(nums, k = 10) {
  const heap = new MaxHeap();
  for (const x of nums) {
    if (heap.size() < k) heap.push(x);
    else if (x < heap.peek()) {
      heap.pop();
      heap.push(x);
    }
  }
  const out = [];
  while (heap.size()) out.push(heap.pop());
  return out.reverse();
}
```

#### Code walkthrough

- **Max-heap** keeps k smallest — root is largest among them (eviction candidate).
- Single O(n) pass; each push/pop O(log k).

#### Complexity

| | |
|-|-|
| Time | O(n log k) |
| Space | O(k) |

#### Edge cases

- **n < k** — return sorted copy of all elements.
- **Duplicates** — heap handles naturally.

</details>

</article>

<article>

Implement a function to perform preorder traversal of a binary tree using both recursive and iterative (loop-based) approaches.

<details><summary>Theory and explanation</summary>

**Preorder (NLR):** Visit **N**ode, then **L**eft subtree, then **R**ight subtree.

**Recursive:** Trivial — process root, recurse left, recurse right.

**Iterative:** Use **stack** simulating call stack:

1. Push root.
2. While stack non-empty: pop node, visit, push **right** then **left** (so left processed first).

**Complexity:** O(n) time, O(h) stack space (h = height).

**Use cases:** Copy tree, prefix expression export, DFS order in puzzles.

#### Further reading

- [Binary tree traversals (GeeksforGeeks)](https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/)
- [LeetCode 144 — Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

#### Complexity

| | |
|-|-|
| Time | O(n) nodes |
| Space | O(h) recursion/stack; O(n) worst skewed tree |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function preorderRecursive(root, visit = (x) => x.val) {
  const out = [];
  function dfs(node) {
    if (!node) return;
    out.push(visit(node));
    dfs(node.left);
    dfs(node.right);
  }
  dfs(root);
  return out;
}

function preorderIterative(root, visit = (x) => x.val) {
  if (!root) return [];
  const out = [];
  const stack = [root];
  while (stack.length) {
    const node = stack.pop();
    out.push(visit(node));
    if (node.right) stack.push(node.right);
    if (node.left) stack.push(node.left);
  }
  return out;
}
```

#### Code walkthrough

- **Recursive** — standard DFS preorder.
- **Iterative** — explicit stack; push right before left for correct order.

#### Complexity

| | |
|-|-|
| Time | O(n) |
| Space | O(h) |

#### Edge cases

- **Empty tree** — return `[]`.
- **Single node** — `[root.val]`.
- **Skewed tree** — stack depth O(n).

</details>

</article>

<article>

Write a program to add and delete a node in a doubly linked list. Your implementation should handle edge cases like deleting the head or tail nodes and adding a node at arbitrary positions.

<details><summary>Theory and explanation</summary>

**Doubly linked list (DLL):** Each node has `prev` and `next`. Supports O(1) insert/delete **given a node pointer**; search still O(n).

**Insert at position `pos` (0-based)**

- Walk `pos` steps from head (or tail if near end).
- Rewire: `new.prev = cur.prev`, `new.next = cur`, fix neighbors.

**Insert after/before known node** — O(1) pointer surgery.

**Delete node**

- **Head:** advance head, null new head's `prev`.
- **Tail:** shrink tail, null new tail's `next`.
- **Middle:** `node.prev.next = node.next`, `node.next.prev = node.prev`.

**Edge cases:** empty list, single element, delete head/tail, invalid position.

#### Further reading

- [GeeksforGeeks: DLL insert/delete](https://www.geeksforgeeks.org/doubly-linked-list-set-1-introduction-insertion/)
- [LeetCode 707 — Design Linked List](https://leetcode.com/problems/design-linked-list/)

#### Complexity

| | |
|-|-|
| Time | O(n) find position; O(1) insert/delete with node ref |
| Space | O(1) per operation |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class DLLNode {
  constructor(val) {
    this.val = val;
    this.prev = null;
    this.next = null;
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  insertAt(pos, val) {
    const node = new DLLNode(val);
    if (pos <= 0 || !this.head) {
      node.next = this.head;
      if (this.head) this.head.prev = node;
      else this.tail = node;
      this.head = node;
    } else if (pos >= this.size) {
      node.prev = this.tail;
      this.tail.next = node;
      this.tail = node;
    } else {
      let cur = this.head;
      for (let i = 0; i < pos; i++) cur = cur.next;
      node.prev = cur.prev;
      node.next = cur;
      cur.prev.next = node;
      cur.prev = node;
    }
    this.size++;
    return node;
  }

  deleteNode(node) {
    if (!node) return;
    if (node.prev) node.prev.next = node.next;
    else this.head = node.next;
    if (node.next) node.next.prev = node.prev;
    else this.tail = node.prev;
    this.size--;
  }
}
```

#### Code walkthrough

- **`insertAt`** — handles head (pos 0), tail (pos ≥ size), and middle.
- **`deleteNode`** — fixes head/tail when removing endpoints.

#### Complexity

| | |
|-|-|
| Time | O(pos) to walk; O(1) delete with node |
| Space | O(1) |

#### Edge cases

- **Delete only node** — head/tail both null, size 0.
- **Insert at tail** — use `pos >= size`.

</details>

</article>

<article>

Compare arrays and linked lists in terms of memory usage, access time, insertion, and deletion. In which scenarios would you prefer one over the other?

<details><summary>Theory and explanation</summary>

| Aspect | Array | Linked list |
|--------|-------|-------------|
| **Memory** | Contiguous; may waste capacity if dynamic array over-allocates; no per-element pointer overhead | Extra `next`/`prev` pointers per node; non-contiguous → cache misses |
| **Access** | O(1) random index | O(n) walk to index |
| **Insert/delete front** | O(n) shift elements | O(1) with head pointer |
| **Insert/delete middle** | O(n) shift | O(1) after finding node; find is O(n) |
| **Cache locality** | Excellent (sequential scan) | Poor (pointer chasing) |

**Prefer arrays when**

- Frequent **random access**, numeric computation, sorting, binary search.
- Known size or dense storage (matrices, buffers).

**Prefer linked lists when**

- Frequent **insert/delete at ends** or known position with iterator.
- **Unbounded** stream, implementing deque/queue internals, or avoiding reallocation copies.
- **Memory fragmentation** concerns with huge contiguous blocks (rare today).

**Modern note:** Dynamic arrays (`vector`, `ArrayList`) often beat linked lists in practice due to cache; linked lists used in kernel structures, LRU internals, and pointer-stable iterators.

#### Further reading

- [Array vs Linked List (GeeksforGeeks)](https://www.geeksforgeeks.org/array-vs-linked-list/)
- [Bjarne Stroustrup: linked list performance myth](https://isocpp.org/blog/2014/12/vector-and-list-performance) — vector often faster

#### Complexity

| Operation | Array | Linked list |
|-----------|-------|-------------|
| Index access | O(1) | O(n) |
| Insert/delete at i | O(n) | O(n) find + O(1) splice |

</details>

<details><summary>Solution (JavaScript)</summary>

Micro-benchmark pattern (illustrative — not rigorous):

```js
function arrayInsertFront(arr, val, n = 1000) {
  const start = performance.now();
  for (let i = 0; i < n; i++) arr.unshift(val); // O(n) each
  return performance.now() - start;
}

function listInsertFront(head, val, n = 1000) {
  const start = performance.now();
  let h = head;
  for (let i = 0; i < n; i++) h = { val, next: h }; // O(1) each
  return performance.now() - start;
}

function randomAccessArray(arr, idx) {
  return arr[idx]; // O(1)
}

function randomAccessList(head, idx) {
  let cur = head;
  for (let i = 0; i < idx && cur; i++) cur = cur.next;
  return cur?.val;
}
```

#### Code walkthrough

- **`unshift`** on array shifts all elements — O(n).
- **List prepend** only rewires head — O(1).
- Random access contrasts O(1) vs O(n).

#### Complexity

| | |
|-|-|
| Time | As per operation above |
| Space | Array dense; list +2 pointers per node |

#### Edge cases

- **Small n** — array constant factors may still win due to cache.
- **Typed arrays** — arrays required for SIMD/binary data.

</details>

</article>

<article>

You are given unlimited coins of denominations `1`, `2`, and `5` cents. How many different ways can you make a total of `1` dollar (`100` cents) using these coins?

<details><summary>Theory and explanation</summary>

**Unbounded coin change — count combinations** (order of coins does not matter).

**Recurrence**

`ways(amount, coins)` — number of ways to make `amount` using coin subset.

```
dp[0] = 1
dp[a] += dp[a - coin] for each coin in ascending order
```

Iterate coins outer loop to avoid counting permutations as distinct.

**For coins {1, 2, 5}, amount 100**

Classic DP table size 101; answer is **241** ways.

**Math alternative:** generating functions — product over coins of `1/(1-x^c)`; DP is simpler in interviews.

#### Further reading

- [LeetCode 518 — Coin Change II](https://leetcode.com/problems/coin-change-ii/)
- [CP-Algorithms: Coin change](https://cp-algorithms.com/dynamic_programming/knapsack.html)
- [GeeksforGeeks: Count ways to make coin change](https://www.geeksforgeeks.org/coin-change-dp-7/)

#### Complexity

| | |
|-|-|
| Time | O(amount × #coins) |
| Space | O(amount) |

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function coinChangeWays(amount, coins = [1, 2, 5]) {
  const dp = Array(amount + 1).fill(0);
  dp[0] = 1;
  for (const coin of coins) {
    for (let a = coin; a <= amount; a++) {
      dp[a] += dp[a - coin];
    }
  }
  return dp[amount];
}

// coinChangeWays(100) === 241
```

#### Code walkthrough

- **`dp[a]`** — ways to make sum `a`.
- Outer loop on **coins** ensures combinations not permutations (1+2 vs 2+1 counted once).

#### Complexity

| | |
|-|-|
| Time | O(100 × 3) = O(300) |
| Space | O(100) |

#### Edge cases

- **amount = 0** — one way (empty set).
- **Impossible denominations** — if no coin divides amount and no 1-cent, may be 0.

</details>

</article>

<article>

Explain the difference between linear and non-linear data structures with examples.  
Mention the advantages and typical use cases of each.

<details><summary>Theory and explanation</summary>

**Linear data structures**

Elements arranged **sequentially** (each has at most one predecessor/successor in traversal order).

- **Examples:** array, linked list, stack, queue, deque.
- **Traversal:** single pass from head to tail (or both ends for deque).
- **Advantages:** Simple memory layout (arrays), predictable iteration, easy serialization.
- **Use cases:** buffers, task queues, undo stacks, sequential files, streaming pipelines.

**Non-linear data structures**

Elements have **multiple relationships** — not a single chain.

- **Examples:** tree (binary, BST, heap), graph, trie, B-tree.
- **Traversal:** DFS, BFS, multiple paths; hierarchical or networked.
- **Advantages:** Model hierarchies (DOM, file systems), fast search (BST, trie), relationships (social graphs, routing).
- **Use cases:** filesystem trees, DB indexes, syntax ASTs, network routing, recommendation graphs.

**Comparison summary**

| | Linear | Non-linear |
|---|--------|------------|
| Relationships | 1:1 sequence | 1:many, many:many |
| Search typical | O(n) unless sorted array | O(log n) tree, O(V+E) graph |
| Memory | Often compact | Pointer overhead |

#### Further reading

- [GeeksforGeeks: Linear vs non-linear DS](https://www.geeksforgeeks.org/linear-vs-non-linear-data-structures/)
- [CLRS — data structures overview](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)

#### Complexity

| | |
|-|-|
| Time | Traversal O(n) linear; graph/tree varies |
| Space | Depends on structure |

</details>

<details><summary>Solution (JavaScript)</summary>

Representative **linear queue** vs **non-linear tree**:

```js
// Linear: queue (FIFO)
class Queue {
  constructor() { this.items = []; }
  enqueue(x) { this.items.push(x); }
  dequeue() { return this.items.shift(); }
}

// Non-linear: binary tree node
class TreeNode {
  constructor(val, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

function bfs(root) {
  if (!root) return [];
  const out = [];
  const q = new Queue();
  q.enqueue(root);
  while (q.items.length) {
    const node = q.dequeue();
    out.push(node.val);
    if (node.left) q.enqueue(node.left);
    if (node.right) q.enqueue(node.right);
  }
  return out;
}
```

#### Code walkthrough

- **Queue** — single sequence; one front, one back.
- **BFS on tree** — visits level-by-level; structure branches (non-linear).

#### Complexity

| | |
|-|-|
| Time | BFS O(n) nodes |
| Space | O(width) queue |

#### Edge cases

- **Degenerate tree (linked list shape)** — still non-linear type; BFS space O(1).

</details>

</article>


## Contributors
- Students of CSE SUST 28th Batch (2019-2020 Session)
